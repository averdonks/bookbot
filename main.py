from stats import (
  get_num_words,
  get_characters_dict,
  characters_dict_to_sorted_list  
)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def print_report(path_to_book, num_words, characters_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for dict in characters_sorted_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============== END ==============")

def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    num_words = get_num_words(book_text)
    characters_dict = get_characters_dict(book_text)
    characters_sorted_list = characters_dict_to_sorted_list(characters_dict)
    print_report(path_to_book, num_words, characters_sorted_list)

main()