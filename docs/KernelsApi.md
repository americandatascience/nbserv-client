# nbserv_client.KernelsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_kernels_get**](KernelsApi.md#api_kernels_get) | **GET** /api/kernels | List the JSON data for all kernels that are currently running
[**api_kernels_kernel_id_delete**](KernelsApi.md#api_kernels_kernel_id_delete) | **DELETE** /api/kernels/{kernel_id} | Kill a kernel and delete the kernel id
[**api_kernels_kernel_id_get**](KernelsApi.md#api_kernels_kernel_id_get) | **GET** /api/kernels/{kernel_id} | Get kernel information
[**api_kernels_kernel_id_interrupt_post**](KernelsApi.md#api_kernels_kernel_id_interrupt_post) | **POST** /api/kernels/{kernel_id}/interrupt | Interrupt a kernel
[**api_kernels_kernel_id_restart_post**](KernelsApi.md#api_kernels_kernel_id_restart_post) | **POST** /api/kernels/{kernel_id}/restart | Restart a kernel
[**api_kernels_post**](KernelsApi.md#api_kernels_post) | **POST** /api/kernels | Start a kernel and return the uuid


# **api_kernels_get**
> List[Kernel] api_kernels_get()

List the JSON data for all kernels that are currently running

### Example


```python
import time
import os
import nbserv_client
from nbserv_client.models.kernel import Kernel
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
    api_instance = nbserv_client.KernelsApi(api_client)

    try:
        # List the JSON data for all kernels that are currently running
        api_response = api_instance.api_kernels_get()
        print("The response of KernelsApi->api_kernels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KernelsApi->api_kernels_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Kernel]**](Kernel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of currently-running kernel uuids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_kernels_kernel_id_delete**
> api_kernels_kernel_id_delete(kernel_id)

Kill a kernel and delete the kernel id

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
    api_instance = nbserv_client.KernelsApi(api_client)
    kernel_id = 'kernel_id_example' # str | kernel uuid

    try:
        # Kill a kernel and delete the kernel id
        api_instance.api_kernels_kernel_id_delete(kernel_id)
    except Exception as e:
        print("Exception when calling KernelsApi->api_kernels_kernel_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kernel_id** | **str**| kernel uuid | 

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
**204** | Kernel deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_kernels_kernel_id_get**
> Kernel api_kernels_kernel_id_get(kernel_id)

Get kernel information

### Example


```python
import time
import os
import nbserv_client
from nbserv_client.models.kernel import Kernel
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
    api_instance = nbserv_client.KernelsApi(api_client)
    kernel_id = 'kernel_id_example' # str | kernel uuid

    try:
        # Get kernel information
        api_response = api_instance.api_kernels_kernel_id_get(kernel_id)
        print("The response of KernelsApi->api_kernels_kernel_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KernelsApi->api_kernels_kernel_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kernel_id** | **str**| kernel uuid | 

### Return type

[**Kernel**](Kernel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kernel information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_kernels_kernel_id_interrupt_post**
> api_kernels_kernel_id_interrupt_post(kernel_id)

Interrupt a kernel

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
    api_instance = nbserv_client.KernelsApi(api_client)
    kernel_id = 'kernel_id_example' # str | kernel uuid

    try:
        # Interrupt a kernel
        api_instance.api_kernels_kernel_id_interrupt_post(kernel_id)
    except Exception as e:
        print("Exception when calling KernelsApi->api_kernels_kernel_id_interrupt_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kernel_id** | **str**| kernel uuid | 

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
**204** | Kernel interrupted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_kernels_kernel_id_restart_post**
> Kernel api_kernels_kernel_id_restart_post(kernel_id)

Restart a kernel

### Example


```python
import time
import os
import nbserv_client
from nbserv_client.models.kernel import Kernel
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
    api_instance = nbserv_client.KernelsApi(api_client)
    kernel_id = 'kernel_id_example' # str | kernel uuid

    try:
        # Restart a kernel
        api_response = api_instance.api_kernels_kernel_id_restart_post(kernel_id)
        print("The response of KernelsApi->api_kernels_kernel_id_restart_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KernelsApi->api_kernels_kernel_id_restart_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kernel_id** | **str**| kernel uuid | 

### Return type

[**Kernel**](Kernel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kernel restarted |  * Location - URL for kernel commands <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_kernels_post**
> Kernel api_kernels_post(options=options)

Start a kernel and return the uuid

### Example


```python
import time
import os
import nbserv_client
from nbserv_client.models.api_kernels_post_request import ApiKernelsPostRequest
from nbserv_client.models.kernel import Kernel
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
    api_instance = nbserv_client.KernelsApi(api_client)
    options = nbserv_client.ApiKernelsPostRequest() # ApiKernelsPostRequest |  (optional)

    try:
        # Start a kernel and return the uuid
        api_response = api_instance.api_kernels_post(options=options)
        print("The response of KernelsApi->api_kernels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KernelsApi->api_kernels_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | [**ApiKernelsPostRequest**](ApiKernelsPostRequest.md)|  | [optional] 

### Return type

[**Kernel**](Kernel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Kernel started |  * Location - URL for kernel commands <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

