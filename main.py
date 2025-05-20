from stats import get_num_words, get_chars_dict, char_report
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path=sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}... \n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
    report = char_report(chars_dict)
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()