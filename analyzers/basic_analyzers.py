from text_analyzer import TextAnalyzer


"""
    
Analyzer for counting total words in the provided text.
Caches the result for efficiency.
    
"""
        
    
class WordCountAnalyzer(TextAnalyzer):
    def __init__(self, text):
        super().__init__(text)
        # Caches the word count to avoid recalculating
        self.word_count = None

        """
                
        Calculates and caches the total word count from the `text`.
        If already calcuated, return the cached result.
                
        """
            
    def get_word_count(self):
        if self.word_count is None:
            words = self.text.split() 
            self.word_count = len(words)
        return self.word_count
        
        
    def analyze(self):
        """

        Return the analysis as a dictionary
        
        """
        
        return {
            "Total Word Count": self.get_word_count(),
            }


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
        return {"Character Count": self.get_char_count()}


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
            
            frequency_data.sort(
                key=lambda x: x["Numbers"],
                reverse=True
                )
            
            
            for data in frequency_data:
                result = f"Characters: '{data['Characters']}' Count: {data['Numbers']}"
                self.char_frequency.append(result)
                
            return self.char_frequency

    def analyze(self):
        return {"Character Frequency": self.get_char_frequency()}


