# from __future__ import unicode_literals
# import sys
# reload(sys)  # noqa
#sys.getdefaultencoding("utf8")

import neurokit as nk
import pandas as pd
import matplotlib.pyplot as plt

import load as load

ecg = load.load_ecg_as_df("data/converted_guginaK23f_1_Dump1.txt.csv")
bio = nk.ecg_process(ecg=ecg['ECG'], sampling_rate=1006)

# too much data to render
#nk.z_score(bio["df"]).plot()
#plt.show()

# df-dictionary contains follow sets (accessible as keys):
# ECG_Raw, ECG_Filtered, ECG_R_Peaks, Heart_Rate,
# ECG_Systole, ECG_Signal_Quality, ECG_RR_Interval,
# ECG_HRV_HF, ECG_HRV_LF, ECG_HRV_ULF, ECG_HRV_VHF, ECG_HRV_VLF

print ("Plot raw ecg...")
nk.z_score(bio["df"]['ECG_Raw']).plot()
plt.show()

print ("Plot R-peaks...")
nk.z_score(bio["df"]['ECG_R_Peaks']).plot()
plt.show()

print ("Plot Heart rate...")
nk.z_score(bio["df"]['Heart_Rate']).plot()
plt.show()

print ("Plot ECG_HRV_VHF...")
nk.z_score(bio["df"]['ECG_HRV_VHF']).plot()
plt.show()

print ("Plot ECG_HRV_HF...")
nk.z_score(bio["df"]['ECG_HRV_HF']).plot()
plt.show()

print ("Plot ECG_HRV_LF...")
nk.z_score(bio["df"]['ECG_HRV_LF']).plot()
plt.show()

print ("Plot ECG_HRV_VLF...")
nk.z_score(bio["df"]['ECG_HRV_VLF']).plot()
plt.show()

print ("Plot ECG_HRV_ULF...")
nk.z_score(bio["df"]['ECG_HRV_ULF']).plot()
plt.show()

print ("Plot HRV low...")
hrv_keys = ('ECG_HRV_LF', 'ECG_HRV_VLF', 'ECG_HRV_ULF')
bio_hrv_subset = {key: bio["df"][key] for key in hrv_keys}
nk.z_score(bio_hrv_subset).plot()
#nk.z_score(bio["df"]['ECG_RR_Interval', 'ECG_HRV_VHF', 'ECG_HRV_HF', 'ECG_HRV_LF', 'ECG_HRV_VLF', 'ECG_HRV_ULF', ]).plot()
plt.show()

print ("Plot HRV high...")
hrv_keys = ('ECG_HRV_HF', 'ECG_HRV_VHF')
bio_hrv_subset = {key: bio["df"][key] for key in hrv_keys}
nk.z_score(bio_hrv_subset).plot()
#nk.z_score(bio["df"]['ECG_RR_Interval', 'ECG_HRV_VHF', 'ECG_HRV_HF', 'ECG_HRV_LF', 'ECG_HRV_VLF', 'ECG_HRV_ULF', ]).plot()
plt.show()
