import falcon


class Index(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = '<html>Hello world</html>'


class HealthCheck(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'ok'


app = falcon.API(media_type="text/html")

app.add_route('/', Index())
app.add_route('/healthz', HealthCheck())
