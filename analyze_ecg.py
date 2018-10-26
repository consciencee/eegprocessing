# from __future__ import unicode_literals
# import sys
# reload(sys)  # noqa
#sys.getdefaultencoding("utf8")

import neurokit as nk

import load as load

ecg = load.load_ecg_as_list("data/converted_light_example.txt.csv")
ecg_processed = nk.ecg_process(ecg=ecg, sampling_rate=1006)
print ecg_processed
