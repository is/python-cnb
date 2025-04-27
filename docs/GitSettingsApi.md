# cnb_api.GitSettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_branch_protection**](GitSettingsApi.md#delete_branch_protection) | **DELETE** /{repo}/-/settings/branch-protections/{id} | 删除仓库保护分支规则。 Delete branch protection rule.
[**get_branch_protection**](GitSettingsApi.md#get_branch_protection) | **GET** /{repo}/-/settings/branch-protections/{id} | 查询仓库保护分支规则。Get branch protection rule.
[**get_pipeline_settings**](GitSettingsApi.md#get_pipeline_settings) | **GET** /{repo}/-/settings/cloud-native-build | 查询仓库云原生构建设置。List pipeline settings.
[**get_pull_request_settings**](GitSettingsApi.md#get_pull_request_settings) | **GET** /{repo}/-/settings/pull-request | 查询仓库合并请求设置。List pull request settings.
[**get_push_limit_settings**](GitSettingsApi.md#get_push_limit_settings) | **GET** /{repo}/-/settings/push-limit | 查询仓库推送设置。List push limit settings.
[**list_branch_protections**](GitSettingsApi.md#list_branch_protections) | **GET** /{repo}/-/settings/branch-protections | 查询仓库保护分支规则列表。List branch protection rules.
[**patch_branch_protection**](GitSettingsApi.md#patch_branch_protection) | **PATCH** /{repo}/-/settings/branch-protections/{id} | 更新仓库保护分支规则。Update branch protection rule.
[**post_branch_protection**](GitSettingsApi.md#post_branch_protection) | **POST** /{repo}/-/settings/branch-protections | 新增仓库保护分支规则。Create branch protection rule.
[**put_pipeline_settings**](GitSettingsApi.md#put_pipeline_settings) | **PUT** /{repo}/-/settings/cloud-native-build | 更新仓库云原生构建设置。Update pipeline settings.
[**put_pull_request_settings**](GitSettingsApi.md#put_pull_request_settings) | **PUT** /{repo}/-/settings/pull-request | 设置仓库推送设置。Set pull request settings.
[**put_push_limit_settings**](GitSettingsApi.md#put_push_limit_settings) | **PUT** /{repo}/-/settings/push-limit | 设置仓库推送设置。Set push limit settings.


# **delete_branch_protection**
> delete_branch_protection(repo, id)

删除仓库保护分支规则。 Delete branch protection rule.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:rw

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
    api_instance = cnb_api.GitSettingsApi(api_client)
    repo = 'repo_example' # str | repo
    id = 'id_example' # str | Branch Protection id

    try:
        # 删除仓库保护分支规则。 Delete branch protection rule.
        api_instance.delete_branch_protection(repo, id)
    except Exception as e:
        print("Exception when calling GitSettingsApi->delete_branch_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **id** | **str**| Branch Protection id | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branch_protection**
> ApiBranchProtection get_branch_protection(repo, id)

查询仓库保护分支规则。Get branch protection rule.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_branch_protection import ApiBranchProtection
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
    api_instance = cnb_api.GitSettingsApi(api_client)
    repo = 'repo_example' # str | repo
    id = 'id_example' # str | branch protection id

    try:
        # 查询仓库保护分支规则。Get branch protection rule.
        api_response = api_instance.get_branch_protection(repo, id)
        print("The response of GitSettingsApi->get_branch_protection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitSettingsApi->get_branch_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **id** | **str**| branch protection id | 

### Return type

[**ApiBranchProtection**](ApiBranchProtection.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_settings**
> ApiPipelineSettings get_pipeline_settings(repo)

查询仓库云原生构建设置。List pipeline settings.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_pipeline_settings import ApiPipelineSettings
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
    api_instance = cnb_api.GitSettingsApi(api_client)
    repo = 'repo_example' # str | repo

    try:
        # 查询仓库云原生构建设置。List pipeline settings.
        api_response = api_instance.get_pipeline_settings(repo)
        print("The response of GitSettingsApi->get_pipeline_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitSettingsApi->get_pipeline_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 

### Return type

[**ApiPipelineSettings**](ApiPipelineSettings.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.cnb.web+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pull_request_settings**
> ApiPullRequestSettings get_pull_request_settings(repo)

查询仓库合并请求设置。List pull request settings.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_pull_request_settings import ApiPullRequestSettings
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
    api_instance = cnb_api.GitSettingsApi(api_client)
    repo = 'repo_example' # str | repo

    try:
        # 查询仓库合并请求设置。List pull request settings.
        api_response = api_instance.get_pull_request_settings(repo)
        print("The response of GitSettingsApi->get_pull_request_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitSettingsApi->get_pull_request_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 

### Return type

[**ApiPullRequestSettings**](ApiPullRequestSettings.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_push_limit_settings**
> ApiPushLimitSettings get_push_limit_settings(repo)

查询仓库推送设置。List push limit settings.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_push_limit_settings import ApiPushLimitSettings
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
    api_instance = cnb_api.GitSettingsApi(api_client)
    repo = 'repo_example' # str | repo

    try:
        # 查询仓库推送设置。List push limit settings.
        api_response = api_instance.get_push_limit_settings(repo)
        print("The response of GitSettingsApi->get_push_limit_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitSettingsApi->get_push_limit_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 

### Return type

[**ApiPushLimitSettings**](ApiPushLimitSettings.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_branch_protections**
> List[ApiBranchProtection] list_branch_protections(repo)

查询仓库保护分支规则列表。List branch protection rules.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_branch_protection import ApiBranchProtection
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
    api_instance = cnb_api.GitSettingsApi(api_client)
    repo = 'repo_example' # str | repo

    try:
        # 查询仓库保护分支规则列表。List branch protection rules.
        api_response = api_instance.list_branch_protections(repo)
        print("The response of GitSettingsApi->list_branch_protections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitSettingsApi->list_branch_protections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 

### Return type

[**List[ApiBranchProtection]**](ApiBranchProtection.md)

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

# **patch_branch_protection**
> patch_branch_protection(repo, id, branch_protection_form)

更新仓库保护分支规则。Update branch protection rule.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_branch_protection import ApiBranchProtection
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
    api_instance = cnb_api.GitSettingsApi(api_client)
    repo = 'repo_example' # str | repo
    id = 'id_example' # str | Branch Protection id
    branch_protection_form = cnb_api.ApiBranchProtection() # ApiBranchProtection | Branch Protection Form

    try:
        # 更新仓库保护分支规则。Update branch protection rule.
        api_instance.patch_branch_protection(repo, id, branch_protection_form)
    except Exception as e:
        print("Exception when calling GitSettingsApi->patch_branch_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **id** | **str**| Branch Protection id | 
 **branch_protection_form** | [**ApiBranchProtection**](ApiBranchProtection.md)| Branch Protection Form | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_branch_protection**
> post_branch_protection(repo, branch_protection_form)

新增仓库保护分支规则。Create branch protection rule.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_branch_protection import ApiBranchProtection
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
    api_instance = cnb_api.GitSettingsApi(api_client)
    repo = 'repo_example' # str | repo
    branch_protection_form = cnb_api.ApiBranchProtection() # ApiBranchProtection | Branch Protection Form

    try:
        # 新增仓库保护分支规则。Create branch protection rule.
        api_instance.post_branch_protection(repo, branch_protection_form)
    except Exception as e:
        print("Exception when calling GitSettingsApi->post_branch_protection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **branch_protection_form** | [**ApiBranchProtection**](ApiBranchProtection.md)| Branch Protection Form | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pipeline_settings**
> put_pipeline_settings(repo, pipeline_form)

更新仓库云原生构建设置。Update pipeline settings.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.web_pipeline_settings import WebPipelineSettings
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
    api_instance = cnb_api.GitSettingsApi(api_client)
    repo = 'repo_example' # str | repo
    pipeline_form = cnb_api.WebPipelineSettings() # WebPipelineSettings | Cloud Native Build Form

    try:
        # 更新仓库云原生构建设置。Update pipeline settings.
        api_instance.put_pipeline_settings(repo, pipeline_form)
    except Exception as e:
        print("Exception when calling GitSettingsApi->put_pipeline_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **pipeline_form** | [**WebPipelineSettings**](WebPipelineSettings.md)| Cloud Native Build Form | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pull_request_settings**
> put_pull_request_settings(repo, pull_request_form)

设置仓库推送设置。Set pull request settings.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_pull_request_settings import ApiPullRequestSettings
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
    api_instance = cnb_api.GitSettingsApi(api_client)
    repo = 'repo_example' # str | repo
    pull_request_form = cnb_api.ApiPullRequestSettings() # ApiPullRequestSettings | Pull Request Form

    try:
        # 设置仓库推送设置。Set pull request settings.
        api_instance.put_pull_request_settings(repo, pull_request_form)
    except Exception as e:
        print("Exception when calling GitSettingsApi->put_pull_request_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **pull_request_form** | [**ApiPullRequestSettings**](ApiPullRequestSettings.md)| Pull Request Form | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_push_limit_settings**
> put_push_limit_settings(repo, push_limit_form)

设置仓库推送设置。Set push limit settings.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_push_limit_settings import ApiPushLimitSettings
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
    api_instance = cnb_api.GitSettingsApi(api_client)
    repo = 'repo_example' # str | repo
    push_limit_form = cnb_api.ApiPushLimitSettings() # ApiPushLimitSettings | Push Limit Form

    try:
        # 设置仓库推送设置。Set push limit settings.
        api_instance.put_push_limit_settings(repo, push_limit_form)
    except Exception as e:
        print("Exception when calling GitSettingsApi->put_push_limit_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **push_limit_form** | [**ApiPushLimitSettings**](ApiPushLimitSettings.md)| Push Limit Form | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

