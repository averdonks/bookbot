import sys

from pathlib import Path

from stats import (
  get_num_words,
  get_characters_dict,
  characters_dict_to_sorted_list  
)

# Checks if the user entered two arguments
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
# Checks if the user entered a .txt file into the second argument
if Path(sys.argv[1]).suffix != ".txt":
    print("Error: The book must be a .txt file")
    sys.exit(1)

# Opens and reads the book text
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

# Prints a report 
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
    path_to_book = sys.argv[1]
    book_text = get_book_text(path_to_book)
    num_words = get_num_words(book_text)
    characters_dict = get_characters_dict(book_text)
    characters_sorted_list = characters_dict_to_sorted_list(characters_dict)
    print_report(path_to_book, num_words, characters_sorted_list)

main()