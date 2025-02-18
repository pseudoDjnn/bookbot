import argparse

from word_counter import word_count
from character_counter import count_characters
from comp_report import comp_report


def parser():
    parse = argparse.ArgumentParser(description='A BookBot: A text analysis tool')
    parse.add_argument('book', help='Path to the book file to analyze')
    return parse.parse_args()



def main():
    
    search = parser()
    
    with open(search.book) as file:
        file_contents = file.read()
    # Now call word_count and print the result
    # Can you add these lines?

    words = word_count(file_contents)
    print(words)

    count = count_characters(file_contents)
    # print(count)
    
    report = comp_report(file_contents)
    # print(report)

main()