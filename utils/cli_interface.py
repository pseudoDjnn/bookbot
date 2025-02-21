class TextAnalyzerInterface:
  def __init__(self):
    # This will be the TextAnalyzer instance once we have text
    self.analyzer = None
    self.text = None

    """

    Initial Welcome Banner
    
    """
    
  def welcome_display(self):
    
    print("\nWelcome to the Text Analyzer")
    print("----------------------------")
    
    self.show_main_menu()
    
  def show_main_menu(self):
    
    while True:
      print("\nPlease select option:")
      print("1.  Input text directly")
      print("2.  Load text from file")
      print("3.  Exit")
        
      choice = input("\nEnter choice (1-3): ")
      self.handle_choice(choice)
        
      """

      Once we get valid text, we will create a TextAnayzer instance
      self.analyzer = TextAnalyzer(self.text)
      The we can call the existing analysis methods
      
      """
      
  def handle_choice(self, choice):
    pass