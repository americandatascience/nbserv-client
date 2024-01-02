# Contents

A contents object.  The content and format keys may be null if content is not contained. The hash maybe null if hash is not required.  If type is 'file', then the mimetype will be null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of file or directory, equivalent to the last part of the path | 
**path** | **str** | Full path for file or directory | 
**type** | **str** | Type of content | 
**writable** | **bool** | indicates whether the requester has permission to edit the file | 
**created** | **str** | Creation timestamp | 
**last_modified** | **str** | Last modified timestamp | 
**size** | **int** | The size of the file or notebook in bytes. If no size is provided, defaults to null. | [optional] 
**mimetype** | **str** | The mimetype of a file.  If content is not null, and type is &#39;file&#39;, this will contain the mimetype of the file, otherwise this will be null. | 
**content** | **str** | The content, if requested (otherwise null).  Will be an array if type is &#39;directory&#39; | 
**format** | **str** | Format of content (one of null, &#39;text&#39;, &#39;base64&#39;, &#39;json&#39;) | 
**hash** | **str** | [optional] The hexdigest hash string of content, if requested (otherwise null). It cannot be null if hash_algorithm is defined. | [optional] 
**hash_algorithm** | **str** | [optional] The algorithm used to produce the hash, if requested (otherwise null). It cannot be null if hash is defined. | [optional] 

## Example

```python
from openapi_client.models.contents import Contents

# TODO update the JSON string below
json = "{}"
# create an instance of Contents from a JSON string
contents_instance = Contents.from_json(json)
# print the JSON string representation of the object
print Contents.to_json()

# convert the object into a dict
contents_dict = contents_instance.to_dict()
# create an instance of Contents from a dict
contents_form_dict = contents.from_dict(contents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


