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

    result = count_characters(file_contents)
    print(result)

main()