# %% 
import os
import re
import json

# 要遍历的目录
notebook_dir_jp = r"D:\OneDrive\Notebook"
# 输出文件
output_file_jp = r"notebook_japanese.json"

# 定义一个函数来提取日语字符（含平假名、片假名、汉字）
# 日语字符范围示例:
# 平假名: \u3040-\u309F
# 片假名: \u30A0-\u30FF
# 汉字:   \u4E00-\u9FAF (等同中文汉字范围)
jp_pattern = r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]+'

def extract_japanese(text):
    return ''.join(re.findall(jp_pattern, text))

data_jp = []

for root, dirs, files in os.walk(notebook_dir_jp):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 提取日语字符
            content_japanese = extract_japanese(content)

            # 存入字典
            file_data = {
                "file_name": file,
                "content": content,            # 原始内容
                "content_japanese": content_japanese # 日语提取结果
            }
            data_jp.append(file_data)

# 将数据逐行写入json文件，每行一个JSON对象
with open(output_file_jp, 'w', encoding='utf-8') as f:
    for item in data_jp:
        json.dump(item, f, ensure_ascii=False)
        f.write('\n')

print(f"日语数据已保存到 {output_file_jp}，每行一个 JSON 对象。")
