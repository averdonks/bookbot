from stats import get_num_words
from stats import get_characters_dict
from stats import characters_dict_to_sorted_list

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
    characters_in_book_text = get_characters_dict(book_text)
    characters_list = characters_dict_to_sorted_list(characters_in_book_text)
    for c in characters_list:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")
    print("============== END ==============")
main()