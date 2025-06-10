def get_num_words(book_text):
    word_list = book_text.split()
    return len(word_list)

# Add each unique character from the provided book text
# into a dictionary. The key is the character and,
# the value (count) starts at 1. Increment the value by one for
# all duplicate characters.
def count_characters(book_text):
    characters = {}
    for c in book_text:
        lower_c = c.lower()
        if lower_c in characters:
            characters[lower_c] += 1
        else:
            characters[lower_c] = 1
    return characters

def sort_characters(characters):

    def sort_on(dict):
        return dict["num"]

    characters_list = []
    for character in characters:
        c = dict()
        c["char"] = character
        c["num"] = characters[character] 
        characters_list.append(c)
        characters_list.sort(reverse=True, key=sort_on)
    return characters_list