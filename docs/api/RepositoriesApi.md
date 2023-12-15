# RepositoriesApi

All URIs are relative to *https://api.ionos.com/containerregistries*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**registries_repositories_delete**](RepositoriesApi.md#registries_repositories_delete) | **DELETE** /registries/{registryId}/repositories/{repositoryName} | Delete repository |
| [**registries_repositories_find_by_name**](RepositoriesApi.md#registries_repositories_find_by_name) | **GET** /registries/{registryId}/repositories/{repositoryName} | Retrieve Repository |
| [**registries_repositories_get**](RepositoriesApi.md#registries_repositories_get) | **GET** /registries/{registryId}/repositories | Retrieve all Repositories |


# **registries_repositories_delete**
> registries_repositories_delete(registry_id, repository_name)

Delete repository

Delete all repository contents    The registry V2 API allows manifests and blobs to be deleted individually but it is not possible to remove an entire repository.   This operation is provided for convenience

### Example

```python
from __future__ import print_function
import time
import ionoscloud_container_registry
from ionoscloud_container_registry.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/containerregistries
configuration = ionoscloud_container_registry.Configuration(
    host = 'https://api.ionos.com/containerregistries',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_container_registry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_container_registry.RepositoriesApi(api_client)
    registry_id = 'registry_id_example' # str | The unique ID of the registry
    repository_name = 'my-service' # str | The name of the repository
    try:
        # Delete repository
        api_instance.registries_repositories_delete(registry_id, repository_name)
    except ApiException as e:
        print('Exception when calling RepositoriesApi.registries_repositories_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **registry_id** | **str**| The unique ID of the registry |  |
| **repository_name** | **str**| The name of the repository |  |

### Return type

void (empty response body)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

# **registries_repositories_find_by_name**
> RepositoryRead registries_repositories_find_by_name(registry_id, repository_name)

Retrieve Repository

Returns the Repository by Name.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **registry_id** | **str**| The ID (UUID) of the Registry. |  |
| **repository_name** | **str**| The Name of the Repository that should be retrieved. |  |

### Return type

[**RepositoryRead**](../models/RepositoryRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **registries_repositories_get**
> RepositoryReadList registries_repositories_get(registry_id, offset=offset, limit=limit, filter_name=filter_name, filter_vulnerability_severity=filter_vulnerability_severity, order_by=order_by)

Retrieve all Repositories

This endpoint enables retrieving all Repositories using pagination and optional filters. 

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **registry_id** | **str**| The ID (UUID) of the Registry. |  |
| **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0] |
| **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100] |
| **filter_name** | **str**| Filter resources by name. | [optional]  |
| **filter_vulnerability_severity** | **str**| Filter resources by vulnerability severity. | [optional]  |
| **order_by** | **str**| The field to order the results by. If not provided, the results will be ordered by the default field. | [optional] [default to &#39;-lastPush&#39;] |

### Return type

[**RepositoryReadList**](../models/RepositoryReadList.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

