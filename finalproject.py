import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("vaccine.csv")
filtered_data = data[["date", "people_vaccinated"]]  # filters on just 2 columns we need
