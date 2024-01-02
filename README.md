# Jupyter NB Server Python Client

An SDK and API-wrapper for the jupyter notebook REST API.

- API version: 5
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://jupyter.org](https://jupyter.org)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import nbserv_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import nbserv_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
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
    except ApiException as e:
        print("Exception when calling ApiSpecApi->api_spec_yaml_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiSpecApi* | [**api_spec_yaml_get**](docs/ApiSpecApi.md#api_spec_yaml_get) | **GET** /api/spec.yaml | Get the current spec for the notebook server&#39;s APIs.
*ConfigApi* | [**api_config_section_name_get**](docs/ConfigApi.md#api_config_section_name_get) | **GET** /api/config/{section_name} | Get a configuration section by name
*ConfigApi* | [**api_config_section_name_patch**](docs/ConfigApi.md#api_config_section_name_patch) | **PATCH** /api/config/{section_name} | Update a configuration section by name
*ContentsApi* | [**api_contents_path_checkpoints_checkpoint_id_delete**](docs/ContentsApi.md#api_contents_path_checkpoints_checkpoint_id_delete) | **DELETE** /api/contents/{path}/checkpoints/{checkpoint_id} | Delete a checkpoint
*ContentsApi* | [**api_contents_path_checkpoints_checkpoint_id_post**](docs/ContentsApi.md#api_contents_path_checkpoints_checkpoint_id_post) | **POST** /api/contents/{path}/checkpoints/{checkpoint_id} | Restore a file to a particular checkpointed state
*ContentsApi* | [**api_contents_path_checkpoints_get**](docs/ContentsApi.md#api_contents_path_checkpoints_get) | **GET** /api/contents/{path}/checkpoints | Get a list of checkpoints for a file
*ContentsApi* | [**api_contents_path_checkpoints_post**](docs/ContentsApi.md#api_contents_path_checkpoints_post) | **POST** /api/contents/{path}/checkpoints | Create a new checkpoint for a file
*ContentsApi* | [**api_contents_path_delete**](docs/ContentsApi.md#api_contents_path_delete) | **DELETE** /api/contents/{path} | Delete a file in the given path
*ContentsApi* | [**api_contents_path_get**](docs/ContentsApi.md#api_contents_path_get) | **GET** /api/contents/{path} | Get contents of file or directory
*ContentsApi* | [**api_contents_path_patch**](docs/ContentsApi.md#api_contents_path_patch) | **PATCH** /api/contents/{path} | Rename a file or directory without re-uploading content
*ContentsApi* | [**api_contents_path_post**](docs/ContentsApi.md#api_contents_path_post) | **POST** /api/contents/{path} | Create a new file in the specified path
*ContentsApi* | [**api_contents_path_put**](docs/ContentsApi.md#api_contents_path_put) | **PUT** /api/contents/{path} | Save or upload file.
*DefaultApi* | [**api_get**](docs/DefaultApi.md#api_get) | **GET** /api/ | Get the Jupyter Server version
*IdentityApi* | [**api_me_get**](docs/IdentityApi.md#api_me_get) | **GET** /api/me | Get the identity of the currently authenticated user. If present, a &#x60;permissions&#x60; argument may be specified to check what actions the user currently is authorized to take. 
*KernelsApi* | [**api_kernels_get**](docs/KernelsApi.md#api_kernels_get) | **GET** /api/kernels | List the JSON data for all kernels that are currently running
*KernelsApi* | [**api_kernels_kernel_id_delete**](docs/KernelsApi.md#api_kernels_kernel_id_delete) | **DELETE** /api/kernels/{kernel_id} | Kill a kernel and delete the kernel id
*KernelsApi* | [**api_kernels_kernel_id_get**](docs/KernelsApi.md#api_kernels_kernel_id_get) | **GET** /api/kernels/{kernel_id} | Get kernel information
*KernelsApi* | [**api_kernels_kernel_id_interrupt_post**](docs/KernelsApi.md#api_kernels_kernel_id_interrupt_post) | **POST** /api/kernels/{kernel_id}/interrupt | Interrupt a kernel
*KernelsApi* | [**api_kernels_kernel_id_restart_post**](docs/KernelsApi.md#api_kernels_kernel_id_restart_post) | **POST** /api/kernels/{kernel_id}/restart | Restart a kernel
*KernelsApi* | [**api_kernels_post**](docs/KernelsApi.md#api_kernels_post) | **POST** /api/kernels | Start a kernel and return the uuid
*KernelspecsApi* | [**api_kernelspecs_get**](docs/KernelspecsApi.md#api_kernelspecs_get) | **GET** /api/kernelspecs | Get kernel specs
*SessionsApi* | [**api_sessions_get**](docs/SessionsApi.md#api_sessions_get) | **GET** /api/sessions | List available sessions
*SessionsApi* | [**api_sessions_post**](docs/SessionsApi.md#api_sessions_post) | **POST** /api/sessions | Create a new session, or return an existing session if a session of the same name already exists
*SessionsApi* | [**api_sessions_session_delete**](docs/SessionsApi.md#api_sessions_session_delete) | **DELETE** /api/sessions/{session} | Delete a session
*SessionsApi* | [**api_sessions_session_get**](docs/SessionsApi.md#api_sessions_session_get) | **GET** /api/sessions/{session} | Get session
*SessionsApi* | [**api_sessions_session_patch**](docs/SessionsApi.md#api_sessions_session_patch) | **PATCH** /api/sessions/{session} | This can be used to rename the session.
*StatusApi* | [**api_status_get**](docs/StatusApi.md#api_status_get) | **GET** /api/status | Get the current status/activity of the server.
*TerminalsApi* | [**api_terminals_get**](docs/TerminalsApi.md#api_terminals_get) | **GET** /api/terminals | Get available terminals
*TerminalsApi* | [**api_terminals_post**](docs/TerminalsApi.md#api_terminals_post) | **POST** /api/terminals | Create a new terminal
*TerminalsApi* | [**api_terminals_terminal_id_delete**](docs/TerminalsApi.md#api_terminals_terminal_id_delete) | **DELETE** /api/terminals/{terminal_id} | Delete a terminal session corresponding to an id.
*TerminalsApi* | [**api_terminals_terminal_id_get**](docs/TerminalsApi.md#api_terminals_terminal_id_get) | **GET** /api/terminals/{terminal_id} | Get a terminal session corresponding to an id.


## Documentation For Models

 - [APIStatus](docs/APIStatus.md)
 - [ApiContentsPathGet400Response](docs/ApiContentsPathGet400Response.md)
 - [ApiContentsPathPostRequest](docs/ApiContentsPathPostRequest.md)
 - [ApiContentsPathPutRequest](docs/ApiContentsPathPutRequest.md)
 - [ApiGet200Response](docs/ApiGet200Response.md)
 - [ApiKernelsPostRequest](docs/ApiKernelsPostRequest.md)
 - [ApiKernelspecsGet200Response](docs/ApiKernelspecsGet200Response.md)
 - [ApiMeGet200Response](docs/ApiMeGet200Response.md)
 - [ApiSessionsPost501Response](docs/ApiSessionsPost501Response.md)
 - [Checkpoints](docs/Checkpoints.md)
 - [Contents](docs/Contents.md)
 - [Identity](docs/Identity.md)
 - [Kernel](docs/Kernel.md)
 - [KernelSpec](docs/KernelSpec.md)
 - [KernelSpecFile](docs/KernelSpecFile.md)
 - [KernelSpecFileHelpLinksInner](docs/KernelSpecFileHelpLinksInner.md)
 - [KernelSpecResources](docs/KernelSpecResources.md)
 - [Session](docs/Session.md)
 - [Terminal](docs/Terminal.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




