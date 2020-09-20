# Modified code from:
# https://www.geeksforgeeks.org/python-program-convert-time-12-hour-24-hour-format/
# 12 hour to 24 hour format

# Function to convert the date format
def convert24(str1):
    # add the leading 0 if its missing
    if str1.find(':') < 2:
        str1 = '0' + str1
    # Checking if last two elements of time
    # is am and first two elements are 12
    if str1[-2:] == "am" and str1[:2] == "12":
        return "00" + str1[2:-3]
    # remove the am
    elif str1[-2:] == "am":
        return str1[:-3]
    # Checking if last two elements of time
    # is pm and first two elements are 12
    elif str1[-2:] == "pm" and str1[:2] == "12":
        return str1[:-3]
    else:
        # add 12 to hours and remove pm
        return str(int(str1[:2]) + 12) + str1[2:8]

# print(convert24('10:25:30 pm'))
# print(convert24('4:43:34 am'))
# print(convert24('5:51:56 pm'))
# print(convert24('10:25:30 am'))
# print(convert24('12:00:00 am'))
# print(convert24('12:00:00 pm'))


import csv
import os

boosted_csv = '/home/vkk/Downloads/boosted.csv'
toggl_csv = './toggl.csv'

if os.path.exists(toggl_csv):
    print("Toggl csv file exists.")
    os.remove(toggl_csv)
    print("Removed toggl csv file.")

with open(boosted_csv, newline='') as boosted:
    with open(toggl_csv, 'w', newline='') as toggl:
        reader = csv.reader(boosted, delimiter=',', quotechar='|')
        writer = csv.writer(toggl, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for row in reader:
            for i in range(0, len(row)):
                if 'am' in row[i] or 'pm' in row[i]:
                    row[i] = convert24(row[i])
            writer.writerow(row)
