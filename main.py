import word_counter
import character_counter
import comp_report



def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
    # Now call word_count and print the result
    # Can you add these lines?

    words = word_counter.word_count(file_contents)
    # print(words)

    count = character_counter.count_characters(file_contents)
    print(count)
    
    report = comp_report.comp_report(file_contents)
    # print(report)

main()