import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.write("logout app")


app = webapp2.WSGIApplication(
		[
			('/logout/*', MainPage),
		],
		debug=True
	)