# Task 1 

import source as s

print(s.BOD5)

print(s.BOD5.loc['BOD_5'])
s.BOD5

print(s.BOD_pri)
print(s.BOD_sec)

if s.BOD_sec > 25:
  print('Final effluent:', s.BOD_sec, 'mg/L' ' , ' 'This facility is not in compliance with EPA Clean Water Act!',)
else:
  print('Final effluent:', s.BOD_sec, 'mg/L' ' , ' 'This facility is in compliance with EPA Clean Water Act.'

print(s.percent_removal,'%')
  
# Task 2 

print(s.BOD_DO)
s.plt.show()

print('BOD_Ultimate:', s.bod_ultimate, 'mg/L')
