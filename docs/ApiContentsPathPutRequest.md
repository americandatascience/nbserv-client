# ApiContentsPathPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new filename if changed | [optional] 
**path** | **str** | New path for file or directory | [optional] 
**type** | **str** | Path dtype (&#39;notebook&#39;, &#39;file&#39;, &#39;directory&#39;) | [optional] 
**format** | **str** | File format (&#39;json&#39;, &#39;text&#39;, &#39;base64&#39;) | [optional] 
**content** | **str** | The actual body of the document excluding directory type | [optional] 

## Example

```python
from openapi_client.models.api_contents_path_put_request import ApiContentsPathPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiContentsPathPutRequest from a JSON string
api_contents_path_put_request_instance = ApiContentsPathPutRequest.from_json(json)
# print the JSON string representation of the object
print ApiContentsPathPutRequest.to_json()

# convert the object into a dict
api_contents_path_put_request_dict = api_contents_path_put_request_instance.to_dict()
# create an instance of ApiContentsPathPutRequest from a dict
api_contents_path_put_request_form_dict = api_contents_path_put_request.from_dict(api_contents_path_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


