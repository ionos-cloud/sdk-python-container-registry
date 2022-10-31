# RepositoriesApi

All URIs are relative to *https://api.ionos.com/containerregistries*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**registries_repositories_delete**](RepositoriesApi.md#registries_repositories_delete) | **DELETE** /registries/{registryId}/repositories/{name} | Delete repository |


# **registries_repositories_delete**
> registries_repositories_delete(registry_id, name)

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
    name = 'ubuntu' # str | The name of the repository
    try:
        # Delete repository
        api_instance.registries_repositories_delete(registry_id, name)
    except ApiException as e:
        print('Exception when calling RepositoriesApi.registries_repositories_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **registry_id** | [**str**](.md)| The unique ID of the registry |  |
| **name** | **str**| The name of the repository |  |

### Return type

void (empty response body)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

