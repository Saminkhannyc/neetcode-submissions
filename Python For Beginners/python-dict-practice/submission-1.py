from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    new_dict = {}
    for i in word:
        if i not in new_dict:
            new_dict[i]= 0
        new_dict[i] += 1
    return new_dict


# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
