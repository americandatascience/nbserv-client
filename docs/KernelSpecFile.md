# KernelSpecFile

Kernel spec json file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | The programming language which this kernel runs. This will be stored in notebook metadata. | 
**argv** | **List[str]** | A list of command line arguments used to start the kernel. The text &#x60;{connection_file}&#x60; in any argument will be replaced with the path to the connection file. | 
**display_name** | **str** | The kernel&#39;s name as it should be displayed in the UI. Unlike the kernel name used in the API, this can contain arbitrary unicode characters. | 
**codemirror_mode** | **str** | Codemirror mode.  Can be a string *or* an valid Codemirror mode object.  This defaults to the string from the &#x60;language&#x60; property. | [optional] 
**env** | **Dict[str, str]** | A dictionary of environment variables to set for the kernel. These will be added to the current environment variables. | [optional] 
**help_links** | [**List[KernelSpecFileHelpLinksInner]**](KernelSpecFileHelpLinksInner.md) | Help items to be displayed in the help menu in the notebook UI. | [optional] 

## Example

```python
from openapi_client.models.kernel_spec_file import KernelSpecFile

# TODO update the JSON string below
json = "{}"
# create an instance of KernelSpecFile from a JSON string
kernel_spec_file_instance = KernelSpecFile.from_json(json)
# print the JSON string representation of the object
print KernelSpecFile.to_json()

# convert the object into a dict
kernel_spec_file_dict = kernel_spec_file_instance.to_dict()
# create an instance of KernelSpecFile from a dict
kernel_spec_file_form_dict = kernel_spec_file.from_dict(kernel_spec_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


