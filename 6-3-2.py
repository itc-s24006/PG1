class Rectangle:
    '''長方形'''
    angle = 90

    def __init__(self, width, height):
        self.name = 'rectangle'
        self.width = width
        self.height = height
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

    def calc_perimeter(self):
        '''周の長さ'''
        w = self.width
        h = self.height
        return (w + h) * 2

    def calc_area(self):
        '''面積'''
        w = self.width
        h = self.height
        return w * h

    def show_attributes(self):
        '''結果表示'''
        ang = self.angle
        n = self.name
        w = self.width
        h = self.height
        p = self.perimeter
        a = self.area
        print(f"name: {n}, width: {w}, height: {h}, angle: {ang}")
        print(f"perimeter: {p}, area: {a}")

#インスタンスを作って実行
r1 = Rectangle(4,3)
r1.show_attributes()


class Square(Rectangle):
    '''正方形'''

    def __init__(self, width):
        super().__init__(width, width)
        self.name = 'square'

#インスタンスを作って実行
s1 = Square(4)
s1.show_attributes()
