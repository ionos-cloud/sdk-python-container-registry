# ArtifactMetadata

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **created_date** | **datetime** | The ISO 8601 creation timestamp. | [optional]  |
| **created_by** | **str** | Unique name of the identity that created the resource. | [optional]  |
| **created_by_user_id** | **str** |  | [optional]  |
| **last_modified_date** | **datetime** | The ISO 8601 modified timestamp. | [optional]  |
| **last_modified_by** | **str** | Unique name of the identity that last modified the resource. | [optional]  |
| **last_modified_by_user_id** | **str** |  | [optional]  |
| **resource_urn** | **str** | Unique name of the resource. | [optional]  |
| **last_pushed_at** | **datetime** | The date and time the artifact was last pushed |  |
| **last_pulled_at** | **datetime** | The date and time the artifact was last pulled | [optional]  |
| **last_scanned_at** | **datetime** | The date and time the artifact was last scanned | [optional]  |
| **push_count** | **int** | The number of times the artifact was pushed |  |
| **pull_count** | **int** | The number of times the artifact was pulled |  |
| **vuln_max_severity** | **str** | The CVSS vulnerability severity rating | [optional]  |
| **vuln_total_score** | **float** | The total CVSS score of all vulnerabilities of the artifact | [optional]  |
| **vuln_total_count** | **int** | The total number of vulnerabilities of the artifact | [optional]  |
| **vuln_fixable_count** | **int** | The number of fixable vulnerabilities of the artifact | [optional]  |


