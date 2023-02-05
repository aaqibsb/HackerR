def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        l = len("{0:b}".format(n))
        print("{0:{l}d} {0:{l}o} {0:{l}x} {0:{l}b}".format(i,l=l))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    # print(str(bin(2)))