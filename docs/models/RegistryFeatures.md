# RegistryFeatures

Optional registry features.  __Note__: some may incur additional charges - see individual feature descriptions for details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vulnerability_scanning** | [**FeatureVulnerabilityScanning**](FeatureVulnerabilityScanning.md) |  | [optional] 

## Example

```python
from ionoscloud_container_registry.models.registry_features import RegistryFeatures

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryFeatures from a JSON string
registry_features_instance = RegistryFeatures.from_json(json)
# print the JSON string representation of the object
print(RegistryFeatures.to_json())

# convert the object into a dict
registry_features_dict = registry_features_instance.to_dict()
# create an instance of RegistryFeatures from a dict
registry_features_from_dict = RegistryFeatures.from_dict(registry_features_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


