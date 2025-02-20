
# main.py
from analyzers import TextAnalyzer
from utils import setup_text_analyzer_cli

def main():
    
    # Read Frankenstein and soon to be other .txt files
    with open('books/frankenstein.txt') as file:
        file_contents = file.read()
    
    # Create analyzer instance with text
    analyzer = TextAnalyzer(file_contents)
    print(f"Word count analysis: {analyzer.get_word_count()}")

main()