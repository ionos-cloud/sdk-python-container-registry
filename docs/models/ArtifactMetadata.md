# ArtifactMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **datetime** | The ISO 8601 creation timestamp. | [optional] [readonly] 
**created_by** | **str** | Unique name of the identity that created the resource. | [optional] [readonly] 
**created_by_user_id** | **str** | Unique id of the identity that created the resource. | [optional] [readonly] 
**last_modified_date** | **datetime** | The ISO 8601 modified timestamp. | [optional] [readonly] 
**last_modified_by** | **str** | Unique name of the identity that last modified the resource. | [optional] [readonly] 
**last_modified_by_user_id** | **str** | Unique id of the identity that last modified the resource. | [optional] [readonly] 
**resource_urn** | **str** | Unique name of the resource. | [optional] [readonly] 
**last_pushed_at** | **datetime** | The date and time the artifact was last pushed | 
**last_pulled_at** | **datetime** | The date and time the artifact was last pulled | [optional] 
**last_scanned_at** | **datetime** | The date and time the artifact was last scanned | [optional] 
**push_count** | **int** | The number of times the artifact was pushed | 
**pull_count** | **int** | The number of times the artifact was pulled | 
**vuln_max_severity** | **str** | The maximum vulnerability severity of the artifact, if any | [optional] 
**vuln_total_score** | **float** | The total CVSS score of all vulnerabilities of the artifact | [optional] 
**vuln_total_count** | **int** | The total number of vulnerabilities of the artifact | [optional] 
**vuln_fixable_count** | **int** | The number of fixable vulnerabilities of the artifact | [optional] 

## Example

```python
from ionoscloud_container_registry.models.artifact_metadata import ArtifactMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactMetadata from a JSON string
artifact_metadata_instance = ArtifactMetadata.from_json(json)
# print the JSON string representation of the object
print(ArtifactMetadata.to_json())

# convert the object into a dict
artifact_metadata_dict = artifact_metadata_instance.to_dict()
# create an instance of ArtifactMetadata from a dict
artifact_metadata_from_dict = ArtifactMetadata.from_dict(artifact_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


