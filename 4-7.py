def circle_func(pi = 3.14):
    #円お麺背系を計算する関数

    def circle_area(radius):
        #円の面積を計算する
        return radius * radius * pi
    return circle_area

#piが初期設定(3.14)のとき
circle_default = circle_func()

#piが3.1415926535のとき
circle_precise = circle_func(pi = 3.1415926535)

#半径２の円の面積、piの精度が異なる
print(circle_default(2))
print(circle_precise(2))
