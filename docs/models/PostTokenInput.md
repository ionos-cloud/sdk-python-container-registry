# PostTokenInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**PostTokenProperties**](PostTokenProperties.md) |  | 

## Example

```python
from ionoscloud_container_registry.models.post_token_input import PostTokenInput

# TODO update the JSON string below
json = "{}"
# create an instance of PostTokenInput from a JSON string
post_token_input_instance = PostTokenInput.from_json(json)
# print the JSON string representation of the object
print(PostTokenInput.to_json())

# convert the object into a dict
post_token_input_dict = post_token_input_instance.to_dict()
# create an instance of PostTokenInput from a dict
post_token_input_from_dict = PostTokenInput.from_dict(post_token_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


