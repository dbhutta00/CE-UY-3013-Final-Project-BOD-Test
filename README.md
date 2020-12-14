# CE-UY-3013-Final-Project-BOD-Test

This program checks the results of a 5-day Biochemical oxygen demand (BOD) test. The program will check to see if the final effluent is less than 25 mg/L to make sure the wastewater management facility is compliant with the EPA's Clean Water Act. The program also has a % removal BOD calculator. This program finds BOD Ultimate and  graphs the DO and BOD vs. time overlayed on the same graph.

Inputs:
*  For Task 1: Dissolved Oxygen (DO) concentrations at t = 0 days and at t = 5 days for primary and secondary effluent wastewater samples in mg/L
* For Task 2: Dissolved Oxygen (DO) and BOD data in mg/L for x number of days 

Outputs: 
* For Task 1
  * 5-day BOD results calculations 
  * Average results for primary and secondary results
  * Whether pr not the facility in question is in compliance with EPA Clean Water Act 
  * Percent removal of BOD

* For Task 2
  * Plot of DO and BOD vs Time 
  * Value of BOD_Ultimate
  
 ## Setup

In order to use the program, you have to download this repository,
and run it on any platform using python3. Make sure you have acces to pandas and matplotlib.pyplot. Change inputs as needed.
  
## How to use the program

Input your data for the DO at day 0 and day 5 for Primaryy Effluent (PE) and Secondary Effluent (SE).
Here a minimum of 3 samples were used. Also add the decimal dilution of your samples in the last column.
Here a standard 2% and 10% was used for Primary and Secondary Effluent respectively.

```
BOD5 = pd.DataFrame({
                   "PE1": [8.68, 1.44, 0.02],
                   "PE2": [7.33, 1.02, 0.02],
                   "PE3": [8.48, 1.49, 0.02],
                   "SE1": [9.39, 5.35, 0.10],
                   "SE2": [7.82, 2.38, 0.10],
                   "SE3": [8.42, 4.07, 0.10]},
                   index = ["DO_0", "DO_5", "Decimal_Dilution"])
```

Run the code and it will provide you with the results for Task 1.

Next, you will need to input data for DO and BOD data in mg/L for x number of days. This example shows 10 data points from 0 to 43 days.

```
BOD_DO = pd.DataFrame({
                   'Day' : [0,1,2,3,4,5,7,14,21,42],
                    'DO' : [9.51,9.20,7.59,4.49,2.38,1.92,1.83,0.71,1.21,1.30],
                   'BOD': [0,16,96,251,357,380,384,440,415,411]})
```

Run the code and it will provide you with the results for Task 2.

