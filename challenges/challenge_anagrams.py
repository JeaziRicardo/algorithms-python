def merge_sort(left, right, string):
    char_list = list(string)
    left_part, right_part = 0, 0

    while left_part < len(left) and right_part < len(right):

        if left[left_part] <= right[right_part]:
            char_list[left_part + right_part] = left[left_part]
            left_part += 1
        else:
            char_list[left_part + right_part] = right[right_part]
            right_part += 1

    for left_part in range(left_part, len(left)):
        char_list[left_part + right_part] = left[left_part]

    for right_part in range(right_part, len(right)):
        char_list[left_part + right_part] = right[right_part]

    return "".join(char_list)


def split_string(string):
    if len(string) < 2:
        return string

    mid = len(string) // 2
    left = split_string(string[:mid])
    right = split_string(string[mid:])

    return merge_sort(left, right, string)


def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()

    sorted_first_string = split_string(first_string)
    sorted_second_string = split_string(second_string)

    if not sorted_first_string or not sorted_second_string:
        return (sorted_first_string, sorted_second_string, False)

    return (
        sorted_first_string,
        sorted_second_string,
        sorted_first_string == sorted_second_string,
    )
