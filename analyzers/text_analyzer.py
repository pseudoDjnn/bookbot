# analyzers/text_analyzer.py
from .total_word_counter import count_total_words
from .total_char_counter import count_total_chars
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
            self.word_count = count_total_words(self.text)
        return self.word_count