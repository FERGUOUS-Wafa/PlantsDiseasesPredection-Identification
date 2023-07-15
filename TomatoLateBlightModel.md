# Tomato Late Blight Model

The dataset used in this study includes daily measurements of weather factors that are important for evaluating the risk of tomato late blight. The specific variables used in the model are:

- Average daily temperature in Celsius (Tav)
- Minimum daily temperature in Celsius (Tmin)
- Average daily humidity (RHav)
- Rainfall accumulation in millimeters over 24 and 48 hours (R)

To calculate the risk index for tomato late blight, a model with polynomial and quadratic functions is used. The model follows these steps:

## Calculate the daily TIndex using the following equation:
TIndex = (-2.19247 + 0.259906 * T - 0.000139 * T^3 - 6.095832e-6 * T^4) * Fc
Here, T represents the daily average temperature in Celsius, and Fc is a correction factor calculated as:
Fc = 0.35 + 0.05 * Tmin

Tmin is the minimum temperature for the day in Celsius.

## Calculate the daily RHIndex using the following equation:
RHIndex = -34.9972725 + 0.751 * RH - 0.003909 * RH^2

RH represents the average daily humidity.

## Calculate the daily Rindex using the following equation:
Rindex = 0.006667 + 0.194405 * R + 0.0002239 * R

R corresponds to the accumulated rainfall in millimeters over the last 48 hours.

## Determine whether the Rindex or RHIndex is higher, and multiply it by the TIndex to find the daily IPI (Integrated Pest Index).
- The IPI is calculated only when certain weather conditions are met:
  - Tmin is above 7°C
  - Tav is between 9°C and 25°C
  - Total rainfall is greater than 0.2 mm
  - RHav is above 80%
- The daily IPI is then compared to a threshold:
  - IPI values below 15 indicate no disease risk
  - An IPI above 15 indicates a high risk of tomato late blight.
