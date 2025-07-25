import streamlit as st

def count_vowels(word):
    vowels = set("aeiouAEIOU")
    count = sum(1 for char in word if char in vowels)
    return count

# Streamlit Web App
st.title("🔠 Vowel Counter App")
st.write("Enter a word, and I'll count how many vowels it contains!")

word = st.text_input("Enter a word:")

if word:
    vowel_count = count_vowels(word)
    st.success(f"The word **'{word}'** contains **{vowel_count}** vowel(s).")