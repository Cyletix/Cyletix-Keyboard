import os
import json
import re

# 设置要遍历的Python代码目录
python_code_dirs = [
    r"D:\OneDrive\Code\Python",
    r"D:\OneDrive\Project"
]

# 定义保存结果的json文件路径
output_file = r"python_code_content_line_by_line.json"

# 定义去除单行注释的正则表达式
comment_pattern = re.compile(r'(^#.*?$)', re.MULTILINE)

# 函数：移除代码中的单行注释
def remove_comments(code):
    return re.sub(comment_pattern, '', code).strip()

# 初始化一个列表，用来存储所有文件的信息
data = []

# 遍历目录下的所有.py文件
for code_dir in python_code_dirs:
    for root, dirs, files in os.walk(code_dir):
        # 跳过隐藏文件夹
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except UnicodeDecodeError:
                    print(f"跳过无法解码的文件: {file_path}")
                    continue
                
                # 移除单行注释
                content_no_comments = remove_comments(content)
                
                # 将文件名和内容存入字典
                file_data = {
                    "file_name": file,
                    "content": content_no_comments
                }
                data.append(file_data)

# 将数据逐行写入json文件，每行一个JSON对象
with open(output_file, 'w', encoding='utf-8') as f:
    for item in data:
        json.dump(item, f, ensure_ascii=False)
        f.write('\n')

print(f"已将数据保存到 {output_file}，每行一个 JSON 对象。")
