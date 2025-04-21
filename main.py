"""
Author: Xiyuan Yang   xiyuan_yang@outlook.com
Date: 2025-04-21 18:52:45
LastEditors: Xiyuan Yang   xiyuan_yang@outlook.com
LastEditTime: 2025-04-21 19:00:58
FilePath: /Blog-word-counting/main.py
Description:
Do you code and make progress today?
Copyright (c) 2025 by Xiyuan Yang, All Rights Reserved.
"""

from datetime import datetime
import os
import json
import re


def count_words(text: str = ""):
    """Count the number of words in a single text.

    Args:
        text (str, optional): Input text. Defaults to "".

    Returns:
        int: The number of words.
    """

    text = text.strip()

    # For Chinese, count all characters
    chinese_count = len(re.findall(r"[\u4e00-\u9fff]", text))

    # For English, use regular expressions to count words
    english_count = len(re.findall(r"\b[a-zA-Z]+\b", text))

    return chinese_count + english_count


def count_words_in_directory(directory: str):
    """Count the number of words in all .md files in the specified directory.

    Args:
        directory (str): The path to the directory.

    Returns:
        list: A list of dictionaries containing file names and word counts.
    """
    blog_word_counts = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                # Check if it is a blog post
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as opened_file:
                    content = opened_file.read()
                    count_num = count_words(content)
                    blog_word_counts.append(
                        {"blog_name": file, "word_count": count_num}
                    )

    return blog_word_counts


def get_log_filename(log_dir="log") -> str:
    """Generate a timestamp-based log filename."""
    # Generate the log dir
    os.makedirs(log_dir, exist_ok=True)

    # Get timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(log_dir, f"log_{timestamp}.txt")


def save_to_json(blog_word_counts):
    """Save the list of word counts to a JSON file.

    Args:
        blog_word_counts (list): A list of dictionaries containing word count data.
    """
    file_name = get_log_filename(log_dir="log")
    with open(file_name, "w", encoding="utf-8") as json_file:
        json.dump(blog_word_counts, json_file, ensure_ascii=False, indent=4)


def do_calculate(blog_word_counts):
    """Calculate the total number of articles and words.

    Args:
        blog_word_counts (list): A list of dictionaries containing word count data.
        file_name (str): The directory path.
    """
    total_article_num = len(blog_word_counts)
    total_word_count = sum(item["word_count"] for item in blog_word_counts)
    total_data = {
        "time": datetime.now().strftime("%Y-%m-%d"),
        "total_articles": total_article_num,
        "total_word_count": total_word_count,
    }
    file_name = "total.json"
    with open(file_name, "w", encoding="utf-8") as json_file:
        json.dump(total_data, json_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    print("Let's see how many words you have typed in your Blog!")
    file_name = "/mnt/d/Blog/source/_posts"
    ans = count_words_in_directory(file_name)
    save_to_json(ans)
    do_calculate(ans)
    print("Finished")
