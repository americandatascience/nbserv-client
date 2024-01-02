# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_get**](DefaultApi.md#api_get) | **GET** /api/ | Get the Jupyter Server version


# **api_get**
> ApiGet200Response api_get()

Get the Jupyter Server version

This endpoint returns only the Jupyter Server version. It does not require any authentication. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.api_get200_response import ApiGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Get the Jupyter Server version
        api_response = api_instance.api_get()
        print("The response of DefaultApi->api_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiGet200Response**](ApiGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Jupyter Server version information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

