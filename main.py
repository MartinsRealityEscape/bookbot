from stats import count_words, count_chars, get_char_report_data
import sys

def get_book_text(file_path):
    try:
        with open(file_path) as f:
            return f.read()
    except Exception as ex:
        print(ex)
        return


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    
    
    book_text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")

    char_data = get_char_report_data(count_chars(book_text))

    for dict in char_data:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")


main()