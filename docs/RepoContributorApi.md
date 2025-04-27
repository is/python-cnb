# cnb_api.RepoContributorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_repo_contributor_trend**](RepoContributorApi.md#get_repo_contributor_trend) | **GET** /{repo}/-/contributor/trend | 查询仓库贡献者前 100 名的详细趋势数据。Query detailed trend data for top 100 contributors of the repository.


# **get_repo_contributor_trend**
> WebRepoContribTrend get_repo_contributor_trend(repo, limit=limit, exclude_external_users=exclude_external_users)

查询仓库贡献者前 100 名的详细趋势数据。Query detailed trend data for top 100 contributors of the repository.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.web_repo_contrib_trend import WebRepoContribTrend
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
    api_instance = cnb_api.RepoContributorApi(api_client)
    repo = 'repo_example' # str | slug
    limit = 14 # int | limit, 0~100 (optional) (default to 14)
    exclude_external_users = False # bool | exclude_external_users, true|false (optional) (default to False)

    try:
        # 查询仓库贡献者前 100 名的详细趋势数据。Query detailed trend data for top 100 contributors of the repository.
        api_response = api_instance.get_repo_contributor_trend(repo, limit=limit, exclude_external_users=exclude_external_users)
        print("The response of RepoContributorApi->get_repo_contributor_trend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepoContributorApi->get_repo_contributor_trend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| slug | 
 **limit** | **int**| limit, 0~100 | [optional] [default to 14]
 **exclude_external_users** | **bool**| exclude_external_users, true|false | [optional] [default to False]

### Return type

[**WebRepoContribTrend**](WebRepoContribTrend.md)

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

