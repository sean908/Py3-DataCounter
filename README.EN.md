# Data Counter and Visualization Tool

A Python program that reads data files from a specified directory, counts the frequency of all values, and generates visualization charts.

## Features

- **Data Reading**: Automatically scans and processes all files in the directory
- **Simple Data Cleaning**: Removes whitespace, handles duplicates, supports case sensitivity options
- **Visualization**: Generates bar charts with PNG format output

## 🛠 Installation

### Requirements
- Python 3.7+
- pip package manager

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Dependencies
```
matplotlib>=3.5.0  # Chart generation library
```

## 📖 Usage

### Basic Usage
```bash
# Use default configuration (reads from raw_data directory)
python data_counter.py
```

### Advanced Usage

#### Data Directory Configuration
```bash
# Specify custom data directory
python data_counter.py --data-dir SampleData
python data_counter.py -d /path/to/your/data
```

#### Case Sensitivity
```bash
# Ignore case when counting
python data_counter.py --ignore-case
python data_counter.py -i
```

#### Output Configuration
```bash
# Specify output chart filename
python data_counter.py --output my_analysis.png
python data_counter.py -o chart.png
```

#### Display Limits
```bash
# Show only the top 15 most frequent values
python data_counter.py --top-n 15
python data_counter.py -n 20
```

#### Mode Selection
```bash
# Show only statistics, no chart generation
python data_counter.py --no-chart
```

#### Combined Parameters
```bash
# Complete example: Use SampleData, ignore case, show top 10 values, no chart
python data_counter.py -d SampleData -i -n 10 --no-chart

# Generate custom chart: specify data directory and output filename
python data_counter.py -d SampleData -o custom_chart.png -n 15
```

## Data Format Specification

### File Organization
Place data files in the specified directory (default is `raw_data/`):

```
your_data_directory/
├── file1.txt
├── file2.txt
├── subfolder/
│   └── file3.txt
└── nested/
    └── data.txt
```

### File Format
Each text file supports the following format:

```
value1, value2, value3
value4, value5, value6
value7, value8
```

**Format Requirements:**

Separate values by comma`,`

### Data Processing Rules

1. **Single File Deduplication**: Duplicate values within the same file are counted only once
2. **Cross-File Accumulation**: Same values across different files are accumulated
3. **Case Handling**: Case sensitivity depends on parameters
4. **Whitespace Processing**: Automatically removes leading/trailing whitespace

## Output Description

### Console Output
```
Data Counter and Visualization Tool
==================================================
Running Mode: Case Insensitive

Reading directory: SampleData
Processing file 1: file1.txt
  - Found 10 unique values
Processing file 2: file2.txt
  - Found 13 unique values
Total files processed: 4

==================================================
Statistics
Mode: Case Insensitive
==================================================
Total unique values: 25
Total count: 42
Average count: 1.68

Top 10 most common values:
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

### Chart Output
- **Default Filename**: `value_counts.png`
- **Content**: Bar chart showing value counts with value labels and grid lines

## Project Structure

```
rate-counter/
├── data_counter.py         # Main program file
├── requirements.txt        # Python dependency list
├── README.md              # Chinese documentation
├── README.EN.md           # English documentation
├── SampleData/            # Sample data directory
│   ├── file1.txt
│   ├── ...
│   └── file4.txt
└── raw_data/              # Default data directory
```

## 💻 Command-Line Parameters

| Parameter | Short | Default | Description |
|-----------|-------|---------|-------------|
| `--data-dir` | `-d` | `raw_data` | Data files directory path |
| `--output` | `-o` | `value_counts.png` | Output chart filename |
| `--top-n` | `-n` | `None` | Show top N most frequent values |
| `--ignore-case` | `-i` | `False` | Ignore case when counting |
| `--no-chart` | - | `False` | Show statistics only, no chart |


## 📄 License

This project is licensed under MIT License. See the LICENSE file for details.

---
