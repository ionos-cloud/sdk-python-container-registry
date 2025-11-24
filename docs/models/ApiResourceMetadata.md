# ApiResourceMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** |  | 
**created_by_user_id** | **str** |  | 
**created_date** | **datetime** |  | 
**last_modified_by** | **str** |  | [optional] 
**last_modified_by_user_id** | **str** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**state** | **str** |  | 

## Example

```python
from ionoscloud_container_registry.models.api_resource_metadata import ApiResourceMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ApiResourceMetadata from a JSON string
api_resource_metadata_instance = ApiResourceMetadata.from_json(json)
# print the JSON string representation of the object
print(ApiResourceMetadata.to_json())

# convert the object into a dict
api_resource_metadata_dict = api_resource_metadata_instance.to_dict()
# create an instance of ApiResourceMetadata from a dict
api_resource_metadata_from_dict = ApiResourceMetadata.from_dict(api_resource_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


