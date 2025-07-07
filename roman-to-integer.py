def RomanToInt(s: str) -> int:
    num = list(s)
    list_of_nums = []

    for i in range(len(num)):
        match num[i]:
            case "I":
                list_of_nums.append(1)
            case "V":
                list_of_nums.append(5)
            case "X":
                list_of_nums.append(10)
            case "L":
                list_of_nums.append(50)
            case "C":
                list_of_nums.append(100)
            case "D":
                list_of_nums.append(500)
            case "M":
                list_of_nums.append(1000)

    print(list_of_nums)
    total = 0
    for i in range(len(list_of_nums) - 1):
        if list_of_nums[i] < list_of_nums[i+1]:
            total -= list_of_nums[i+1]
        else:
            total += list_of_nums[i]
    print(total + list_of_nums[-1])

RomanToInt("MCMXCIV")
