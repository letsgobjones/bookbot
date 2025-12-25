def get_num_words(path_to_file): 
    with open(path_to_file) as f:
        file_contents = f.read()
        words_split = file_contents.split()
        num_words = len(words_split)
        print(f"Found {num_words} total words")


def get_char_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        lower_case_text = file_contents.lower()
            
        char_dict: dict[str, int] = {} 
        for char in lower_case_text:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

        return char_dict



def sort_on(dict_item):
    return dict_item["num"]


def sort_list(path_to_file):
   unsorted_dict = get_char_count(path_to_file)
   
   char_list = []
   for char in unsorted_dict:
    if char.isalpha():
        char_list.append({"char": char, "num" : unsorted_dict[char]})
    char_list.sort(reverse=True, key=sort_on)

   for char in char_list:
    print(f"{char["char"]}: {char["num"]}")