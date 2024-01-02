# APIStatus

Notebook server API status. Added in notebook 5.0. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started** | **str** | ISO8601 timestamp indicating when the notebook server started.  | [optional] 
**last_activity** | **str** | ISO8601 timestamp indicating the last activity on the server, either on the REST API or kernel activity.  | [optional] 
**connections** | **float** | The total number of currently open connections to kernels.  | [optional] 
**kernels** | **float** | The total number of running kernels.  | [optional] 

## Example

```python
from openapi_client.models.api_status import APIStatus

# TODO update the JSON string below
json = "{}"
# create an instance of APIStatus from a JSON string
api_status_instance = APIStatus.from_json(json)
# print the JSON string representation of the object
print APIStatus.to_json()

# convert the object into a dict
api_status_dict = api_status_instance.to_dict()
# create an instance of APIStatus from a dict
api_status_form_dict = api_status.from_dict(api_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


