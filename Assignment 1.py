
#Assignment A1 - “Pulses”

import csv
import matplotlib.pyplot as plt

# Question 1

#manually split each row on commas.

with open('pulses.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        print(",")

#Create a list for all the timestamps in column 1.

with open('pulses.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    timestamps = []
    for lines in readCSV:
       timestamp = lines[0]
       timestamps.append(timestamp)

    print(timestamps)


#Create a list of lists for the detector readings - you can access elements with
#foo[1][4]

with open('pulses.csv') as csvfile:
    rows = csv.reader(csvfile)
    foo = list(rows)
    print(foo)
    print(foo[1][4])


# Question 2

#1. Modify your code for Question 1, so that the readings are converted back to voltages,
#according to this formula (the ** means “raised to the power of” in Python):
#Voltage (Volts) = (ADC Reading) / (2**10 - 1) * 0.6

with open('pulses.csv') as csvfile:
    rows = csv.reader(csvfile)
    foo = list(rows)
    #print('foo=', foo[1][1])

    for i in range(len(foo)):
        for j in range(len(foo[i])):
            vol = 0
            vol = (j) / (2**10 - 1) * 0.6
            print('vol', vol)

#2. Refactor the code so that this conversion (for a single value) is in a separate function,
#name it appropriately.
#3. Specify the conversion parameter as a constant at the top of your code. (In Python, we
#put constants in UPPER_CASE by convention).

C = (2**10 - 1) * 0.6
def vol_function(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            vol = 0
            vol = (j) / C
            print('vol1', vol)

with open('pulses.csv') as csvfile:
    rows = csv.reader(csvfile)
    foo = list(rows)

    vol_function(foo)


# Question 3

#1. Plot a single pulse (i.e. row of the CSV file).
#2. Add axis labels, and a title.
#3. Save the figure to disk using .savefig(..)

x = []
y = []

with open('pulses.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        #y.append(int(row[1]))

plt.plot(x, label=' A single pulse')
plt.xlabel('x')
#plt.ylabel('y')
plt.title('Loaded from pulses')
plt.legend()
plt.show()
plt.savefig('fig.png')


# Question 4

#1. Build a new list of lists.
#2. For each row/pulse:
#a. find the mean (average) of the first 10 elements.
#b. Use a for loop to subtract this value from all values in that row.


with open('pulses.csv') as csvfile:
    rows = csv.reader(csvfile)
    data = list(rows)

    for i in range(len(data)):
      sum = 0
      mean = 0
      for j in range(10):
        sum += int(data[i][j])
        mean = sum/10
      print('mean=',mean) #mean
      sub =0
      for k in range(len(data[i])):
          sub = k - mean
          print('sub=', sub)

#3. Refactor this code into its own function (for a row), and name it accordingly.
#4. Use a constant for 10.
C =10
def my_function(data):

    for i in range(len(data)):
        sum = 0
        mean = 0
        for j in range(C):
            sum += int(data[i][j])
            mean = sum / C
        print('mean=', mean)  # mean
        sub = []
        for k in range(len(data[i])):
            sub = k - mean
            print('sub=', sub)

with open('pulses.csv') as csvfile:
    rows = csv.reader(csvfile)
    data1 = list(rows)

    my_function(data1)









