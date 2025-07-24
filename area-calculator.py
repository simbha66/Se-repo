import streamlit as st
import math

# Area functions
def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

# Streamlit App UI
st.set_page_config(page_title="Area Calculator", page_icon="📐")
st.title("📏 Area Calculator")

# Shape selection
shape = st.selectbox("Choose a shape", ["Circle", "Rectangle", "Triangle"])

if shape == "Circle":
    radius = st.number_input("Enter radius (cm):", min_value=0.0, format="%.2f")
    if st.button("Calculate Area"):
        area = area_circle(radius)
        st.success(f"Area of Circle: {area:.2f} cm²")

elif shape == "Rectangle":
    length = st.number_input("Enter length (cm):", min_value=0.0, format="%.2f")
    width = st.number_input("Enter width (cm):", min_value=0.0, format="%.2f")
    if st.button("Calculate Area"):
        area = area_rectangle(length, width)
        st.success(f"Area of Rectangle: {area:.2f} c
