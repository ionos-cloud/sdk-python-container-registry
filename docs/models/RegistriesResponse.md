# RegistriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaginationLinks**](PaginationLinks.md) |  | 
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**items** | [**list[RegistryResponse]**](RegistryResponse.md) |  | [optional] 
**pagination** | [**RegistryPagination**](RegistryPagination.md) |  | 
**type** | **str** |  | [optional] 

## Example

```python
from ionoscloud_container_registry.models.registries_response import RegistriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegistriesResponse from a JSON string
registries_response_instance = RegistriesResponse.from_json(json)
# print the JSON string representation of the object
print(RegistriesResponse.to_json())

# convert the object into a dict
registries_response_dict = registries_response_instance.to_dict()
# create an instance of RegistriesResponse from a dict
registries_response_from_dict = RegistriesResponse.from_dict(registries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


