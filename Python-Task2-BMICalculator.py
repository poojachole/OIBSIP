def calculate_bmi():
    print("--- BMI (Body Mass Index) Calculator ---")
    
    try:
        # Unit choice: meters ya feet/inches
        unit = input("Choose unit for height - Enter 'm' for Meters or 'f' for Feet/Inches: ").strip().lower()
        
        weight = float(input("Enter your weight in kg (e.g., 70): "))
        
        if unit == 'f':
            feet = float(input("Enter feet (e.g., 4): "))
            inches = float(input("Enter inches (e.g., 10): "))
            
            if feet < 0 or inches < 0:
                print("Error: Height cannot be negative.")
                return
            
            # Feet aur inches ko meters mein convert karna
            total_inches = (feet * 12) + inches
            height = total_inches * 0.0254
            
        else:
            height = float(input("Enter your height in meters (e.g., 1.47): "))
            # Agar user ne meters diya hai, toh use wapas feet aur inches mein convert kar lenge print ke liye
            total_inches = height / 0.0254
            feet = int(total_inches // 12)
            inches = round(total_inches % 12, 1)
        
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
        print(f"\n--- Results ---")
        print(f"Your Height: {feet} feet {inches} inches (or {round(height, 2)} meters)")
        print(f"Your BMI value is: {bmi_rounded}")
        print(f"Health Category: {category}")
        
    except ValueError:
        # Non-numeric input validation error handling
        print("Error: Please enter a valid numeric value.")

if __name__ == "__main__":
    calculate_bmi()
