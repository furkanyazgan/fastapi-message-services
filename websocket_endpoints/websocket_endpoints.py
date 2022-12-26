from fastapi import WebSocket, WebSocketDisconnect


class WebsocketEndpointsClass:
    
    def __init__(self,app,manager):
        self.app = app
        self.manager = manager
        self.endpoints()



    def endpoints(self):
        @self.app.websocket("/harem")
        async def websocket_endpoint(websocket: WebSocket):
            await self.manager.connect(websocket, channel="harem")
            try:
                while True:

                    message  = await websocket.receive_text()
                    print(message)
                    await self.manager.send_message(websocket_referance=websocket,message=message,channel="harem")


            except WebSocketDisconnect:                
                self.manager.disconnect(websocket)


