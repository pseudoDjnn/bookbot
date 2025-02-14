import count_characters


def comp_report(char_counts):
  result = []

  char_count = count_characters.count_characters(char_counts)

  container = []

  for char, num in char_count.items():
    if char.isalpha():
      container.append({"char": char, "num": num})

  # Using .sort()
  def sort_on(dict):
    return dict["num"]

  container.sort(key=sort_on, reverse=True)

  # Lambda
  # container.sort(key=lambda x: x["num"], reverse=True)

  for content in container:
    final_string = f"The '{content['char']}' character was found {content['num']} times"
    result.append(final_string)
  
  return result