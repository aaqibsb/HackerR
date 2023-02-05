if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for key, value in student_marks.items():
        # print(key, query_name)
        if key == query_name:
            # print(key, query_name)
            res = format((sum(value) / len(value)), '.2f')
            print(res)
