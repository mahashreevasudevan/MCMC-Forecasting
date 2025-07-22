# Forecasting Temperature Using Markov Chain Monte Carlo (MCMC)

## Key Objectives:

- To identify the possibility of using the Markov Chain Monte Carlo (MCMC) method for forecasting atmospheric temperature.
- To study temperature patterns across an arid region over a yearly cycle and simulate future values.
- To evaluate the accuracy and reliability of MCMC-based forecasts.

## Methodology:

This study uses historical temperature data from an arid region for the probabilistic modeling using the MCMC method to forecast temperature values over a 12-month period.

## Model Pipeline:

1. **Data Preprocessing**
   - Input Excel dataset is read using the `pandas` library.
   - Data visualization and initial statistical analysis are done, including plotting and distribution analysis.

2. **Distribution Analysis**
   - Skewness of the temperature distribution is calculated to understand variations.
   - A Q-Q plot is used to compare the observed temperature distribution against a standard normal distribution.

3. **Forecasting Using MCMC Principles**
   - Synthetic data is generated using the `skewnorm.rvs()` function.
   - Forecast values are obtained using the original dataset’s mean and standard deviation.
   - Actual and forecasted data are plotted together.

## Challenges Addressed:

- Using temperature data with slight non-normal skewness.
- Possibility of MCMC-based simulation in replicating temperature trends.

## Results:

- While the MCMC-based simulation produced temperature-like data, the forecasted values did not align closely with the actual data trend. 
- This mismatch suggests that MCMC may not be suitable for accurate temperature forecasting.

## Impact:

- This study shows the use of probabilistic simulation methods (like MCMC) in atmospheric data analysis. Although the model did not yield accurate forecasts, it offered insights into how statistical simulations behave with slightly skewed environmental data.

## Technology and Tools

- **Language**: Python
- **Libraries**:
  - `pandas` for data manipulation
  - `numpy` and `scipy` for statistical operations
  - `matplotlib` for visualization
  - `statsmodels` for Q-Q plotting


---

 **Note**: The dataset used in this study is confidential. Hence, the dataset and figures has not been included.  
