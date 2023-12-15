# CHANGELOG

## 1.1.0
### Features:
Added support for **Container Registry Vulnerability Scanning**:
- New APIs added `artifacts_api` and `vulnerabilities_api`

### Fixes:
- Fixed wrong parsing of `IONOS_HTTP_PROXY_HEADERS` by @hegerdes
- Fixed wrong error being shown when timeout is reached inside `wait_for`.
- Added asn1crypto and pydantic as requirements

## 1.0.0
This is the first release of the SDK Python Container Registry. Container Registry service enables IONOS clients to manage docker and OCI compliant registries for use by their managed Kubernetes clusters. Use a Container Registry to ensure you have a privately accessed registry to efficiently support image pulls.
