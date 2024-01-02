# ApiKernelsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Kernel spec name (defaults to default kernel spec for server) | 
**path** | **str** | API path from root to the cwd of the kernel | [optional] 

## Example

```python
from nbserv_client.models.api_kernels_post_request import ApiKernelsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKernelsPostRequest from a JSON string
api_kernels_post_request_instance = ApiKernelsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiKernelsPostRequest.to_json()

# convert the object into a dict
api_kernels_post_request_dict = api_kernels_post_request_instance.to_dict()
# create an instance of ApiKernelsPostRequest from a dict
api_kernels_post_request_form_dict = api_kernels_post_request.from_dict(api_kernels_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


