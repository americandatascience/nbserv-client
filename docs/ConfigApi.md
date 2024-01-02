# nbserv_client.ConfigApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_config_section_name_get**](ConfigApi.md#api_config_section_name_get) | **GET** /api/config/{section_name} | Get a configuration section by name
[**api_config_section_name_patch**](ConfigApi.md#api_config_section_name_patch) | **PATCH** /api/config/{section_name} | Update a configuration section by name


# **api_config_section_name_get**
> object api_config_section_name_get(section_name)

Get a configuration section by name

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
    api_instance = nbserv_client.ConfigApi(api_client)
    section_name = 'section_name_example' # str | Name of config section

    try:
        # Get a configuration section by name
        api_response = api_instance.api_config_section_name_get(section_name)
        print("The response of ConfigApi->api_config_section_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->api_config_section_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_name** | **str**| Name of config section | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_config_section_name_patch**
> object api_config_section_name_patch(section_name, configuration=configuration)

Update a configuration section by name

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
    api_instance = nbserv_client.ConfigApi(api_client)
    section_name = 'section_name_example' # str | Name of config section
    configuration = None # object |  (optional)

    try:
        # Update a configuration section by name
        api_response = api_instance.api_config_section_name_patch(section_name, configuration=configuration)
        print("The response of ConfigApi->api_config_section_name_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConfigApi->api_config_section_name_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_name** | **str**| Name of config section | 
 **configuration** | **object**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Configuration object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

