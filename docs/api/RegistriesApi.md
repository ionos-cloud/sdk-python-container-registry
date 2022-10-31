# RegistriesApi

All URIs are relative to *https://api.ionos.com/containerregistries*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**registries_delete**](RegistriesApi.md#registries_delete) | **DELETE** /registries/{registryId} | Delete registry |
| [**registries_find_by_id**](RegistriesApi.md#registries_find_by_id) | **GET** /registries/{registryId} | Get a registry |
| [**registries_get**](RegistriesApi.md#registries_get) | **GET** /registries | List all container registries |
| [**registries_patch**](RegistriesApi.md#registries_patch) | **PATCH** /registries/{registryId} | Update the properties of a registry |
| [**registries_post**](RegistriesApi.md#registries_post) | **POST** /registries | Create container registry |
| [**registries_put**](RegistriesApi.md#registries_put) | **PUT** /registries/{registryId} | Create or replace a container registry |


# **registries_delete**
> registries_delete(registry_id)

Delete registry

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
    api_instance = ionoscloud_container_registry.RegistriesApi(api_client)
    registry_id = 'registry_id_example' # str | The unique ID of the registry
    try:
        # Delete registry
        api_instance.registries_delete(registry_id)
    except ApiException as e:
        print('Exception when calling RegistriesApi.registries_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **registry_id** | [**str**](.md)| The unique ID of the registry |  |

### Return type

void (empty response body)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **registries_find_by_id**
> RegistryResponse registries_find_by_id(registry_id)

Get a registry

Get all information for a specific container registry

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
    api_instance = ionoscloud_container_registry.RegistriesApi(api_client)
    registry_id = 'registry_id_example' # str | The unique ID of the registry
    try:
        # Get a registry
        api_response = api_instance.registries_find_by_id(registry_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling RegistriesApi.registries_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **registry_id** | [**str**](.md)| The unique ID of the registry |  |

### Return type

[**RegistryResponse**](../models/RegistryResponse.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **registries_get**
> RegistriesResponse registries_get(filter_name=filter_name, limit=limit, next_page_token=next_page_token)

List all container registries

List all managed container registries for your account

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
    api_instance = ionoscloud_container_registry.RegistriesApi(api_client)
    try:
        # List all container registries
        api_response = api_instance.registries_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling RegistriesApi.registries_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **filter_name** | **str**| The registry name to search for | [optional]  |
| **limit** | **str**| The maximum number of elements to return (used together with nextPageToken for pagination) | [optional] [default to &#39;100&#39;] |
| **next_page_token** | **str**| The next page from the complete list of elements (used together with limit for pagination) | [optional]  |

### Return type

[**RegistriesResponse**](../models/RegistriesResponse.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **registries_patch**
> RegistryResponse registries_patch(registry_id, patch_registry_input)

Update the properties of a registry

Update the properties of a registry - \"garbageCollectionSchedule\" time and days of the week for runs

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
    api_instance = ionoscloud_container_registry.RegistriesApi(api_client)
    registry_id = 'registry_id_example' # str | The unique ID of the registry
    patch_registry_input = ionoscloud_container_registry.PatchRegistryInput() # PatchRegistryInput | 
    try:
        # Update the properties of a registry
        api_response = api_instance.registries_patch(registry_id, patch_registry_input)
        print(api_response)
    except ApiException as e:
        print('Exception when calling RegistriesApi.registries_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **registry_id** | [**str**](.md)| The unique ID of the registry |  |
| **patch_registry_input** | [**PatchRegistryInput**](PatchRegistryInput.md)|  |  |

### Return type

[**RegistryResponse**](../models/RegistryResponse.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **registries_post**
> PostRegistryOutput registries_post(post_registry_input)

Create container registry

Create a registry to hold container images or OCI compliant artifacts - \"name\" must have passed validation - \"location\" must be one of the available location IDs - \"garbageCollectionSchedule\" time and days of the week for runs

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
    api_instance = ionoscloud_container_registry.RegistriesApi(api_client)
    post_registry_input = ionoscloud_container_registry.PostRegistryInput() # PostRegistryInput | 
    try:
        # Create container registry
        api_response = api_instance.registries_post(post_registry_input)
        print(api_response)
    except ApiException as e:
        print('Exception when calling RegistriesApi.registries_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **post_registry_input** | [**PostRegistryInput**](PostRegistryInput.md)|  |  |

### Return type

[**PostRegistryOutput**](../models/PostRegistryOutput.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **registries_put**
> PutRegistryOutput registries_put(registry_id, put_registry_input)

Create or replace a container registry

Create/replace a registry to hold container images or OCI compliant artifacts  **On create** - \"name\" must have passed validation - \"location\" must be one of the available location IDs  **On update** - \"name\" cannot be changed - \"location\" cannot be changed  **On create or update** - \"garbageCollectionSchedule\": time and days of the week for runs 

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
    api_instance = ionoscloud_container_registry.RegistriesApi(api_client)
    registry_id = 'registry_id_example' # str | The unique ID of the registry
    put_registry_input = ionoscloud_container_registry.PutRegistryInput() # PutRegistryInput | 
    try:
        # Create or replace a container registry
        api_response = api_instance.registries_put(registry_id, put_registry_input)
        print(api_response)
    except ApiException as e:
        print('Exception when calling RegistriesApi.registries_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **registry_id** | [**str**](.md)| The unique ID of the registry |  |
| **put_registry_input** | [**PutRegistryInput**](PutRegistryInput.md)|  |  |

### Return type

[**PutRegistryOutput**](../models/PutRegistryOutput.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

