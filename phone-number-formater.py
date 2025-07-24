import streamlit as st

def format_phone_number(number):
    # Clean input to contain only digits
    digits = ''.join(filter(str.isdigit, str(number)))
    
    if len(digits) != 10:
        return "❌ Please enter a valid 10-digit number."
    
    return f"📞 Formatted Number: ({digits[:3]}) {digits[3:6]}-{digits[6:]}"

# Streamlit app
st.set_page_config(page_title="Phone Number Formatter", page_icon="📱")
st.title("📱 Phone Number Formatter")
st.markdown("Enter a **10-digit number** below to format it as `(XXX) XXX-XXXX`.")

number_input = st.text_input("🔢 Enter your 10-digit number:")

if number_input:
    result = format_phone_number(number_input)
    st.success(result)