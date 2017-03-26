from google.appengine.ext import ndb


class Weather(ndb.Model):
    city_name = ndb.StringProperty()
    country_name = ndb.StringProperty()
    description = ndb.StringProperty()
    temperature = ndb.StringProperty()
    humidity = ndb.StringProperty()
    author_email = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)