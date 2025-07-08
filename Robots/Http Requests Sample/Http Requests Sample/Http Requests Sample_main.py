import clr

clr.AddReference("cAlgo.API")

# Import cAlgo API types
from cAlgo.API import *

# Import trading wrapper functions
from robot_wrapper import *

# Import http requests functions
from http_requests import *
from System import Uri

EXAMPLE_URL = "https://example.com/"

class HttpRequestsSample():
    def on_start(self):
        print("Robot started!")
        
        # Callback function for async functions
        def on_reposnse(reposnse):
            print(reposnse.Body)
        
        # Synchronous GET request execution
        response = http_get(EXAMPLE_URL)
        print(response.Body)

        # Asynchronous GET request execution
        http_get_async(EXAMPLE_URL, on_reposnse)

        request = HttpRequest(Uri(EXAMPLE_URL))
        request.Method = HttpMethod.Post

        # Synchronous execution of a generic HTTP request (POST, GET, etc.)
        response = http_send(request)
        print(response.Body)

        # Asynchronous execution of a generic HTTP request (POST, GET, etc.)
        http_send_async(request, on_reposnse)

        # To learn more about cTrader Algo visit our Help Center:
        # https://help.ctrader.com/ctrader-algo/