from stats import get_num_words
from stats import count_characters

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"{get_num_words(book_text)} words found in the document")
    characters_in_book_text = count_characters(book_text)
    print(characters_in_book_text)

main()