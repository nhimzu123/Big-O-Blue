a = [[3, 2], [4, 2], [1, 2]]
a.sort(key=lambda x: x[0])


# Săps xếp theo mảng cấu trúc
class Fraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom


li_1 = [Fraction(5, 4), Fraction(7, 9), Fraction(1, 8), Fraction(9, 2), Fraction(12, 8)]

# Ascending
li_1.sort(key=lambda fraction: fraction.num / fraction.denom)

# Descending
li_1.sort(key=lambda fraction: -fraction.num / fraction.denom)


class Student:
    def __init__(self, student_id, score):
        self.id = student_id
        self.score = score


list_student = [Student(100, 8.5), Student(101, 7.5), Student(102, 9.5), Student(103, 6.5), Student(104, 4.5),
                Student(105, 5.5)]

# Sắp xếp theo điểm giảm dần, nếu điểm bằng nhau thì sắp xếp theo id tăng dần
list_student.sort(key=lambda s: (-s.score, s.id))

for student in list_student:
    print(student.id, student.score)
