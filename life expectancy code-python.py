import numpy as np 
import pandas as pd 
import time
import math
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import median_absolute_error
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv('C:\Users\ADITYA\Desktop\Business Process Analytics\Life Expectancy Data.csv')

data.columns