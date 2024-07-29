# Component on lines 44-107

# Insures number of infected is an integer between 0-200
def validate_num_infected(min_amount, max_amount):
      """Purpose: Validates the input of the number of infected
      Passed: An integer indicating the max number of infected
      Returns: A positive integer between 0 and 200"""

      while True:
            try:
                  input_data = int(input())
                  if input_data >= min_amount and input_data <= max_amount:
                        return input_data
                  else:
                        print("The number of infected mus be between", min_amount,  "and", max_amount, ":")
            except:
                  print("The number of infected must be a whole number between", min_amount,  "and", max_amount, ":")


# Data Creation: Prompt users to create and give the number of infected for 3 countries
def create_country(countries, infected):
      """Purpose: Prompts user to input countries and number of infected to be stored
      Passed: countries and infected
      Returns: Nothing"""

      MIN_AMOUNT = 50
      MAX_AMOUNT = 200

      while len(countries) != 3:
            print("Please enter the name of your country:")
            country_name = input()

            while len(country_name) == 0:
                  print("You didn't enter anything. Please try again:")
                  country_name = input()

            countries.append(country_name)
            print("Please enter the number of infected in this country. "
                  "The number of infected mus be between", MIN_AMOUNT, "and", MAX_AMOUNT, ":")
            num_infected = validate_num_infected(MIN_AMOUNT, MAX_AMOUNT)
            infected.append(num_infected)


# Ensures that the user selects one of their previously inputted countries
def validate_country(countries):
      """Purpose: Validates the input of a country
      Passed: Nothing
      Returns: A valid country"""

      while True:
            try:
                  chosen_country = input()
                  if chosen_country == countries[0]:
                        return chosen_country

                  elif chosen_country == countries[1]:
                        return chosen_country

                  elif chosen_country == countries[2]:
                        return chosen_country

                  else:
                     print("That is not one of your countries. Please check your spelling and try again:")
            except:
                  print("That is not one of your countries. Please check your spelling and try again:")


# Modifying/Adjusting data: Prompts user to select on country to help
def increase_decrease_infected(countries, infected, num_countries):
      """Purpose: Prompt user to select one country to help by decreasing amount of infected by 30 while
      others increase by 20
      Passed: countries, infected and number of countries
      Return: Nothing"""

      INCREASE_INFECTED = int(20)
      DECREASE_INFECTED = int(30)

      for i in range(num_countries):
            print(countries[i], "has", infected[i], "infected citizens")

      print()
      print("Please select one country to help:")
      help_country = validate_country(countries)
      if help_country == countries[0]:
            infected[0] -= DECREASE_INFECTED
            infected[1] += INCREASE_INFECTED
            infected[2] += INCREASE_INFECTED

      elif help_country == countries[1]:
            infected[1] -= DECREASE_INFECTED
            infected[0] += INCREASE_INFECTED
            infected[2] += INCREASE_INFECTED

      elif help_country == countries[2]:
            infected[2] -= DECREASE_INFECTED
            infected[0] += INCREASE_INFECTED
            infected[1] += INCREASE_INFECTED


countries = []
infected = []
create_country(countries, infected)
print()
num_countries = len(countries)
increase_decrease_infected(countries, infected, num_countries)
print(countries)
print(infected)