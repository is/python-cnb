# cnb_api.RepoLabelsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_label**](RepoLabelsApi.md#delete_label) | **DELETE** /{repo}/-/labels/{name} | 删除指定的仓库标签 label。Delete the specified repository label.
[**list_labels**](RepoLabelsApi.md#list_labels) | **GET** /{repo}/-/labels | 查询仓库的标签(label) 列表。List repository labels.
[**patch_label**](RepoLabelsApi.md#patch_label) | **PATCH** /{repo}/-/labels/{name} | 更新标签信息。Update label information.
[**post_label**](RepoLabelsApi.md#post_label) | **POST** /{repo}/-/labels | 创建一个 标签。Create a label.


# **delete_label**
> delete_label(repo, name)

删除指定的仓库标签 label。Delete the specified repository label.

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
    api_instance = cnb_api.RepoLabelsApi(api_client)
    repo = 'repo_example' # str | repo
    name = 'name_example' # str | label name

    try:
        # 删除指定的仓库标签 label。Delete the specified repository label.
        api_instance.delete_label(repo, name)
    except Exception as e:
        print("Exception when calling RepoLabelsApi->delete_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **name** | **str**| label name | 

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

# **list_labels**
> List[ApiLabel] list_labels(repo, page=page, page_size=page_size, keyword=keyword)

查询仓库的标签(label) 列表。List repository labels.

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
    api_instance = cnb_api.RepoLabelsApi(api_client)
    repo = 'repo_example' # str | repo
    page = 1 # int | pagination page number (optional) (default to 1)
    page_size = 30 # int | pagination page size (optional) (default to 30)
    keyword = 'keyword_example' # str | label search key (optional)

    try:
        # 查询仓库的标签(label) 列表。List repository labels.
        api_response = api_instance.list_labels(repo, page=page, page_size=page_size, keyword=keyword)
        print("The response of RepoLabelsApi->list_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepoLabelsApi->list_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **page** | **int**| pagination page number | [optional] [default to 1]
 **page_size** | **int**| pagination page size | [optional] [default to 30]
 **keyword** | **str**| label search key | [optional] 

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

# **patch_label**
> ApiLabel patch_label(repo, name, patch_label_form)

更新标签信息。Update label information.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_label import ApiLabel
from cnb_api.models.api_patch_label_form import ApiPatchLabelForm
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
    api_instance = cnb_api.RepoLabelsApi(api_client)
    repo = 'repo_example' # str | repo
    name = 'name_example' # str | label name
    patch_label_form = cnb_api.ApiPatchLabelForm() # ApiPatchLabelForm | Patch Label Form

    try:
        # 更新标签信息。Update label information.
        api_response = api_instance.patch_label(repo, name, patch_label_form)
        print("The response of RepoLabelsApi->patch_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepoLabelsApi->patch_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **name** | **str**| label name | 
 **patch_label_form** | [**ApiPatchLabelForm**](ApiPatchLabelForm.md)| Patch Label Form | 

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

# **post_label**
> ApiLabel post_label(repo, post_label_form)

创建一个 标签。Create a label.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-notes:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_label import ApiLabel
from cnb_api.models.api_post_label_form import ApiPostLabelForm
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
    api_instance = cnb_api.RepoLabelsApi(api_client)
    repo = 'repo_example' # str | repo
    post_label_form = cnb_api.ApiPostLabelForm() # ApiPostLabelForm | Post Label Form

    try:
        # 创建一个 标签。Create a label.
        api_response = api_instance.post_label(repo, post_label_form)
        print("The response of RepoLabelsApi->post_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepoLabelsApi->post_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **post_label_form** | [**ApiPostLabelForm**](ApiPostLabelForm.md)| Post Label Form | 

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
**201** | Created |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

