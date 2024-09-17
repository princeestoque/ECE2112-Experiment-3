import pandas as pd # Import the pandas library with the alias pd

pd.set_option('display.width',1000) # Included in order to avoid the line break in large dataframe

# Load the CSV file into a DataFrame named cars
cars = pd.read_csv("cars.csv")

# Display the first five rows
print("First 5 rows:")
print(cars.head(5))

# Display the last five rows
print("\nLast 5 rows:")
print(cars.tail(5))