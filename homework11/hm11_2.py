class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        x = self.point2[0] - self.point1[0]
        y = self.point2[1] - self.point1[1]

        x_squar = x * x
        y_squar = y * y

        sum_squares = x_squar + y_squar

        length = sum_squares ** 0.5
        return length

    def compare(self, other_line):
        length1 = self.length()
        length2 = other_line.length()
        if length1 > length2:
            return "Перша лінія довша."
        elif length1 < length2:
            return "Друга лінія довша."
        else:
            return "Лінії рівні."
