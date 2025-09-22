def count_words(string):
    words = string.split()
    return len(words)

def count_chars(string):
    result = {}

    for char in string:
        lower_char = char.lower()

        if lower_char in result:
            result[lower_char] += 1
            continue

        result[lower_char] = 1

    return result

def sort_on(items):
    return items["num"]

def get_char_report_data(charcter_dict):
    result = []
    for char in charcter_dict:
        result.append({ "char": char, "num": charcter_dict[char]})

    result.sort(reverse=True, key=sort_on)
    return result 
