import requests
import json
import sys
sys.path.append("..")
from Reusable_code.Must_contain import must_contain_this

def get_population(year):

    if 1968 > int(year) > 2023:
        raise ValueError("The year must be between 1968 and 2023")

    my_post = {
        "query": [
            {"code": "ContentsCode", "selection": {"filter": "item", "values": ["BE0101N1"]}},
            {"code": "Tid", "selection": {"filter": "item", "values": [year]}},
        ],
        "response": {"format": "json"},
    }
    SCB = "https://api.scb.se/OV0104/v1/doris/sv/ssd/BE/BE0101/BE0101A/BefolkningNy"

    try: # Try sending a post request
        response = requests.post(SCB, json = my_post)
        response.raise_for_status() # Raise error if unsuccessful
    except (json.JSONDecodeError, requests.exceptions.HTTPError):  # Catch error
        print("400 Client Error: Access denied due to bad Request for SCB API")
        sys.exit()
    
    data = response.json() # Get the data from the API
    population = data["data"][0]["values"][0] # Extract population
    return int(population)

def validate(year):
    try:           # Try validating the year
        temp = get_population(year)
        return temp
    except ValueError:     # Catch and print the error
        print("Failed to fetch data")


def main():
    year1 = input("Population from year: ")     # Get the first year
    population1 = validate(year1)

    year2 = input("Population from year: ")     # Get the second year
    population2 = validate(year2)

    # Calculate and print difference in population
    difference = population2 - population1
    print(f"\nThe population in {year1}: {population1}") # Population of the first year
    print(f"The population in {year2}: {population2}") # Population of the second year
    print(f"Difference in population: {difference}") # Difference in population

if __name__ == '__main__':
    main()