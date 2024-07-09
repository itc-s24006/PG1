#importのいろいろな書き方

import random as rd
from random import randint as rint

print(rd.randint(0,10)) #rd(random)の中のrandintを使うから、rintではだめ
print(rint(0,10))
