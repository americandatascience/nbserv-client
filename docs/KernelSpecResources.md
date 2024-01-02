# KernelSpecResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kernel_js** | **str** | path for kernel.js file | [optional] 
**kernel_css** | **str** | path for kernel.css file | [optional] 
**logo_** | **str** | path for logo file.  Logo filenames are of the form &#x60;logo-widthxheight&#x60; | [optional] 

## Example

```python
from openapi_client.models.kernel_spec_resources import KernelSpecResources

# TODO update the JSON string below
json = "{}"
# create an instance of KernelSpecResources from a JSON string
kernel_spec_resources_instance = KernelSpecResources.from_json(json)
# print the JSON string representation of the object
print KernelSpecResources.to_json()

# convert the object into a dict
kernel_spec_resources_dict = kernel_spec_resources_instance.to_dict()
# create an instance of KernelSpecResources from a dict
kernel_spec_resources_form_dict = kernel_spec_resources.from_dict(kernel_spec_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


