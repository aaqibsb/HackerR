def lucky_number(nums):
    value = False
    if nums == []:
        print("n")
        return value
    else:
        for num in nums:
            if num % 7 == 0:
                value = True
                return value
        return value


print(lucky_number([2,4]))