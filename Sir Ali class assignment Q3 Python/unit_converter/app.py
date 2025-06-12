import streamlit as st

# 🏷️ App ka Title
st.title("🔄 Unit Converter")

# 📌 Conversion Types
conversion_types = ["📏 Length", "⚖️ Weight", "🌡️ Temperature"]
conversion_select = st.selectbox("⚙️ Select Conversion Type:", conversion_types)

# 📏 Length Conversion
if conversion_select == "📏 Length":
    length_units = ["Meters", "Kilometers", "Feet", "Inches", "Centimeters"]
    input_value = st.number_input("🔢 Enter Length Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("🔀 From Unit:", length_units)
    to_unit = st.selectbox("🔁 To Unit:", length_units)

    # Length conversion dictionary
    length_conversion = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Inches": 0.0254,
        "Centimeters": 0.01
    }

    # 🔄 Conversion Logic
    if st.button("📏 Convert"):
        result = input_value * (length_conversion[from_unit] / length_conversion[to_unit])
        st.success(f"✅ {input_value} {from_unit} is equal to {result:.2f} {to_unit}")

# ⚖️ Weight Conversion
elif conversion_select == "⚖️ Weight":
    weight_units = ["Grams", "Kilograms", "Pounds", "Ounces"]
    input_value = st.number_input("⚖️ Enter Weight Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("⚖️ From Unit:", weight_units)
    to_unit = st.selectbox("🔄 To Unit:", weight_units)

    # Weight conversion dictionary
    weight_conversion = {
        "Grams": 1,
        "Kilograms": 1000,
        "Pounds": 453.592,
        "Ounces": 28.3495
    }

    # 🔄 Conversion Logic
    if st.button("⚖️ Convert"):
        result = input_value * (weight_conversion[from_unit] / weight_conversion[to_unit])
        st.success(f"✅ {input_value} {from_unit} is equal to {result:.2f} {to_unit}")

# 🌡️ Temperature Conversion
elif conversion_select == "🌡️ Temperature":
    temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]
    input_value = st.number_input("🌡️ Enter Temperature Value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("🌡️ From Unit:", temperature_units)
    to_unit = st.selectbox("🔁 To Unit:", temperature_units)

    # 🔥 Temperature Conversion Function
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
        return value

    # 🔄 Convert Button
    if st.button("🌡️ Convert"):
        result = convert_temperature(input_value, from_unit, to_unit)
        st.success(f"✅ {input_value:.2f} {from_unit} is equal to {result:.2f} {to_unit}")

# 🔚 Footer
st.markdown("---")
st.caption("🔄 Made with ❤️ by Aiman  Khan using Streamlit")
