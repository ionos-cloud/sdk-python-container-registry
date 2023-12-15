# ArtifactsApi

All URIs are relative to *https://api.ionos.com/containerregistries*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**registries_artifacts_get**](ArtifactsApi.md#registries_artifacts_get) | **GET** /registries/{registryId}/artifacts | Retrieve all Artifacts by Registry |
| [**registries_repositories_artifacts_find_by_digest**](ArtifactsApi.md#registries_repositories_artifacts_find_by_digest) | **GET** /registries/{registryId}/repositories/{repositoryName}/artifacts/{digest} | Retrieve Artifact |
| [**registries_repositories_artifacts_get**](ArtifactsApi.md#registries_repositories_artifacts_get) | **GET** /registries/{registryId}/repositories/{repositoryName}/artifacts | Retrieve all Artifacts by Repository |
| [**registries_repositories_artifacts_vulnerabilities_get**](ArtifactsApi.md#registries_repositories_artifacts_vulnerabilities_get) | **GET** /registries/{registryId}/repositories/{repositoryName}/artifacts/{digest}/vulnerabilities | Retrieve all Vulnerabilities |


# **registries_artifacts_get**
> RegistryArtifactsReadList registries_artifacts_get(registry_id, offset=offset, limit=limit, filter_vulnerability_id=filter_vulnerability_id, order_by=order_by)

Retrieve all Artifacts by Registry

This endpoint enables retrieving all Artifacts using pagination and optional filters. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **registry_id** | **str**| The ID (UUID) of the Registry. |  |
| **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100] |
| **filter_vulnerability_id** | **str**| Filter resources by vulnerabilityId. | [optional]  |
| **order_by** | **str**| The field to order the results by. If not provided, the results will be ordered by the default field. | [optional] [default to &#39;-pullCount&#39;] |

### Return type

[**RegistryArtifactsReadList**](../models/RegistryArtifactsReadList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **registries_repositories_artifacts_find_by_digest**
> ArtifactRead registries_repositories_artifacts_find_by_digest(registry_id, repository_name, digest)

Retrieve Artifact

Returns the Artifact by Digest.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **registry_id** | **str**| The ID (UUID) of the Registry. |  |
| **repository_name** | **str**| The Name of the Repository. |  |
| **digest** | **str**| The Digest of the Artifact that should be retrieved. |  |

### Return type

[**ArtifactRead**](../models/ArtifactRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **registries_repositories_artifacts_get**
> ArtifactReadList registries_repositories_artifacts_get(registry_id, repository_name, offset=offset, limit=limit, order_by=order_by)

Retrieve all Artifacts by Repository

This endpoint enables retrieving all Artifacts using pagination and optional filters. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **registry_id** | **str**| The ID (UUID) of the Registry. |  |
| **repository_name** | **str**| The Name of the Repository. |  |
| **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100] |
| **order_by** | **str**| The field to order the results by. If not provided, the results will be ordered by the default field. | [optional] [default to &#39;-lastPush&#39;] |

### Return type

[**ArtifactReadList**](../models/ArtifactReadList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **registries_repositories_artifacts_vulnerabilities_get**
> ArtifactVulnerabilityReadList registries_repositories_artifacts_vulnerabilities_get(registry_id, repository_name, digest, offset=offset, limit=limit, filter_severity=filter_severity, filter_fixable=filter_fixable, order_by=order_by)

Retrieve all Vulnerabilities

This endpoint enables retrieving all Vulnerabilities using pagination and optional filters. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **registry_id** | **str**| The ID (UUID) of the Registry. |  |
| **repository_name** | **str**| The Name of the Repository. |  |
| **digest** | **str**| The Digest of the Artifact. |  |
| **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100] |
| **filter_severity** | **str**| Filter resources by vulnerability severity. | [optional]  |
| **filter_fixable** | **bool**| Filter resources by fixable (i.e. remediation action is available) | [optional]  |
| **order_by** | **str**| The field to order the results by. If not provided, the results will be ordered by the default field. | [optional] [default to &#39;-score&#39;] |

### Return type

[**ArtifactVulnerabilityReadList**](../models/ArtifactVulnerabilityReadList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

