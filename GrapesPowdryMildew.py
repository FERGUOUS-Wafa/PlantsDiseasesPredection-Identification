# Conidial stage
* The start of the conidial stage of the model is triggered early in the growing season by three consecutive days with six consecutive hours 
of temperatures between 21.1 and 29.4 C ; for each of these three days, the model assigns 20 points to the disease risk index.
* The conidial infection index increases by 20 points on each subsequent day where at least six continuous hours
of temperatures between 21.1 and 29.4 C occur.
* If there are less than six consecutive hours of temperatures between 21.1 and 29.4 C, 10 points are subtracted from the index.
This is the case if the temperature falls below 21.1 C or goes above 29.4 C for more than 45 minutes,
since this amount of time is considered to break the accumulation of conducive temperature hours.
* If the temperature is 35 C or higher for at least 15 minutes, 10 points are subtracted from the index for the day.
* If on the same day with 6 continuous hours between 21.1-29.4 C the temperature exceeds 35 C for 15 minutes or more, 
then the model adds 20 points for the six hours but subtracts 10 points due to the high temperature. Thus,
for that day the model adds 10 points.
* If after subtracting a days points the index is less than zero, reset the index to zero. If after adding a days points the index 
is greater than 100, reset the index to 100.
* On any one day the index should not decline by more than 10 points or increase by more than 20 points.

def disease_risk_index(temp):    
    # Initialize the disease risk index and consecutive hours counter
    risk_index = 0
    consecutive_hours = 0
    
    # Loop through each temperature reading
    for i in temp_readings:
        # Check if the temperature is between 21.1 and 29.4 C
        if 21.1 <= i <= 29.4:
            # Increment the consecutive hours counter and add points to the index
            consecutive_hours += 1
            if consecutive_hours <= 3:
                risk_index += 20
            else:
                risk_index += 40
        # Check if the temperature is less than 21.1 C or greater than 29.4 C
        elif i < 21.1 or i > 29.4:
            # Subtract points from the index and reset the consecutive hours counter
            risk_index -= 10
            consecutive_hours = 0
        # Check if the temperature is 35 C or higher
        elif i >= 35:
            # Subtract points from the index
            risk_index -= 10
        # Check if the temperature exceeds 35 C for at least 15 minutes during a 6-hour period
        elif i > 29.4:
            # Add and subtract points from the index accordingly
            if consecutive_hours <= 3:
                risk_index += 10
            else:
                risk_index += 20
            consecutive_hours = 0
    
        # Ensure the index is within bounds
        if risk_index < 0:
            risk_index = 0
        elif risk_index > 100:
            risk_index = 100
        
        # Ensure the index change is within limits
        if consecutive_hours == 1 and risk_index > 20:
            risk_index = 20
        elif consecutive_hours > 1 and risk_index - 20 * (consecutive_hours - 1) > 20:
            risk_index = 20 * (consecutive_hours - 1) + 20
        
    return risk_index
