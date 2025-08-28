from stats import words_in_book

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    print(f"{words_in_book(text)} words found in the document")  
     
main()