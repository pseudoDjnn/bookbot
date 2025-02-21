
# main.py
from analyzers import TextAnalyzer
from utils import TextAnalyzerInterface

def main():
    interface = TextAnalyzerInterface()
    # interface.welcome_display()
    
    # Read Frankenstein and soon to be other .txt files
    with open('books/frankenstein.txt') as file:
        file_contents = file.read()
    
    # Create analyzer instance with text
    analyzer = TextAnalyzer(file_contents)
    print(analyzer.get_char_frequency())

main()