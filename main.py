
# main.py
from analyzers import TextAnalyzer
from utils import TextAnalyzerInterface

def main():
    interface = TextAnalyzerInterface()
    
    # Read Frankenstein and soon to be other .txt files
    with open('books/frankenstein.txt') as file:
        file_contents = file.read()
    

main()