from .text_analyzer import  TextAnalyzer

"""

Initialize with the ratio of the original text to keep in summary

Args:
  ratio: Float between 0 and 1 representing the proportion of sentences to keep in the summary

"""

class SummrizationAnalyzer(TextAnalyzer):
  def __init__(self, text):
    super().__init__(text)
    
    
  def analyze(self):
    # Impplementation will go here
    pass
  
  
  def _preprocess(self, text):
    # Split into sentences, tokenize, etc...
    pass
  
  def _score_sentences(self, sentences):
    # Score each sentence based on importance
    pass