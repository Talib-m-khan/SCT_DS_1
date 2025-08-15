
import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {'Age Group': ['0-20', '21-44', '45+'],
        'Population (millions)': [512, 807, 148]}

df = pd.DataFrame(data)

# Create Bar Chart
plt.bar(df['Age Group'], df['Population (millions)'], color=['yellow','blue','pink'])
plt.xlabel('Age Group')
plt.ylabel('Population (millions)')
plt.title("India's Population by Age (2022)")
plt.show()
