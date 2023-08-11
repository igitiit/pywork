count = 0
totalCost = 0.0

# cost * kWh

# local variable declarations

# declare variable as a float type to accumulate total charges
appName = ""
# declare a variable for the appliance name
costPerKW = 0.0
# declare a variable for the cost per KW - hr
annualUsage = 0.0
# declare a variable for the annual usage

km_hr_list = []

total_KW_hr = 0.0

print("[ please enter the requested data ]")
print(" Input 0 Exit !")

# average = sum KW/hr / number of cost items
# variance = (variance + (average - costPerItem) ** 2) / item count
# stdDev = variance ** .5


while True:
    print("appliance name:")
    appName = input()
    if appName == "0":
        break

    print("cost per KW - hr of the appliance (in cents):")
    costPerKW = float(input())
    print("annual usage (in KW - hr):")
    annualUsage = float(input())
    print("Total thus far $%.2f" % (costPerKW * annualUsage))
    count += 1
    totalCost += costPerKW * annualUsage
    total_KW_hr += costPerKW
    km_hr_list.append(costPerKW)

print("Total Annual Cost $%.2f" % totalCost)
Average = (total_KW_hr / count)
print("Average           $%.4f" % (total_KW_hr / count))
Variance = (sum((Average - i) ** 2 for i in km_hr_list) / count)
print("Variance          $%.4f" % (sum((Average - i) ** 2 for i in km_hr_list) / count))
print("StdDev            $%.4f" % Variance ** .5)


