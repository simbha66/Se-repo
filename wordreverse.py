def reverse_words_in_sentence(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

if __name__ == "__main__":
    sentence = input("Enter a sentence: ").strip()
    result = reverse_words_in_sentence(sentence)
    print("Sentence with reversed words:", result)