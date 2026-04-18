"""
In this project, you will use object-oriented programming to create a Rectangle class and a Square class.
The Square class should be a subclass of Rectangle and inherit its methods and attributes.
"""


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        return (self.width**2 + self.height**2) ** 0.5

    def set_width(self, new_width: int) -> None:
        self.width = new_width

    def set_height(self, new_height: int) -> None:
        self.height = new_height

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for i in range(self.height):
            for j in range(self.width):
                picture += "*"
            picture += "\n"
        return picture

    def get_amount_inside(self, figure: "Rectangle") -> int:
        min_self = min(self.width, self.height)
        max_self = max(self.width, self.height)
        min_figure = min(figure.width, figure.height)
        max_figure = max(figure.width, figure.height)
        return (min_self // min_figure) * (max_self // max_figure)


class Square(Rectangle):
    def __init__(self, side: int) -> None:
        self.side = side
        super().__init__(side, side)

    def __str__(self) -> str:
        return f"Square(side={self.side})"

    def set_side(self, new_side: int) -> None:
        self.side = new_side
        super().set_width(new_side)
        super().set_height(new_side)

    def set_width(self, new_width: int) -> None:
        self.set_side(new_width)

    def set_height(self, new_height: int) -> None:
        self.set_side(new_height)


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
