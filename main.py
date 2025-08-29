from stats import words_in_book, get_char, dict_to_sorted_list
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        text = get_book_text(path)
        print("===========BOOKBOT============")
        print(f"Analyzing book found at {path}...")
        print("---------Word Count-----------")
        print(f"Found {words_in_book(text)} total words")
        print("------ Character Count -------")
        first_dic = get_char(text)
        last_dictionary = dict_to_sorted_list(first_dic)
        for each in last_dictionary:
            if each["char"].isalpha():
                print(f"{each["char"]}: {each["num"]}")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
     
main()