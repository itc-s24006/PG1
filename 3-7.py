with open('sample.txt','r') as f:
    line = f.readline()
    print(line)

with open('sample.txt','r') as f:
    lines = f.readlines()
    print(lines)

with open('sample2.txt','w') as f:
     f.write('test\n')

with open('sample2.txt','a') as f:
    f.write('\ntest2')

'''
with open('number.txt','r') as f:
    sum = 0
    for data in f:
        num = int(data)
        sum += num 
    print(sum)
'''
