class HttpEndpointsClass:

    def __init__(self,app):
        self.app = app

        self.endpoints()

    def endpoints(self):
        @self.app.get("/services")
        async def http_endpoint():

            return {"data": "merhaba nasılsın"}
 




