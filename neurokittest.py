# Import packages
import neurokit as nk
import pandas as pd
import numpy as np
#import seaborn as sns
import matplotlib.pyplot as plt

# Download data
df = pd.read_csv("https://raw.githubusercontent.com/neuropsychology/NeuroKit.py/master/examples/Bio/bio_100Hz.csv")
# Plot it
df.plot()
plt.show()

# Process the signals
bio = nk.bio_process(ecg=df["ECG"], rsp=df["RSP"], eda=df["EDA"], add=df["Photosensor"], sampling_rate=100)
# Plot the processed dataframe, normalizing all variables for viewing purpose
nk.z_score(bio["df"]).plot()
plt.show()

