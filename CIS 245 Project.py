import requests
from pandas import json_normalize

def cityZip():
    callType = ''
    # Loop through request until user a entered a value of 1 or 2
    while callType != '1' and callType != '2':
        print("To view weather report please enter 1 for city or 2 to view by zip.")
        callType = input()
    return callType

def city(api_key):
    print("Please enter the city.")
    userCity = input()
    url = "http://api.openweathermap.org/data/2.5/forecast?q=" + userCity + "&appid=" + api_key
    return url

def zip(api_key):
    print("Please enter the zip.")
    # Error handling to check if a proper zip code has been entered.
    while True:
        userZip = input()
        try:
            userZip = int(userZip)
            if len(str(userZip)) != 5:
                print("Please enter a valid 5 digit zip.")
        except ValueError:
            print("Please enter a valid 5 digit zip.")
        if type(userZip) == type(int()) and len(str(userZip)) == 5:
            break
    url = "http://api.openweathermap.org/data/2.5/forecast?zip="+ str(userZip) + "&appid=" + api_key
    return url

def api_call(url):
    try:
        headers = {"Accept": "application/json"}
        response = requests.request("GET", url, headers=headers)
        weatherData = response.json()
        df1 = json_normalize(weatherData['list'], 'weather')
        df2 = json_normalize(weatherData['list'])
        weatherData = df2.drop('weather', axis=1).join(df1)
    except:
        print("Error")

    return weatherData

def main ():
    api_key = "d0d1ca66c3a38e2f0479613ba5b2ab3f"

    while True:
        callType = cityZip()

        if callType == '1':
            url = city(api_key)
        elif callType == '2':
            url = zip(api_key)

        weatherReport = api_call(url)
        print(weatherReport)

        print('Would you like to get another weather report? (yes or no)')
        getWeather = input()
        if getWeather == 'no':
            break

if __name__ == "__main__":
    main()