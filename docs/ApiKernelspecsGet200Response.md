# ApiKernelspecsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Default kernel name | [optional] 
**kernelspecs** | [**Dict[str, KernelSpec]**](KernelSpec.md) |  | [optional] 

## Example

```python
from nbserv_client.models.api_kernelspecs_get200_response import ApiKernelspecsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKernelspecsGet200Response from a JSON string
api_kernelspecs_get200_response_instance = ApiKernelspecsGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiKernelspecsGet200Response.to_json()

# convert the object into a dict
api_kernelspecs_get200_response_dict = api_kernelspecs_get200_response_instance.to_dict()
# create an instance of ApiKernelspecsGet200Response from a dict
api_kernelspecs_get200_response_form_dict = api_kernelspecs_get200_response.from_dict(api_kernelspecs_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


