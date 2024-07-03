#小数点の誤差による処理結果の違い
from decimal import Decimal
print(Decimal.from_float(0.5))
print(Decimal.from_float(0.1))
print(Decimal.from_float(0.3))

