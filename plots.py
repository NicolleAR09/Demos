import pandas as pd 
import matplotlib.pyplot as plt
import csv



#df = pd.read_csv(r"C:\Users\Usuario\Triggers1.csv")
headers = ['Time', 'Trigger']

df = pd.read_csv(r"C:\Users\Usuario\Triggers1.csv")
print(df)

plt.plot(df.Time, df.Trigger)

print(type(df.Time))
#plt.show()






