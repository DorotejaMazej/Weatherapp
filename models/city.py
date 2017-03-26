from google.appengine.ext import ndb


class City(ndb.Model):
    name = ndb.StringProperty()
    weather = ndb.StringProperty()
    author_email = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)

    @classmethod
    def delete(cls, city):
        city.deleted = True
        city.put()

        return city

