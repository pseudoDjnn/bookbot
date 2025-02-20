# analyzers/text_analyzer.py
# from .total_word_counter import count_total_words
# from .total_char_counter import count_total_chars
from .char_frequency_analyzer import analyze_char_frequency

class TextAnalyzer:
    # Your TextAnalyzer class implementation
    def __init__(self, text):
        self.text = text
        self.word_count = None
        self.char_count = None
        self.char_frequency = None 
        
    def analyze_all(self):
        # This just orchestrates the individual methods
        self.get_word_count()
        
        
    def get_word_count(self):
        if self.word_count is None:
            # Move the word counting logic here
            words = self.text.split()
            self.word_count = len(words)
        return self.word_count
    
    def get_char_count(self):
        if self.char_count is None:
            self.char_count  = {}
            for char in self.text:
                lower_char = char.lower()
                
                if lower_char in self.char_count:
                    self.char_count[lower_char] += 1
                else:
                    self.char_count[lower_char] = 1
            return self.char_count
