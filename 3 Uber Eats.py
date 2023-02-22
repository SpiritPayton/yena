"""Program to keep track of details for uber eats driver
"""


name = input("Who is your UBER EATS driver?: ")

trip_count = 0
total_time = 0.0  # Setting these up to take floats
total_income = 0.0
base_cost = 10.00  # Using constants rather than literals for
minute_cost = 2.00  # these two costs
start_new_trip = "Yes"  # Set the loop to true

while start_new_trip == "Yes":
    # Float allows for half minutes
    trip_time = float(input("how many minutes did the trip take? "))
    trip_count += 1
    total_time += trip_time
    trip_cost = (trip_time * minute_cost) + base_cost
    total_income += trip_cost
    print(f"This trip cost ${trip_cost:.2f}\n")
    startNewTrip = input("Do you want to enter a new trip? Yes or No: ")
    # "No" above will break the loop

print("================================")
print(f"Driver {name} had {trip_count} tr"
      f"ips totalling {round (total_time)} "
      f"minutes\n"
      #  the "round" function above rounds up or down from .5
      #  however, the two below round to 2dp
      f"The average time of all trips was"
      f" {round (total_time / trip_count, 2)} minutes\n"
      f"The total income for the day was ${total_income:.2f}\n"
      f"The average cost of all trips was ${total_income / trip_count:.2f}")
