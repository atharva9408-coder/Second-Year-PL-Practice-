def calculate_cals():
	carbs = float(input("Enter carbs intake(gm): "))
	fats = float(input("Enter fats intake(gm): "))
	proteins = float(input("Enter protein intake(gm): "))
	total_cals = (carbs * 4) + (fats * 9) + (proteins * 4)

	print("\n-------------Daily Caloric Intake-------------")
	print("The total calories consumed in a day are ", total_cals)
	
calculate_cals()