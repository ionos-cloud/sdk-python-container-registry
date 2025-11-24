# PutTokenOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**metadata** | [**ApiResourceMetadata**](ApiResourceMetadata.md) |  | 
**properties** | [**TokenProperties**](TokenProperties.md) |  | 
**type** | **str** |  | [optional] 

## Example

```python
from ionoscloud_container_registry.models.put_token_output import PutTokenOutput

# TODO update the JSON string below
json = "{}"
# create an instance of PutTokenOutput from a JSON string
put_token_output_instance = PutTokenOutput.from_json(json)
# print the JSON string representation of the object
print(PutTokenOutput.to_json())

# convert the object into a dict
put_token_output_dict = put_token_output_instance.to_dict()
# create an instance of PutTokenOutput from a dict
put_token_output_from_dict = PutTokenOutput.from_dict(put_token_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


