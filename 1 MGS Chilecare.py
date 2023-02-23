"""program to keep track of children throughout the day
yes i just copied you for this one sorry
"""


# This is the menu function
def menu():
      choice = ""
      while choice != "5":
            print("What do you want to do?")
            print()
            print("1 Drop off a child")
            print("2 Pick up a child")
            print("3 Calculate cost")
            print("4 Print roll")
            print("5 Exit the system")
            print()
            print("=============================================")

            choice = input ("Enter your choice (number between 1 and 5): ")
            if choice == "1":
                  drop_off()

            elif choice == "2":
                  pick_up()

            elif choice == "3":
                  print (f"The charge for looking after {len (roll)} children is "
                         f"${calc_cost(len(roll)):.2f}")

            elif choice == "4":
                  print_roll()

            elif choice == "5":
                  exit("no sign of STU")

            else: #In the event of any integer not in the required range
                  print("Must be an integer between 1 and 5")


# Separate Functions for each menu item
def drop_off():
      name1 = input("What is the name of the child you are dropping off? ")
      while len(
              name1) < 3: # To prevent user entering a blank or too short name
            name1 = input("Please enter a valid name: ")
      roll.append(name1)
      print()
      print(name1, "was added to the roll.")
      print()


def pick_up():
      name2= input("What is the name of the child you are picking up? ")
      if name2 in roll:
            roll.remove(name2)
            print(name2, "was removed from the roll.")
            print()
      else:
            print("There's no ", name2, "here at present. Please check name.")
            print()


def calc_cost(number):
      rate = 12.00
      hours = int(input("How many hours to charge for: "))
      cost = number * hours * rate
      return cost


def print_roll():
      print("MGS Daycare clients currently present are: ")
      for item in roll:
            print(f"\t{item}")
      print()


# Main routine
roll = []

print("-----------------------------------------------------------------")

print("Welcome to MGS Childcare")
print("What would you like to do? Please choose one of the items below")
print("-------------------------------------------------------------------")
menu()
