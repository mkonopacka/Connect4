import asyncio
import itertools
import json
import websockets
from connect4 import PLAYER1, PLAYER2, Connect4

async def handler(websocket):
    # Initialize the board and alternate turns.
    game = Connect4()
    turns = itertools.cycle([PLAYER1, PLAYER2])
    player = next(turns)
    # Iterate over messages from the client ad update the game state based on received events.
    async for message in websocket:
        print(message)
        event = json.loads(message)
        assert event["type"] == "play"
        column = event["column"]
        try:
            row = game.play(player, column)
        # Send error message if the move was illegal and wait for the next message.
        except RuntimeError as exc:
            event = {"type": "error","message": str(exc)}
            await websocket.send(json.dumps(event))
            continue

        # Send a "play" event to update the UI.
        event = {
            "type": "play",
            "player": player,
            "column": column,
            "row": row,
        }
        # Wait until the event is sent before continuing.
        await websocket.send(json.dumps(event))

        # If move is winning, send a "win" event.
        if game.winner is not None:
            event = {"type": "win","player": game.winner}
            await websocket.send(json.dumps(event))

        # Alternate turns.
        player = next(turns)


async def main():
    async with websockets.serve(handler, "", 8001):
        print("Server started at http://localhost:8001")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())