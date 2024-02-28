
def main():
   create_report("./books/frankenstein.txt")


def create_report(book_path):
    
    print(f"--- Analyzing document contents of {book_path} ---")
    file_contents = read_book(book_path)
    
    num_words = get_num_words(file_contents)
    print(f"The document contains {num_words} words!")
    letter_count = get_letter_count(file_contents)
    sorted_list = chars_dict_to_sorted_list(letter_count)
    print_letter_count(sorted_list)

    print("--- Document Analysis complete ---")

def read_book(book_path):
    with open(book_path) as f:
        contents = f.read()
        return contents

def get_num_words(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    lowered = text.lower()
    letter_count = {}
    for letter in lowered:
        if letter.isalpha():
            if(letter in letter_count):
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count

def print_letter_count(letters):
    for letter in letters:
        print(f"The character {letter["char"]} is found {letter["num"]} times in the document")



def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    #make the empty list
    sorted_list = []
    #iterate over the dictionary
    for ch in num_chars_dict:
        #add new entry for each letter as it's own dictionary with num/char keys
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    #sort the list according to the previously definined "sort_on" function
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()