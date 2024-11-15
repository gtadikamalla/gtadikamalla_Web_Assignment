import requests
import json
import pandas as pd


#Displaying the sample data for year 2024 and country code is AT
sample_API="https://date.nager.at/api/v3/PublicHolidays/2024/AT"

response=requests.get(sample_API)
data=response.json()
print(json.dumps(data,indent=4))
print('_________________________________________________________')
print('According to API URL, Year and Country code variables are inputs.')

#Promt user for year and Country code.
#Allow the user try multiple times.
while True:
    API_URL="https://date.nager.at/api/v3/PublicHolidays/"
    Year=input('Enter year(eg: 1998):')
    if not Year.isdigit():
        print('______________________________________')
        print('Invalid input. Please enter only year.')
        print('______________________________________')
        continue
    Country_Code=input("Enter country code (AD or AL or AM or AR or AT):")
    if not Country_Code.isalpha():
        print('___________________')
        print('Invalid input. \nPlease enter country code in AD or AL or AM or AR or AT:')
        print('___________________________________________________')
        continue

    API_URL += Year +'/'+Country_Code

    response= requests.get(API_URL)

    data=response.json()

    holidays_df=pd.DataFrame(data)
    print('In table format:')
    print('================')

    print(holidays_df)
    print('____________________________________________________________')
    print('In JSON format:')
    print('================')

    print(json.dumps(data, indent=4))

    choice=input('Do you want to continue or quit? (Enter c/q):')
    if choice in 'cC':
        continue
    else:
        break
