def calculate_bmi():
    print("--- BMI (Body Mass Index) Calculator ---")
    
    try:
        # Take weight (kg) and height (meters) input from the user
        weight = float(input("Enter your weight in kg (e.g., 70): "))
        height = float(input("Enter your height in meters (e.g., 1.75): "))
        
        # Input validation: reject negative or zero values
        if weight <= 0 or height <= 0:
            print("Error: Weight and height cannot be zero or negative.")
            return

        # BMI formula calculation
        bmi = weight / (height ** 2)
        bmi_rounded = round(bmi, 2)

        # Classify according to health categories
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi <= 24.9:
            category = "Normal"
        elif 25 <= bmi <= 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        # Display the result
        print(f"\nYour BMI value is: {bmi_rounded}")
        print(f"Health Category: {category}")
        
    except ValueError:
        # Non-numeric input validation error handling
        print("Error: Please enter a valid numeric value.")

if __name__ == "__main__":
    calculate_bmi()