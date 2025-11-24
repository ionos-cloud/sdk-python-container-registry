# PutRegistryInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**PostRegistryProperties**](PostRegistryProperties.md) |  | 

## Example

```python
from ionoscloud_container_registry.models.put_registry_input import PutRegistryInput

# TODO update the JSON string below
json = "{}"
# create an instance of PutRegistryInput from a JSON string
put_registry_input_instance = PutRegistryInput.from_json(json)
# print the JSON string representation of the object
print(PutRegistryInput.to_json())

# convert the object into a dict
put_registry_input_dict = put_registry_input_instance.to_dict()
# create an instance of PutRegistryInput from a dict
put_registry_input_from_dict = PutRegistryInput.from_dict(put_registry_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


