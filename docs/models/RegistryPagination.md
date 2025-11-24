# RegistryPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The maximum number of elements to return (used together with pagination.token for pagination) | 
**token** | **str** | An opaque token used to iterate the set of results (used together with limit for pagination) | 

## Example

```python
from ionoscloud_container_registry.models.registry_pagination import RegistryPagination

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryPagination from a JSON string
registry_pagination_instance = RegistryPagination.from_json(json)
# print the JSON string representation of the object
print(RegistryPagination.to_json())

# convert the object into a dict
registry_pagination_dict = registry_pagination_instance.to_dict()
# create an instance of RegistryPagination from a dict
registry_pagination_from_dict = RegistryPagination.from_dict(registry_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


