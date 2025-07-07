def isPalindrome(num: int) -> bool:
    number = str(num)
    num_list = list(number)
    number_reverse = reversed(number)
    number_reverse_list = list(number_reverse)

    if number_reverse_list == num_list:
        return True
    else:
        return False

