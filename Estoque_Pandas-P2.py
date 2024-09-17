import pandas as pd # Import the pandas library with the alias pd

pd.set_option('display.width',1000) # Included in order to avoid the line break in large dataframe

# Load the CSV file into a DataFrame named cars
cars = pd.read_csv('cars.csv')

# a. Display the first five rows with odd-numbered columns
first_five_odd_columns = cars.iloc[:5, 1::2]
print("First five rows with odd-numbered columns:")
print(first_five_odd_columns)

# b. Display the row that contains the Model of Mazda RX4
mazda_rx4_row = cars.loc[cars['Model']=='Mazda RX4']
print("\nRow containing Mazda RX4:")
print(mazda_rx4_row)

# c. Display how many cylinders (cyl) the car model Camaro Z28 have
camaro_z28_cyl = cars.loc[(cars['Model']=='Camaro Z28'), ['cyl']]
print("\nNumber of cyl in Camaro Z28:")
print(camaro_z28_cyl)

# d. Display how many cylinders (cyl) and what gear type (gear) the selected three car models have
selected_car_1 = cars.loc[(cars['Model']=='Mazda RX4 Wag'), ['cyl', 'gear']]
selected_car_2 = cars.loc[(cars['Model']=='Ford Pantera L'), ['cyl', 'gear']]
selected_car_3 = cars.loc[(cars['Model']=='Honda Civic'), ['cyl', 'gear']]
print("\nNumber of cyl and gear in selected cars:")
print("Mazda RX4 Wag")
print(selected_car_1)
print("\nFord Pantera L")
print(selected_car_2)
print("\nHonda Civic")
print(selected_car_3)