# RegistryResponse


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
from ionoscloud_container_registry.models.registry_response import RegistryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryResponse from a JSON string
registry_response_instance = RegistryResponse.from_json(json)
# print the JSON string representation of the object
print(RegistryResponse.to_json())

# convert the object into a dict
registry_response_dict = registry_response_instance.to_dict()
# create an instance of RegistryResponse from a dict
registry_response_from_dict = RegistryResponse.from_dict(registry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


