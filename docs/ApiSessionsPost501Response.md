# ApiSessionsPost501Response

error message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**short_message** | **str** |  | [optional] 

## Example

```python
from nbserv_client.models.api_sessions_post501_response import ApiSessionsPost501Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSessionsPost501Response from a JSON string
api_sessions_post501_response_instance = ApiSessionsPost501Response.from_json(json)
# print the JSON string representation of the object
print ApiSessionsPost501Response.to_json()

# convert the object into a dict
api_sessions_post501_response_dict = api_sessions_post501_response_instance.to_dict()
# create an instance of ApiSessionsPost501Response from a dict
api_sessions_post501_response_form_dict = api_sessions_post501_response.from_dict(api_sessions_post501_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


