# ApiContentsPathPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copy_from** | **str** |  | [optional] 
**ext** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from nbserv_client.models.api_contents_path_post_request import ApiContentsPathPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiContentsPathPostRequest from a JSON string
api_contents_path_post_request_instance = ApiContentsPathPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiContentsPathPostRequest.to_json()

# convert the object into a dict
api_contents_path_post_request_dict = api_contents_path_post_request_instance.to_dict()
# create an instance of ApiContentsPathPostRequest from a dict
api_contents_path_post_request_form_dict = api_contents_path_post_request.from_dict(api_contents_path_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


