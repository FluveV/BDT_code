'''
The aim is to store in Redis the final
dataframe containing the computed risks for
each city. The df will be stored in form of
document. It is possible to query the document
for all cities or one city.
'''
import json
from BDT_code.redis_configuration.data_conversion import DataPreparation
from BDT_code.redis_configuration.redis_operations import RedIngestion

RedIngestion.store_data()

city_demo = "To obtain city-specific results, please insert one of the following locations" + \
             " or find out from the official documentation which cities that we did not list here we have data on." + \
             "Birmingham, Cambridge, Cardiff, London"
print(city_demo)
user_input = input("Enter a city: ")

print(f"You entered {user_input}.")

result = RedIngestion.retrieve_city_data(user_input)

if result:
    city_data = json.loads(result)
    print(f"Data for {user_input}:\n", json.dumps(city_data, indent=4))
else:
    print(f"No data found for {user_input}.")

