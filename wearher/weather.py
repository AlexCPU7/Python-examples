import pyowm

owm = pyowm.OWM('475268169da15c00e73233befb333b11')  # You MUST provide a valid API key

city = input('В каком городе Вы желаете узнать температуру? ')

observation = owm.weather_at_place(city)
res = observation.get_weather()
temperature = res.get_temperature('celsius')['temp']

print('В городе ' + city + ' сейчас тмпература ' + str(temperature) + ' C')
print('Так же город имеет статус: ' + res.get_detailed_status())
