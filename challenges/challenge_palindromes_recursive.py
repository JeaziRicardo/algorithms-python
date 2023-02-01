def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    elif high_index == 0:
        return True
    elif word[low_index].lower() != word[high_index].lower():
        return False
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
