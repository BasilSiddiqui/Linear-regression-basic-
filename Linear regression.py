import pandas as pd
import numpy as np

# Load CSV (try different encodings if needed)
df = pd.read_excel(r"C:\Users\basil\OneDrive\Desktop\eh.xlsx")

# Assuming the independent variable is in 'X' column and dependent in 'Y' column
X = df['X']
Y = df['Y']

# Calculate required summations
n = len(X)
sumX = X.sum()
sumY = Y.sum()
x_bar = sumX/n
y_bar = sumY/n
sumX2 = (X**2).sum()
sumY2 = (Y**2).sum()
sumXY = (X * Y).sum()

Sxx = sumX2 - (1/n) * (sumX**2)
Syy = sumY2 - (1/n) * (sumY**2)
Sxy = (sumXY - (1/n) * sumX * sumY)

r = (sumXY - (1/n) * sumX * sumY) / (np.sqrt((sumX2 - (1/n) * (sumX**2)) * (sumY2 - (1/n) * (sumY**2))))

# Compute beta (slope) and alpha (intercept)
beta = Sxy / Sxx
alpha = y_bar - beta * x_bar

# Print results
print(f"Mean X: {x_bar}")
print(f"Mean Y: {y_bar}")

print("\n")

print(f"sumX: {sumX}")
print(f"sumY: {sumY}")
print(f"sumX2: {sumX2}")
print(f"sumY2: {sumY2}")
print(f"sumXY: {sumXY}")

print("\n")


print(f"Sxx: {Sxx}")
print(f"Syy: {Syy}")
print(f"Sxy: {Sxy}")

print("\n")


print(f"r: {r}")

print("\n")


print(f"Alpha: {alpha}")
print(f"Beta: {beta}")

print("\n")


print(f"Linear Regression Line: Y = {alpha:.4f} + {beta:.4f}X")