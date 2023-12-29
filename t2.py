# Task: Create a function that reverses the words in a given sentence

def reversed_sentence(sentence):
    words = sentence.split()
    # Use Copilot to complete the code to reverse the words in the sentence
    reversed_sentence = ' '.join(reversed(words))
    # TODO: Return the reversed sentence
    return reversed_sentence
# Example usage:
input_sentence = "This is an example sentence."
reversed_result = reversed_sentence(input_sentence)
print("Original sentence:", input_sentence)
print("Reversed sentence:", reversed_result)
