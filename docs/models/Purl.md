# Purl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The affected package type | 
**name** | **str** | The affected package name | 
**version** | **str** | The affected package version | 

## Example

```python
from ionoscloud_container_registry.models.purl import Purl

# TODO update the JSON string below
json = "{}"
# create an instance of Purl from a JSON string
purl_instance = Purl.from_json(json)
# print the JSON string representation of the object
print(Purl.to_json())

# convert the object into a dict
purl_dict = purl_instance.to_dict()
# create an instance of Purl from a dict
purl_from_dict = Purl.from_dict(purl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


