cities=['Paris','Berlin','Madrid','Rome','Lisbon','Vienna']
weather_data={
    'Paris':'20°C',
    'Berlin':'18°C',
    'Madrid':'22°C',
    'Rome':'24°C',
    'Lisbon':'21°C',
    'Vienna':'23°C'
}
def list_cities():
    return cities
def get_weather(city):
    return weather_data.get(city, "City not found")
