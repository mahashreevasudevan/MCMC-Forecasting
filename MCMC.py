import pandas as pd
import numpy as np
from scipy.stats import skewnorm
from statsmodels.graphics.gofplots import qqplot
import matplotlib.pyplot as plt

# Read the data from the input file
df = pd.read_excel("your_data.xlsx")  
value = df['Temperature']  

# Statistics and Plots of the chosen parameter
print("Skewness:", round(value.skew(), 2))
plt.hist(value)
plt.title("Temperature Variation")
plt.show()

# Q-Q plot
qqplot(value, line='s')
plt.title("Q-Q Plot")
plt.show()

# Generating simulated data
mu = np.mean(value)
sigma = np.std(value)
a = 5
simulated = skewnorm.rvs(a, size=len(value))
forecast = mu + sigma * simulated

# Comparing trends
plt.plot(forecast, label="Forecasted")
plt.plot(value, label="Actual")
plt.legend()
plt.title("Forecasted vs Actual")
plt.show()

# Saving the forecasted output in separate Excel
output_df = pd.DataFrame(forecast)
output_df.to_excel("forecast_output.xlsx", index=False, header=False)