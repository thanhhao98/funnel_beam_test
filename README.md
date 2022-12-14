# Find Phone Number
This service for finding `formatted_phone_number` from `address` by using google api.
## CodeGen information
This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  This
This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.8

## Usage

Prepare
```bash
pip3 install -r requirements.txt
pip3 install tox==3.20.1
```

To run the server, please execute the following from the root directory:
```bash
export G_API_KEY=your_google_api_key
python3 -m swagger_server
```

and open your browser to here/postman:
```
http://localhost:8080/ui/
```

To launch the unittest:
```bash
tox swagger_server/test/unit_test
```

To launch the integration tests, replace your `G_API_KEY` in `tox.init` and run:
```bash
tox swagger_server/test/integration_test 
```

## Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t find_phone_number -f docker/Dockerfile .

# starting up a container
docker run -e G_API_KEY=your_google_api_key -p 8080:8080 find_phone_number
```

and also open your browser to here/postman:
```
http://localhost:8080/ui/
```
