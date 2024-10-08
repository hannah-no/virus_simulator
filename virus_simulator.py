# Last Updated: 01.08.2024
import time

# Insures number of infected is an integer between 0-200
def validate_num_infected(min_amount):
    """Purpose: Validates the input of the number of infected
    Passed: An integer indicating the max number of infected
    Returns: A positive integer between 0 and 200"""

    while True:
        # noinspection PyBroadException
        try:
            input_data = int(input())
            if min_amount <= input_data <= max_num_infected:
                return input_data

            else:
                print("The number of infected must be between", min_amount,  "and", max_num_infected, ":")
        except:
            print("The number of infected must be a whole number between", min_amount,  "and", max_num_infected, ":")


# Data Creation: Prompt users to create and give the number of infected for 3 countries
def create_country():
    """Purpose: Prompts user to input countries and number of infected to be stored
    Passed: countries and infected
    Returns: Nothing"""

    MIN_AMOUNT = 50

    while len(countries) != 3:
        print("Please enter the name of your country:")
        country_name = input()

        while len(country_name) == 0:
            print("You didn't enter anything. Please try again:")
            country_name = input()

        countries.append(country_name)
        print("Please enter the number of infected in this country.")
        print("The number of infected must be between", MIN_AMOUNT, "and", max_num_infected, ":")
        num_infected = validate_num_infected(MIN_AMOUNT)
        infected.append(num_infected)


# Ensures that the user selects one of their previously inputted countries
def validate_country():
    """Purpose: Validates the input of a country
    Passed: Nothing
    Returns: A valid country"""

    while True:
        # noinspection PyBroadException
        try:
            chosen_country = input()
            if chosen_country == countries[0]:
                return chosen_country

            elif chosen_country == countries[1]:
                return chosen_country

            elif chosen_country == countries[2]:
                return chosen_country

            elif len(chosen_country) == 0:
                print("You have not typed anything please try again.")

            else:
                print("That is not one of your countries. Please check your spelling and try again:")

        except:
            print("That is not one of your countries. Please check your spelling and try again:")


# Checks that the number of infected has not decreased to below zero and replaces it with zero if it has
def validate_decrease_infected(num_infected):
    """Purpose: Ensures that the number of infected id=s decreased sensibly
    Passed: infected
    Returns: Nothing"""
    if infected[num_infected] < 0:
        infected.pop(num_infected)
        infected.insert(num_infected, int(0))


# Modifying/Adjusting data: Prompts user to select on country to help
def increase_decrease_infected():
    """Purpose: Prompt user to select one country to help by decreasing amount of infected by 30 whole
    others increase by 20
    Passed: countries, infected and number of countries
    Return: Nothing"""

    INCREASE_INFECTED = int(20)
    DECREASE_INFECTED = int(30)

    for i in range(num_countries):
        print(countries[i], "has", infected[i], "infected citizens")
        time.sleep(0.5)

    print()
    print("Please select one country to help:")
    help_country = validate_country()
    if help_country == countries[0]:
        infected[0] -= DECREASE_INFECTED
        infected[1] += INCREASE_INFECTED
        infected[2] += INCREASE_INFECTED
        validate_decrease_infected(0)

    elif help_country == countries[1]:
        infected[1] -= DECREASE_INFECTED
        infected[0] += INCREASE_INFECTED
        infected[2] += INCREASE_INFECTED
        validate_decrease_infected(1)

    elif help_country == countries[2]:
        infected[2] -= DECREASE_INFECTED
        infected[0] += INCREASE_INFECTED
        infected[1] += INCREASE_INFECTED
        validate_decrease_infected(2)


# Repeats the program 5 times for five days
def five_days():
    """Purpose: Repeats program Five times
    Passes: Nothing
    Returns: Nothing"""
    for i in range(1, 6, 1):
        time.sleep(1)
        print("Day", i)
        increase_decrease_infected()
        print()


# Gives the final amount of infected for each country and whether or not they've gone into lockdown
def final_stats():
    """Purpose: Give each country's final amount of infect and lockdown status
    Passed: countries, infected, and number of countries
    Returns: Nothing"""

    for i in range(num_countries):
        if infected[i] > max_num_infected:
            print(countries[i], "has", infected[i], "citizens and has gone into lockdown.")
            time.sleep(0.5)
        else:
            print(countries[i], "has", infected[i], "citizens and has successfully stayed out of lockdown.")
            time.sleep(0.5)


countries = []
infected = []
max_num_infected = 200

print("You have been selected to participate in a virus simulation which will happen over five days.")
time.sleep(1.5)
print("Your goal is to control the spread of infection and prevent three countries from going into lockdown.")
time.sleep(1.5)
print("You will receive more information later, but first you need to create your countries and state how many ")
print("infected citizens are in each. the number or infected must be between 50 and", max_num_infected, ".")
time.sleep(1.5)
create_country()
print()

print("Now you have to control the spread of infection.")
time.sleep(1.5)
print("At the start of each day you will choose one country to help. The number of infected in this country ")
print("will decrease by 30 while the others increase by 20.")
time.sleep(1.5)
print("Once five days have passed, any country with more than", max_num_infected, "infected will be put in lock down,")
print("deeming you unsuccessful.")
print()

num_countries = len(countries)
five_days()
time.sleep(1.5)
final_stats()
