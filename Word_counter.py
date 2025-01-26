# Function to count the number of words in the given text
def count_words(text):
    # Split the text by whitespace and count the number of words
    words = text.split()
    return len(words)

# Main program logic
def main():

    user_input = input("Please enter a sentence or paragraph: ")


    if not user_input.strip():
        print("Error: Please enter a valid sentence or paragraph.")
        return

    # Count the words using the count_words function
    word_count = count_words(user_input)

    # Display the word count
    print(f"The total word count is: {word_count}")

if __name__ == "__main__":
    main()
