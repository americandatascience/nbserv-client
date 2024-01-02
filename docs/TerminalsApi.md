# openapi_client.TerminalsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_terminals_get**](TerminalsApi.md#api_terminals_get) | **GET** /api/terminals | Get available terminals
[**api_terminals_post**](TerminalsApi.md#api_terminals_post) | **POST** /api/terminals | Create a new terminal
[**api_terminals_terminal_id_delete**](TerminalsApi.md#api_terminals_terminal_id_delete) | **DELETE** /api/terminals/{terminal_id} | Delete a terminal session corresponding to an id.
[**api_terminals_terminal_id_get**](TerminalsApi.md#api_terminals_terminal_id_get) | **GET** /api/terminals/{terminal_id} | Get a terminal session corresponding to an id.


# **api_terminals_get**
> List[Terminal] api_terminals_get()

Get available terminals

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.terminal import Terminal
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
    api_instance = openapi_client.TerminalsApi(api_client)

    try:
        # Get available terminals
        api_response = api_instance.api_terminals_get()
        print("The response of TerminalsApi->api_terminals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalsApi->api_terminals_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Terminal]**](Terminal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of all available terminal ids. |  -  |
**403** | Forbidden to access |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_terminals_post**
> Terminal api_terminals_post()

Create a new terminal

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.terminal import Terminal
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
    api_instance = openapi_client.TerminalsApi(api_client)

    try:
        # Create a new terminal
        api_response = api_instance.api_terminals_post()
        print("The response of TerminalsApi->api_terminals_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalsApi->api_terminals_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Terminal**](Terminal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new terminal |  -  |
**403** | Forbidden to access |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_terminals_terminal_id_delete**
> api_terminals_terminal_id_delete(terminal_id)

Delete a terminal session corresponding to an id.

### Example


```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.TerminalsApi(api_client)
    terminal_id = 'terminal_id_example' # str | ID of terminal session

    try:
        # Delete a terminal session corresponding to an id.
        api_instance.api_terminals_terminal_id_delete(terminal_id)
    except Exception as e:
        print("Exception when calling TerminalsApi->api_terminals_terminal_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal_id** | **str**| ID of terminal session | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deleted terminal session |  -  |
**403** | Forbidden to access |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_terminals_terminal_id_get**
> Terminal api_terminals_terminal_id_get(terminal_id)

Get a terminal session corresponding to an id.

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.terminal import Terminal
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
    api_instance = openapi_client.TerminalsApi(api_client)
    terminal_id = 'terminal_id_example' # str | ID of terminal session

    try:
        # Get a terminal session corresponding to an id.
        api_response = api_instance.api_terminals_terminal_id_get(terminal_id)
        print("The response of TerminalsApi->api_terminals_terminal_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalsApi->api_terminals_terminal_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminal_id** | **str**| ID of terminal session | 

### Return type

[**Terminal**](Terminal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Terminal session with given id |  -  |
**403** | Forbidden to access |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

