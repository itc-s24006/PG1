import collections

data = 'すもももももももものうち'
count_dic = {}
for v in data:
    if v in count_dic:
        count_dic[v] += 1
    else:
        count_dic[v] = 1
print(count_dic)

count_dic2 = collections.defaultdict(int)
for v in data:
    count_dic2[v] += 1
print(count_dic2)


count_dic3 = collections.defaultdict(list)

for v in data:
    count_dic3[v].append(v)
print(count_dic3)


counter = collections.Counter(data)
print(counter)


print(counter['す'])
print(counter['ぽ'])

CharCount = collections.namedtuple('CharCount',['char', 'count'])
mo = CharCount('も',8)
print(mo)
print(mo.char, mo.count)


count = collections.Counter(data)
res_dict = collections.defaultdict(list)
for ch, cnt in count.items():
    res_dict[cnt].append(ch)
print(res_dict[1])
