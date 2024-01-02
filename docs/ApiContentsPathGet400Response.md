# ApiContentsPathGet400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error condition | [optional] 
**reason** | **str** | Explanation of error reason | [optional] 

## Example

```python
from openapi_client.models.api_contents_path_get400_response import ApiContentsPathGet400Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiContentsPathGet400Response from a JSON string
api_contents_path_get400_response_instance = ApiContentsPathGet400Response.from_json(json)
# print the JSON string representation of the object
print ApiContentsPathGet400Response.to_json()

# convert the object into a dict
api_contents_path_get400_response_dict = api_contents_path_get400_response_instance.to_dict()
# create an instance of ApiContentsPathGet400Response from a dict
api_contents_path_get400_response_form_dict = api_contents_path_get400_response.from_dict(api_contents_path_get400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


