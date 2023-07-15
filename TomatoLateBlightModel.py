# importing required libraries/packages
import pandas as pd
import numpy as np
import math

def calculate_TIndex(T, Tmin):
    Fc = 0.35 + 0.05 * Tmin
    TIndex = (-2.19247 + 0.259906 * T - 0.000139 * T**3 - 6.095832 * 10**-6 * T**4) * Fc
    return TIndex
  
  def calculate_RHIndex(RH):
    RHIndex = -34.9972725 + 0.751 * RH - 0.003909 * RH**2
    return RHIndex

def calculate_RIndex(R):
    Rindex = 0.006667 + 0.194405 * R + 0.0002239 * R**2
    return Rindex

def calculate_IPI(T, Tmin, RH, R):
    if Tmin <= 7 or not (9 <= T <= 25) or RH <= 80 or R <= 0.2:
       return None # IPI cannot be calculated
    else:
        Tindex = calculate_TIndex(T, Tmin)
        RHindex = calculate_RHIndex(RH)
        Rindex = calculate_RIndex(R)
        if RHindex > Rindex:
           IPI = Tindex * RHindex
        else:
           IPI = Tindex * Rindex
        return IPI

  def Tomato_DRI(IPI):
    if IPI is not None:
       if IPI < 15:

         return 0 #high risk of disease
       else:

         return 1 #no risk of disease
    else:
         return None
      
