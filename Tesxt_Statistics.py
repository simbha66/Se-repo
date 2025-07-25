import re

def get_text_statistics(text):
    # Count characters (excluding spaces)
    characters = len(text.replace(" ", ""))
    
    # Count words
    words = len(text.split())
    
    # Count sentences using punctuation as delimiter
    sentences = len(re.findall(r'[.!?]+', text))
    
    return {
        "Characters (no spaces)": characters,
        "Words": words,
        "Sentences": sentences
    }

if __name__ == "__main__":
    paragraph = input("Enter a paragraph:\n")
    stats = get_text_statistics(paragraph)
    
    print("\n📊 Text Statistics:")
    for key, value in stats.items():
        print(f"{key}: {value}")
