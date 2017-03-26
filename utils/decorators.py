from google.appengine.api import memcache


def validate_csrf(handler):
    def wrapper(self, *args, **kwargs):
        csrf_token = self.request.get("csrf_token")
        mem_token = memcache.get(key=csrf_token) # find if this CSRF exist in memcache

        if mem_token:
            return handler(self, *args, **kwargs)
        else:
            return self.write("You are an evil attacker!")

    return wrapper