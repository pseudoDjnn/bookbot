from analyzers.text_analyzer import TextAnalyzer

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
    
    """

    Main Menu Display and input handling
    
    """
    
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
    try:
      if choice == "1":
        self.direct_text_input()
      elif choice == "2":
        self.file_text_input()
      elif choice == "3":
        print("\nShutting down now...")
        exit()
      else:
        print("\nInvalid response. Select...")

    except Exception as e:
      print(f"\nAn error occured: {str(e)}")
      
      """

      Direct Text Input Handler
      
      """
      
  def direct_text_input(self):
    print("\nEnter your text (press Enter twice to finish):")
    
    lines = []
    
    # Collect lines until empty line (double Enter) is received
    while True:
      line = input()
      # Break loop on empty line
      if line == "":
        break
      # Add non-empty line to the collection
      lines.append(line)
      
    # Join the lines with newline characters to create complete text
    self.text = "\n".join(lines)
    # Validate text is not whitespaced
    if self.text != self.text.strip():
      print("Error: Follow The Rules")
      return
    
    # Create TextAnalyzer instance with validated text
    self.analyzer = TextAnalyzer(self.text)
    
    # show analysis options menu
    self.show_analysis_menu()
  
  def file_text_input(self):
    pass
  
  def show_analysis_menu(self):
    pass