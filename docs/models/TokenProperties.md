# TokenProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**Credentials**](Credentials.md) |  | 
**expiry_date** | **datetime** |  | [optional] 
**name** | **str** |  | 
**scopes** | [**list[Scope]**](Scope.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from ionoscloud_container_registry.models.token_properties import TokenProperties

# TODO update the JSON string below
json = "{}"
# create an instance of TokenProperties from a JSON string
token_properties_instance = TokenProperties.from_json(json)
# print the JSON string representation of the object
print(TokenProperties.to_json())

# convert the object into a dict
token_properties_dict = token_properties_instance.to_dict()
# create an instance of TokenProperties from a dict
token_properties_from_dict = TokenProperties.from_dict(token_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


