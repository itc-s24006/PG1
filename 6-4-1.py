def reverse(data):
    '''引数に受け取ったシーケンスを逆向きに返す'''
    for index in range(len(data)-1, -1, -1):
        yield data[index]

#ジェネレータをforループのinに加える
for char in reverse('golf'):
    print(char, end=" ")
print("\n")
