# PutRegistryOutput


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
from ionoscloud_container_registry.models.put_registry_output import PutRegistryOutput

# TODO update the JSON string below
json = "{}"
# create an instance of PutRegistryOutput from a JSON string
put_registry_output_instance = PutRegistryOutput.from_json(json)
# print the JSON string representation of the object
print(PutRegistryOutput.to_json())

# convert the object into a dict
put_registry_output_dict = put_registry_output_instance.to_dict()
# create an instance of PutRegistryOutput from a dict
put_registry_output_from_dict = PutRegistryOutput.from_dict(put_registry_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


