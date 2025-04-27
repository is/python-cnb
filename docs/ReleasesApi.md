# cnb_api.ReleasesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_release**](ReleasesApi.md#delete_release) | **DELETE** /{repo}/-/releases/{release_id} | 删除指定的 release。Delete a release.
[**delete_release_asset**](ReleasesApi.md#delete_release_asset) | **DELETE** /{repo}/-/releases/{release_id}/assets/{asset_id} | 删除指定的 release asset。Delete the specified release asset.
[**get_latest_release**](ReleasesApi.md#get_latest_release) | **GET** /{repo}/-/releases/latest | 查询 latest release。Query the latest release.
[**get_release_asset**](ReleasesApi.md#get_release_asset) | **GET** /{repo}/-/releases/{release_id}/assets/{asset_id} | 查询指定的 release asset。Get the specified release asset.
[**get_release_by_id**](ReleasesApi.md#get_release_by_id) | **GET** /{repo}/-/releases/{release_id} | 根据 id 查询指定 release。Get a release by id.
[**get_release_by_tag**](ReleasesApi.md#get_release_by_tag) | **GET** /{repo}/-/releases/tags/{tag} | 通过 tag 查询指定 release。Get a release by tag.
[**list_releases**](ReleasesApi.md#list_releases) | **GET** /{repo}/-/releases | 查询 release 列表。List releases.
[**patch_release**](ReleasesApi.md#patch_release) | **PATCH** /{repo}/-/releases/{release_id} | 更新 release。Update a release.
[**post_release**](ReleasesApi.md#post_release) | **POST** /{repo}/-/releases | 新增一个 Release。Create a release.
[**post_release_asset_upload_confirmation**](ReleasesApi.md#post_release_asset_upload_confirmation) | **POST** /{repo}/-/releases/{release_id}/asset-upload-confirmation/{token}/{asset_path} | 确认 Release asset 上传完成。Confirm release asset upload.
[**post_release_asset_upload_url**](ReleasesApi.md#post_release_asset_upload_url) | **POST** /{repo}/-/releases/{release_id}/asset-upload-url | 新增一个 Release asset。Create a release asset.


# **delete_release**
> delete_release(repo, release_id)

删除指定的 release。Delete a release.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:rw

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
    api_instance = cnb_api.ReleasesApi(api_client)
    repo = 'repo_example' # str | repo
    release_id = 56 # int | release id

    try:
        # 删除指定的 release。Delete a release.
        api_instance.delete_release(repo, release_id)
    except Exception as e:
        print("Exception when calling ReleasesApi->delete_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **release_id** | **int**| release id | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_release_asset**
> delete_release_asset(repo, release_id, asset_id)

删除指定的 release asset。Delete the specified release asset.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:rw

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
    api_instance = cnb_api.ReleasesApi(api_client)
    repo = 'repo_example' # str | repo
    release_id = 56 # int | release id
    asset_id = 56 # int | asset id

    try:
        # 删除指定的 release asset。Delete the specified release asset.
        api_instance.delete_release_asset(repo, release_id, asset_id)
    except Exception as e:
        print("Exception when calling ReleasesApi->delete_release_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **release_id** | **int**| release id | 
 **asset_id** | **int**| asset id | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_release**
> ApiRelease get_latest_release(repo)

查询 latest release。Query the latest release.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_release import ApiRelease
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
    api_instance = cnb_api.ReleasesApi(api_client)
    repo = 'repo_example' # str | repo

    try:
        # 查询 latest release。Query the latest release.
        api_response = api_instance.get_latest_release(repo)
        print("The response of ReleasesApi->get_latest_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasesApi->get_latest_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 

### Return type

[**ApiRelease**](ApiRelease.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release_asset**
> ApiReleaseAsset get_release_asset(repo, release_id, asset_id)

查询指定的 release asset。Get the specified release asset.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_release_asset import ApiReleaseAsset
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
    api_instance = cnb_api.ReleasesApi(api_client)
    repo = 'repo_example' # str | repo
    release_id = 56 # int | release id
    asset_id = 56 # int | asset id

    try:
        # 查询指定的 release asset。Get the specified release asset.
        api_response = api_instance.get_release_asset(repo, release_id, asset_id)
        print("The response of ReleasesApi->get_release_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasesApi->get_release_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **release_id** | **int**| release id | 
 **asset_id** | **int**| asset id | 

### Return type

[**ApiReleaseAsset**](ApiReleaseAsset.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release_by_id**
> ApiRelease get_release_by_id(repo, release_id)

根据 id 查询指定 release。Get a release by id.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_release import ApiRelease
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
    api_instance = cnb_api.ReleasesApi(api_client)
    repo = 'repo_example' # str | repo
    release_id = 56 # int | release id

    try:
        # 根据 id 查询指定 release。Get a release by id.
        api_response = api_instance.get_release_by_id(repo, release_id)
        print("The response of ReleasesApi->get_release_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasesApi->get_release_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **release_id** | **int**| release id | 

### Return type

[**ApiRelease**](ApiRelease.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_release_by_tag**
> ApiRelease get_release_by_tag(repo, tag)

通过 tag 查询指定 release。Get a release by tag.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_release import ApiRelease
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
    api_instance = cnb_api.ReleasesApi(api_client)
    repo = 'repo_example' # str | repo
    tag = 'tag_example' # str | tag name

    try:
        # 通过 tag 查询指定 release。Get a release by tag.
        api_response = api_instance.get_release_by_tag(repo, tag)
        print("The response of ReleasesApi->get_release_by_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasesApi->get_release_by_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **tag** | **str**| tag name | 

### Return type

[**ApiRelease**](ApiRelease.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_releases**
> List[ApiRelease] list_releases(repo, page=page, page_size=page_size)

查询 release 列表。List releases.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_release import ApiRelease
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
    api_instance = cnb_api.ReleasesApi(api_client)
    repo = 'repo_example' # str | repo
    page = 1 # int | pagination page number (optional) (default to 1)
    page_size = 30 # int | pagination page size (optional) (default to 30)

    try:
        # 查询 release 列表。List releases.
        api_response = api_instance.list_releases(repo, page=page, page_size=page_size)
        print("The response of ReleasesApi->list_releases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasesApi->list_releases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **page** | **int**| pagination page number | [optional] [default to 1]
 **page_size** | **int**| pagination page size | [optional] [default to 30]

### Return type

[**List[ApiRelease]**](ApiRelease.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_release**
> patch_release(repo, release_id, patch_release_form)

更新 release。Update a release.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.openapi_patch_release_form import OpenapiPatchReleaseForm
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
    api_instance = cnb_api.ReleasesApi(api_client)
    repo = 'repo_example' # str | repo
    release_id = 56 # int | release id
    patch_release_form = cnb_api.OpenapiPatchReleaseForm() # OpenapiPatchReleaseForm | patch release form

    try:
        # 更新 release。Update a release.
        api_instance.patch_release(repo, release_id, patch_release_form)
    except Exception as e:
        print("Exception when calling ReleasesApi->patch_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **release_id** | **int**| release id | 
 **patch_release_form** | [**OpenapiPatchReleaseForm**](OpenapiPatchReleaseForm.md)| patch release form | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_release**
> ApiRelease post_release(repo, create_release_form)

新增一个 Release。Create a release.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_release import ApiRelease
from cnb_api.models.openapi_post_release_form import OpenapiPostReleaseForm
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
    api_instance = cnb_api.ReleasesApi(api_client)
    repo = 'repo_example' # str | repo
    create_release_form = cnb_api.OpenapiPostReleaseForm() # OpenapiPostReleaseForm | Post Release Form, attachment is optional

    try:
        # 新增一个 Release。Create a release.
        api_response = api_instance.post_release(repo, create_release_form)
        print("The response of ReleasesApi->post_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasesApi->post_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **create_release_form** | [**OpenapiPostReleaseForm**](OpenapiPostReleaseForm.md)| Post Release Form, attachment is optional | 

### Return type

[**ApiRelease**](ApiRelease.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_release_asset_upload_confirmation**
> post_release_asset_upload_confirmation(repo, release_id, token, asset_path)

确认 Release asset 上传完成。Confirm release asset upload.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:rw

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
    api_instance = cnb_api.ReleasesApi(api_client)
    repo = 'repo_example' # str | repo
    release_id = 56 # int | release id
    token = 'token_example' # str | upload token
    asset_path = 'asset_path_example' # str | release asset path

    try:
        # 确认 Release asset 上传完成。Confirm release asset upload.
        api_instance.post_release_asset_upload_confirmation(repo, release_id, token, asset_path)
    except Exception as e:
        print("Exception when calling ReleasesApi->post_release_asset_upload_confirmation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **release_id** | **int**| release id | 
 **token** | **str**| upload token | 
 **asset_path** | **str**| release asset path | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_release_asset_upload_url**
> OpenapiReleaseAssetUploadURL post_release_asset_upload_url(repo, release_id, create_release_asset_upload_url_form)

新增一个 Release asset。Create a release asset.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.openapi_post_release_asset_upload_url_form import OpenapiPostReleaseAssetUploadURLForm
from cnb_api.models.openapi_release_asset_upload_url import OpenapiReleaseAssetUploadURL
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
    api_instance = cnb_api.ReleasesApi(api_client)
    repo = 'repo_example' # str | repo
    release_id = 56 # int | release id
    create_release_asset_upload_url_form = cnb_api.OpenapiPostReleaseAssetUploadURLForm() # OpenapiPostReleaseAssetUploadURLForm | Post Release Asset Upload URL Form

    try:
        # 新增一个 Release asset。Create a release asset.
        api_response = api_instance.post_release_asset_upload_url(repo, release_id, create_release_asset_upload_url_form)
        print("The response of ReleasesApi->post_release_asset_upload_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReleasesApi->post_release_asset_upload_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **release_id** | **int**| release id | 
 **create_release_asset_upload_url_form** | [**OpenapiPostReleaseAssetUploadURLForm**](OpenapiPostReleaseAssetUploadURLForm.md)| Post Release Asset Upload URL Form | 

### Return type

[**OpenapiReleaseAssetUploadURL**](OpenapiReleaseAssetUploadURL.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

