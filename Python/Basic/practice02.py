math = float(input("Enter Math marks: "))
english = float(input("Enter English marks: "))
physics = float(input("Enter Physics marks: "))

# Total Marks 
total = math + english + physics

# Average Marks 
average = total / 3

# Output 
print("\n--- Results ---")
print("Total =", total)
# round(average, 2) 
print("Average =", round(average, 2))