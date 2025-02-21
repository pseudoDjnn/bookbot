
# main.py
# from analyzers import TextAnalyzer
from utils import TextAnalyzerInterface

def main():
    interface = TextAnalyzerInterface()
    interface.welcome_display()
    
if __name__ == "__main__":
    main()