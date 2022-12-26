from typing import List
from fastapi import WebSocket


class  WebsocketManagerClass:
    def __init__(self):
        self.active_connections: List[WebSocket,str] = []
        self.channelList = {}


    async def connect(self, websocket: WebSocket,channel:str):
        await websocket.accept()
        await self.send_personal_message("*Yazgun Server*",websocket=websocket)
        await self.send_personal_message("Lütfen Bir username Giriniz : ",websocket=websocket)
        username = await websocket.receive_text()

        self.active_connections.append(websocket)

        if(channel  not in self.channelList.keys()):
            self.channelList[channel] = []
        self.channelList[channel].append([websocket,username])
        await self.send_personal_message("Hoşgeldin "+username, websocket=websocket)
        await self.send_message(websocket_referance=websocket,message="<-Sunucuya katıldı. ",channel="services")

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

    async def send_message(self,websocket_referance:WebSocket, message: str,channel:str):
        try:

            username = ""
            for connection in self.channelList[channel]:
                if websocket_referance == connection[0]:
                    username = connection[1]



            for connection in self.channelList[channel]:

                if websocket_referance == connection[0]:

                    print(username+" bir mesaj gönderdi...")
                else:
                    await connection[0].send_text(username+" : "+message)
        except KeyError:
            return "websocket not online"