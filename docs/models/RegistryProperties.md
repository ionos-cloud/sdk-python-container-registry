# RegistryProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**garbage_collection_schedule** | [**WeeklySchedule**](WeeklySchedule.md) |  | [optional] 
**hostname** | **str** |  | [optional] 
**location** | **str** |  | 
**name** | **str** |  | 
**storage_usage** | [**StorageUsage**](StorageUsage.md) |  | [optional] 
**features** | [**RegistryFeatures**](RegistryFeatures.md) |  | [optional] 
**api_subnet_allow_list** | **list[str]** | Subnets and IPs that are allowed to access the registry API, supports IPv4 and IPv6. Maximum of 25 items may be specified. If no CIDR is given /32 and /128 are assumed for IPv4 and IPv6 respectively. 0.0.0.0/0 can be used to deny all traffic. __Note__: If this list is empty or not set, there are no restrictions.  | [optional] 

## Example

```python
from ionoscloud_container_registry.models.registry_properties import RegistryProperties

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryProperties from a JSON string
registry_properties_instance = RegistryProperties.from_json(json)
# print the JSON string representation of the object
print(RegistryProperties.to_json())

# convert the object into a dict
registry_properties_dict = registry_properties_instance.to_dict()
# create an instance of RegistryProperties from a dict
registry_properties_from_dict = RegistryProperties.from_dict(registry_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


