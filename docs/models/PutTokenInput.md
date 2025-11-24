# PutTokenInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**PostTokenProperties**](PostTokenProperties.md) |  | 

## Example

```python
from ionoscloud_container_registry.models.put_token_input import PutTokenInput

# TODO update the JSON string below
json = "{}"
# create an instance of PutTokenInput from a JSON string
put_token_input_instance = PutTokenInput.from_json(json)
# print the JSON string representation of the object
print(PutTokenInput.to_json())

# convert the object into a dict
put_token_input_dict = put_token_input_instance.to_dict()
# create an instance of PutTokenInput from a dict
put_token_input_from_dict = PutTokenInput.from_dict(put_token_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


