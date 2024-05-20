def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(words[::-1])
    return reversed_sentence

if __name__ == "__main__":
    print("Sentences\n\n ")
    sentence = input("Enter a sentence: ")
    reversed_sentence = reverse_sentence(sentence)
    print("Reversed sentence:", reversed_sentence)