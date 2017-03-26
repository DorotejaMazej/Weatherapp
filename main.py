#!/usr/bin/env python
import webapp2
from handlers.base import MainHandler, CookieAlertHandler
from handlers.cities import CityAdd, CityDetails, DeleteCity
from handlers.weathers import WeatherHandler, WeatherDetails, LondonWeather, LjubljanaWeather, MadridWeather, \
    LisbonWeather, BerlinWeather, ParisWeather

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="set-cookie"),
    webapp2.Route('/city/add', CityAdd, name="city_add"),
    webapp2.Route('/city/<city_id:\d+>', CityDetails, name="city-details"),
    webapp2.Route('/city/<city_id:\d+>/delete', DeleteCity, name="city-delete"),
    webapp2.Route('/result', WeatherHandler, name="data"),
    webapp2.Route('/weather/<weather_id:\d+>', WeatherDetails, name="weather-details"),

    webapp2.Route('/weather/city', LondonWeather, name="london"),
    webapp2.Route('/weather/paris', ParisWeather, name="paris"),
    webapp2.Route('/weather/berlin', BerlinWeather, name="berlin"),
    webapp2.Route('/weather/lisbon', LisbonWeather, name="lisbon"),
    webapp2.Route('/weather/madrid', MadridWeather, name="madrid"),
    webapp2.Route('/weather/ljubljana', LjubljanaWeather, name="ljubljana"),
], debug=True)
