from stats import words_in_book, get_char

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    print("===========BOOKBOT============")
    print(f"Analyzing book found at {path}...")
    print("---------Word Count-----------")
    print(f"Found {words_in_book(text)} total words")
    print("------ Character Count -------")
    last_dictionary = get_char(text)
    for each in last_dictionary:
        print(f"{each}: {last_dictionary[each]}")
     
main()