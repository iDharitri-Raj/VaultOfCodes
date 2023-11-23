def count_word_frequencies(text):
    # Convert the text to lowercase to ensure case-insensitivity
    text = text.lower()

    # Remove punctuation and split the text into words
    words = [word.strip('.,?!') for word in text.split()]

    # Create a dictionary to store word frequencies
    word_freq = {}

    # Count the frequency of each word
    for word in words:
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq


input_text = input("Enter input text : ")
result = count_word_frequencies(input_text)

# Displaying the Word Frequencies
for word, frequency in result.items():
    print(f'Word: {word}, Frequency: {frequency}')
