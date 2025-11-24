# RepositoryRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**href** | **str** |  | 
**metadata** | [**RepositoryMetadata**](RepositoryMetadata.md) |  | 
**properties** | [**Repository**](Repository.md) |  | 

## Example

```python
from ionoscloud_container_registry.models.repository_read import RepositoryRead

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRead from a JSON string
repository_read_instance = RepositoryRead.from_json(json)
# print the JSON string representation of the object
print(RepositoryRead.to_json())

# convert the object into a dict
repository_read_dict = repository_read_instance.to_dict()
# create an instance of RepositoryRead from a dict
repository_read_from_dict = RepositoryRead.from_dict(repository_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


