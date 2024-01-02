# openapi_client.StatusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_status_get**](StatusApi.md#api_status_get) | **GET** /api/status | Get the current status/activity of the server.


# **api_status_get**
> APIStatus api_status_get()

Get the current status/activity of the server.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.api_status import APIStatus
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
    api_instance = openapi_client.StatusApi(api_client)

    try:
        # Get the current status/activity of the server.
        api_response = api_instance.api_status_get()
        print("The response of StatusApi->api_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusApi->api_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**APIStatus**](APIStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current status of the server |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

