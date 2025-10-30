# 数据计数和可视化工具

一个Python程序，用于读取指定目录中的数据文件，统计所有值的出现频率，并生成可视化图表。

## 功能点

-  **数据读取**：自动扫描并处理目录中的所有文件
-  **简单数据清洗**：去除空白字符、处理重复值、支持大小写选项
-  **可视化**：生成柱状图，支持PNG格式输出

## 🛠 安装说明

### 环境要求
- Python 3.7+
- pip 包管理器

### 安装依赖
```bash
pip install -r requirements.txt
```

### 依赖包说明
```
matplotlib>=3.5.0  # 图表生成库
```

## 📖 使用方法

### 基本用法
```bash
# 使用默认配置（读取raw_data目录）
python data_counter.py
```

### 高级用法

#### 数据目录配置
```bash
# 指定自定义数据目录
python data_counter.py --data-dir SampleData
python data_counter.py -d /path/to/your/data
```

#### 大小写处理
```bash
# 忽略大小写进行统计
python data_counter.py --ignore-case
python data_counter.py -i
```

#### 输出配置
```bash
# 指定输出图片文件名
python data_counter.py --output my_analysis.png
python data_counter.py -o chart.png
```

#### 显示限制
```bash
# 只显示前15个最频繁的值
python data_counter.py --top-n 15
python data_counter.py -n 20
```

#### 模式选择
```bash
# 只显示统计信息，不生成图表
python data_counter.py --no-chart
```

#### 参数组合使用
```bash
# 完整示例：使用SampleData，忽略大小写，只显示前10个值，不生成图表
python data_counter.py -d SampleData -i -n 10 --no-chart

# 生成自定义图表：指定数据目录和输出文件名
python data_counter.py -d SampleData -o custom_chart.png -n 15
```

## 数据格式规范

### 文件组织
将数据文件放置在指定目录中（默认为 `raw_data/`）：

```
your_data_directory/
├── file1.txt
├── file2.txt
├── subfolder/
│   └── file3.txt
└── nested/
    └── data.txt
```

### 文件格式
每个文本文件支持以下格式：

```
value1, value2, value3
value4, value5, value6
value7, value8
```

**格式要求：**

逗号`,`分隔各数据值 

### 数据处理规则

1. **单文件去重**：同一个文件中重复出现的值只计算一次
2. **跨文件累加**：不同文件中的相同值会累加计数
3. **大小写处理**：根据参数决定是否区分大小写
4. **空白处理**：自动去除前后空白字符

## 输出示例

### 控制台输出
```
数据计数和可视化工具
==================================================
运行模式：大小写不敏感

正在读取目录：SampleData
处理文件 1: file1.txt
  - 找到 10 个唯一值
处理文件 2: file2.txt
  - 找到 13 个唯一值
总共处理了 4 个文件

==================================================
统计信息
模式：大小写不敏感
==================================================
唯一值总数：25
总计数：42
平均计数：1.68

前10个最常见的值：
 1. grape                : 3
 2. apple                : 3
 3. kiwi                 : 3
 4. banana               : 3
 5. coconut              : 3
 6. mango                : 3
 7. orange               : 3
 8. watermelon           : 2
 9. pineapple            : 2
10. papaya               : 2
```

### 图表输出
- **默认文件名**：`value_counts.png`
- **内容**：柱状图显示值的计数，包含数值标签和网格线

## 项目结构

```
rate-counter/
├── data_counter.py         # 主程序文件
├── requirements.txt        # Python依赖包列表
├── README.md              # 中文文档
├── README.EN.md           # 英文文档
├── SampleData/            # 示例数据目录
│   ├── file1.txt
│   ├── ...
│   └── file4.txt
└── raw_data/              # 默认数据目录
```

## 💻 命令行参数详解

| 参数 | 简写 | 默认值 | 说明 |
|------|------|--------|------|
| `--data-dir` | `-d` | `raw_data` | 数据文件目录路径 |
| `--output` | `-o` | `value_counts.png` | 输出图表文件名 |
| `--top-n` | `-n` | `None` | 显示前N个最频繁的值 |
| `--ignore-case` | `-i` | `False` | 忽略大小写进行统计 |
| `--no-chart` | - | `False` | 不生成图表，只显示统计信息 |

## 📄 许可证

本项目采用 MIT 许可证，详见 LICENSE 文件。

---
