from stats import get_num_words
from stats import count_characters
from stats import sort_characters

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    print("============ BOOKBOT ============")

    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print(f"--------- Character Count -------")
    characters_in_book_text = count_characters(book_text)
    characters_list = sort_characters(characters_in_book_text)
    for c in characters_list:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")
    print("============== END ==============")
main()