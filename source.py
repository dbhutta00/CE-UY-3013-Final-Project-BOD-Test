# Imports 

import pandas as pd
import matplotlib.pyplot as plt

# TASK 1: 5-Day BOD Calculations

# Insert your dataframe for Dissolved Oxygen at Day 0 and Day 5 per primary and secondary treatment 
# Standard is three samples but can input more
# Also input the decimal dilution of your samples 
# 2% and 10% are standards used for primary and secondary effluent respectively
# Can change decimal dilution if needed
# PE = Primary Effluent and SE= Secondary

BOD5 = pd.DataFrame({
                   "PE1": [8.68, 1.44, 0.02],
                   "PE2": [7.33, 1.02, 0.02],
                   "PE3": [8.48, 1.49, 0.02],
                   "SE1": [9.39, 5.35, 0.10],
                   "SE2": [7.82, 2.38, 0.10],
                   "SE3": [8.42, 4.07, 0.10]},
                   index = ["DO_0", "DO_5", "Decimal_Dilution"])
BOD5

# BOD_5 (mg/L) = (DO_0 - DO_5) / Decimal Dilution

BOD5.loc['BOD_5'] = (BOD5.loc['DO_0'] - BOD5.loc['DO_5']) / BOD5.loc['Decimal_Dilution']

print(BOD5.loc['BOD_5'])
BOD5

# Compute average value of BOD_5 for primary effluent

avg_pe_bod = BOD5[['PE1', 'PE2', 'PE3']]
avg_pe_bod
BOD_pri = avg_pe_bod.loc['BOD_5'].mean()
print(BOD_pri)

# Compute average values of BOD_5 for secondary effluent

avg_se_bod = BOD5[['SE1', 'SE2', 'SE3']]
avg_se_bod
BOD_sec = avg_se_bod.loc['BOD_5'].mean()
print(BOD_sec)

# Check to see if this wastewater management facility is compliant with EPA Clean Water Act

if BOD_sec > 25:
  print('Final effluent:', BOD_sec, 'mg/L' ' , ' 'This facility is not in compliance with EPA Clean Water Act!',)
else:
  print('Final effluent:', BOD_sec, 'mg/L' ' , ' 'This facility is in compliance with EPA Clean Water Act.')
  
