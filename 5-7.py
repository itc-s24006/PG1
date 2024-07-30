prefecture_of_japan = {1:'Hokkaido',2:'Aomori',3:'Iwate'}
print(prefecture_of_japan)

print()
print(prefecture_of_japan[1])

print('キーを指定して値を取得する')
print(prefecture_of_japan.get(0))
print(prefecture_of_japan.get(1))
print('(get()メソッドの第二引数には、キーが登録されていなかったときに返される値を指定できる)')
print(prefecture_of_japan.get(0,'Not Found'))

print('要素を追加する')
prefecture_of_japan[4] = 'Miyagi'
print(prefecture_of_japan)

print('キーが辞書に登録されているか確認する')
print(1 in prefecture_of_japan)

print('キーを指定して要素を削除する')
del prefecture_of_japan[4]
print(prefecture_of_japan)

#popメソッドを使用して要素を取り出す
print(prefecture_of_japan.pop(3))
print(prefecture_of_japan)

prefecture_of_japan[3] = 'Iwate'
for x in prefecture_of_japan.keys():
    print(x)

for x in prefecture_of_japan.values():
    print(x)

for key, x in prefecture_of_japan.items():
    print(key,x)
