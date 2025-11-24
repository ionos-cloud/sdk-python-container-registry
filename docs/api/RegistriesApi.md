# ionoscloud_container_registry.RegistriesApi

All URIs are relative to *https://api.ionos.com/containerregistries*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registries_delete**](RegistriesApi.md#registries_delete) | **DELETE** /registries/{registryId} | Delete registry
[**registries_find_by_id**](RegistriesApi.md#registries_find_by_id) | **GET** /registries/{registryId} | Get a registry
[**registries_get**](RegistriesApi.md#registries_get) | **GET** /registries | List all container registries
[**registries_patch**](RegistriesApi.md#registries_patch) | **PATCH** /registries/{registryId} | Update the properties of a registry
[**registries_post**](RegistriesApi.md#registries_post) | **POST** /registries | Create container registry
[**registries_put**](RegistriesApi.md#registries_put) | **PUT** /registries/{registryId} | Create or replace a container registry


# **registries_delete**
> registries_delete(registry_id)

Delete registry



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
    api_instance = ionoscloud_container_registry.RegistriesApi(api_client)
    registry_id = 'registry_id_example' # str | The unique ID of the registry

    try:
        # Delete registry
        api_instance.registries_delete(registry_id)
    except Exception as e:
        print("Exception when calling RegistriesApi->registries_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| The unique ID of the registry | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_find_by_id**
> RegistryResponse registries_find_by_id(registry_id)

Get a registry

Get all information for a specific container registry

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):

```python
import ionoscloud_container_registry
from ionoscloud_container_registry.models.registry_response import RegistryResponse
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
    api_instance = ionoscloud_container_registry.RegistriesApi(api_client)
    registry_id = 'registry_id_example' # str | The unique ID of the registry

    try:
        # Get a registry
        api_response = api_instance.registries_find_by_id(registry_id)
        print("The response of RegistriesApi->registries_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->registries_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| The unique ID of the registry | 

### Return type

[**RegistryResponse**](RegistryResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_get**
> RegistriesResponse registries_get(filter_name=filter_name, limit=limit, pagination_token=pagination_token)

List all container registries

List all managed container registries for your account

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):

```python
import ionoscloud_container_registry
from ionoscloud_container_registry.models.registries_response import RegistriesResponse
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
    api_instance = ionoscloud_container_registry.RegistriesApi(api_client)
    filter_name = 'my-registry' # str | The registry name to search for (optional)
    limit = '100' # str | The maximum number of elements to return (used together with pagination.token for pagination) (optional) (default to '100')
    pagination_token = 'eyJ2IjoibWV0YS5rOHMuaW8vdjEiLCJydiI6MTYzMjQ0OTk2ODAsInN0YXJ0IjoiM2RmYTc3YjctZGIwNS00MjMwLThmMjAtOGU3NjJlOTUxOTUzXHUwMDAwIn0' # str | An opaque token used to iterate the set of results (used together with limit for pagination) (optional)

    try:
        # List all container registries
        api_response = api_instance.registries_get(filter_name=filter_name, limit=limit, pagination_token=pagination_token)
        print("The response of RegistriesApi->registries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->registries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_name** | **str**| The registry name to search for | [optional] 
 **limit** | **str**| The maximum number of elements to return (used together with pagination.token for pagination) | [optional] [default to &#39;100&#39;]
 **pagination_token** | **str**| An opaque token used to iterate the set of results (used together with limit for pagination) | [optional] 

### Return type

[**RegistriesResponse**](RegistriesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_patch**
> RegistryResponse registries_patch(registry_id, patch_registry_input)

Update the properties of a registry

Update the properties of a registry
- "garbageCollectionSchedule" time and days of the week for runs

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):

```python
import ionoscloud_container_registry
from ionoscloud_container_registry.models.patch_registry_input import PatchRegistryInput
from ionoscloud_container_registry.models.registry_response import RegistryResponse
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
    api_instance = ionoscloud_container_registry.RegistriesApi(api_client)
    registry_id = 'registry_id_example' # str | The unique ID of the registry
    patch_registry_input = ionoscloud_container_registry.PatchRegistryInput() # PatchRegistryInput | 

    try:
        # Update the properties of a registry
        api_response = api_instance.registries_patch(registry_id, patch_registry_input)
        print("The response of RegistriesApi->registries_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->registries_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| The unique ID of the registry | 
 **patch_registry_input** | [**PatchRegistryInput**](PatchRegistryInput.md)|  | 

### Return type

[**RegistryResponse**](RegistryResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_post**
> PostRegistryOutput registries_post(post_registry_input)

Create container registry

Create a registry to hold container images or OCI compliant artifacts
- "name" must have passed validation
- "location" must be one of the available location IDs
- "garbageCollectionSchedule" time and days of the week for runs
- "features": "vulnerabilityScanning" default is enabled

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):

```python
import ionoscloud_container_registry
from ionoscloud_container_registry.models.post_registry_input import PostRegistryInput
from ionoscloud_container_registry.models.post_registry_output import PostRegistryOutput
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
    api_instance = ionoscloud_container_registry.RegistriesApi(api_client)
    post_registry_input = ionoscloud_container_registry.PostRegistryInput() # PostRegistryInput | 

    try:
        # Create container registry
        api_response = api_instance.registries_post(post_registry_input)
        print("The response of RegistriesApi->registries_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->registries_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_registry_input** | [**PostRegistryInput**](PostRegistryInput.md)|  | 

### Return type

[**PostRegistryOutput**](PostRegistryOutput.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created container registry is returned with &#39;metadata.status&#39; set to \&quot;BUSY\&quot;. |  * Location -  <br>  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registries_put**
> PutRegistryOutput registries_put(registry_id, put_registry_input)

Create or replace a container registry

Create/replace a registry to hold container images or OCI compliant
artifacts
**On create**
- "name" must have passed validation
- "location" must be one of the available location IDs
**On update**
- "name" cannot be changed
- "location" cannot be changed
**On create or update**
- "garbageCollectionSchedule": time and days of the week for runs


### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):

```python
import ionoscloud_container_registry
from ionoscloud_container_registry.models.put_registry_input import PutRegistryInput
from ionoscloud_container_registry.models.put_registry_output import PutRegistryOutput
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
    api_instance = ionoscloud_container_registry.RegistriesApi(api_client)
    registry_id = 'registry_id_example' # str | The unique ID of the registry
    put_registry_input = ionoscloud_container_registry.PutRegistryInput() # PutRegistryInput | 

    try:
        # Create or replace a container registry
        api_response = api_instance.registries_put(registry_id, put_registry_input)
        print("The response of RegistriesApi->registries_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegistriesApi->registries_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | **str**| The unique ID of the registry | 
 **put_registry_input** | [**PutRegistryInput**](PutRegistryInput.md)|  | 

### Return type

[**PutRegistryOutput**](PutRegistryOutput.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created container registry is returned with &#39;metadata.status&#39; set to \&quot;BUSY\&quot;. |  * Location -  <br>  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

