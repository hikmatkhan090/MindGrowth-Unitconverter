import streamlit as st

st.title("🌟 The Unit Converter App By Hikmat Khan")
st.markdown("### Converts Length, Weight And Time Instatnly")
st.write("Welcome🥰! Select a type of category , enter a value and get the converted result in real-time.")

category = st.selectbox("Select a Category", ["Length", "Weight", "Time"])


def convert_units(category, value, unit):
    if category == "Kilometers to Miles":
        return value * 0.621371
    elif unit == "Miles to Kilometers":
        return value / 1.60934
    
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
        elif category == "Time":
            if unit == "Seconds to Minutes":
                return value / 60
            elif unit == "Minutes to Seconds":
                return value * 60
            elif unit == "Minutes to Hours":
                return value / 60
            elif unit == "Hours to Minutes":
                return value * 60
            elif unit == "Hours to Days":
                return value / 24
            elif unit == "Days to Hours":
                return value * 24
    return 0
            
if category == "Length":
    unit = st.selectbox("📏 Select Conversation", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox(" ⚖️ Select Conversation", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⏰ Select Conversation", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])                
    
value = st.number_input("Enter the  Value to Convert")  

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")
