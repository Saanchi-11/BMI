import streamlit as st

def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula: BMI = weight (kg) / (height (m)^2)
    """
    return weight / (height ** 2)

def bmi_category(bmi):
    """
    Categorize BMI based on standard ranges.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Please enter positive values for weight and height.")
            return
        
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Based on your BMI, you are categorized as: {category}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

if __name__ == "__main__":
    main()

