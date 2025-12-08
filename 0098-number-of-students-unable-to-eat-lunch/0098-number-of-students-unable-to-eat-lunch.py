class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = 0

        while len(students) > cnt:
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                cnt = 0
            else:
                students.append(students[0])
                cnt += 1
            students.pop(0)

        return cnt
        

