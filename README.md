# Connect 4 game
Single browser version of connect4 game implemented in Python using websockets, based on this tutorial: https://websockets.readthedocs.io/en/stable/intro/tutorial1.html

## How to run?
1. Start the server by running 
```python3 server.py``` 
in the terminal. It is running on port 8001, where the client will connect. If there is a error message saying "adress already in use", kill the running process by 

```
kill -9 $(ps -A | grep python | awk '{print $1}')
```
(it kills all python processes).

2. Open the client in web browser by typing 
```
python -m http.server
```
Frontend is running on port 8000. If you try to do this before starting the server, the client will not be able to connect to the server and error message will be displayed in the console.

3. Go to [localhost:8000](localhost:8000) in the browser to see the game.

4. Players can play their moves interchangably in the opened window. The game ends when one of the players wins or when the board is full. The game can be restarted by refreshing the page.