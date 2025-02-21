
# main.py
from analyzers import TextAnalyzer
from utils import welcome_display

def main():
    welcome_display()
    
    # Read Frankenstein and soon to be other .txt files
    with open('books/frankenstein.txt') as file:
        file_contents = file.read()
    
    # Create analyzer instance with text
    analyzer = TextAnalyzer(file_contents)
    print(f"Word count analysis: {analyzer.get_char_frequency()}")

main()