import asyncio
import websockets

async def chatroom():
    url = ("ws://localhost:8765")
    # connect to websocket server with declared url.
    async with websockets.connect(url) as websocket:
        # direct user to enter their name and send it.
        name = input("Enter your name:")
        await websocket.send(name)
        # receive the greeting.
        greeting = await websocket.recv()
        print(f"{greeting}")
        while True:
            # let user send messages repeatedly.
            message=input("Write:")
            # if the message is "exit" close the client side.
            if message == 'exit':
                break
            await websocket.send(message)

if __name__ == "__main__":
    asyncio.run(chatroom())