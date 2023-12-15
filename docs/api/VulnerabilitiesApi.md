# VulnerabilitiesApi

All URIs are relative to *https://api.ionos.com/containerregistries*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**vulnerabilities_find_by_id**](VulnerabilitiesApi.md#vulnerabilities_find_by_id) | **GET** /vulnerabilities/{vulnerabilityId} | Retrieve Vulnerability |


# **vulnerabilities_find_by_id**
> VulnerabilityRead vulnerabilities_find_by_id(vulnerability_id)

Retrieve Vulnerability

Returns the Vulnerability by ID.

### Example

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **vulnerability_id** | **str**| The ID of the Vulnerability that should be retrieved. |  |

### Return type

[**VulnerabilityRead**](../models/VulnerabilityRead.md)

### Authorization

tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

