import subprocess
import platform
import os

from analyzers.text_analyzer import TextAnalyzer

class TextAnalyzerInterface:
  def __init__(self):
    # This will be the TextAnalyzer instance
    self.analyzer = None
    
  def open_system_file_explorer(self):
    # system = platform.system()
    pass