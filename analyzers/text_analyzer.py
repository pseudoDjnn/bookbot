class TextAnalyzer:
    # Your TextAnalyzer class implementation
    def __init__(self, text):
        # Initialize with the text to be analyzed
        self.text = text
                    
    """

    Clean the text by lowercasing and stirpping whitespace.
    This method can be overridden by child classes if they need more specific preprocessing.
    
    """
    def clean_text(self):
        return self.text.lower().strip()
    
    """
    
    Tokenize the text into words by splitting on whitespace.
    Override this method in child classes for more complex tokenization (e.g. using NLP libraries).

    """
    def word_tokenization(self):
        return self.clean_text().split()
    
    """

    Abstract method placeholder for child classes.
    Forces child classes to implement their own analytics.
    
    """
    def analyze(self):
        raise NotImplementedError("Child classes must implement the 'analyze' method")
             
        
"""
    
Initialize with the text to analyze and prepare to cache the word count.
    
"""
    
class WordCountAnalyzer(TextAnalyzer):
    def __init__(self, text):
        super().__init__(text)
        self.word_count = None

    """
            
    Calculates and caches the total word count from the text
            
    """
            
    def get_word_count(self):
        if self.word_count is None:
            words = self.text.split()
            self.word_count = len(words)
        return self.word_count
        
        
    def analyze(self):
        return{"total word count": self.get_word_count()}


"""

Initialize with the text to analyze and prepare the character count cache.

"""


class CharacterCountAnalyzer(TextAnalyzer):
    def __init__(self, text):
        super().__init__(text)
        self.char_count = None
        
    """

    Calculates and caches the total letter count from the test and
    places it into a dictionary
        
    """
        
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

    def analyze(self):
        return {"character_count": self.get_char_count()}


"""

Initialize with the text to analyze and prepare the character count frequency cache.

"""
class CharacterFrequencyAnalyzer(TextAnalyzer):
    def __init__(self, text):
        super().__init__(text)
        self.char_frequency = None
        self.char_count_analyzer = CharacterCountAnalyzer(text)

    """

    Calculates and caches the total letter count frequency from the test and places it into a dictionay list

    """
        
    def get_char_frequency(self):
        # pass
        if self.char_frequency is None:
            self.char_frequency = []
            
            char_count = self.char_count_analyzer.get_char_count()
            # print(f"char_count contains: {char_count}")
            
            frequency_data = []

            for char, num in char_count.items():
                if char.isalpha():
                    frequency_data.append({
                        "Characters": char,
                        "Numbers": num
                        })
            
            frequency_data.sort(key=lambda x: x["Numbers"], reverse=True)
            
            
            for data in frequency_data:
                result = f"The '{data['Characters']}' character was found {data['Numbers']} times"
                self.char_frequency.append(result)
                
            return self.char_frequency
        
    def analyze(self):
        return {"character_frequency_count": self.get_char_frequency()}
                