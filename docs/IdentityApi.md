# openapi_client.IdentityApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_me_get**](IdentityApi.md#api_me_get) | **GET** /api/me | Get the identity of the currently authenticated user. If present, a &#x60;permissions&#x60; argument may be specified to check what actions the user currently is authorized to take. 


# **api_me_get**
> ApiMeGet200Response api_me_get(permissions=permissions)

Get the identity of the currently authenticated user. If present, a `permissions` argument may be specified to check what actions the user currently is authorized to take. 

### Example


```python
import time
import os
import openapi_client
from openapi_client.models.api_me_get200_response import ApiMeGet200Response
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
    api_instance = openapi_client.IdentityApi(api_client)
    permissions = 'permissions_example' # str | JSON-serialized dictionary of `{\"resource\": [\"action\",]}` (dict of lists of strings) to check. The same dictionary structure will be returned, containing only the actions for which the user is authorized.  (optional)

    try:
        # Get the identity of the currently authenticated user. If present, a `permissions` argument may be specified to check what actions the user currently is authorized to take. 
        api_response = api_instance.api_me_get(permissions=permissions)
        print("The response of IdentityApi->api_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->api_me_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permissions** | **str**| JSON-serialized dictionary of &#x60;{\&quot;resource\&quot;: [\&quot;action\&quot;,]}&#x60; (dict of lists of strings) to check. The same dictionary structure will be returned, containing only the actions for which the user is authorized.  | [optional] 

### Return type

[**ApiMeGet200Response**](ApiMeGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user&#39;s identity and permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

