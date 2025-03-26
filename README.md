# Linear Regression Analysis

## Overview
This project performs a simple linear regression analysis using Python and Pandas. It calculates essential statistical metrics such as means, summations, correlation coefficient, and the linear regression equation.

## Features
- Reads data from an Excel file
- Computes key statistical metrics including:
  - Mean of X and Y
  - Summations (sumX, sumY, sumX2, sumY2, sumXY)
  - Variance components (Sxx, Syy, Sxy)
  - Correlation coefficient (r)
- Fits a simple linear regression model
- Outputs the regression equation in the form:
  
  **Y = alpha + beta * X**

## Usage
1. Ensure your dataset is stored in an Excel file (`eh.xlsx`) with at least two columns: `X` (independent variable) and `Y` (dependent variable).
2. Update the file path in the script if necessary.
3. Run the script:
   ```sh
   python regression_analysis.py
   ```
4. The computed results, including statistical values and the regression equation, will be printed in the console.

## Example Output
```
Mean X: 5.32
Mean Y: 6.41

sumX: 53.2
sumY: 64.1
sumX2: 345.23
sumY2: 412.45
sumXY: 359.76

Sxx: 45.23
Syy: 50.67
Sxy: 39.82

r: 0.89

Alpha: 1.23
Beta: 0.78

Linear Regression Line: Y = 1.2300 + 0.7800X
```
