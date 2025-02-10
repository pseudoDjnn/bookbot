def comp_report(char_counts):
  result = []

  char_count = count_characters(char_counts)

  char_list = []
  for char, count in char_count.items():
    if char.isalpha():
      char_list.append({"char": char, "num": count})

  char_list.sort(key=lambda x: x["num"], reverse=True)

  for item in char_list:
    formatted = f"The '{item['char']}' character was found {item['num']} times"
    result.append(formatted)
  
  return result

def count_characters(text):
  result = {}
  for t in text:

    # print(t)
    lower_t = t.lower()

    if lower_t in result:
      result[lower_t] += 1
    else:
      result[lower_t] = 1

  return result

def word_count(words):
    result = words.split()
    return len(result)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    # Now call word_count and print the result
    # Can you add these lines?

    result = comp_report(file_contents)
    print(result)

main()