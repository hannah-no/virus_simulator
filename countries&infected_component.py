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
                        print("The number of infected mus be between", min_amount, "and", max_amount)
            except:
                  print("The number of infected must be a whole number between", min_amount, "and", max_amount)


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


countries = []
infected = []
create_country(countries, infected)
print(countries)
print(infected)

