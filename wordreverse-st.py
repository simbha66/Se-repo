import streamlit as st

def reverse_words_in_sentence(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

def main():
    st.title("🔁 Reverse Words in a Sentence")

    st.write("This app reverses each word in your sentence but keeps the word order unchanged.")

    sentence = st.text_input("Enter your sentence:")

    if st.button("Reverse Words"):
        if sentence.strip() == "":
            st.warning("Please enter a sentence!")
        else:
            result = reverse_words_in_sentence(sentence)
            st.success(f"Reversed Sentence: {result}")

if __name__ == "__main__":
    main()
