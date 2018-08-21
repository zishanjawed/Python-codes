"""
Sample Input

12.00
20
8
Sample Output

The total meal cost is 15 dollars.
@author : Zishan jawed
"""
mealCost = float(input("Enter the meal cost : "))
tipPercent = float(input("Enter the tip percent : "))
taxPercent = float(input("Enter the tax percent :"))

def solve(mealCost, tipPercent, taxPercent):
	totalCost = round(mealCost + (tipPercent*(mealCost/100)) + taxPercent*(mealCost/100))
	return totalCost

total = solve(mealCost, tipPercent, taxPercent)
print("The total meal cost is ", total ," dollars." )