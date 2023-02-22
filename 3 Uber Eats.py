"""Program to keep track of details for a taxi
"""


name = input("Who is your UBER EATS driver? ")
tripCount = 0
totalTime = 0.0  # Setting these up to take floats
totalIncome = 0.0
baseCost = 10.00  # Using constants rather than literals for
minuteCost = 2.00  # these two costs
startNewTrip = "Yes"  # Set the loop to true

while startNewTrip == "yes":
    # Float allows for half minutes
    tripTime = float(input("how many minutes did the trip take? "))
    if tripTime == str():
        tripCount += 1
        totalTime += tripTime
        tripCost = (tripTime * minuteCost) + baseCost
        totalIncome += tripCost
        print(f"This trip cost ${tripCost:.2f}\n")
        startNewTrip = input("Do you want to enter a new trip? Yes or No: ")
        # "No" above will break the loop

print("================================")
print(f"Driver {name} had {tripCount} tr"
      f"ips totalling {round (totalTime)} "
      f"minutes\n"
      #  the "round" function above rounds up or down from .5
      #  however, the two below round to 2dp
      f"The average time of all trips was {round (totalTime / tripCount, 2)}" f"minutes\n"
      f"The total income for the day was ${totalIncome:.2f}\n"
      f"The average cost of all trips was ${totalIncome / tripCount:.2f}")
