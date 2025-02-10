def count_characters():

def word_count(words):
    result = words.split()
    return len(result)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    # Now call word_count and print the result
    # Can you add these lines?

    result = word_count(file_contents)
    print(result)

main()