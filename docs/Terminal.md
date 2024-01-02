# Terminal

A Terminal object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of terminal | 
**last_activity** | **str** | ISO 8601 timestamp for the last-seen activity on this terminal.  Use this to identify which terminals have been inactive since a given time. Timestamps will be UTC, indicated &#39;Z&#39; suffix.  | [optional] 

## Example

```python
from nbserv_client.models.terminal import Terminal

# TODO update the JSON string below
json = "{}"
# create an instance of Terminal from a JSON string
terminal_instance = Terminal.from_json(json)
# print the JSON string representation of the object
print Terminal.to_json()

# convert the object into a dict
terminal_dict = terminal_instance.to_dict()
# create an instance of Terminal from a dict
terminal_form_dict = terminal.from_dict(terminal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


