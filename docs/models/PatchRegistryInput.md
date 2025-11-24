# PatchRegistryInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**garbage_collection_schedule** | [**WeeklySchedule**](WeeklySchedule.md) |  | [optional] 
**features** | [**RegistryFeatures**](RegistryFeatures.md) |  | [optional] 
**api_subnet_allow_list** | **list[str]** | Subnets and IPs that are allowed to access the registry API, supports IPv4 and IPv6. Maximum of 25 items may be specified. If no CIDR is given /32 and /128 are assumed for IPv4 and IPv6 respectively. 0.0.0.0/0 can be used to deny all traffic. __Note__: If this list is empty or not set, there are no restrictions.  | [optional] 

## Example

```python
from ionoscloud_container_registry.models.patch_registry_input import PatchRegistryInput

# TODO update the JSON string below
json = "{}"
# create an instance of PatchRegistryInput from a JSON string
patch_registry_input_instance = PatchRegistryInput.from_json(json)
# print the JSON string representation of the object
print(PatchRegistryInput.to_json())

# convert the object into a dict
patch_registry_input_dict = patch_registry_input_instance.to_dict()
# create an instance of PatchRegistryInput from a dict
patch_registry_input_from_dict = PatchRegistryInput.from_dict(patch_registry_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


