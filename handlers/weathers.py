from handlers.base import BaseHandler
from google.appengine.api import urlfetch, users
from models.weather import Weather
import json
from utils import secrets


class WeatherHandler(BaseHandler):
    def post(self):
        city = self.request.get("city")

        url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric" + "&APPID=" + secrets.secrets()

        nd_url = "http://api.openweathermap.org/data/2.5/forecast?q=" + city + "&units=metric&APPID=" + secrets.secrets()


        result = urlfetch.fetch(url)
        zp = urlfetch.fetch(nd_url)

        data = json.loads(result.content)
        forecast = json.loads(zp.content)

        params = {"data": data, "forecast": forecast}

        self.render_template("weather.html", params=params)


class WeatherDetails(BaseHandler):
    def get(self, weather_id):
        weather = Weather.get_by_id(int(weather_id))

        params = {"weather": weather}

        return self.render_template("weather.html", params=params)


class LondonWeather(BaseHandler):
    def get(self):
        url = "http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&APPID=" + secrets.secrets()
        result = urlfetch.fetch(url)
        london = json.loads(result.content)
        params = {"london": london}

        return self.render_template("london.html", params=params)


class ParisWeather(BaseHandler):
    def get(self):
        url = "http://api.openweathermap.org/data/2.5/weather?q=Paris&units=metric&APPID=" + secrets.secrets()
        result = urlfetch.fetch(url)
        paris = json.loads(result.content)
        params = {"paris": paris}

        return self.render_template("paris.html", params=params)


class BerlinWeather(BaseHandler):
    def get(self):
        url = "http://api.openweathermap.org/data/2.5/weather?q=Berlin&units=metric&APPID=" + secrets.secrets()
        result = urlfetch.fetch(url)
        berlin = json.loads(result.content)
        params = {"berlin": berlin}

        return self.render_template("berlin.html", params=params)


class LisbonWeather(BaseHandler):
    def get(self):
        url = "http://api.openweathermap.org/data/2.5/weather?q=Lisbon&units=metric&APPID=" + secrets.secrets()
        result = urlfetch.fetch(url)
        lisbon = json.loads(result.content)
        params = {"lisbon": lisbon}

        return self.render_template("lisbon.html", params=params)


class MadridWeather(BaseHandler):
    def get(self):
        url = "http://api.openweathermap.org/data/2.5/weather?q=Madrid&units=metric&APPID=" + secrets.secrets()
        result = urlfetch.fetch(url)
        madrid = json.loads(result.content)
        params = {"madrid": madrid}

        return self.render_template("madrid.html", params=params)


class LjubljanaWeather(BaseHandler):
    def get(self):
        url = "http://api.openweathermap.org/data/2.5/weather?q=Ljubljana&units=metric&APPID=" + secrets.secrets()
        result = urlfetch.fetch(url)
        ljubljana = json.loads(result.content)
        params = {"ljubljana": ljubljana}

        return self.render_template("ljubljana.html", params=params)

