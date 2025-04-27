# cnb_api.PullsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pull_label**](PullsApi.md#delete_pull_label) | **DELETE** /{repo}/-/pulls/{number}/labels/{name} | 删除 Pull 标签。Remove a label from a pull.
[**delete_pull_labels**](PullsApi.md#delete_pull_labels) | **DELETE** /{repo}/-/pulls/{number}/labels | 清空 Pull 标签。Remove all labels from a pull.
[**get_pull**](PullsApi.md#get_pull) | **GET** /{repo}/-/pulls/{number} | 查询指定 Pull。Get a pull request.
[**list_pull_comments**](PullsApi.md#list_pull_comments) | **GET** /{repo}/-/pulls/{number}/comments | 查询 Pull Comments 列表。List pull comments requests.
[**list_pull_labels**](PullsApi.md#list_pull_labels) | **GET** /{repo}/-/pulls/{number}/labels | 查询 Pull 的标签(label) 列表。List labels for a pull.
[**list_pulls**](PullsApi.md#list_pulls) | **GET** /{repo}/-/pulls | 查询 Pull 列表。List pull requests.
[**list_pulls_by_numbers**](PullsApi.md#list_pulls_by_numbers) | **GET** /{repo}/-/pull-in-batch | 根据numbers查询 Pull 列表。List pull requests by numbers.
[**merge_pull**](PullsApi.md#merge_pull) | **PUT** /{repo}/-/pulls/{number}/merge | 合并一个 Pull Request。Merge a pull request.
[**patch_pull**](PullsApi.md#patch_pull) | **PATCH** /{repo}/-/pulls/{number} | 更新一个 Pull Request。Update a pull request.
[**post_pull**](PullsApi.md#post_pull) | **POST** /{repo}/-/pulls | 新增一个 Pull。Create a pull request.
[**post_pull_comment**](PullsApi.md#post_pull_comment) | **POST** /{repo}/-/pulls/{number}/comments | 新增一个 Pull Comment。Create a pull comment.
[**post_pull_labels**](PullsApi.md#post_pull_labels) | **POST** /{repo}/-/pulls/{number}/labels | 新增 Pull 标签。Add labels to a pull.
[**post_pull_review**](PullsApi.md#post_pull_review) | **POST** /{repo}/-/pulls/{number}/reviews | 新增一次 pull request 评审。Create a pull review.
[**put_pull_labels**](PullsApi.md#put_pull_labels) | **PUT** /{repo}/-/pulls/{number}/labels | 设置 Pull 标签。Set the new labels for a pull.


# **delete_pull_label**
> ApiLabel delete_pull_label(repo, number, name)

删除 Pull 标签。Remove a label from a pull.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_label import ApiLabel
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
    api_instance = cnb_api.PullsApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | number
    name = 'name_example' # str | label name

    try:
        # 删除 Pull 标签。Remove a label from a pull.
        api_response = api_instance.delete_pull_label(repo, number, name)
        print("The response of PullsApi->delete_pull_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PullsApi->delete_pull_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **number** | **int**| number | 
 **name** | **str**| label name | 

### Return type

[**ApiLabel**](ApiLabel.md)

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

# **delete_pull_labels**
> delete_pull_labels(repo, number)

清空 Pull 标签。Remove all labels from a pull.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:rw

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
    api_instance = cnb_api.PullsApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | number

    try:
        # 清空 Pull 标签。Remove all labels from a pull.
        api_instance.delete_pull_labels(repo, number)
    except Exception as e:
        print("Exception when calling PullsApi->delete_pull_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **number** | **int**| number | 

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
**204** | No Content |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pull**
> ApiPull get_pull(repo, number)

查询指定 Pull。Get a pull request.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-pr:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_pull import ApiPull
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
    api_instance = cnb_api.PullsApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | pull request number

    try:
        # 查询指定 Pull。Get a pull request.
        api_response = api_instance.get_pull(repo, number)
        print("The response of PullsApi->get_pull:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PullsApi->get_pull: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **number** | **int**| pull request number | 

### Return type

[**ApiPull**](ApiPull.md)

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

# **list_pull_comments**
> List[ApiPullRequestComment] list_pull_comments(repo, number, page=page, page_size=page_size)

查询 Pull Comments 列表。List pull comments requests.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_pull_request_comment import ApiPullRequestComment
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
    api_instance = cnb_api.PullsApi(api_client)
    repo = 'repo_example' # str | repo
    number = 'number_example' # str | number
    page = 1 # int | pagination page number (optional) (default to 1)
    page_size = 30 # int | pagination page size (optional) (default to 30)

    try:
        # 查询 Pull Comments 列表。List pull comments requests.
        api_response = api_instance.list_pull_comments(repo, number, page=page, page_size=page_size)
        print("The response of PullsApi->list_pull_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PullsApi->list_pull_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **number** | **str**| number | 
 **page** | **int**| pagination page number | [optional] [default to 1]
 **page_size** | **int**| pagination page size | [optional] [default to 30]

### Return type

[**List[ApiPullRequestComment]**](ApiPullRequestComment.md)

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

# **list_pull_labels**
> List[ApiLabel] list_pull_labels(repo, number, page=page, page_size=page_size)

查询 Pull 的标签(label) 列表。List labels for a pull.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_label import ApiLabel
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
    api_instance = cnb_api.PullsApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | number
    page = 1 # int | pagination page number (optional) (default to 1)
    page_size = 30 # int | pagination page size (optional) (default to 30)

    try:
        # 查询 Pull 的标签(label) 列表。List labels for a pull.
        api_response = api_instance.list_pull_labels(repo, number, page=page, page_size=page_size)
        print("The response of PullsApi->list_pull_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PullsApi->list_pull_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **number** | **int**| number | 
 **page** | **int**| pagination page number | [optional] [default to 1]
 **page_size** | **int**| pagination page size | [optional] [default to 30]

### Return type

[**List[ApiLabel]**](ApiLabel.md)

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

# **list_pulls**
> List[ApiPullRequest] list_pulls(repo, page=page, page_size=page_size, state=state, authors=authors, reviewers=reviewers, assignees=assignees, base_ref=base_ref)

查询 Pull 列表。List pull requests.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-pr:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_pull_request import ApiPullRequest
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
    api_instance = cnb_api.PullsApi(api_client)
    repo = 'repo_example' # str | repo
    page = 1 # int | pagination page number (optional) (default to 1)
    page_size = 30 # int | pagination page size (optional) (default to 30)
    state = 'open' # str | pull state `open`，`closed`, `all` (optional) (default to 'open')
    authors = 'authors_example' # str | pull authors name, example: 张三,李四 (optional)
    reviewers = 'reviewers_example' # str | pull reviewers name, example: 张三,李四; - means nobody to review (optional)
    assignees = 'assignees_example' # str | pull assignees name, example: 张三,李四,-; - means assign to nobody (optional)
    base_ref = 'base_ref_example' # str | pull base ref,  example: refs/heads/master (optional)

    try:
        # 查询 Pull 列表。List pull requests.
        api_response = api_instance.list_pulls(repo, page=page, page_size=page_size, state=state, authors=authors, reviewers=reviewers, assignees=assignees, base_ref=base_ref)
        print("The response of PullsApi->list_pulls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PullsApi->list_pulls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **page** | **int**| pagination page number | [optional] [default to 1]
 **page_size** | **int**| pagination page size | [optional] [default to 30]
 **state** | **str**| pull state &#x60;open&#x60;，&#x60;closed&#x60;, &#x60;all&#x60; | [optional] [default to &#39;open&#39;]
 **authors** | **str**| pull authors name, example: 张三,李四 | [optional] 
 **reviewers** | **str**| pull reviewers name, example: 张三,李四; - means nobody to review | [optional] 
 **assignees** | **str**| pull assignees name, example: 张三,李四,-; - means assign to nobody | [optional] 
 **base_ref** | **str**| pull base ref,  example: refs/heads/master | [optional] 

### Return type

[**List[ApiPullRequest]**](ApiPullRequest.md)

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

# **list_pulls_by_numbers**
> List[ApiPullRequestInfo] list_pulls_by_numbers(repo, n)

根据numbers查询 Pull 列表。List pull requests by numbers.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-pr:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_pull_request_info import ApiPullRequestInfo
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
    api_instance = cnb_api.PullsApi(api_client)
    repo = 'repo_example' # str | repo
    n = ['n_example'] # List[str] | pull request numbers

    try:
        # 根据numbers查询 Pull 列表。List pull requests by numbers.
        api_response = api_instance.list_pulls_by_numbers(repo, n)
        print("The response of PullsApi->list_pulls_by_numbers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PullsApi->list_pulls_by_numbers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **n** | [**List[str]**](str.md)| pull request numbers | 

### Return type

[**List[ApiPullRequestInfo]**](ApiPullRequestInfo.md)

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

# **merge_pull**
> ApiMergePullResponse merge_pull(repo, number, merge_pull_request_form)

合并一个 Pull Request。Merge a pull request.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-pr:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_merge_pull_request import ApiMergePullRequest
from cnb_api.models.api_merge_pull_response import ApiMergePullResponse
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
    api_instance = cnb_api.PullsApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | Pull Request Number
    merge_pull_request_form = cnb_api.ApiMergePullRequest() # ApiMergePullRequest | Merge Pull Request Form

    try:
        # 合并一个 Pull Request。Merge a pull request.
        api_response = api_instance.merge_pull(repo, number, merge_pull_request_form)
        print("The response of PullsApi->merge_pull:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PullsApi->merge_pull: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **number** | **int**| Pull Request Number | 
 **merge_pull_request_form** | [**ApiMergePullRequest**](ApiMergePullRequest.md)| Merge Pull Request Form | 

### Return type

[**ApiMergePullResponse**](ApiMergePullResponse.md)

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

# **patch_pull**
> ApiPull patch_pull(repo, number, update_pull_request_form)

更新一个 Pull Request。Update a pull request.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-pr:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_patch_pull_request import ApiPatchPullRequest
from cnb_api.models.api_pull import ApiPull
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
    api_instance = cnb_api.PullsApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | Pull Request Number
    update_pull_request_form = cnb_api.ApiPatchPullRequest() # ApiPatchPullRequest | Update Pull Request Form

    try:
        # 更新一个 Pull Request。Update a pull request.
        api_response = api_instance.patch_pull(repo, number, update_pull_request_form)
        print("The response of PullsApi->patch_pull:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PullsApi->patch_pull: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **number** | **int**| Pull Request Number | 
 **update_pull_request_form** | [**ApiPatchPullRequest**](ApiPatchPullRequest.md)| Update Pull Request Form | 

### Return type

[**ApiPull**](ApiPull.md)

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

# **post_pull**
> ApiPull post_pull(repo, post_pull_form)

新增一个 Pull。Create a pull request.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-pr:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_pull import ApiPull
from cnb_api.models.api_pull_creation_form import ApiPullCreationForm
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
    api_instance = cnb_api.PullsApi(api_client)
    repo = 'repo_example' # str | repo
    post_pull_form = cnb_api.ApiPullCreationForm() # ApiPullCreationForm | Post Pull Request Form

    try:
        # 新增一个 Pull。Create a pull request.
        api_response = api_instance.post_pull(repo, post_pull_form)
        print("The response of PullsApi->post_pull:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PullsApi->post_pull: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **post_pull_form** | [**ApiPullCreationForm**](ApiPullCreationForm.md)| Post Pull Request Form | 

### Return type

[**ApiPull**](ApiPull.md)

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

# **post_pull_comment**
> post_pull_comment(repo, number, post_pull_comment_form)

新增一个 Pull Comment。Create a pull comment.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_pull_comment_creation_form import ApiPullCommentCreationForm
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
    api_instance = cnb_api.PullsApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | number
    post_pull_comment_form = cnb_api.ApiPullCommentCreationForm() # ApiPullCommentCreationForm | Post Pull Request Comment Form

    try:
        # 新增一个 Pull Comment。Create a pull comment.
        api_instance.post_pull_comment(repo, number, post_pull_comment_form)
    except Exception as e:
        print("Exception when calling PullsApi->post_pull_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **number** | **int**| number | 
 **post_pull_comment_form** | [**ApiPullCommentCreationForm**](ApiPullCommentCreationForm.md)| Post Pull Request Comment Form | 

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
**201** | Created |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pull_labels**
> ApiLabel post_pull_labels(repo, number, post_pull_labels_form)

新增 Pull 标签。Add labels to a pull.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_label import ApiLabel
from cnb_api.models.api_post_pull_labels_form import ApiPostPullLabelsForm
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
    api_instance = cnb_api.PullsApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | number
    post_pull_labels_form = cnb_api.ApiPostPullLabelsForm() # ApiPostPullLabelsForm | Post Pull Labels Form

    try:
        # 新增 Pull 标签。Add labels to a pull.
        api_response = api_instance.post_pull_labels(repo, number, post_pull_labels_form)
        print("The response of PullsApi->post_pull_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PullsApi->post_pull_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **number** | **int**| number | 
 **post_pull_labels_form** | [**ApiPostPullLabelsForm**](ApiPostPullLabelsForm.md)| Post Pull Labels Form | 

### Return type

[**ApiLabel**](ApiLabel.md)

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

# **post_pull_review**
> post_pull_review(repo, number, post_pull_review_form)

新增一次 pull request 评审。Create a pull review.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_pull_review_creation_form import ApiPullReviewCreationForm
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
    api_instance = cnb_api.PullsApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | number
    post_pull_review_form = cnb_api.ApiPullReviewCreationForm() # ApiPullReviewCreationForm | Post Pull Review Form

    try:
        # 新增一次 pull request 评审。Create a pull review.
        api_instance.post_pull_review(repo, number, post_pull_review_form)
    except Exception as e:
        print("Exception when calling PullsApi->post_pull_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **number** | **int**| number | 
 **post_pull_review_form** | [**ApiPullReviewCreationForm**](ApiPullReviewCreationForm.md)| Post Pull Review Form | 

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
**201** | Created |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pull_labels**
> ApiLabel put_pull_labels(repo, number, put_pull_labels_form)

设置 Pull 标签。Set the new labels for a pull.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_label import ApiLabel
from cnb_api.models.api_put_pull_labels_form import ApiPutPullLabelsForm
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
    api_instance = cnb_api.PullsApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | number
    put_pull_labels_form = cnb_api.ApiPutPullLabelsForm() # ApiPutPullLabelsForm | Put Pull Labels Form

    try:
        # 设置 Pull 标签。Set the new labels for a pull.
        api_response = api_instance.put_pull_labels(repo, number, put_pull_labels_form)
        print("The response of PullsApi->put_pull_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PullsApi->put_pull_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **number** | **int**| number | 
 **put_pull_labels_form** | [**ApiPutPullLabelsForm**](ApiPutPullLabelsForm.md)| Put Pull Labels Form | 

### Return type

[**ApiLabel**](ApiLabel.md)

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

