# %% 
import json
import random

ARXIV_JSON = 'arxiv-metadata-oai-snapshot.json'
TEST_SAMPLE_SIZE = 3000  # 可以根据需要调整样本数大小
legal_chars = 'qazwsxedcrfvtgbyhnujmik,ol.p;:? '

# 首先统计文件总行数
total_lines = 0
with open(ARXIV_JSON, 'r', encoding='utf-8') as f:
    for _ in f:
        total_lines += 1

# 从total_lines中随机选取TEST_SAMPLE_SIZE个行号作为抽样
sample_line_indices = set(random.sample(range(total_lines), TEST_SAMPLE_SIZE))

full_text['arxiv_test'] = ''  # 增加一个新的测试数据子集
with open(ARXIV_JSON, 'r', encoding='utf-8') as file:
    for i, line in enumerate(file):
        if i in sample_line_indices:
            abstract = json.loads(line)['abstract'].replace('\n', ' ').strip().lower()
            # 如果abstract中有不合法字符则跳过
            if any(char not in legal_chars for char in abstract):
                continue
            full_text['arxiv_test'] += ' ' + abstract

print("测试数据集构建完成，arxiv_test长度:", len(full_text['arxiv_test']))
