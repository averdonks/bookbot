def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(book_text):
    word_list = book_text.split()
    return len(word_list)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"{get_num_words(book_text)} words found in the document")

main()