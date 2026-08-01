def add_two_numbers() -> int:
    line = input()
    list_of_strings = line.split(",")
    sum = 0
    for string in list_of_strings:
        int(string)
        sum += int(string)
    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
