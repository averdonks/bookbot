def get_num_words(book_text):
    word_list = book_text.split()
    return len(word_list)

# Add each unique character from the provided book text
# into a dictionary. The key is the character and,
# the value (count) starts at 1. Increment the value by one for
# all duplicate characters.
def get_characters_dict(book_text):
    characters = {}
    for c in book_text:
        lower_c = c.lower()
        if lower_c in characters:
            characters[lower_c] += 1
        else:
            characters[lower_c] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def characters_dict_to_sorted_list(characters_dict):
    sorted_list = []
    for char in characters_dict:
        sorted_list.append({"char": char, "num": characters_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list