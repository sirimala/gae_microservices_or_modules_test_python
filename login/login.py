import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write("login app")


app = webapp2.WSGIApplication(
		[
			('/login/*', MainPage),
		],
		debug=True
	)