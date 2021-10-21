import heapq


class Student:
    def __init__(self, student_id, mark):
        self.student_id = student_id
        self.mark = mark

    def __lt__(self, other):
        return (self.mark, self.student_id) > (other.mark, other.student_id)


li = [Student(9, 5), Student(11, 5), Student(10, 4)]
# li = [6, 4, 5]
heap = []
# li.sort(key= lambda s: (-s.mark, -s.student_id))
for student in li:
    heapq.heappush(heap, student)
    # print(student.student_id, student.mark)
for student in heap:
    print(student.student_id, student.mark)
