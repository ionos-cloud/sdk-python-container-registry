# PostRegistryInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**PostRegistryProperties**](PostRegistryProperties.md) |  | 

## Example

```python
from ionoscloud_container_registry.models.post_registry_input import PostRegistryInput

# TODO update the JSON string below
json = "{}"
# create an instance of PostRegistryInput from a JSON string
post_registry_input_instance = PostRegistryInput.from_json(json)
# print the JSON string representation of the object
print(PostRegistryInput.to_json())

# convert the object into a dict
post_registry_input_dict = post_registry_input_instance.to_dict()
# create an instance of PostRegistryInput from a dict
post_registry_input_from_dict = PostRegistryInput.from_dict(post_registry_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


