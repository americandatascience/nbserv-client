# Checkpoints

A checkpoint object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id for the checkpoint. | 
**last_modified** | **str** | Last modified timestamp | 

## Example

```python
from openapi_client.models.checkpoints import Checkpoints

# TODO update the JSON string below
json = "{}"
# create an instance of Checkpoints from a JSON string
checkpoints_instance = Checkpoints.from_json(json)
# print the JSON string representation of the object
print Checkpoints.to_json()

# convert the object into a dict
checkpoints_dict = checkpoints_instance.to_dict()
# create an instance of Checkpoints from a dict
checkpoints_form_dict = checkpoints.from_dict(checkpoints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


