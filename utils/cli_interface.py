from pathlib import Path

from analyzers.text_analyzer import TextAnalyzer

class TextAnalyzerInterface:
  def __init__(self):
    # This will be the TextAnalyzer instance
    self.analyzer = None
    self.text = None

