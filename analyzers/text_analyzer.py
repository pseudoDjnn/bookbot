class TextAnalyzer:
    # Your TextAnalyzer class implementation
    def __init__(self, text):
        self.text = text
        self.word_count = None
        print(f"Debug: Text analyzer initialized with {len(text)} characters")  # Debug line


        self.char_count = None
        self.char_frequency = None 
        
    def analyze_all(self):
        # This just orchestrates the individual methods
        self.get_word_count()
        
        
    """
        
    Calculates and caches the total word count from the text
        
    """
        
    def get_word_count(self):
        if self.word_count is None:
            words = self.text.split()
            self.word_count = len(words)
        return self.word_count
    
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
    
    """

    Calculates and caches the total letter count frequency from the test and places it into a dictionay list
    
    """
        
    def get_char_frequency(self):
        # pass
        if self.char_frequency is None:
            self.char_frequency = []
            
            char_count = self.get_char_count()
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
                