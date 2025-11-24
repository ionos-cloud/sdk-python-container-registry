# PostTokenProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_date** | **datetime** |  | [optional] 
**name** | **str** |  | 
**scopes** | [**list[Scope]**](Scope.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from ionoscloud_container_registry.models.post_token_properties import PostTokenProperties

# TODO update the JSON string below
json = "{}"
# create an instance of PostTokenProperties from a JSON string
post_token_properties_instance = PostTokenProperties.from_json(json)
# print the JSON string representation of the object
print(PostTokenProperties.to_json())

# convert the object into a dict
post_token_properties_dict = post_token_properties_instance.to_dict()
# create an instance of PostTokenProperties from a dict
post_token_properties_from_dict = PostTokenProperties.from_dict(post_token_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


