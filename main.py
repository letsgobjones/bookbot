from stats import get_num_words, get_char_count, sort_list
import sys






def main():
    # book_text = get_book_text("books/frankenstein.txt")
    
  # get_num_words("books/frankenstein.txt")
  # file_path = input("Please enter the file path: ")
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  file_path = sys.argv[1]


  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {file_path}...")
  print("----------- Word Count ----------")
  get_num_words(file_path)
  print("--------- Character Count -------")
  sort_list(file_path)


  print("============ BOOKBOT ============")


main()