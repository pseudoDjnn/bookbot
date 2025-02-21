def welcome_display():
  """

  Initial Welcome Banner
  
  """
  
  print("\nWelcome to the Text Analyzer")
  print("----------------------------")
  
  while True:
    print("\nPlease select option:")
    print("1.  Input text directly")
    print("2.  Load text from file")
    print("3.  Exit")
    
    choice = input("\nEnter choice (1-3): ")