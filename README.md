# EXPERIMENT 3 - Python Data Analysis
This repository contains my solutions for the third experiment in ECE 2112: Advanced Computer Programming and Algorithms. I've used Jupyter Notebook to implement and test my Python code. The data is sourced from the cars.csv file, located within the Jupyter notebook folder. The code will automatically print the results.<br />

### Library Used
- Pandas: library is built on NumPy and provides easy-to-use data structures and data analysis tools for the Python programming language.

### Problem 1
Using knowledge obtained from the experiment and demonstrations:
1. Load the corresponding .csv file into a data frame named cars using pandas
2. Display the first five and last five rows of the resulting cars.

### Problem 2
Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.
1. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
2. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
3. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
4. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

## Sample Output
This section showcasing the expected output for each problem, formatted as code blocks for clarity.
### Problem 1
```
First 5 rows:
               Model   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  carb
0          Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4     4
1      Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4     4
2         Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4     1
3     Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3     1
4  Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0     3     2

Last 5 rows:
             Model   mpg  cyl   disp   hp  drat     wt  qsec  vs  am  gear  carb
27    Lotus Europa  30.4    4   95.1  113  3.77  1.513  16.9   1   1     5     2
28  Ford Pantera L  15.8    8  351.0  264  4.22  3.170  14.5   0   1     5     4
29    Ferrari Dino  19.7    6  145.0  175  3.62  2.770  15.5   0   1     5     6
30   Maserati Bora  15.0    8  301.0  335  3.54  3.570  14.6   0   1     5     8
31      Volvo 142E  21.4    4  121.0  109  4.11  2.780  18.6   1   1     4     2
```

### Problem 2
```
First five rows with odd-numbered columns:
    mpg   disp  drat   qsec  am  carb
0  21.0  160.0  3.90  16.46   1     4
1  21.0  160.0  3.90  17.02   1     4
2  22.8  108.0  3.85  18.61   1     1
3  21.4  258.0  3.08  19.44   0     1
4  18.7  360.0  3.15  17.02   0     2

Row containing Mazda RX4:
       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb
0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4

Number of cyl in Camaro Z28:
    cyl
23    8

Number of cyl and gear in selected cars:
Mazda RX4 Wag
   cyl  gear
1    6     4

Ford Pantera L
    cyl  gear
28    8     5

Honda Civic
    cyl  gear
18    4     4
```

## Contact Information
Name: Prince Emmanuel Estoque<br /> 
Email: princeemmanuel.estoque.eng@ust.edu.ph
