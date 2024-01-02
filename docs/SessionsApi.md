# nbserv_client.SessionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_sessions_get**](SessionsApi.md#api_sessions_get) | **GET** /api/sessions | List available sessions
[**api_sessions_post**](SessionsApi.md#api_sessions_post) | **POST** /api/sessions | Create a new session, or return an existing session if a session of the same name already exists
[**api_sessions_session_delete**](SessionsApi.md#api_sessions_session_delete) | **DELETE** /api/sessions/{session} | Delete a session
[**api_sessions_session_get**](SessionsApi.md#api_sessions_session_get) | **GET** /api/sessions/{session} | Get session
[**api_sessions_session_patch**](SessionsApi.md#api_sessions_session_patch) | **PATCH** /api/sessions/{session} | This can be used to rename the session.


# **api_sessions_get**
> List[Session] api_sessions_get()

List available sessions

### Example


```python
import time
import os
import nbserv_client
from nbserv_client.models.session import Session
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
    api_instance = nbserv_client.SessionsApi(api_client)

    try:
        # List available sessions
        api_response = api_instance.api_sessions_get()
        print("The response of SessionsApi->api_sessions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->api_sessions_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Session]**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of current sessions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sessions_post**
> Session api_sessions_post(session=session)

Create a new session, or return an existing session if a session of the same name already exists

### Example


```python
import time
import os
import nbserv_client
from nbserv_client.models.session import Session
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
    api_instance = nbserv_client.SessionsApi(api_client)
    session = nbserv_client.Session() # Session |  (optional)

    try:
        # Create a new session, or return an existing session if a session of the same name already exists
        api_response = api_instance.api_sessions_post(session=session)
        print("The response of SessionsApi->api_sessions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->api_sessions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session** | [**Session**](Session.md)|  | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Session created or returned |  * Location - URL for kernel commands <br>  |
**501** | Session not available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sessions_session_delete**
> api_sessions_session_delete(session)

Delete a session

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
    api_instance = nbserv_client.SessionsApi(api_client)
    session = 'session_example' # str | session uuid

    try:
        # Delete a session
        api_instance.api_sessions_session_delete(session)
    except Exception as e:
        print("Exception when calling SessionsApi->api_sessions_session_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session** | **str**| session uuid | 

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
**204** | Session (and kernel) were deleted |  -  |
**410** | Kernel was deleted before the session, and the session was *not* deleted (TODO - check to make sure session wasn&#39;t deleted) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sessions_session_get**
> Session api_sessions_session_get(session)

Get session

### Example


```python
import time
import os
import nbserv_client
from nbserv_client.models.session import Session
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
    api_instance = nbserv_client.SessionsApi(api_client)
    session = 'session_example' # str | session uuid

    try:
        # Get session
        api_response = api_instance.api_sessions_session_get(session)
        print("The response of SessionsApi->api_sessions_session_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->api_sessions_session_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session** | **str**| session uuid | 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Session |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_sessions_session_patch**
> Session api_sessions_session_patch(session, model)

This can be used to rename the session.

### Example


```python
import time
import os
import nbserv_client
from nbserv_client.models.session import Session
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
    api_instance = nbserv_client.SessionsApi(api_client)
    session = 'session_example' # str | session uuid
    model = nbserv_client.Session() # Session | 

    try:
        # This can be used to rename the session.
        api_response = api_instance.api_sessions_session_patch(session, model)
        print("The response of SessionsApi->api_sessions_session_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionsApi->api_sessions_session_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session** | **str**| session uuid | 
 **model** | [**Session**](Session.md)|  | 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Session |  -  |
**400** | No data provided |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

