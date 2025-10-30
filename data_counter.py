#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import matplotlib.pyplot as plt
from collections import Counter
import argparse


def read_data_from_directory(raw_data_dir, ignore_case=False):
    """
    从raw_data目录读取所有文件，返回统计结果

    Args:
        raw_data_dir (str): 数据目录路径
        ignore_case (bool): 是否忽略大小写

    Returns:
        Counter: 所有value的计数器
    """
    if not os.path.exists(raw_data_dir):
        print(f"错误：目录 {raw_data_dir} 不存在")
        return Counter()

    value_counter = Counter()
    file_count = 0

    print(f"正在读取目录：{raw_data_dir}")

    # 遍历目录中的所有文件
    for filename in os.listdir(raw_data_dir):
        filepath = os.path.join(raw_data_dir, filename)

        # 只处理普通文件
        if not os.path.isfile(filepath):
            continue

        file_count += 1
        print(f"处理文件 {file_count}: {filename}")

        try:
            # 读取文件内容
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read().strip()

                if not content:
                    continue

                # 按换行符分割成多行，然后处理每行
                lines = content.split('\n')
                raw_values = []

                for line in lines:
                    line = line.strip()
                    if line:
                        # 按逗号分割每行内容
                        line_values = line.split(',')
                        raw_values.extend(line_values)

                # 处理每个value：去除空白并去重（单个文件内）
                file_values = set()
                for raw_value in raw_values:
                    clean_value = raw_value.strip()
                    if clean_value:  # 忽略空字符串
                        # 根据ignore_case参数决定是否转换大小写
                        processed_value = clean_value.lower() if ignore_case else clean_value
                        file_values.add(processed_value)

                # 更新全局计数器
                for value in file_values:
                    value_counter[value] += 1

                print(f"  - 找到 {len(file_values)} 个唯一值")

        except Exception as e:
            print(f"  - 错误：无法读取文件 {filename}: {e}")

    print(f"总共处理了 {file_count} 个文件")
    return value_counter


def generate_chart(value_counter, output_file='value_counts.png', top_n=None):
    """
    生成计数图表

    Args:
        value_counter (Counter): 计数器对象
        output_file (str): 输出图片文件名
        top_n (int): 只显示前N个最频繁的值，None表示显示全部
    """
    if not value_counter:
        print("没有数据可以生成图表")
        return

    # 准备数据
    if top_n:
        # 获取前N个最常见的值
        most_common = value_counter.most_common(top_n)
        labels = [item[0] for item in most_common]
        counts = [item[1] for item in most_common]
        title = f'Value Counts (Top {top_n})'
    else:
        # 获取所有数据（按计数值排序）
        sorted_items = value_counter.most_common()
        labels = [item[0] for item in sorted_items]
        counts = [item[1] for item in sorted_items]
        title = 'Value Counts (All)'

    # 设置中文字体（防止中文显示为方框）
    plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False

    # 创建图表
    plt.figure(figsize=(12, 8))

    # 创建柱状图
    bars = plt.bar(range(len(labels)), counts)

    # 设置标题和标签
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel('Values', fontsize=12)
    plt.ylabel('Count', fontsize=12)

    # 设置x轴标签
    plt.xticks(range(len(labels)), labels, rotation=45, ha='right')

    # 在每个柱子上显示数值
    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom')

    # 添加网格线
    plt.grid(axis='y', alpha=0.3)

    # 调整布局
    plt.tight_layout()

    # 保存图表
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"图表已保存到：{output_file}")

    # 显示图表（可选）
    plt.show()


def print_statistics(value_counter, ignore_case=False):
    """
    打印统计信息到控制台

    Args:
        value_counter (Counter): 计数器对象
        ignore_case (bool): 是否忽略了大小写
    """
    if not value_counter:
        print("没有统计数据")
        return

    print(f"\n{'='*50}")
    print("统计信息")
    if ignore_case:
        print("模式：大小写不敏感")
    else:
        print("模式：区分大小写")
    print(f"{'='*50}")
    print(f"唯一值总数：{len(value_counter)}")
    print(f"总计数：{sum(value_counter.values())}")
    print(f"平均计数：{sum(value_counter.values()) / len(value_counter):.2f}")

    print(f"\n前10个最常见的值：")
    print("-" * 40)
    for i, (value, count) in enumerate(value_counter.most_common(10), 1):
        print(f"{i:2d}. {value:<20} : {count}")

    print(f"\n后5个最罕见的值：")
    print("-" * 40)
    least_common = value_counter.most_common()[:-6:-1]
    for i, (value, count) in enumerate(least_common, 1):
        print(f"{i}. {value:<20} : {count}")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='数据计数和可视化工具')
    parser.add_argument('--data-dir', '-d', default='raw_data',
                       help='数据目录路径 (默认: raw_data)')
    parser.add_argument('--output', '-o', default='value_counts.png',
                       help='输出图片文件名 (默认: value_counts.png)')
    parser.add_argument('--top-n', '-n', type=int, default=None,
                       help='只显示前N个最频繁的值 (默认: 显示全部)')
    parser.add_argument('--no-chart', action='store_true',
                       help='不生成图表，只显示统计信息')
    parser.add_argument('--ignore-case', '-i', action='store_true',
                       help='忽略大小写进行统计')

    args = parser.parse_args()

    print("数据计数和可视化工具")
    print("=" * 50)
    if args.ignore_case:
        print("运行模式：大小写不敏感")
    else:
        print("运行模式：区分大小写")

    # 读取数据
    value_counter = read_data_from_directory(args.data_dir, args.ignore_case)

    if not value_counter:
        print("没有找到任何数据")
        return

    # 打印统计信息
    print_statistics(value_counter, args.ignore_case)

    # 生成图表（除非用户指定不要图表）
    if not args.no_chart:
        generate_chart(value_counter, args.output, args.top_n)

    print(f"\n处理完成！")


if __name__ == "__main__":
    main()