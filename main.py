from stats import get_chars_dict, get_num_words, chars_dict_to_sorted_list
import sys


def main():
    # book_text = get_book_text("books/frankenstein.txt")
    #
    # get_num_words("books/frankenstein.txt")
    # file_path = input("Please enter the file path: ")

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    text = get_book_text(file_path)
    word_count = get_num_words(text)
    char_dict = get_chars_dict(text)
    sorted_char_list = chars_dict_to_sorted_list(char_dict)
    print_report(file_path, word_count, sorted_char_list)

    # print("============ BOOKBOT ============")
    # print(f"Analyzing book found at {file_path}...")
    #
    # print("----------- Word Count ----------")
    # num_count = get_num_words(file_path)
    # print(f"Found {num_count} total words")
    #
    # print("--------- Character Count -------")
    # char_dict = get_char_count(file_path)
    # sorted_char_list = chars_dict_to_sorted_list(char_dict)
    # for char, count in sorted_char_list:
    #     print(f"{char}: {count}")
    #
    # print("============ BOOKBOT ============")


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def print_report(
    book_path: str, word_count: int, sorted_char_list: list[tuple[str, int]]
):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for char, count in sorted_char_list:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")

    print("============ BOOKBOT ============")


main()
