# openapi_client.KernelspecsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_kernelspecs_get**](KernelspecsApi.md#api_kernelspecs_get) | **GET** /api/kernelspecs | Get kernel specs


# **api_kernelspecs_get**
> ApiKernelspecsGet200Response api_kernelspecs_get()

Get kernel specs

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.api_kernelspecs_get200_response import ApiKernelspecsGet200Response
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
    api_instance = openapi_client.KernelspecsApi(api_client)

    try:
        # Get kernel specs
        api_response = api_instance.api_kernelspecs_get()
        print("The response of KernelspecsApi->api_kernelspecs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KernelspecsApi->api_kernelspecs_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiKernelspecsGet200Response**](ApiKernelspecsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kernel specs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

