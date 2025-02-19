def count_total_chars(text):
  result = {}
  for letter in text:

    # print(letter)
    lower_letter = letter.lower()

    if lower_letter in result:
      result[lower_letter] += 1
    else:
      result[lower_letter] = 1

  return result