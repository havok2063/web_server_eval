# web_server_eval
evaluation of various web servers for API

This repo evaluates and compares the following APIs:

- Flask
- Quart
- FastAPI
- Starlette (not yet)
- Black Sheep (not yet)

To run a web server individually, navigate into the relevant API subdirectory within `apitest`

- Flask - `flask run -p [PORT]`
- Quart - `quart run`
- FastAPI - `uvicorn app:app --reload`
- Starlette
- Black Sheep

In a browser window, navigate to the appropriate host e.g. `http://localhost:5000`.

To use `locust` to simulate web users making API requests, navigate into the `apitest` subdirectory and run `locust`.  In a browser, navigate to `http://localhost:8089` and input the following:

- the total number of users to simulate
- the rate at which to spawn new users
- the client host IP address

You can optionally specify client host on the command line with `locust -H hostname`, in which case, leave the hostname field in the UI blank.
