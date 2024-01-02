# Kernel

Kernel information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | uuid of kernel | 
**name** | **str** | kernel spec name | 
**last_activity** | **str** | ISO 8601 timestamp for the last-seen activity on this kernel. Use this in combination with execution_state &#x3D;&#x3D; &#39;idle&#39; to identify which kernels have been idle since a given time. Timestamps will be UTC, indicated &#39;Z&#39; suffix. Added in notebook server 5.0.  | [optional] 
**connections** | **float** | The number of active connections to this kernel.  | [optional] 
**execution_state** | **str** | Current execution state of the kernel (typically &#39;idle&#39; or &#39;busy&#39;, but may be other values, such as &#39;starting&#39;). Added in notebook server 5.0.  | [optional] 

## Example

```python
from openapi_client.models.kernel import Kernel

# TODO update the JSON string below
json = "{}"
# create an instance of Kernel from a JSON string
kernel_instance = Kernel.from_json(json)
# print the JSON string representation of the object
print Kernel.to_json()

# convert the object into a dict
kernel_dict = kernel_instance.to_dict()
# create an instance of Kernel from a dict
kernel_form_dict = kernel.from_dict(kernel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


