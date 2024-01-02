# KernelSpecFileHelpLinksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | menu item link text | 
**url** | **str** | menu item link url | 

## Example

```python
from nbserv_client.models.kernel_spec_file_help_links_inner import KernelSpecFileHelpLinksInner

# TODO update the JSON string below
json = "{}"
# create an instance of KernelSpecFileHelpLinksInner from a JSON string
kernel_spec_file_help_links_inner_instance = KernelSpecFileHelpLinksInner.from_json(json)
# print the JSON string representation of the object
print KernelSpecFileHelpLinksInner.to_json()

# convert the object into a dict
kernel_spec_file_help_links_inner_dict = kernel_spec_file_help_links_inner_instance.to_dict()
# create an instance of KernelSpecFileHelpLinksInner from a dict
kernel_spec_file_help_links_inner_form_dict = kernel_spec_file_help_links_inner.from_dict(kernel_spec_file_help_links_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


