# ApiErrorMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from ionoscloud_container_registry.models.api_error_message import ApiErrorMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ApiErrorMessage from a JSON string
api_error_message_instance = ApiErrorMessage.from_json(json)
# print the JSON string representation of the object
print(ApiErrorMessage.to_json())

# convert the object into a dict
api_error_message_dict = api_error_message_instance.to_dict()
# create an instance of ApiErrorMessage from a dict
api_error_message_from_dict = ApiErrorMessage.from_dict(api_error_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


