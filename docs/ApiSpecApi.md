# nbserv_client.ApiSpecApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_spec_yaml_get**](ApiSpecApi.md#api_spec_yaml_get) | **GET** /api/spec.yaml | Get the current spec for the notebook server&#39;s APIs.


# **api_spec_yaml_get**
> bytearray api_spec_yaml_get()

Get the current spec for the notebook server's APIs.

### Example


```python
import time
import os
import nbserv_client
from nbserv_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = nbserv_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with nbserv_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nbserv_client.ApiSpecApi(api_client)

    try:
        # Get the current spec for the notebook server's APIs.
        api_response = api_instance.api_spec_yaml_get()
        print("The response of ApiSpecApi->api_spec_yaml_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiSpecApi->api_spec_yaml_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/x-yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current spec for the notebook server&#39;s APIs. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

