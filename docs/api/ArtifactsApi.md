# ionoscloud_container_registry.ArtifactsApi

All URIs are relative to *https://api.ionos.com/containerregistries*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registries_artifacts_get**](ArtifactsApi.md#registries_artifacts_get) | **GET** /registries/{registryId}/artifacts | Retrieve all Artifacts by Registry
[**registries_repositories_artifacts_find_by_digest**](ArtifactsApi.md#registries_repositories_artifacts_find_by_digest) | **GET** /registries/{registryId}/repositories/{repositoryName}/artifacts/{digest} | Retrieve Artifact
[**registries_repositories_artifacts_get**](ArtifactsApi.md#registries_repositories_artifacts_get) | **GET** /registries/{registryId}/repositories/{repositoryName}/artifacts | Retrieve all Artifacts by Repository
[**registries_repositories_artifacts_vulnerabilities_get**](ArtifactsApi.md#registries_repositories_artifacts_vulnerabilities_get) | **GET** /registries/{registryId}/repositories/{repositoryName}/artifacts/{digest}/vulnerabilities | Retrieve all Vulnerabilities


# **registries_artifacts_get**
> RegistryArtifactsReadList registries_artifacts_get(registry_id, offset=offset, limit=limit, filter_vulnerability_id=filter_vulnerability_id, order_by=order_by)

Retrieve all Artifacts by Registry

This endpoint enables retrieving all Artifacts using
pagination and optional filters.


### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_container_registry
from ionoscloud_container_registry.models.registry_artifacts_read_list import RegistryArtifactsReadList
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
    api_instance = ionoscloud_container_registry.ArtifactsApi(api_client)
    registry_id = '1e41a73c-59d0-5507-86dd-fa2fc2501cfd' # str | The ID (UUID) of the Registry.
    offset = 0 # int | The first element (of the total list of elements) to include in the response. Use together with limit for pagination. (optional) (default to 0)
    limit = 100 # int | The maximum number of elements to return. Use together with offset for pagination. (optional) (default to 100)
    filter_vulnerability_id = 'filter_vulnerability_id_example' # str | Filter resources by vulnerabilityId. (optional)
    order_by = -pullCount # str | The field to order the results by. If not provided, the results will be ordered by the default field. (optional) (default to -pullCount)

    try:
        # Retrieve all Artifacts by Registry
        api_response = api_instance.registries_artifacts_get(registry_id, offset=offset, limit=limit, filter_vulnerability_id=filter_vulnerability_id, order_by=order_by)
        print("The response of ArtifactsApi->registries_artifacts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->registries_artifacts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| The ID (UUID) of the Registry. | 
 **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0]
 **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100]
 **filter_vulnerability_id** | **str**| Filter resources by vulnerabilityId. | [optional] 
 **order_by** | **str**| The field to order the results by. If not provided, the results will be ordered by the default field. | [optional] [default to -pullCount]

### Return type

[**RegistryArtifactsReadList**](RegistryArtifactsReadList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned all requested Artifacts successfully.  |  -  |
**400** | ### Bad Request The request send to the API was malformed.  |  -  |
**401** | ### Unauthorized The request is missing authorization information or the authorization information provided are expired.  |  -  |
**403** | ### Not Allowed The user issuing the request does not have the needed permissions.  |  -  |
**429** | ### Too Many Requests The user has sent too many requests in a given amount of time.  |  -  |
**500** | ### Internal Server Error An internal error occurred. We apologize for the inconvenience!  |  -  |
**503** | ### Service Unavailable The server is currently unable to handle the request due to a temporary overloading or maintenance of the server.  |  -  |
**0** | ### Unexpected Internal Server Error An unexpected internal error occurred. We apologize for the inconvenience!  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_repositories_artifacts_find_by_digest**
> ArtifactRead registries_repositories_artifacts_find_by_digest(registry_id, repository_name, digest)

Retrieve Artifact

Returns the Artifact by Digest.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_container_registry
from ionoscloud_container_registry.models.artifact_read import ArtifactRead
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
    api_instance = ionoscloud_container_registry.ArtifactsApi(api_client)
    registry_id = '1e41a73c-59d0-5507-86dd-fa2fc2501cfd' # str | The ID (UUID) of the Registry.
    repository_name = 'my-service' # str | The Name of the Repository.
    digest = 'sha256:12345678901234567890123456789012' # str | The Digest of the Artifact.

    try:
        # Retrieve Artifact
        api_response = api_instance.registries_repositories_artifacts_find_by_digest(registry_id, repository_name, digest)
        print("The response of ArtifactsApi->registries_repositories_artifacts_find_by_digest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->registries_repositories_artifacts_find_by_digest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| The ID (UUID) of the Registry. | 
 **repository_name** | **str**| The Name of the Repository. | 
 **digest** | **str**| The Digest of the Artifact. | 

### Return type

[**ArtifactRead**](ArtifactRead.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Getting Artifact was successful. |  -  |
**400** | ### Bad Request The request send to the API was malformed.  |  -  |
**401** | ### Unauthorized The request is missing authorization information or the authorization information provided are expired.  |  -  |
**403** | ### Not Allowed The user issuing the request does not have the needed permissions.  |  -  |
**404** | ### Not Found The resource that was requested could not be found.  |  -  |
**429** | ### Too Many Requests The user has sent too many requests in a given amount of time.  |  -  |
**500** | ### Internal Server Error An internal error occurred. We apologize for the inconvenience!  |  -  |
**503** | ### Service Unavailable The server is currently unable to handle the request due to a temporary overloading or maintenance of the server.  |  -  |
**0** | ### Unexpected Internal Server Error An unexpected internal error occurred. We apologize for the inconvenience!  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_repositories_artifacts_get**
> ArtifactReadList registries_repositories_artifacts_get(registry_id, repository_name, offset=offset, limit=limit, order_by=order_by)

Retrieve all Artifacts by Repository

This endpoint enables retrieving all Artifacts using
pagination and optional filters.


### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_container_registry
from ionoscloud_container_registry.models.artifact_read_list import ArtifactReadList
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
    api_instance = ionoscloud_container_registry.ArtifactsApi(api_client)
    registry_id = '1e41a73c-59d0-5507-86dd-fa2fc2501cfd' # str | The ID (UUID) of the Registry.
    repository_name = 'my-service' # str | The Name of the Repository.
    offset = 0 # int | The first element (of the total list of elements) to include in the response. Use together with limit for pagination. (optional) (default to 0)
    limit = 100 # int | The maximum number of elements to return. Use together with offset for pagination. (optional) (default to 100)
    order_by = -lastPush # str | The field to order the results by. If not provided, the results will be ordered by the default field. (optional) (default to -lastPush)

    try:
        # Retrieve all Artifacts by Repository
        api_response = api_instance.registries_repositories_artifacts_get(registry_id, repository_name, offset=offset, limit=limit, order_by=order_by)
        print("The response of ArtifactsApi->registries_repositories_artifacts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->registries_repositories_artifacts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| The ID (UUID) of the Registry. | 
 **repository_name** | **str**| The Name of the Repository. | 
 **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0]
 **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100]
 **order_by** | **str**| The field to order the results by. If not provided, the results will be ordered by the default field. | [optional] [default to -lastPush]

### Return type

[**ArtifactReadList**](ArtifactReadList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned all requested Artifacts successfully.  |  -  |
**400** | ### Bad Request The request send to the API was malformed.  |  -  |
**401** | ### Unauthorized The request is missing authorization information or the authorization information provided are expired.  |  -  |
**403** | ### Not Allowed The user issuing the request does not have the needed permissions.  |  -  |
**429** | ### Too Many Requests The user has sent too many requests in a given amount of time.  |  -  |
**500** | ### Internal Server Error An internal error occurred. We apologize for the inconvenience!  |  -  |
**503** | ### Service Unavailable The server is currently unable to handle the request due to a temporary overloading or maintenance of the server.  |  -  |
**0** | ### Unexpected Internal Server Error An unexpected internal error occurred. We apologize for the inconvenience!  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_repositories_artifacts_vulnerabilities_get**
> ArtifactVulnerabilityReadList registries_repositories_artifacts_vulnerabilities_get(registry_id, repository_name, digest, offset=offset, limit=limit, filter_severity=filter_severity, filter_fixable=filter_fixable, order_by=order_by)

Retrieve all Vulnerabilities

This endpoint enables retrieving all Vulnerabilities using
pagination and optional filters.


### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_container_registry
from ionoscloud_container_registry.models.artifact_vulnerability_read_list import ArtifactVulnerabilityReadList
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
    api_instance = ionoscloud_container_registry.ArtifactsApi(api_client)
    registry_id = '1e41a73c-59d0-5507-86dd-fa2fc2501cfd' # str | The ID (UUID) of the Registry.
    repository_name = 'my-service' # str | The Name of the Repository.
    digest = 'sha256:12345678901234567890123456789012' # str | The Digest of the Artifact.
    offset = 0 # int | The first element (of the total list of elements) to include in the response. Use together with limit for pagination. (optional) (default to 0)
    limit = 100 # int | The maximum number of elements to return. Use together with offset for pagination. (optional) (default to 100)
    filter_severity = 'filter_severity_example' # str | Filter resources by vulnerability severity. (optional)
    filter_fixable = True # bool | Filter resources by fixable (i.e. remediation action is available) (optional)
    order_by = -score # str | The field to order the results by. If not provided, the results will be ordered by the default field. (optional) (default to -score)

    try:
        # Retrieve all Vulnerabilities
        api_response = api_instance.registries_repositories_artifacts_vulnerabilities_get(registry_id, repository_name, digest, offset=offset, limit=limit, filter_severity=filter_severity, filter_fixable=filter_fixable, order_by=order_by)
        print("The response of ArtifactsApi->registries_repositories_artifacts_vulnerabilities_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->registries_repositories_artifacts_vulnerabilities_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| The ID (UUID) of the Registry. | 
 **repository_name** | **str**| The Name of the Repository. | 
 **digest** | **str**| The Digest of the Artifact. | 
 **offset** | **int**| The first element (of the total list of elements) to include in the response. Use together with limit for pagination. | [optional] [default to 0]
 **limit** | **int**| The maximum number of elements to return. Use together with offset for pagination. | [optional] [default to 100]
 **filter_severity** | **str**| Filter resources by vulnerability severity. | [optional] 
 **filter_fixable** | **bool**| Filter resources by fixable (i.e. remediation action is available) | [optional] 
 **order_by** | **str**| The field to order the results by. If not provided, the results will be ordered by the default field. | [optional] [default to -score]

### Return type

[**ArtifactVulnerabilityReadList**](ArtifactVulnerabilityReadList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned all requested Vulnerabilities successfully.  |  -  |
**400** | ### Bad Request The request send to the API was malformed.  |  -  |
**401** | ### Unauthorized The request is missing authorization information or the authorization information provided are expired.  |  -  |
**403** | ### Not Allowed The user issuing the request does not have the needed permissions.  |  -  |
**429** | ### Too Many Requests The user has sent too many requests in a given amount of time.  |  -  |
**500** | ### Internal Server Error An internal error occurred. We apologize for the inconvenience!  |  -  |
**503** | ### Service Unavailable The server is currently unable to handle the request due to a temporary overloading or maintenance of the server.  |  -  |
**0** | ### Unexpected Internal Server Error An unexpected internal error occurred. We apologize for the inconvenience!  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

