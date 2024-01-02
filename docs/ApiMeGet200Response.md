# ApiMeGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | [**Identity**](Identity.md) |  | [optional] 
**permissions** | **Dict[str, List[str]]** | A dict of the form: &#x60;{\&quot;resource\&quot;: [\&quot;action\&quot;,]}&#x60; containing only the AUTHORIZED subset of resource+actions from the permissions specified in the request. If no permission checks were made in the request, this will be empty.  | [optional] 

## Example

```python
from openapi_client.models.api_me_get200_response import ApiMeGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMeGet200Response from a JSON string
api_me_get200_response_instance = ApiMeGet200Response.from_json(json)
# print the JSON string representation of the object
print ApiMeGet200Response.to_json()

# convert the object into a dict
api_me_get200_response_dict = api_me_get200_response_instance.to_dict()
# create an instance of ApiMeGet200Response from a dict
api_me_get200_response_form_dict = api_me_get200_response.from_dict(api_me_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


