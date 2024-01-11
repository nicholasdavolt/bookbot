from operator import itemgetter
def main():
   book_path = "books/frankenstein.txt"
   text = get_text(book_path)
   num_words = wordcount(text)
   print(f"--- Begin report of {book_path}")
   print(f"{num_words} words found in the document\n\n\n\n") 
   character_count = get_character_count(text)
   report_list = generate_char_report(character_count)
   for item in report_list:
       key, value = item
       if key.isalpha():
           print(f"The '{key}' character was found {value} times")

def wordcount(text):
    words_count =  len(text.split())
    return words_count

def get_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    char_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

def generate_char_report(char_dict):
    result = [(key, value) for key, value in char_dict.items()]
    result.sort(key=itemgetter(1), reverse= True)
    return result

main()