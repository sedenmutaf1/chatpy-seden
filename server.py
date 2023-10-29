import asyncio
import websockets


async def chatroom(websocket, path):
    global name
    try:
        # wait for and receive user's name.
        name = await websocket.recv()
        print(f"\n{name} has entered the chat.")
        await websocket.send(f"\nWelcome {name}, you are added to the chatroom")
        while True:
            # wait for and receive user's message repeatedly.
            message = await websocket.recv()
            # print the message on server.
            print(f"{name}:{message}")
    except websockets.exceptions.ConnectionClosedError:
        # if the connection is lost, express this.
        print(f"{name} has left the chat.")
    except Exception as e:
        print(f"An error occurred: {e}")


async def main():
    # start a websocket server that listens on "localhost" at port 8765
    async with websockets.serve(chatroom, "localhost", 8765):
        # run forever.
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
