import falcon
import json

class Index(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = '<html>Hello world</html>'

        print("Received GET")

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_201
        resp.body = req.stream.read()
        
        print("Received POST")


class HealthCheck(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({'status':'ok'})

        print("Recieved Health Check")

app = falcon.API()

app.add_route('/', Index())
app.add_route('/healthz', HealthCheck())
