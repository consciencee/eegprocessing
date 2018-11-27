import matplotlib.pyplot as plt

import preprocessing.logsynchronizing as sync

dataA, dataC = sync.load_log_csv("guginaK23f_1")

dataA.plot()
dataC.plot()

plt.show()