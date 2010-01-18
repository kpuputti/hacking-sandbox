# -*- coding: utf-8 -*-
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from notifier import is_profane
import simplejson


_debug = False

class ProfanierPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain; charset=UTF-8'
        s = self.request.get('s')
        response = dict(string=s, isProfane=is_profane(s))
        self.response.out.write(simplejson.dumps(response))

def main():
    app = webapp.WSGIApplication([('/isProfane', ProfanierPage)], debug=_debug)
    run_wsgi_app(app)

if __name__ == "__main__":
    main()
