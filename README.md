# eegprocessing
eeg processing tools for lower-level features aquisition

## Input data
### Format
Toolkit works with comma-separated text files
### EDF
It's available to use edf (converted to txt) files, but they are need to be converted to pure csv. To do this you should use convertations.py script.
Input edf-txt data must be placed in data/input directory, then in the convertations.py script you should provide channels from your source file you are interested in.
After execution, script will place processed files in data directory with "converted" prefix and ".csv" extension.

## Dependencies
All biosignals processing is provided by Neurokit python toolset (<a href='https://github.com/neuropsychology/NeuroKit.py'>repository</a>, <a href='https://neurokit.readthedocs.io/en/latest/index.html'>documentation</a>) and BioSPPy(<a href='https://github.com/PIA-Group/BioSPPy'>repository</a>, <a href='https://biosppy.readthedocs.io/en/stable/'>documentation</a>)
