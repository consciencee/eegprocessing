import os
import csv
import pandas as pd
import time
import datetime

''' CONFIG '''

log_location = '../data/logs'
log_endind = '_log.csv'

src_location = '../data/converted'
src_file_prefix = 'converted_'

username = "B"
botnames = ["C BOT_moral", "A BOT"]


def merge_eeg_and_log(fileprefix):
    if not check_log_existing(fileprefix):
        print("Log for " + fileprefix + " not found!")
        exit(1)
    if not check_eeg_existing(fileprefix):
        print("Source file for " + fileprefix + " not found!")
        exit(1)


    log_file = load_log_csv(fileprefix)

def check_log_existing(fileprefix):
    return os.path.isfile(log_location + '/' + fileprefix + log_endind)

def check_eeg_existing(fileprefix):
    return os.path.isfile(src_location + '/' + src_file_prefix + fileprefix)

def load_log_csv(fileprefix):
    resultC = pd.DataFrame()
    resultA = pd.DataFrame()
    timestamps = []
    first_timestamp = 0
    b_to_c_bot_valence = []
    b_to_a_bot_valence = []
    b_to_c_bot_dominance = []
    b_to_a_bot_dominance = []
    b_from_a_bot_valence = []
    b_from_a_bot_dominance = []
    b_from_c_bot_valence = []
    b_from_c_bot_dominance = []
    log_file = open(log_location + '/' + fileprefix + log_endind, 'rb')
    for line in log_file:
        appraisals = line.decode().split('{')[1].split("}")[0]
        dom, val = get_current_appraisal(appraisals, "B", "A BOT")
        b_to_a_bot_dominance.append(dom)
        b_to_a_bot_valence.append(val)
        dom, val = get_current_appraisal(appraisals, "B", "C BOT_moral")
        b_to_c_bot_dominance.append(dom)
        b_to_c_bot_valence.append(val)
        dom, val = get_current_appraisal(appraisals, "A BOT", "B")
        b_from_a_bot_dominance.append(dom)
        b_from_a_bot_valence.append(val)
        dom, val = get_current_appraisal(appraisals, "C BOT_moral", "B")
        b_from_c_bot_dominance.append(dom)
        b_from_c_bot_valence.append(val)
        timestamp = line.decode().split(",")[0]
        if len(timestamps) == 0:
            first_timestamp = get_millis(timestamp)
        timestamps.append(get_millis(timestamp) - first_timestamp)

    #result["Time"] = timestamps
    resultA["to_A_v"] = b_to_a_bot_valence
    resultA["to_A_d"] = b_to_a_bot_dominance
    resultC["to_C_moral_v"] = b_to_c_bot_valence
    resultC["to_C_moral_d"] = b_to_c_bot_dominance

    resultA["from_A_v"] = b_from_a_bot_valence
    resultA["from_A_d"] = b_from_a_bot_dominance
    resultC["from_C_moral_v"] = b_from_c_bot_valence
    resultC["from_C_moral_d"] = b_from_c_bot_dominance

    return resultA, resultC


def get_current_appraisal(appraisal_arr, actorname, targetname):
    #{BToC BOT_moral=(0.991, 0.9914999999999999), C BOT_moralToB=(0.991, 0.9885), C BOT_moralToC BOT_moral=(1.0, 1.0), BToB=(1.0, 1.0)}
    appraisal_pairs = appraisal_arr.split("), ")
    for appraisal_raw in appraisal_pairs:
        actor, target, valence, dominance = parse_appraisal(appraisal_raw)
        if (actor == actorname) and (target == targetname):
            return float(valence), float(dominance)

    return float(1), float(1) # 1 for not found values was chosen for smoother plot representation

def parse_appraisal(raw_str):
    lst = raw_str.split("=")
    names = lst[0].split("To")
    appraisals = lst[1].split(",")
    valence = appraisals[0].replace("(", "")
    dominance = appraisals[1].replace(" ", "")
    return names[0], names[1], valence, dominance

def get_millis(raw_str):
    without_millis = ":".join(raw_str.split(":")[:-1])
    millis = raw_str.split(":")[-1]
    seconds = time.mktime(datetime.datetime.strptime(without_millis, "%m/%d/%Y %H:%M:%S").timetuple())

    return seconds*1000 + int(millis)
    #4/25/2018 14:07:25:240