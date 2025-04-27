# cnb_api.ArtifactoryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_package_tag**](ArtifactoryApi.md#delete_package_tag) | **DELETE** /{slug}/-/packages/{type}/{name}/-/tag/{tag} | 删除制品标签。 Delete the specific tag under specific package
[**delete_registry**](ArtifactoryApi.md#delete_registry) | **DELETE** /{registry} | 删除制品仓库。Delete the artifact repository.
[**download_quotas_by_project_name**](ArtifactoryApi.md#download_quotas_by_project_name) | **GET** /{slug}/-/packages/{type}/-/quotas/download | 下载制品配额信息。 Download registry quota details.
[**get_package**](ArtifactoryApi.md#get_package) | **GET** /{slug}/-/packages/{type}/{name} | 获取某一制品的详细信息。 Get the package detail.
[**get_package_tag_detail**](ArtifactoryApi.md#get_package_tag_detail) | **GET** /{slug}/-/packages/{type}/{name}/-/tag/{tag} | 获取制品标签详情。 Get the specific tag under specific package.
[**get_quota_by_project_name**](ArtifactoryApi.md#get_quota_by_project_name) | **GET** /{slug}/-/packages/{type}/-/quota | 查询制品配额。 Get quota of specific registry.
[**get_quotas_by_project_name**](ArtifactoryApi.md#get_quotas_by_project_name) | **GET** /{slug}/-/packages/{type}/-/quotas | 查询全部制品配额。 Get quotas of packages under one registry.
[**head_packages**](ArtifactoryApi.md#head_packages) | **HEAD** /{slug}/-/packages | 查询制品数量。 Head all packages.
[**list_package_tags**](ArtifactoryApi.md#list_package_tags) | **GET** /{slug}/-/packages/{type}/{pkgname}/-/tags | 查询制品标签列表。 List all tags under specific package.
[**list_packages**](ArtifactoryApi.md#list_packages) | **GET** /{slug}/-/packages | 查询制品列表。 List all packages.


# **delete_package_tag**
> delete_package_tag(slug, type, name, tag)

删除制品标签。 Delete the specific tag under specific package

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
registry-package-delete:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cnb_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cnb_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cnb_api.ArtifactoryApi(api_client)
    slug = 'slug_example' # str | Slug
    type = 'type_example' # str | Type
    name = 'name_example' # str | Name
    tag = 'tag_example' # str | Tag

    try:
        # 删除制品标签。 Delete the specific tag under specific package
        api_instance.delete_package_tag(slug, type, name, tag)
    except Exception as e:
        print("Exception when calling ArtifactoryApi->delete_package_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Slug | 
 **type** | **str**| Type | 
 **name** | **str**| Name | 
 **tag** | **str**| Tag | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registry**
> delete_registry(registry, x_cnb_identity_ticket=x_cnb_identity_ticket)

删除制品仓库。Delete the artifact repository.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
registry-delete:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cnb_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cnb_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cnb_api.ArtifactoryApi(api_client)
    registry = 'registry_example' # str | registry path
    x_cnb_identity_ticket = 'x_cnb_identity_ticket_example' # str | 微信身份验证票据，首次请求不传会返回新票据。WeChat auth ticket, will return new ticket if not provided in first request. (optional)

    try:
        # 删除制品仓库。Delete the artifact repository.
        api_instance.delete_registry(registry, x_cnb_identity_ticket=x_cnb_identity_ticket)
    except Exception as e:
        print("Exception when calling ArtifactoryApi->delete_registry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry** | **str**| registry path | 
 **x_cnb_identity_ticket** | **str**| 微信身份验证票据，首次请求不传会返回新票据。WeChat auth ticket, will return new ticket if not provided in first request. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_quotas_by_project_name**
> List[DtoQuotaRsp] download_quotas_by_project_name(slug, type, page=page, page_size=page_size, ordering=ordering)

下载制品配额信息。 Download registry quota details.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
registry-package:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_quota_rsp import DtoQuotaRsp
from cnb_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cnb_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cnb_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cnb_api.ArtifactoryApi(api_client)
    slug = 'slug_example' # str | Slug
    type = 'type_example' # str | Type
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)
    ordering = 'ordering_example' # str | Ordering type (optional)

    try:
        # 下载制品配额信息。 Download registry quota details.
        api_response = api_instance.download_quotas_by_project_name(slug, type, page=page, page_size=page_size, ordering=ordering)
        print("The response of ArtifactoryApi->download_quotas_by_project_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactoryApi->download_quotas_by_project_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Slug | 
 **type** | **str**| Type | 
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]
 **ordering** | **str**| Ordering type | [optional] 

### Return type

[**List[DtoQuotaRsp]**](DtoQuotaRsp.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.cnb.api+json, application/vnd.cnb.web+json, application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_package**
> DtoPackageDetail get_package(slug, type, name)

获取某一制品的详细信息。 Get the package detail.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
registry-package:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_package_detail import DtoPackageDetail
from cnb_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cnb_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cnb_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cnb_api.ArtifactoryApi(api_client)
    slug = 'slug_example' # str | Slug
    type = 'type_example' # str | Type
    name = 'name_example' # str | Name

    try:
        # 获取某一制品的详细信息。 Get the package detail.
        api_response = api_instance.get_package(slug, type, name)
        print("The response of ArtifactoryApi->get_package:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactoryApi->get_package: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Slug | 
 **type** | **str**| Type | 
 **name** | **str**| Name | 

### Return type

[**DtoPackageDetail**](DtoPackageDetail.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.cnb.web+json, application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_package_tag_detail**
> DtoTagDetail get_package_tag_detail(slug, type, name, tag, sha256=sha256)

获取制品标签详情。 Get the specific tag under specific package.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
registry-package:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_tag_detail import DtoTagDetail
from cnb_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cnb_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cnb_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cnb_api.ArtifactoryApi(api_client)
    slug = 'slug_example' # str | Slug
    type = 'type_example' # str | Type
    name = 'name_example' # str | Name
    tag = 'tag_example' # str | Tag
    sha256 = 'sha256_example' # str | 摘要，容器制品时必须。Digest (SHA256), required for container artifacts. (optional)

    try:
        # 获取制品标签详情。 Get the specific tag under specific package.
        api_response = api_instance.get_package_tag_detail(slug, type, name, tag, sha256=sha256)
        print("The response of ArtifactoryApi->get_package_tag_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactoryApi->get_package_tag_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Slug | 
 **type** | **str**| Type | 
 **name** | **str**| Name | 
 **tag** | **str**| Tag | 
 **sha256** | **str**| 摘要，容器制品时必须。Digest (SHA256), required for container artifacts. | [optional] 

### Return type

[**DtoTagDetail**](DtoTagDetail.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.cnb.api+json, application/vnd.cnb.web+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quota_by_project_name**
> DtoQuotaRsp get_quota_by_project_name(slug, type)

查询制品配额。 Get quota of specific registry.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
registry-package:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_quota_rsp import DtoQuotaRsp
from cnb_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cnb_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cnb_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cnb_api.ArtifactoryApi(api_client)
    slug = 'slug_example' # str | Slug
    type = 'type_example' # str | Type

    try:
        # 查询制品配额。 Get quota of specific registry.
        api_response = api_instance.get_quota_by_project_name(slug, type)
        print("The response of ArtifactoryApi->get_quota_by_project_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactoryApi->get_quota_by_project_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Slug | 
 **type** | **str**| Type | 

### Return type

[**DtoQuotaRsp**](DtoQuotaRsp.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.cnb.api+json, application/vnd.cnb.web+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quotas_by_project_name**
> List[DtoQuotaRsp] get_quotas_by_project_name(slug, type, page=page, page_size=page_size, ordering=ordering)

查询全部制品配额。 Get quotas of packages under one registry.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
registry-package:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_quota_rsp import DtoQuotaRsp
from cnb_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cnb_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cnb_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cnb_api.ArtifactoryApi(api_client)
    slug = 'slug_example' # str | Slug
    type = 'type_example' # str | Type
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)
    ordering = 'ordering_example' # str | Ordering type (optional)

    try:
        # 查询全部制品配额。 Get quotas of packages under one registry.
        api_response = api_instance.get_quotas_by_project_name(slug, type, page=page, page_size=page_size, ordering=ordering)
        print("The response of ArtifactoryApi->get_quotas_by_project_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactoryApi->get_quotas_by_project_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Slug | 
 **type** | **str**| Type | 
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]
 **ordering** | **str**| Ordering type | [optional] 

### Return type

[**List[DtoQuotaRsp]**](DtoQuotaRsp.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.cnb.api+json, application/vnd.cnb.web+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_packages**
> head_packages(slug, type, page=page, page_size=page_size, ordering=ordering, name=name)

查询制品数量。 Head all packages.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
registry-package:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cnb_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cnb_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cnb_api.ArtifactoryApi(api_client)
    slug = 'slug_example' # str | Slug
    type = 'type_example' # str | Type
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)
    ordering = 'ordering_example' # str | Ordering type (optional)
    name = 'name_example' # str | key word to search package (optional)

    try:
        # 查询制品数量。 Head all packages.
        api_instance.head_packages(slug, type, page=page, page_size=page_size, ordering=ordering, name=name)
    except Exception as e:
        print("Exception when calling ArtifactoryApi->head_packages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Slug | 
 **type** | **str**| Type | 
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]
 **ordering** | **str**| Ordering type | [optional] 
 **name** | **str**| key word to search package | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_package_tags**
> DtoTag list_package_tags(slug, type, pkgname, page=page, page_size=page_size, ordering=ordering, name=name)

查询制品标签列表。 List all tags under specific package.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
registry-package:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_tag import DtoTag
from cnb_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cnb_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cnb_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cnb_api.ArtifactoryApi(api_client)
    slug = 'slug_example' # str | Slug
    type = 'type_example' # str | Type
    pkgname = 'pkgname_example' # str | Package name
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)
    ordering = 'ordering_example' # str | Ordering type (optional)
    name = 'name_example' # str | Key word (optional)

    try:
        # 查询制品标签列表。 List all tags under specific package.
        api_response = api_instance.list_package_tags(slug, type, pkgname, page=page, page_size=page_size, ordering=ordering, name=name)
        print("The response of ArtifactoryApi->list_package_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactoryApi->list_package_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Slug | 
 **type** | **str**| Type | 
 **pkgname** | **str**| Package name | 
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]
 **ordering** | **str**| Ordering type | [optional] 
 **name** | **str**| Key word | [optional] 

### Return type

[**DtoTag**](DtoTag.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.cnb.api+json, application/vnd.cnb.web+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_packages**
> List[DtoPackage] list_packages(slug, type, page=page, page_size=page_size, ordering=ordering, name=name)

查询制品列表。 List all packages.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
registry-package:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_package import DtoPackage
from cnb_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cnb_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cnb_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cnb_api.ArtifactoryApi(api_client)
    slug = 'slug_example' # str | Slug
    type = 'type_example' # str | Type
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)
    ordering = 'ordering_example' # str | Ordering type (optional)
    name = 'name_example' # str | Key word to search package name (optional)

    try:
        # 查询制品列表。 List all packages.
        api_response = api_instance.list_packages(slug, type, page=page, page_size=page_size, ordering=ordering, name=name)
        print("The response of ArtifactoryApi->list_packages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactoryApi->list_packages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| Slug | 
 **type** | **str**| Type | 
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]
 **ordering** | **str**| Ordering type | [optional] 
 **name** | **str**| Key word to search package name | [optional] 

### Return type

[**List[DtoPackage]**](DtoPackage.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.cnb.api+json, application/vnd.cnb.web+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

