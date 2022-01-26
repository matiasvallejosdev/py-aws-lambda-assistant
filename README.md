<h1 align="center"> Python Lambda Handler </h1>
  <div align="center">

  [![GitHub release (latest by date)](https://img.shields.io/github/v/release/matiasvallejosdev/py-aws-lambda-handlers?color=4cc51e)](https://github.com/matiasvallejosdev/py-aws-lambda-handlers)
  [![GitHub top language](https://img.shields.io/github/languages/top/matiasvallejosdev/py-aws-lambda-handlers?color=1081c2)](https://github.com/matiasvallejosdev/py-aws-lambda-handlers/search?l=c%23)
  [![GitHub Watchers](https://img.shields.io/github/watchers/matiasvallejosdev/py-aws-lambda-handlers?color=4cc51e)](https://github.com/matiasvallejosdev/py-aws-lambda-handlers/watchers)
  <br />
  [![GitHub Repo stars](https://img.shields.io/github/stars/matiasvallejosdev/py-aws-lambda-handlers?color=4cc51e)](https://github.com/matiasvallejosdev/py-aws-lambda-handlers/stargazers)
  [![GitHub Forks](https://img.shields.io/github/forks/matiasvallejosdev/py-aws-lambda-handlers?color=4cc51e)](https://github.com/matiasvallejosdev/py-aws-lambda-handlers/network/members)
  [![made-for-VSCode](https://img.shields.io/badge/Made%20for-VSCode-1f425f.svg)](https://code.visualstudio.com/)
  </div>
<p align="center"> 
This repository contains a python package that serves as a controller for AWS lambda functions, including http output handler, input validation, error handling, and response formatting.
<p/>

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Examples](#examples)
    - [HTTP Handler](#http-handler)
    - [Lambda Errors](#lambda-errors)
- [Contributing](#contributing)
- [Credits](#credits)
- [Thanks](#thanks)

## Installation
　1. Clone a repository or download it as zip.
```
    git clone https://github.com/matiasvallejosdev/unity-tensorflow-image-classifier
```

## Examples:
### HTTP handler

Now you perform your result with ```buildLambdaBody(route, response)``` and ```HTTPHandler``` performs your Headers with CORS and also perform Body with your errors response and HTTPs status codes.

```python
from lambda_handlers.errors import *
from lambda_handlers.handlers.event_handler import *
from lambda_handlers.handlers.http_handler import *

# Example of lambda function
@HTTPHandler(headers=CORSHeaders(origin='localhost', credentials=True))
def lambda_function(event, context):
    routeKey = event['routeKey']
    # Do something
    return buildLambdaBody(
        routeKey, 
        "Hello World from lambda function!" # Result response
    )
```

```bash
aws lambda invoke --function-name example response.json
cat response.json
```

```json
{
    "headers":{
        "Access-Control-Allow-Credentials": true,
        "Access-Control-Allow-Origin": "localhost",
        "Content-Type": "application/json"
    },
    "statusCode": 200,
    "body": "{\"message\": \"Hello World from lambda function!\"}"
}
```
### Lambda errors
You can construct your own errors using the father class ```LambdaError()``` with a ```CustomHttpError()``` _-> @dataclass_ that can help you in your http response body.

```python
error = LambdaError(NotFoundError())
error = error.asDict()
```
```python
error = LambdaError(PutDataFailedError())
error = error.asDict()
```
```python
error = LambdaError(DeleteDataFailedError())
error = error.asDict()
```
```python
error = LambdaError(ConflictConnectionError())
error = error.asDict()
```
```python
error = LambdaError(GetDataFailedError())
error = error.asDict()
```
```python
error = LambdaError(BadRequestError())
error = error.asDict()
```
```python
error = LambdaError(InternalServerError())
error = error.asDict()
```
```python
print(error) # -> LambdaError(InternalServerError()).asDict()
```
If you print your lambda error dictionary you can get the following results. This results will be performed by the lambda wrapper and also you can send 'Error' attribute to the body in the response.
```python
{
    'Error': {
        'statusCode': 500,
        'message': "Server got itself in trouble",
        'type': 'internalServerError'
    }
}
```

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are greatly appreciated. <br /><br />
　1.　Fork the Project. <br />
　2.　Create your Feature Branch. <br />
　3.　Commit your Changes. <br />
　4.　Push to the Branch. <br />
　5.　Open a Pull Request. <br />

## Credits

- Main Developer: [Matias A. Vallejos](https://www.linkedin.com/in/matiasvallejos/)

## Thanks

_For more information about the project contact me! Do not hesitate to write me just do it!_
