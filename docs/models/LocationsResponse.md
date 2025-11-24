# LocationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**items** | [**list[Location]**](Location.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from ionoscloud_container_registry.models.locations_response import LocationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LocationsResponse from a JSON string
locations_response_instance = LocationsResponse.from_json(json)
# print the JSON string representation of the object
print(LocationsResponse.to_json())

# convert the object into a dict
locations_response_dict = locations_response_instance.to_dict()
# create an instance of LocationsResponse from a dict
locations_response_from_dict = LocationsResponse.from_dict(locations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


