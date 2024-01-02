# nbserv_client.ContentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_contents_path_checkpoints_checkpoint_id_delete**](ContentsApi.md#api_contents_path_checkpoints_checkpoint_id_delete) | **DELETE** /api/contents/{path}/checkpoints/{checkpoint_id} | Delete a checkpoint
[**api_contents_path_checkpoints_checkpoint_id_post**](ContentsApi.md#api_contents_path_checkpoints_checkpoint_id_post) | **POST** /api/contents/{path}/checkpoints/{checkpoint_id} | Restore a file to a particular checkpointed state
[**api_contents_path_checkpoints_get**](ContentsApi.md#api_contents_path_checkpoints_get) | **GET** /api/contents/{path}/checkpoints | Get a list of checkpoints for a file
[**api_contents_path_checkpoints_post**](ContentsApi.md#api_contents_path_checkpoints_post) | **POST** /api/contents/{path}/checkpoints | Create a new checkpoint for a file
[**api_contents_path_delete**](ContentsApi.md#api_contents_path_delete) | **DELETE** /api/contents/{path} | Delete a file in the given path
[**api_contents_path_get**](ContentsApi.md#api_contents_path_get) | **GET** /api/contents/{path} | Get contents of file or directory
[**api_contents_path_patch**](ContentsApi.md#api_contents_path_patch) | **PATCH** /api/contents/{path} | Rename a file or directory without re-uploading content
[**api_contents_path_post**](ContentsApi.md#api_contents_path_post) | **POST** /api/contents/{path} | Create a new file in the specified path
[**api_contents_path_put**](ContentsApi.md#api_contents_path_put) | **PUT** /api/contents/{path} | Save or upload file.


# **api_contents_path_checkpoints_checkpoint_id_delete**
> api_contents_path_checkpoints_checkpoint_id_delete(path, checkpoint_id)

Delete a checkpoint

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
    api_instance = nbserv_client.ContentsApi(api_client)
    path = 'path_example' # str | file path
    checkpoint_id = 'checkpoint_id_example' # str | Checkpoint id for a file

    try:
        # Delete a checkpoint
        api_instance.api_contents_path_checkpoints_checkpoint_id_delete(path, checkpoint_id)
    except Exception as e:
        print("Exception when calling ContentsApi->api_contents_path_checkpoints_checkpoint_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| file path | 
 **checkpoint_id** | **str**| Checkpoint id for a file | 

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
**204** | Checkpoint deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_contents_path_checkpoints_checkpoint_id_post**
> api_contents_path_checkpoints_checkpoint_id_post(path, checkpoint_id)

Restore a file to a particular checkpointed state

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
    api_instance = nbserv_client.ContentsApi(api_client)
    path = 'path_example' # str | file path
    checkpoint_id = 'checkpoint_id_example' # str | Checkpoint id for a file

    try:
        # Restore a file to a particular checkpointed state
        api_instance.api_contents_path_checkpoints_checkpoint_id_post(path, checkpoint_id)
    except Exception as e:
        print("Exception when calling ContentsApi->api_contents_path_checkpoints_checkpoint_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| file path | 
 **checkpoint_id** | **str**| Checkpoint id for a file | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Checkpoint restored |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_contents_path_checkpoints_get**
> List[Checkpoints] api_contents_path_checkpoints_get(path)

Get a list of checkpoints for a file

List checkpoints for a given file. There will typically be zero or one results.

### Example


```python
import time
import os
import nbserv_client
from nbserv_client.models.checkpoints import Checkpoints
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
    api_instance = nbserv_client.ContentsApi(api_client)
    path = 'path_example' # str | file path

    try:
        # Get a list of checkpoints for a file
        api_response = api_instance.api_contents_path_checkpoints_get(path)
        print("The response of ContentsApi->api_contents_path_checkpoints_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentsApi->api_contents_path_checkpoints_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| file path | 

### Return type

[**List[Checkpoints]**](Checkpoints.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | No item found |  -  |
**400** | Bad request |  -  |
**200** | List of checkpoints for a file |  -  |
**500** | Model key error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_contents_path_checkpoints_post**
> Checkpoints api_contents_path_checkpoints_post(path)

Create a new checkpoint for a file

Create a new checkpoint with the current state of a file. With the default FileContentsManager, only one checkpoint is supported, so creating new checkpoints clobbers existing ones.

### Example


```python
import time
import os
import nbserv_client
from nbserv_client.models.checkpoints import Checkpoints
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
    api_instance = nbserv_client.ContentsApi(api_client)
    path = 'path_example' # str | file path

    try:
        # Create a new checkpoint for a file
        api_response = api_instance.api_contents_path_checkpoints_post(path)
        print("The response of ContentsApi->api_contents_path_checkpoints_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentsApi->api_contents_path_checkpoints_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| file path | 

### Return type

[**Checkpoints**](Checkpoints.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Checkpoint created |  * Location - URL for kernel commands <br>  |
**404** | No item found |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_contents_path_delete**
> api_contents_path_delete(path)

Delete a file in the given path

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
    api_instance = nbserv_client.ContentsApi(api_client)
    path = 'path_example' # str | file path

    try:
        # Delete a file in the given path
        api_instance.api_contents_path_delete(path)
    except Exception as e:
        print("Exception when calling ContentsApi->api_contents_path_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| file path | 

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
**204** | File deleted |  * Location - URL for kernel commands <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_contents_path_get**
> Contents api_contents_path_get(path, type=type, format=format, content=content, hash=hash)

Get contents of file or directory

A client can optionally specify a type and/or format argument via URL parameter. When given, the Contents service shall return a model in the requested type and/or format. If the request cannot be satisfied, e.g. type=text is requested, but the file is binary, then the request shall fail with 400 and have a JSON response containing a 'reason' field, with the value 'bad format' or 'bad type', depending on what was requested.

### Example


```python
import time
import os
import nbserv_client
from nbserv_client.models.contents import Contents
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
    api_instance = nbserv_client.ContentsApi(api_client)
    path = 'path_example' # str | file path
    type = 'type_example' # str | File type ('file', 'directory') (optional)
    format = 'format_example' # str | How file content should be returned ('text', 'base64') (optional)
    content = 56 # int | Return content (0 for no content, 1 for return content) (optional)
    hash = 56 # int | May return hash hexdigest string of content and the hash algorithm (0 for no hash - default, 1 for return hash). It may be ignored by the content manager. (optional)

    try:
        # Get contents of file or directory
        api_response = api_instance.api_contents_path_get(path, type=type, format=format, content=content, hash=hash)
        print("The response of ContentsApi->api_contents_path_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentsApi->api_contents_path_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| file path | 
 **type** | **str**| File type (&#39;file&#39;, &#39;directory&#39;) | [optional] 
 **format** | **str**| How file content should be returned (&#39;text&#39;, &#39;base64&#39;) | [optional] 
 **content** | **int**| Return content (0 for no content, 1 for return content) | [optional] 
 **hash** | **int**| May return hash hexdigest string of content and the hash algorithm (0 for no hash - default, 1 for return hash). It may be ignored by the content manager. | [optional] 

### Return type

[**Contents**](Contents.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | No item found |  -  |
**400** | Bad request |  -  |
**200** | Contents of file or directory |  * Last-Modified - Last modified date for file <br>  |
**500** | Model key error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_contents_path_patch**
> Contents api_contents_path_patch(path)

Rename a file or directory without re-uploading content

### Example


```python
import time
import os
import nbserv_client
from nbserv_client.models.contents import Contents
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
    api_instance = nbserv_client.ContentsApi(api_client)
    path = 'path_example' # str | file path

    try:
        # Rename a file or directory without re-uploading content
        api_response = api_instance.api_contents_path_patch(path)
        print("The response of ContentsApi->api_contents_path_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentsApi->api_contents_path_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| file path | 

### Return type

[**Contents**](Contents.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Path updated |  * Location - URL for kernel commands <br>  |
**400** | No data provided |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_contents_path_post**
> Contents api_contents_path_post(path, model=model)

Create a new file in the specified path

A POST to /api/contents/path creates a New untitled, empty file or directory. A POST to /api/contents/path with body {'copy_from': '/path/to/OtherNotebook.ipynb'} creates a new copy of OtherNotebook in path.

### Example


```python
import time
import os
import nbserv_client
from nbserv_client.models.api_contents_path_post_request import ApiContentsPathPostRequest
from nbserv_client.models.contents import Contents
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
    api_instance = nbserv_client.ContentsApi(api_client)
    path = 'path_example' # str | file path
    model = nbserv_client.ApiContentsPathPostRequest() # ApiContentsPathPostRequest | Path of file to copy (optional)

    try:
        # Create a new file in the specified path
        api_response = api_instance.api_contents_path_post(path, model=model)
        print("The response of ContentsApi->api_contents_path_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentsApi->api_contents_path_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| file path | 
 **model** | [**ApiContentsPathPostRequest**](ApiContentsPathPostRequest.md)| Path of file to copy | [optional] 

### Return type

[**Contents**](Contents.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | File created |  * Location - URL for kernel commands <br>  |
**404** | No item found |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_contents_path_put**
> Contents api_contents_path_put(path, model=model)

Save or upload file.

Saves the file in the location specified by name and path.  PUT is very similar to POST, but the requester specifies the name, whereas with POST, the server picks the name.

### Example


```python
import time
import os
import nbserv_client
from nbserv_client.models.api_contents_path_put_request import ApiContentsPathPutRequest
from nbserv_client.models.contents import Contents
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
    api_instance = nbserv_client.ContentsApi(api_client)
    path = 'path_example' # str | file path
    model = nbserv_client.ApiContentsPathPutRequest() # ApiContentsPathPutRequest | New path for file or directory (optional)

    try:
        # Save or upload file.
        api_response = api_instance.api_contents_path_put(path, model=model)
        print("The response of ContentsApi->api_contents_path_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentsApi->api_contents_path_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| file path | 
 **model** | [**ApiContentsPathPutRequest**](ApiContentsPathPutRequest.md)| New path for file or directory | [optional] 

### Return type

[**Contents**](Contents.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File saved |  * Location - URL for kernel commands <br>  |
**201** | Path created |  * Location - URL for kernel commands <br>  |
**400** | No data provided |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

