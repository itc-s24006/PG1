#モジュールの利用

import random
import my_module

print(random.randint(0,10))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(random.choice(alphabet))

print(random.sample(alphabet,5))

print(my_module.func(5))
