import clr

clr.AddReference("cAlgo.API")

from System import Action
from cAlgo.API import HttpResponse
    
def http_get(uri):
    """
    Performs a GET request to the specified URI.
    
    Args:
        uri: The URI that the GET request should be made to. Can be either a string or Uri object.
        
    Returns:
        The HttpResponse object representing the result of the request.
        
    Examples:
        response = get("https://api.example.com/data")
        status_code = response.StatusCode
        content = response.Content
        
        from System import Uri
        uri_object = Uri("https://api.example.com/data")
        response = get(uri_object)
    """
    return api.Http.Get(uri)


def http_send(request):
    """
    Performs a request to the specified URI. The request method depends on the value of the request.Method property.
    
    Args:
        request: The HttpRequest object representing the request contents.
        
    Returns:
        The HttpResponse object representing the result of the request.
        
    Examples:
        from cAlgo.API import HttpRequest
        
        request = HttpRequest("https://api.example.com/data", "POST")
        request.AddHeader("Content-Type", "application/json")
        request.SetBody('{"name": "John", "age": 30}')
        
        response = send(request)
        status_code = response.StatusCode
        content = response.Content
    """
    return api.Http.Send(request)


def http_get_async(uri, callback):
    """
    Performs a GET request to the specified URI asynchronously.
    
    Args:
        uri: The URI that the GET request should be made to. Can be either a string or Uri object.
        callback: The method to be invoked when the request is being sent.
        
    Examples:
        def on_response(response):
            print(f"Status: {response.StatusCode}")
            print(f"Content: {response.Content}")
            
        get_async("https://api.example.com/data", on_response)
    """
    action = Action[HttpResponse](callback)
    return api.Http.GetAsync(uri, action)


def http_send_async(request, callback):
    """
    Performs a request to the specified URI asynchronously. The request method depends on the value of the request.Method property.
    
    Args:
        request: The HttpRequest object representing the request contents.
        callback: The method to be invoked when the request is being sent.
        
    Examples:
        def on_response(response):
            print(f"Status: {response.StatusCode}")
            print(f"Content: {response.Content}")
            
        from cAlgo.API import HttpRequest
        request = HttpRequest("https://api.example.com/data", "POST")
        request.AddHeader("Content-Type", "application/json")
        request.SetBody('{"name": "John", "age": 30}')
        
        send_async(request, on_response)
    """
    action = Action[HttpResponse](callback)
    return api.Http.SendAsync(request, action)