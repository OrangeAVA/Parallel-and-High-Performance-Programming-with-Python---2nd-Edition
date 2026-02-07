import azure.functions as func
import logging

app = func.FunctionApp()

@app.route(route='hello_function', auth_level=func.AuthLevel.ANONYMOUS)
def hello_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse('Hello, Azure!', status_code=200)
