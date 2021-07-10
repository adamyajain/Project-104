import csv
from collections import Counter

with open('SOCR-HeightWeight.csv', newline = '') as f:
    file_data = list(csv.reader(f))
file_data.pop(0)

def mean(data):
    new_data = []
    for i in range(len(data)):
        n_num = data[i][1]
        new_data.append(float(n_num))
    n = len(new_data)
    total = 0
    for x in new_data :
        total += x
        mean = total/n
    print("Mean Average is " + str(mean))


def median(data):
    new_data=[]
    for i in range(len(file_data)):
        n_num = file_data[i][1]
        new_data.append(n_num)

    n = len(new_data)
    new_data.sort()

    if n % 2 == 0 :
        median1 = float(new_data[n//2])

        median2 = float(new_data[n//2 - 1])

        median = (median1 + median2)/2
    else: 
        median = new_data[n//2] 
    print("Median is " + str(median))


def mode(data):
    new_data=[]
    for i in range(len(file_data)):
        n_num = data[i][1]
        new_data.append(n_num)
        data = Counter(new_data)
        mode_data_for_range = {
            "50-60" : 0,
            "60-70" : 0,
            "70-80" : 0
        }
    for heght, occurence in data.items():
        if 50 < float(height) < 60:
            mode_data_for_range["50-60"] += occurence
        elif 60 < float(height) < 70:
            mode_data_for_range["60-70"] += occurence
        elif 70 < float(height)["70-80"] < 80:
            mode_data_for_range["70-80"] += occurence

    mode_range, mode_occurence = 0, 0

    for range, occurnce in mode_data_for_range.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode = float(mode_range[0] + mode_range[1] / 2)
    print(f"Mode is -> {mode:2f}")

mean(file_data)
median(file_data)
mode(file_data)