from collections import defaultdict

qwerty='qazwsxedcrfvtgbyhnujmik,ol.p;/'
cyletix34='qazwsxdecrtvfgbyhnjlmki,po.;u/'
cyletix10 = 'qazwsxdecrtvfgb;hnjlmki,yo.pu/'


# 定义所有可能的声母
initials = ["zh", "ch", "sh", "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "x", "z", "y", "w"]

# 分离拼音音节为列表
pinyin_list = """
a ai an ang ao
ba bai ban bang bao bei ben beng bi bian biao bie bin bing bo bu
ca cai can cang cao ce cen ceng cha chai chan chang chao che chen cheng chi chong chou chu chua chuai chuan chuang chui chun chuo ci cong cou cu cuan cui cun cuo
da dai dan dang dao de dei den deng di dia dian diao die ding diu dong dou du duan dui dun duo
e ei en eng er
fa fan fang fei fen feng fiao fo fou fu
ga gai gan gang gao ge gei gen geng gong gou gu gua guai guan guang gui gun guo
ha hai han hang hao he hei hen heng hong hou hu hua huai huan huang hui hun huo
ji jia jian jiang jiao jie jin jing jiong jiu ju juan jue jun
ka kai kan kang kao ke kei ken keng kong kou ku kua kuai kuan kuang kui kun kuo
la lai lan lang lao le lei leng li lia lian liang liao lie lin ling liu lo long lou lu luan lue lun luo lv
ma mai man mang mao me mei men meng mi mian miao mie min ming miu mo mou mu
na nai nan nang nao ne nei nen neng ni nian niang niao nie nin ning niu nong nou nu nuan nue nun nuo nü
o ou
pa pai pan pang pao pei pen peng pi pian piao pie pin ping po pou pu
qi qia qian qiang qiao qie qin qing qiong qiu qu quan que qun
ran rang rao re ren reng ri rong rou ru rua ruan rui run ruo
sa sai san sang sao se sen seng sha shai shan shang shao she shei shen sheng shi shou shu shua shuai shuan shuang shui shun shuo si song sou su suan sui sun suo
ta tai tan tang tao te tei teng ti tian tiao tie ting tong tou tu tuan tui tun tuo
wa wai wan wang wei wen weng wo wu
xi xia xian xiang xiao xie xin xing xiong xiu xu xuan xue xun
ya yan yang yao ye yi yin ying yo yong you yu yuan yue yun
za zai zan zang zao ze zei zen zeng zha zhai zhan zhang zhao zhe zhei zhen zheng zhi zhong zhou zhu zhua zhuai zhuan zhuang zhui zhun zhuo zi zong zou zu zuan zui zun zuo
"""

# 将拼音音节拆分成列表
pinyin_syllables = pinyin_list.split()

# 用一个字典来分类这些音节
categories = {initial: [] for initial in initials}
categories["-"] = []  # 用于存放零声母的音节

# 定义分类函数
for syllable in pinyin_syllables:
    categorized = False
    for initial in initials:
        if syllable.startswith(initial):
            categories[initial].append(syllable)
            categorized = True
            break
    if not categorized:
        categories["-"].append(syllable)

# 定义每个手指负责的键位
keys_per_finger = [
    [0, 1, 2], 
    [3, 4, 5], 
    [6, 7], 
    [8, 9, 10, 11, 12, 13, 14], 
    [15, 16, 17, 18, 19, 20], 
    [21, 22, 23], 
    [24, 25, 26], 
    [27, 28, 29]
]

# 创建一个字典映射每个键位到对应的手指
key_to_finger = {key: finger for finger, keys in enumerate(keys_per_finger) for key in keys}

def calculate_finger_repeat(qwerty, categories):
    # 定义一个函数将拼音字符转换为键位索引
    char_to_index = {char: index for index, char in enumerate(qwerty)}
    
    def pinyin_to_key_indices(pinyin):
        return [char_to_index[char] for char in pinyin if char in char_to_index]

    # 记录重复使用手指的字母对并进行计数
    repeated_pairs_count = defaultdict(int)
    same_finger_count = 0
    same_finger_pinyin = defaultdict(set)

    # 检查是否使用同一根手指连续输入
    for syllables in categories.values():
        for pinyin in syllables:
            key_indices = pinyin_to_key_indices(pinyin)
            finger_indices = [key_to_finger[key] for key in key_indices]
            repeated_pairs = [
                (pinyin[i], pinyin[i + 1]) 
                for i in range(len(finger_indices) - 1) 
                if finger_indices[i] == finger_indices[i + 1]
            ]
            if repeated_pairs:
                same_finger_count += 1
                for pair in repeated_pairs:
                    repeated_pairs_count[pair] += 1
                    same_finger_pinyin[pair].add(pinyin)

    # 按照出现次数从大到小排序
    sorted_repeated_pairs = sorted(
        repeated_pairs_count.items(), 
        key=lambda item: item[1], 
        reverse=True
    )

    # 打印排序后的列表
    print("连续输入字母对-出现次数:")
    for pair, count in sorted_repeated_pairs:
        print(f"{pair}-{count} |音节: {' '.join(same_finger_pinyin[pair])}")

    print(f"同手指连续输入的音节总数: {same_finger_count}")

def main():
    calculate_finger_repeat(qwerty, categories)
    calculate_finger_repeat(cyletix34, categories)

if __name__ == "__main__":
    main()
