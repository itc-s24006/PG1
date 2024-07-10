import random as rd
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ch = rd.choice(alphabet)
while True:
    val = input(アルファベットを入力してください:)
    if ch == val:
        print('OK!!!')
        break
    else:
        print('NG')


