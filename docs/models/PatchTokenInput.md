# PatchTokenInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_date** | **datetime** |  | [optional] 
**scopes** | [**list[Scope]**](Scope.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from ionoscloud_container_registry.models.patch_token_input import PatchTokenInput

# TODO update the JSON string below
json = "{}"
# create an instance of PatchTokenInput from a JSON string
patch_token_input_instance = PatchTokenInput.from_json(json)
# print the JSON string representation of the object
print(PatchTokenInput.to_json())

# convert the object into a dict
patch_token_input_dict = patch_token_input_instance.to_dict()
# create an instance of PatchTokenInput from a dict
patch_token_input_from_dict = PatchTokenInput.from_dict(patch_token_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


