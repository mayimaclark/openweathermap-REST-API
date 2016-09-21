# openweathermap-REST-API

This project uses the OpenWeatherMap site to provide a simple REST API to get weather data. The requests HTTP package is used and can be studied here as well.

The script will get the current weather data for a particular zip code and print some of the data in a table. For example, the zip code 30144 will have the following output:

Name:                     Kennesaw 
Current Temperature:      40.44 degrees Fahrenheit
Atmospheric Pressure:     992.52 hPa
Wind Speed                9.86 mph
Wind Direction            287.503 
Time of Report            2016-02-25 11:13:24 

Data is sent back encoded as JSON and will be decoded to access and print the information from the response.

It's important to note, at the beginning of the script, variables user_id and user_apiid are strings with the values of the id and apiid from OpenWeatherMap. These values are not included directly in the code, just the variables, so they can be substitutued for anyone downloading the project.
