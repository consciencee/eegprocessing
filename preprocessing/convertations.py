import csv
import os
import sys
import re

''' CONFIG '''

# PATHS
''' Path relative to this script for input data files '''
input_path = '../data/input/'

''' Path relative to this script for output data files '''
output_path = '../data'


# SETTINGS

'''
Data doesn't include a timestamp. We'll calculate the
timestamps based on the sample rate.
'''

input_sample_rate = 1006
input_channels_names_linenum = 14
input_channels_amn_linenum = 10
input_data_firstline_linenum = 22
input_sr_linenum = 8

''' END CONFIG '''

input_headers = ['ECG']
output_headers = ['Time','ECG']

files = os.listdir(input_path)

input_files = []
for filename in files:
  if '.txt' in filename:
    input_files.append(filename)

if(len(input_files) < 1):
  print "ERROR: No input files found! \n Input files must be placed in the '"+input_path+"' directory  (relative \n to  the location of this script), or change the 'input_path'\n parameter in the script"
  raw_input()

for input_fn in input_files:

  print "Processing file: "+input_fn+" ... "

  output_data = []

  time_counter = 0
  time_increment = float(1)/float(input_sample_rate)

  print "Sample rate: "+str(input_sample_rate)+" ... "
  print "Time increment: "+str(time_increment)+" ... "


  with open(os.path.join(input_path,input_fn), 'rb') as input_file:

      contents = input_file.readlines()

      input_sample_rate = re.sub(" +", " ", contents[input_sr_linenum - 1]).split(" ")[3]
      input_ch_names = re.sub("[ \n]+", " ", contents[input_channels_names_linenum - 1]).split(" ")[1:-1]
      input_ch_indices = {i: e for i, e in enumerate(input_ch_names) if e in input_headers}

      if(len(input_ch_indices) == 0):
          print "Error: No channels found! Provide any correct input channels names and try again"
          exit(1)

      if(len(input_ch_indices) != len(input_headers)):
          print "Warning: Amount of found channels is not equal to amount of requested channels. " \
                "If it shouldn't be, check for input channels names correctness"

      output_fn = "converted_"+input_fn+".csv"
      output_csv_file = open(os.path.join(output_path,output_fn), 'wb')
      csv_output = csv.DictWriter(output_csv_file, fieldnames=output_headers, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

      data_contents = contents[input_data_firstline_linenum - 1:]

      row_count = 0

      for line in data_contents:
          row_count = row_count + 1
          output = {}
          time_counter = time_counter + time_increment
          output['Time'] = time_counter
          all_channels_data = re.sub("[ \n]+", " ", line).split(" ")[1:-1]
          for i, name in input_ch_indices.iteritems():
              output[name] = all_channels_data[i]
          output_data.append(output)

      headers_text = {}

      for val in output_headers:
          headers_text[val] = val

      csv_output.writerow(headers_text)

      for row in output_data:
          csv_output.writerow(row)

      output_csv_file.close()
          #channels_data = [all_channels_data[i] for i in input_ch_indices]


  #    csv_input = csv.DictReader(input_file, fieldnames=input_headers, dialect='excel')
  #    row_count = 0
  #
  #    for row in csv_input:
  #
  #         row_count = row_count + 1
  #
  #         if(row_count > 2):
  #
  #           output = {}
  #
  #           time_counter = time_counter + time_increment
  #
  #           output['Time'] = time_counter
  #
  #           for i in range(1,9):
  #             channel_key = 'chan'+str(i)
  #             output[channel_key] = row[channel_key]
  #
  #           output['Sample_rate'] = input_sample_rate
  #
  #           output_data.append(output)
  #
  #
  #
  # output_fn = "converted_"+input_fn
  #
  # output_csv_file = open(os.path.join(output_path,output_fn), 'wb')
  #
  # csv_output = csv.DictWriter(output_csv_file, fieldnames=output_headers, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  #
  # headers_text = {}
  #
  # for val in output_headers:
  #   headers_text[val] = val
  #
  # csv_output.writerow(headers_text)
  #
  # for row in output_data:
  #   csv_output.writerow(row)
  #
  # output_csv_file.close()