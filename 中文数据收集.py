import os
import re
import json
from pypinyin import lazy_pinyin

# 设置要遍历的目录
notebook_dir = r"D:\OneDrive\Notebook"

# 定义保存结果的json文件路径
output_file = r"notebook_content.json"

# 定义一个函数来提取中文字符
def extract_chinese(text):
    return ''.join(re.findall(r'[\u4e00-\u9fff]+', text))

# 定义一个函数将中文转换为拼音
def chinese_to_pinyin(chinese_text):
    return ' '.join(lazy_pinyin(chinese_text))

# 初始化一个列表，用来存储所有文件的信息
data = []

# 遍历目录下的所有md文件
for root, dirs, files in os.walk(notebook_dir):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 提取中文字符
            content_chinese = extract_chinese(content)
            
            # 将中文内容转换为拼音
            content_pinyin = chinese_to_pinyin(content_chinese)
            
            # 将文件名和内容存入字典
            file_data = {
                "file_name": file,
                "content": content,
                "content_chinese": content_chinese,
                "content_pinyin": content_pinyin
            }
            data.append(file_data)

# 将数据逐行写入json文件，每行一个JSON对象
with open(output_file, 'w', encoding='utf-8') as f:
    for item in data:
        json.dump(item, f, ensure_ascii=False)
        f.write('\n')

print(f"已将数据保存到 {output_file}，每行一个 JSON 对象。")
