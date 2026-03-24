# Видалення знаків пунктуації з рядка: ,.?!;:
def remove_punctuation(string: str):
    punctuation = ",.?!;:"

    for char in punctuation:
        string = string.replace(char, "")

    return string


def count_vowels(string: str):
    count = 0
    litter = "aeiou"

    for char in string:
        if char.lower() in litter:
            count += 1

    return count


def is_palindrome(text):
    cleaned = text.replace(" ", "")

    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    text = "Hello ,,,:World"

    print(count_vowels(text))
    print(is_palindrome(text))
    print(remove_punctuation(text))
