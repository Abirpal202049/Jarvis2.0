# Python program to find current 
# weather details of any city 
# using openweathermap api 

# import required modules 
import requests,json
from JARVIS import*

# Enter your API key here 
api_key = "e342367614d61e912d92e29103041f54"

# base_url variable to store url 
base_url = "api.openweathermap.org/data/2.5/weather?"

# Give city name 
speak('Sir, Enter the name of the city')
city_name = input("Enter city name : ") 

# complete_url variable to store 
# complete url address 
complete_url = 'http://api.openweathermap.org/data/2.5/weather?'+'q='+city_name+'&appid='+api_key 

# get method of requests module 
# return response object 
response = requests.get(complete_url) 

# json method of response object 
# convert json format data into 
# python format data 
x = response.json() 

# print(response)

# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 



if x["cod"] != "404": 

	# store the value of "main" 
	# key in variable y 
	y = x["main"] 

	# store the value corresponding 
	# to the "temp" key of y 
	current_temperature = y["temp"] 

	# store the value corresponding 
	# to the "pressure" key of y 
	current_pressure = y["pressure"] 

	# store the value corresponding 
	# to the "humidity" key of y 
	current_humidiy = y["humidity"] 

	# store the value of "weather" 
	# key in variable z 
	z = x["weather"] 

	# store the value corresponding 
	# to the "description" key at 
	# the 0th index of z 
	weather_description = z[0]["description"] 

	# print following values 
	print(" Sir the Temperature is " +
					str(round(current_temperature-273.15,2)) + 'degree Celsius' +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidiy) +
		"\n description = " +
					weather_description) 
	

	speak(" Sir, The Temperature is " +
					str(round(current_temperature-273.15,0)) + 'degree Celsius in,'+ city_name)
	speak(f'Sir The weather outside is {weather_description}. And The humidity and presser is {current_humidiy}grams per kg. and {current_pressure} Pascel, respectively ')


else: 
	print(" City Not Found ") 
'''
this can be made more better
'''