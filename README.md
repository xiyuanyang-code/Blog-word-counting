# Blog Word Counter - README

**Update**: Scripts for push the updates everyday automatically to github is available now! See `src/autopush.sh` for more details.

## Overview

The Blog Word Counter is a Python utility designed to help bloggers and content creators track their writing progress by counting words in Markdown (.md) files. This tool is particularly useful for:

- Tracking writing milestones
- Measuring content production over time
- Analyzing writing habits
- Maintaining consistency in blog post lengths

The tool handles both English and Chinese content, providing accurate word counts for multilingual bloggers. It generates detailed logs of word counts per article and summary statistics of your entire blog repository.

## Features

1. **Bilingual Support**: Accurately counts words in both English and Chinese
2. **Directory Scanning**: Processes all Markdown files in a directory recursively
3. **Progress Tracking**: Maintains historical logs of your word counts
4. **Statistics Generation**: Provides total article count and aggregate word count
5. **JSON Output**: Produces machine-readable output for further analysis

## Installation

Just clone the directory via:

```bash
git clone https://github.com/xiyuanyang-code/Blog-word-counting.git
cd blog-word-counting
```

## Usage

By default, the script looks for Markdown files in `/mnt/d/Blog/source/_posts`. You need to replace it with your own directory.

run the scripts via:

```bash
bash src/run.sh
```

### Expected Output

```
Let's see how many words you have typed in your Blog!
Finished
```

### Output Files

The script generates two types of output files:

1. **Individual Article Logs**: Timestamped JSON files in the `log/` directory containing word counts for each article
2. **Summary Statistics**: A `total.json` file with aggregate statistics


## Code Explanation

### Core Functions

#### 1. `count_words(text: str = "")`

This function handles the actual word counting logic.

**Key Features:**
- Uses regular expressions to identify Chinese characters (`[\u4e00-\u9fff]`)
- Counts English words using word boundary detection (`\b[a-zA-Z]+\b`)
- Combines counts for bilingual content

**Implementation Details:**

```python
def count_words(text: str = ""):
    text = text.strip()
    chinese_count = len(re.findall(r"[\u4e00-\u9fff]", text))
    english_count = len(re.findall(r"\b[a-zA-Z]+\b", text))
    return chinese_count + english_count
```

#### 2. `count_words_in_directory(directory: str)`

Processes all Markdown files in a directory recursively.

**Key Features:**
- Walks through directory tree using `os.walk()`
- Filters for `.md` files
- Returns a list of dictionaries with filename and word count

**Implementation Details:**

```python
def count_words_in_directory(directory: str):
    blog_word_counts = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as opened_file:
                    content = opened_file.read()
                    count_num = count_words(content)
                    blog_word_counts.append(
                        {"blog_name": file, "word_count": count_num}
                    )
    return blog_word_counts
```

#### 3. Logging and Statistics Functions

**`get_log_filename(log_dir="log")`**
- Creates timestamped log filenames
- Ensures log directory exists

**`save_to_json(blog_word_counts)`**
- Saves individual article counts to JSON

**`do_calculate(blog_word_counts)`**
- Computes total articles and words
- Includes timestamp in output

### Main Execution Flow

1. Directory scanning and word counting
2. Log file generation
3. Summary statistics calculation
4. Output file creation



## Example Outputs

### Individual Article Log (log/log_20250421_190058.txt)

```json
[
    {
        "blog_name": "getting_started_with_python.md",
        "word_count": 1245
    },
    {
        "blog_name": "machine_learning_basics.md",
        "word_count": 2876
    }
]
```

### Summary Statistics (total.json)

```json
{
    "time": "2025-04-21",
    "total_articles": 42,
    "total_word_count": 87654
}
```

