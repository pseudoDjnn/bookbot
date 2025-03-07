from .text_analyzer import TextAnalyzer


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
            
    def analyze(self):
        if self.word_count is None:
            words = self.text.split() 
            self.word_count = len(words)
        return self.word_count



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
        
    def analyze(self):
        if self.char_count is None:
            self.char_count  = {}
            for char in self.text:
                lower_char = char.lower()
                
                if lower_char in self.char_count:
                    self.char_count[lower_char] += 1
                else:
                    self.char_count[lower_char] = 1
                    
        return self.char_count


"""

Initialize with the text to analyze and format character count for display.

"""


class CharacterDisplayFormatter(TextAnalyzer):
    def __init__(self, text):
        super().__init__(text)
        self.formatted_char_count = None
        self.char_count_analyzer = CharacterCountAnalyzer(text)

    """

    Formats character count data into strings, sorted by frequency.

    """
        
    def analyze(self):
        if self.formatted_char_count is None:
            char_count = self.char_count_analyzer.analyze()
            self.formatted_char_count = []
            
            # Sort characters by frequency, descending
            sorted_char = sorted(
                char_count.items(), key=lambda x: x[1], reverse=True
            )[:50]
            
            # Store as a dictionary
            self.formatted_char_count = {char: count for char, count in sorted_char}
                    
                
        return self.formatted_char_count


"""

Initializes the count for the total amount of sentences and caches it

"""
class SentenceCountAnalyzer(TextAnalyzer):
  def __init__(self, text):
      super().__init__(text)
      self.sentence_count = None
      
  """
  
  Count the number of sentences in the text
  
  """
  def analyze(self):
    if self.sentence_count is None:
        count = 0
        in_sentence = False

        for char in self.text:
            if char in [".", "!", "?"]:
                if in_sentence:
                    count += 1
                    in_sentence = False
          
            elif char.strip():
                in_sentence = True
            
        if in_sentence:
          count += 1
          
        self.sentence_count = count
    return self.sentence_count


"""

Initialize the count for total amounts of an individual word being used throughout a book or text (meant for literature mainly)

"""
class WordFrequencyAnalyzer(TextAnalyzer):
    def __init__(self, text):
        super().__init__(text)
        self.individual_word = None
        
    """

    The method for the count to take place
    
    """ 
    def analyze(self):
        if self.individual_word is None:
            # Convert to lowercase to make everything eassier to grab
            words = self.text.lower()

            # Define any punctuation to remove
            punctuations = ",.;:!?\"'({)[]}-_`~@#$%^&*+=|\\/<>"
            
            # Remove each punctuation
            for punctuation in punctuations:
                words = words.replace(punctuation, ' ')
                
            # Split into words after removing all punctuation
            normalized_text = words.split()
            
            # initialize a dictionary for word counts
            self.individual_word = {}

            # Count how many times a word occurs
            for word in normalized_text:
                if word in self.individual_word:
                    self.individual_word[word] += 1
                else:
                    self.individual_word[word] = 1
                    
        # Sort the infor again for the jinja html
        sorted_words = dict(sorted(self.individual_word.items(), key=lambda x: x[1], reverse=True)[:50])
        return sorted_words