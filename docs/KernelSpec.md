# KernelSpec

Kernel spec (contents of kernel.json)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name for kernel | [optional] 
**kernel_spec_file** | [**KernelSpecFile**](KernelSpecFile.md) |  | [optional] 
**resources** | [**KernelSpecResources**](KernelSpecResources.md) |  | [optional] 

## Example

```python
from nbserv_client.models.kernel_spec import KernelSpec

# TODO update the JSON string below
json = "{}"
# create an instance of KernelSpec from a JSON string
kernel_spec_instance = KernelSpec.from_json(json)
# print the JSON string representation of the object
print KernelSpec.to_json()

# convert the object into a dict
kernel_spec_dict = kernel_spec_instance.to_dict()
# create an instance of KernelSpec from a dict
kernel_spec_form_dict = kernel_spec.from_dict(kernel_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


