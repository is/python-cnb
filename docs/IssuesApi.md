# cnb_api.IssuesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_issue**](IssuesApi.md#create_issue) | **POST** /{repo}/-/issues | 创建一个 Issue。Create an issue.
[**delete_issue_label**](IssuesApi.md#delete_issue_label) | **DELETE** /{repo}/-/issues/{number}/labels/{name} | 删除 Issue 标签。Remove a label from an issue.
[**delete_issue_labels**](IssuesApi.md#delete_issue_labels) | **DELETE** /{repo}/-/issues/{number}/labels | 清空 Issue 标签。Remove all labels from an issue.
[**get_issue**](IssuesApi.md#get_issue) | **GET** /{repo}/-/issues/{number} | 查询指定的 Issues。Get an issue.
[**get_issue_comment**](IssuesApi.md#get_issue_comment) | **GET** /{repo}/-/issues/{number}/comments/{comment_id} | 获取一个 Issue Comment。Get an issue comment.
[**list_issue_comments**](IssuesApi.md#list_issue_comments) | **GET** /{repo}/-/issues/{number}/comments | 查询仓库的 Issue 评论列表。List repository issue comments.
[**list_issue_labels**](IssuesApi.md#list_issue_labels) | **GET** /{repo}/-/issues/{number}/labels | 查询 Issue 的标签(label) 列表。List labels for an issue.
[**list_issues**](IssuesApi.md#list_issues) | **GET** /{repo}/-/issues | 查询仓库的 Issues。List issues.
[**patch_issue_comment**](IssuesApi.md#patch_issue_comment) | **PATCH** /{repo}/-/issues/{number}/comments/{comment_id} | 修改一个 Issue Comment。Update an issue comment.
[**post_issue_comment**](IssuesApi.md#post_issue_comment) | **POST** /{repo}/-/issues/{number}/comments | 创建一个 Issue Comment。Create an issue comment.
[**post_issue_labels**](IssuesApi.md#post_issue_labels) | **POST** /{repo}/-/issues/{number}/labels | 新增 Issue 标签。Add labels to an issue.
[**put_issue_labels**](IssuesApi.md#put_issue_labels) | **PUT** /{repo}/-/issues/{number}/labels | 设置 Issue 标签。 Set the new labels for an issue.
[**update_issue**](IssuesApi.md#update_issue) | **PATCH** /{repo}/-/issues/{number} | 更新一个 Issue。Update an issue.


# **create_issue**
> ApiIssueDetail create_issue(repo, post_issue_form)

创建一个 Issue。Create an issue.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_issue_detail import ApiIssueDetail
from cnb_api.models.api_post_issue_form import ApiPostIssueForm
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
    api_instance = cnb_api.IssuesApi(api_client)
    repo = 'repo_example' # str | repo
    post_issue_form = cnb_api.ApiPostIssueForm() # ApiPostIssueForm | Post Issue Form

    try:
        # 创建一个 Issue。Create an issue.
        api_response = api_instance.create_issue(repo, post_issue_form)
        print("The response of IssuesApi->create_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->create_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **post_issue_form** | [**ApiPostIssueForm**](ApiPostIssueForm.md)| Post Issue Form | 

### Return type

[**ApiIssueDetail**](ApiIssueDetail.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_issue_label**
> ApiLabel delete_issue_label(repo, number, name)

删除 Issue 标签。Remove a label from an issue.

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
    api_instance = cnb_api.IssuesApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | number
    name = 'name_example' # str | label name

    try:
        # 删除 Issue 标签。Remove a label from an issue.
        api_response = api_instance.delete_issue_label(repo, number, name)
        print("The response of IssuesApi->delete_issue_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->delete_issue_label: %s\n" % e)
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

# **delete_issue_labels**
> delete_issue_labels(repo, number)

清空 Issue 标签。Remove all labels from an issue.

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
    api_instance = cnb_api.IssuesApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | number

    try:
        # 清空 Issue 标签。Remove all labels from an issue.
        api_instance.delete_issue_labels(repo, number)
    except Exception as e:
        print("Exception when calling IssuesApi->delete_issue_labels: %s\n" % e)
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

# **get_issue**
> ApiIssueDetail get_issue(repo, number)

查询指定的 Issues。Get an issue.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_issue_detail import ApiIssueDetail
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
    api_instance = cnb_api.IssuesApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | issue number

    try:
        # 查询指定的 Issues。Get an issue.
        api_response = api_instance.get_issue(repo, number)
        print("The response of IssuesApi->get_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->get_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **number** | **int**| issue number | 

### Return type

[**ApiIssueDetail**](ApiIssueDetail.md)

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

# **get_issue_comment**
> ApiIssueComment get_issue_comment(repo, number, comment_id)

获取一个 Issue Comment。Get an issue comment.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_issue_comment import ApiIssueComment
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
    api_instance = cnb_api.IssuesApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | number
    comment_id = 56 # int | comment_id

    try:
        # 获取一个 Issue Comment。Get an issue comment.
        api_response = api_instance.get_issue_comment(repo, number, comment_id)
        print("The response of IssuesApi->get_issue_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->get_issue_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **number** | **int**| number | 
 **comment_id** | **int**| comment_id | 

### Return type

[**ApiIssueComment**](ApiIssueComment.md)

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

# **list_issue_comments**
> List[ApiIssueComment] list_issue_comments(repo, number, page=page, page_size=page_size)

查询仓库的 Issue 评论列表。List repository issue comments.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_issue_comment import ApiIssueComment
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
    api_instance = cnb_api.IssuesApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | issue number
    page = 1 # int | pagination page number (optional) (default to 1)
    page_size = 30 # int | pagination page size (optional) (default to 30)

    try:
        # 查询仓库的 Issue 评论列表。List repository issue comments.
        api_response = api_instance.list_issue_comments(repo, number, page=page, page_size=page_size)
        print("The response of IssuesApi->list_issue_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->list_issue_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **number** | **int**| issue number | 
 **page** | **int**| pagination page number | [optional] [default to 1]
 **page_size** | **int**| pagination page size | [optional] [default to 30]

### Return type

[**List[ApiIssueComment]**](ApiIssueComment.md)

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

# **list_issue_labels**
> List[ApiLabel] list_issue_labels(repo, number, page=page, page_size=page_size)

查询 Issue 的标签(label) 列表。List labels for an issue.

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
    api_instance = cnb_api.IssuesApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | number
    page = 1 # int | pagination page number (optional) (default to 1)
    page_size = 30 # int | pagination page size (optional) (default to 30)

    try:
        # 查询 Issue 的标签(label) 列表。List labels for an issue.
        api_response = api_instance.list_issue_labels(repo, number, page=page, page_size=page_size)
        print("The response of IssuesApi->list_issue_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->list_issue_labels: %s\n" % e)
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

# **list_issues**
> List[ApiIssue] list_issues(repo, page=page, page_size=page_size, state=state, keyword=keyword, priority=priority, labels=labels, authors=authors, assignees=assignees, updated_time_begin=updated_time_begin, updated_time_end=updated_time_end, order_by=order_by)

查询仓库的 Issues。List issues.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_issue import ApiIssue
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
    api_instance = cnb_api.IssuesApi(api_client)
    repo = 'repo_example' # str | repo
    page = 1 # int | pagination page number (optional) (default to 1)
    page_size = 30 # int | pagination page size (optional) (default to 30)
    state = 'state_example' # str | issue state open or closed (optional)
    keyword = 'keyword_example' # str | issue search key (optional)
    priority = 'priority_example' # str | issue priority example: p0,p1,p2,p3 (optional)
    labels = 'labels_example' # str | issue labels example: git,bug,feature (optional)
    authors = 'authors_example' # str | issue authors name, example: 张三,李四 (optional)
    assignees = 'assignees_example' # str | issue assignees name, example: 张三,李四,-; - means assign to nobody (optional)
    updated_time_begin = 'updated_time_begin_example' # str | issue filter update time begin  example: 2022-01-31 (optional)
    updated_time_end = 'updated_time_end_example' # str | issue filter update time end,  example: 2022-01-31 (optional)
    order_by = 'order_by_example' # str | issue order, example: created_at, -updated_at, reference_count。‘-’ prefix means descending order (optional)

    try:
        # 查询仓库的 Issues。List issues.
        api_response = api_instance.list_issues(repo, page=page, page_size=page_size, state=state, keyword=keyword, priority=priority, labels=labels, authors=authors, assignees=assignees, updated_time_begin=updated_time_begin, updated_time_end=updated_time_end, order_by=order_by)
        print("The response of IssuesApi->list_issues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->list_issues: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **page** | **int**| pagination page number | [optional] [default to 1]
 **page_size** | **int**| pagination page size | [optional] [default to 30]
 **state** | **str**| issue state open or closed | [optional] 
 **keyword** | **str**| issue search key | [optional] 
 **priority** | **str**| issue priority example: p0,p1,p2,p3 | [optional] 
 **labels** | **str**| issue labels example: git,bug,feature | [optional] 
 **authors** | **str**| issue authors name, example: 张三,李四 | [optional] 
 **assignees** | **str**| issue assignees name, example: 张三,李四,-; - means assign to nobody | [optional] 
 **updated_time_begin** | **str**| issue filter update time begin  example: 2022-01-31 | [optional] 
 **updated_time_end** | **str**| issue filter update time end,  example: 2022-01-31 | [optional] 
 **order_by** | **str**| issue order, example: created_at, -updated_at, reference_count。‘-’ prefix means descending order | [optional] 

### Return type

[**List[ApiIssue]**](ApiIssue.md)

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

# **patch_issue_comment**
> ApiIssueComment patch_issue_comment(repo, number, comment_id, patch_issue_comment_form)

修改一个 Issue Comment。Update an issue comment.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_issue_comment import ApiIssueComment
from cnb_api.models.api_patch_issue_comment_form import ApiPatchIssueCommentForm
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
    api_instance = cnb_api.IssuesApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | number
    comment_id = 56 # int | comment_id
    patch_issue_comment_form = cnb_api.ApiPatchIssueCommentForm() # ApiPatchIssueCommentForm | Patch Issue Comment Form

    try:
        # 修改一个 Issue Comment。Update an issue comment.
        api_response = api_instance.patch_issue_comment(repo, number, comment_id, patch_issue_comment_form)
        print("The response of IssuesApi->patch_issue_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->patch_issue_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **number** | **int**| number | 
 **comment_id** | **int**| comment_id | 
 **patch_issue_comment_form** | [**ApiPatchIssueCommentForm**](ApiPatchIssueCommentForm.md)| Patch Issue Comment Form | 

### Return type

[**ApiIssueComment**](ApiIssueComment.md)

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

# **post_issue_comment**
> ApiIssueComment post_issue_comment(repo, number, post_issue_comment_form)

创建一个 Issue Comment。Create an issue comment.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_issue_comment import ApiIssueComment
from cnb_api.models.api_post_issue_comment_form import ApiPostIssueCommentForm
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
    api_instance = cnb_api.IssuesApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | number
    post_issue_comment_form = cnb_api.ApiPostIssueCommentForm() # ApiPostIssueCommentForm | Post Issue Comment Form

    try:
        # 创建一个 Issue Comment。Create an issue comment.
        api_response = api_instance.post_issue_comment(repo, number, post_issue_comment_form)
        print("The response of IssuesApi->post_issue_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->post_issue_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **number** | **int**| number | 
 **post_issue_comment_form** | [**ApiPostIssueCommentForm**](ApiPostIssueCommentForm.md)| Post Issue Comment Form | 

### Return type

[**ApiIssueComment**](ApiIssueComment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.cnb.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_issue_labels**
> ApiLabel post_issue_labels(repo, number, post_issue_labels_form)

新增 Issue 标签。Add labels to an issue.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_label import ApiLabel
from cnb_api.models.api_post_issue_labels_form import ApiPostIssueLabelsForm
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
    api_instance = cnb_api.IssuesApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | number
    post_issue_labels_form = cnb_api.ApiPostIssueLabelsForm() # ApiPostIssueLabelsForm | Post Issue Labels Form

    try:
        # 新增 Issue 标签。Add labels to an issue.
        api_response = api_instance.post_issue_labels(repo, number, post_issue_labels_form)
        print("The response of IssuesApi->post_issue_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->post_issue_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **number** | **int**| number | 
 **post_issue_labels_form** | [**ApiPostIssueLabelsForm**](ApiPostIssueLabelsForm.md)| Post Issue Labels Form | 

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

# **put_issue_labels**
> ApiLabel put_issue_labels(repo, number, put_issue_labels_form)

设置 Issue 标签。 Set the new labels for an issue.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_label import ApiLabel
from cnb_api.models.api_put_issue_labels_form import ApiPutIssueLabelsForm
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
    api_instance = cnb_api.IssuesApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | number
    put_issue_labels_form = cnb_api.ApiPutIssueLabelsForm() # ApiPutIssueLabelsForm | Put Issue Labels Form

    try:
        # 设置 Issue 标签。 Set the new labels for an issue.
        api_response = api_instance.put_issue_labels(repo, number, put_issue_labels_form)
        print("The response of IssuesApi->put_issue_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->put_issue_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **number** | **int**| number | 
 **put_issue_labels_form** | [**ApiPutIssueLabelsForm**](ApiPutIssueLabelsForm.md)| Put Issue Labels Form | 

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

# **update_issue**
> ApiIssueDetail update_issue(repo, number, patch_issue_form)

更新一个 Issue。Update an issue.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_issue_detail import ApiIssueDetail
from cnb_api.models.api_patch_issue_form import ApiPatchIssueForm
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
    api_instance = cnb_api.IssuesApi(api_client)
    repo = 'repo_example' # str | repo
    number = 56 # int | issue number
    patch_issue_form = cnb_api.ApiPatchIssueForm() # ApiPatchIssueForm | Patch Issue Form

    try:
        # 更新一个 Issue。Update an issue.
        api_response = api_instance.update_issue(repo, number, patch_issue_form)
        print("The response of IssuesApi->update_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->update_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **number** | **int**| issue number | 
 **patch_issue_form** | [**ApiPatchIssueForm**](ApiPatchIssueForm.md)| Patch Issue Form | 

### Return type

[**ApiIssueDetail**](ApiIssueDetail.md)

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

