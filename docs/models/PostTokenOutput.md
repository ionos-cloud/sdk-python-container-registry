# PostTokenOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**metadata** | [**ApiResourceMetadata**](ApiResourceMetadata.md) |  | 
**properties** | [**TokenProperties**](TokenProperties.md) |  | 
**type** | **str** |  | [optional] 

## Example

```python
from ionoscloud_container_registry.models.post_token_output import PostTokenOutput

# TODO update the JSON string below
json = "{}"
# create an instance of PostTokenOutput from a JSON string
post_token_output_instance = PostTokenOutput.from_json(json)
# print the JSON string representation of the object
print(PostTokenOutput.to_json())

# convert the object into a dict
post_token_output_dict = post_token_output_instance.to_dict()
# create an instance of PostTokenOutput from a dict
post_token_output_from_dict = PostTokenOutput.from_dict(post_token_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


