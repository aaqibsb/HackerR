if __name__ == '__main__':

    T = []
    R = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        T = [name, score]
        R.append(T)

    R.sort()
    R.sort(key=lambda x: x[1])

    temp = []
    for i in range(0, len(R)):
        temp.append(R[i][1])

    A = set(temp)

    for i in range(0, len(R)):
        if R[i][1] == list(A)[1]:
            print(R[i][0])
