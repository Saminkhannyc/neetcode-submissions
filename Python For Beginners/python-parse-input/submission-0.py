from typing import List

def read_integers() -> List[int]:
    line = input()
    list_of_strings = line.split(",")
    list_of_integers = []

    for string in list_of_strings:
        list_of_integers.append(int(string))
    return list_of_integers

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
