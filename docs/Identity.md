# Identity

The identity of the currently authenticated user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Unique string identifying the user  | [optional] 
**name** | **str** | For-humans name of the user. May be the same as &#x60;username&#x60; in systems where only usernames are available.  | [optional] 
**display_name** | **str** | Alternate rendering of name for display. Often the same as &#x60;name&#x60;.  | [optional] 
**initials** | **str** | Short string of initials. Initials should not be derived automatically due to localization issues. May be &#x60;null&#x60; if unavailable.  | [optional] 
**avatar_url** | **str** | URL of an avatar to be used for the user. May be &#x60;null&#x60; if unavailable.  | [optional] 
**color** | **str** | A CSS color string to use as a preferred color, such as for collaboration cursors. May be &#x60;null&#x60; if unavailable.  | [optional] 

## Example

```python
from openapi_client.models.identity import Identity

# TODO update the JSON string below
json = "{}"
# create an instance of Identity from a JSON string
identity_instance = Identity.from_json(json)
# print the JSON string representation of the object
print Identity.to_json()

# convert the object into a dict
identity_dict = identity_instance.to_dict()
# create an instance of Identity from a dict
identity_form_dict = identity.from_dict(identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


