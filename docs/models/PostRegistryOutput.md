# PostRegistryOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**metadata** | [**ApiResourceMetadata**](ApiResourceMetadata.md) |  | 
**properties** | [**RegistryProperties**](RegistryProperties.md) |  | 
**type** | **str** |  | [optional] 

## Example

```python
from ionoscloud_container_registry.models.post_registry_output import PostRegistryOutput

# TODO update the JSON string below
json = "{}"
# create an instance of PostRegistryOutput from a JSON string
post_registry_output_instance = PostRegistryOutput.from_json(json)
# print the JSON string representation of the object
print(PostRegistryOutput.to_json())

# convert the object into a dict
post_registry_output_dict = post_registry_output_instance.to_dict()
# create an instance of PostRegistryOutput from a dict
post_registry_output_from_dict = PostRegistryOutput.from_dict(post_registry_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


