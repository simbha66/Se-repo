def count_vowels(word):
    vowels = set("aeiouAEIOU")
    count = sum(1 for char in word if char in vowels)
    return count
if __name__ == "__main__":
    word = input("Enter a word: ").strip()
    vowel_count = count_vowels(word)
    print(f"The word '{word}' contains {vowel_count} vowel(s).")

