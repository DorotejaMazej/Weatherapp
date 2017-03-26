from google.appengine.api import users
from handlers.base import BaseHandler
from models.city import City
from utils.decorators import validate_csrf


class CityAdd(BaseHandler):
    def get(self):
        return self.render_template("city_add.html")

    @validate_csrf
    def post(self):
        user = users.get_current_user()

        if not user:
            return self.write("Please login before you're allowed to post a topic.")

        title = self.request.get("name")
        text = self.request.get("text")

        new_city = City(name=title, weather=text, author_email=user.email())
        new_city.put()

        return self.redirect_to("city-details", city_id=new_city.key.id())


class CityDetails(BaseHandler):
    def get(self, city_id):
        city = City.get_by_id(int(city_id))

        params = {"city": city}
        return self.render_template("city_details.html", params=params)


class DeleteCity(BaseHandler):
    @validate_csrf
    def post(self, city_id):
        city = City.get_by_id(int(city_id))

        user = users.get_current_user()

        if city.author_email == user.email() or user.is_current_user_admin():
            City.delete(city=city)

        return self.redirect_to("main-page")
