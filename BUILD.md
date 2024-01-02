# Initial Build

# OpenAPI Generator

Website: `https://openapi-generator.tech`

Docker: 
```
docker run --rm \
    -v ${PWD}:/local openapitools/openapi-generator-cli generate \
    -i /local/api.yaml \
    -g python \
    -o /local \
    --additional-properties=packageName=nbserv_client
```

# Origin OpenAPI Configurations YAML

Website: `https://jupyter-server.readthedocs.io/en/latest/developers/rest-api.html`

YAML: `https://raw.githubusercontent.com/jupyter/jupyter_server/master/jupyter_server/services/api/api.yaml`
