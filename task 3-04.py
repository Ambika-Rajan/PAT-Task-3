def sum_of_first_and_last_digit(n):
    # convert the input number to a string
    str_n = str(n)

    # extract the first and last digit
    first_digit = int(str_n[0])
    last_digit = int(str_n[-1])

    # add the first and last digit
    sum = first_digit + last_digit

    # return the sum
    return sum


# Example
n = 1247
result = sum_of_first_and_last_digit(n)
print(result)
