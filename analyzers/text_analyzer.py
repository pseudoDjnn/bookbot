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
        """
        
        Calculates and caches the total word count from the text
        
        """
        if self.word_count is None:
            # Move the word counting logic here
            words = self.text.split()
            self.word_count = len(words)
        return self.word_count
    
    def get_char_count(self):
        """

        Calculates and caches the total letter count from the test and
        places it into a dictionary
        
        """
        if self.char_count is None:
            self.char_count  = {}
            for char in self.text:
                lower_char = char.lower()
                
                if lower_char in self.char_count:
                    self.char_count[lower_char] += 1
                else:
                    self.char_count[lower_char] = 1
        return self.char_count
        
    def get_char_frequency(self):
        # pass
        if self.char_frequency is None:
            self.char_frequency = []
            
            char_count = self.get_char_count()
            # print(f"char_count contains: {char_count}")
            
            container = []

            for char, num in char_count.items():
                if char.isalpha():
                    container.append({"Characters": char, "Numbers": num})
                    
            # Use .sort()
            # def sort_on(self, dict):
                # return dict["Numbers"]
            
            container.sort(key=lambda x: x["Numbers"], reverse=True)
            
            
            for content in container:
                result = f"The '{content['Characters']}' character was found {content['Numbers']} times"
                self.char_frequency.append(result)
                
            return self.char_frequency
                