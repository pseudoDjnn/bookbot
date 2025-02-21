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
    print("\n[TEXT ANALYSIS SYSTEM]")
    print("=====================")
    print("INITIALIZING...")
    print("Status: ONLINE")
    print("=====================")
    
    self.show_main_menu()
    
    """

    Main Menu Display and input handling
    
    """
    
  def show_main_menu(self):
    
    while True:
      print("\n[TEXT ANALYSIS SYSTEM]")
      print("====================")
      print("\nSelect Input Method:")
      print("1.  Direct Text Input")
      print("2.  File Import")
      print("3.  Exit System")
        
      choice = input()
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
            print("\n[SYSTEM] Initiating shutdown sequence...")
            print("Status: OFFLINE")
            print("=====================")
            exit()
        else:
            print("\n[ERROR] Invalid selection")
            print("Please choose a valid option (1-3)")

    except Exception as e:
        print("\n[SYSTEM ERROR]")
        print("=====================")
        print(f"Error details: {str(e)}")
        print("Please try again")
      
        """

        Direct Text Input Handler
      
        """
      
  def direct_text_input(self):
    print("\n[TEXT ANALYSIS SYSTEM]")
    print("=====================")
    print("\nSelect analysis focus:")
    print("1. Word Usage & Patterns")
    print("   - Word frequency and distribution")
    print("   - Common phrases and patterns")
    
    print("\n2. Readability Assessment")
    print("   - Sentence structure")
    print("   - Text complexity")
    
    print("\n3. Statistical Overview")
    print("   - Word and sentence counts")
    print("   - Text composition metrics")
    
    while True:
      try:
          print("\nSelect analysis type (1-3): ", end='')
          analysis_type = int(input())
          if 1 <= analysis_type <= 3:
              break
          print("\n[ERROR] Please select a valid option (1-3)")
      except ValueError:
            print("\n[ERROR] Please enter a number between 1-3")
    
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