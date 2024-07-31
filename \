class Nigiri:  #親クラス
    category = "にぎり"
    top = "ねた"
    base = "しゃり"
    
    def show_attributes(self):
        print(f"top:{self.top}, base:{self.base}, category:{self.category}")


class Maguro(Nigiri):  #子クラス
    top = "まぐろ"  #クラス変数topを上書き(子クラス内のみ)
    price = 100

    def show_attributes(self):
        super().show_attributes()  #親クラスのメソッド呼び出し
        print(f"price:{self.price}円")  #処理追加

    def show_one_dish_price(self, num_nigiri=2):
        result = self.price * num_nigiri  #1皿の値段を計算
        print(f"1皿({num_nigiri}かん)の値段：{result}円")


m5 = Maguro()
m5.show_attributes()
m5.show_one_dish_price()
