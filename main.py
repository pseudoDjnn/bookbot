from word_counter import word_count
from character_counter import count_characters
from comp_report import comp_report



def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
    # Now call word_count and print the result
    # Can you add these lines?

    words = word_count(file_contents)
    # print(words)

    count = count_characters(file_contents)
    # print(count)
    
    report = comp_report(file_contents)
    print(report)

main()