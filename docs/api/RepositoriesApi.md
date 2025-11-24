# ionoscloud_container_registry.RepositoriesApi

All URIs are relative to *https://api.ionos.com/containerregistries*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registries_repositories_delete**](RepositoriesApi.md#registries_repositories_delete) | **DELETE** /registries/{registryId}/repositories/{repositoryName} | Delete repository
[**registries_repositories_find_by_name**](RepositoriesApi.md#registries_repositories_find_by_name) | **GET** /registries/{registryId}/repositories/{repositoryName} | Retrieve Repository
[**registries_repositories_get**](RepositoriesApi.md#registries_repositories_get) | **GET** /registries/{registryId}/repositories | Retrieve all Repositories


# **registries_repositories_delete**
> registries_repositories_delete(registry_id, repository_name)

Delete repository

Delete all repository contents

		The registry V2 API allows manifests and blobs to be deleted individually but it is not possible to remove an entire repository.
		This operation is provided for convenience

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):

```python
import ionoscloud_container_registry
from ionoscloud_container_registry.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/containerregistries
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_container_registry.Configuration(
    host = "https://api.ionos.com/containerregistries"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = ionoscloud_container_registry.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_container_registry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_container_registry.RepositoriesApi(api_client)
    registry_id = 'registry_id_example' # str | The unique ID of the registry
    repository_name = 'my-service' # str | The name of the repository

    try:
        # Delete repository
        api_instance.registries_repositories_delete(registry_id, repository_name)
    except Exception as e:
        print("Exception when calling RepositoriesApi->registries_repositories_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| The unique ID of the registry | 
 **repository_name** | **str**| The name of the repository | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_repositories_find_by_name**
> RepositoryRead registries_repositories_find_by_name(registry_id, repository_name)

Retrieve Repository

Returns the Repository by Name.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_container_registry
from ionoscloud_container_registry.models.repository_read import RepositoryRead
from ionoscloud_container_registry.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/containerregistries
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_container_registry.Configuration(
    host = "https://api.ionos.com/containerregistries"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_container_registry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_container_registry.RepositoriesApi(api_client)
    registry_id = '1e41a73c-59d0-5507-86dd-fa2fc2501cfd' # str | The ID (UUID) of the Registry.
    repository_name = 'my-service' # str | The Name of the Repository.

    try:
        # Retrieve Repository
        api_response = api_instance.registries_repositories_find_by_name(registry_id, repository_name)
        print("The response of RepositoriesApi->registries_repositories_find_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->registries_repositories_find_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| The ID (UUID) of the Registry. | 
 **repository_name** | **str**| The Name of the Repository. | 

### Return type

[**RepositoryRead**](RepositoryRead.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Getting Repository was successful. |  -  |
**400** | ### Bad Request The request send to the API was malformed.  |  -  |
**401** | ### Unauthorized The request is missing authorization information or the authorization information provided are expired.  |  -  |
**403** | ### Not Allowed The user issuing the request does not have the needed permissions.  |  -  |
**404** | ### Not Found The resource that was requested could not be found.  |  -  |
**429** | ### Too Many Requests The user has sent too many requests in a given amount of time.  |  -  |
**500** | ### Internal Server Error An internal error occurred. We apologize for the inconvenience!  |  -  |
**503** | ### Service Unavailable The server is currently unable to handle the request due to a temporary overloading or maintenance of the server.  |  -  |
**0** | ### Unexpected Internal Server Error An unexpected internal error occurred. We apologize for the inconvenience!  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_repositories_get**
> RepositoryReadList registries_repositories_get(registry_id, offset=offset, limit=limit, filter_name=filter_name, filter_vulnerability_severity=filter_vulnerability_severity, order_by=order_by)

Retrieve all Repositories

This endpoint enables retrieving all Repositories using
pagination and optional filters.


### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_container_registry
from ionoscloud_container_registry.models.repository_read_list import RepositoryReadList
from ionoscloud_container_registry.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/containerregistries
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_container_registry.Configuration(
    host = "https://api.ionos.com/containerregistries"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_container_registry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_container_registry.RepositoriesApi(api_client)
    registry_id = '1e41a73c-59d0-5507-86dd-fa2fc2501cfd' # str | The ID (UUID) of the Registry.
    offset = 0 # int | The first element (of the total list of elements) to include in the response. Use together with limit for pagination. (optional) (default to 0)
    limit = 100 # int | The maximum number of elements to return. Use together with offset for pagination. (optional) (default to 100)
    filter_name = 'filter_name_example' # str | Filter resources by name. (optional)
    filter_vulnerability_severity = 'filter_vulnerability_severity_example' # str | Filter resources by vulnerability severity. (optional)
    order_by = -lastPush # str | The field to order the results by. If not provided, the results will be ordered by the default field. (optional) (default to -lastPush)

    try:
        # Retrieve all Repositories
        api_response = api_instance.registries_repositories_get(registry_id, offset=offset, limit=limit, filter_name=filter_name, filter_vulnerability_severity=filter_vulnerability_severity, order_by=order_by)
        print("The response of RepositoriesApi->registries_repositories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->registries_repositories_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| The ID (UUID) of the Registry. | 
 **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0]
 **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100]
 **filter_name** | **str**| Filter resources by name. | [optional] 
 **filter_vulnerability_severity** | **str**| Filter resources by vulnerability severity. | [optional] 
 **order_by** | **str**| The field to order the results by. If not provided, the results will be ordered by the default field. | [optional] [default to -lastPush]

### Return type

[**RepositoryReadList**](RepositoryReadList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned all requested Repositories successfully.  |  -  |
**400** | ### Bad Request The request send to the API was malformed.  |  -  |
**401** | ### Unauthorized The request is missing authorization information or the authorization information provided are expired.  |  -  |
**403** | ### Not Allowed The user issuing the request does not have the needed permissions.  |  -  |
**429** | ### Too Many Requests The user has sent too many requests in a given amount of time.  |  -  |
**500** | ### Internal Server Error An internal error occurred. We apologize for the inconvenience!  |  -  |
**503** | ### Service Unavailable The server is currently unable to handle the request due to a temporary overloading or maintenance of the server.  |  -  |
**0** | ### Unexpected Internal Server Error An unexpected internal error occurred. We apologize for the inconvenience!  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

