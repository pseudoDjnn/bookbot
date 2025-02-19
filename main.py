
# main.py
from analyzers import TextAnalyzer
from utils import setup_text_analyzer_cli






def main():
    
    search = setup_text_analyzer_cli()
    
    with open(search.book) as file:
        file_contents = file.read()
    # Now call word_count and print the result
    # Can you add these lines?

    # words = count_total_words(file_contents)
    # print(words)

    # count = count_total_chars(file_contents)
    # print(count)
    
    # report = analyze_char_frequency(file_contents)
    # print(report)

main()