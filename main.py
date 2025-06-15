import sys

from stats import get_book_text, get_num_words, letter_count, chars_dict_to_list
def main(book_path):
    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    word_count = get_num_words(book_text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_counts = letter_count(book_text)
    letter_list = chars_dict_to_list(char_counts)
    for item in letter_list:
                character = item["char"]
                count = item["num"]
                if character.isalpha():
                    print(f"{character}: {count}")
    print("============= END ===============")
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])
