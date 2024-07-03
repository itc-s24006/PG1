#input,len

name = input('お名前は？:')
print(name)
print(f"文字数:{len(name)}")
print()

#itre
name_iter = iter(name)
print(next(name_iter))
print(next(name_iter))
print(next(name_iter))
print(next(name_iter))
print(next(name_iter))

