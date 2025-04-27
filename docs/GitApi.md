# cnb_api.GitApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_blob**](GitApi.md#create_blob) | **POST** /{repo}/-/git/blobs | 创建一个 blob。Create a blob.
[**create_branch**](GitApi.md#create_branch) | **POST** /{repo}/-/git/branches | 创建新分支。Create a new branch based on a start point.
[**create_tag**](GitApi.md#create_tag) | **POST** /{repo}/-/git/tags | 创建一个 tag。Create a tag.
[**delete_branch**](GitApi.md#delete_branch) | **DELETE** /{repo}/-/git/branches/{branch} | 删除指定分支。Delete the specified branch.
[**delete_commit_annotation**](GitApi.md#delete_commit_annotation) | **DELETE** /{repo}/-/git/commit-annotations/{sha}/{key} | 删除指定 commit 的元数据。Delete commit annotation.
[**delete_commit_asset**](GitApi.md#delete_commit_asset) | **DELETE** /{repo}/-/git/commit-assets/{sha1}/{asset_id} | 删除指定 commit 的附件。Delete commit asset.
[**delete_tag**](GitApi.md#delete_tag) | **DELETE** /{repo}/-/git/tags/{tag} | 删除指定标签。Delete the specified tag.
[**delete_tag_annotation**](GitApi.md#delete_tag_annotation) | **DELETE** /{repo}/-/git/tag-annotations/{tag_with_key} | 删除指定 tag 的元数据。Delete the metadata of the specified tag.
[**get_archive_commit_changed_files**](GitApi.md#get_archive_commit_changed_files) | **GET** /{repo}/-/git/archive-commit-changed-files/{sha1} | 打包下载 commit 变更文件。Download archive of changed files for a commit.
[**get_archive_compare_changed_files**](GitApi.md#get_archive_compare_changed_files) | **GET** /{repo}/-/git/archive-compare-changed-files/{base_head} | 打包下载两次 ref 之间的变更文件。Download archive of changed files for a compare.
[**get_branch**](GitApi.md#get_branch) | **GET** /{repo}/-/git/branches/{branch} | 查询指定分支。Get a branch.
[**get_commit**](GitApi.md#get_commit) | **GET** /{repo}/-/git/commits/{ref} | 查询指定 commit。Get a commit.
[**get_commit_annotations**](GitApi.md#get_commit_annotations) | **GET** /{repo}/-/git/commit-annotations/{sha} | 查询指定 commit 的元数据。Get commit annotations.
[**get_commit_annotations_in_batch**](GitApi.md#get_commit_annotations_in_batch) | **POST** /{repo}/-/git/commit-annotations-in-batch | 查询指定 commit 的元数据。Get commit annotations in batch.
[**get_commit_assets_by_sha**](GitApi.md#get_commit_assets_by_sha) | **GET** /{repo}/-/git/commit-assets/{sha1} | 查询指定 commit 的附件。List commit assets.
[**get_commit_statuses**](GitApi.md#get_commit_statuses) | **GET** /{repo}/-/git/commit-statuses/{commitish} | 查询指定 commit 的 check statuses。List commit check statuses.
[**get_compare_commits**](GitApi.md#get_compare_commits) | **GET** /{repo}/-/git/compare/{base_head} | 对比 base...head。Compare two commits.
[**get_content**](GitApi.md#get_content) | **GET** /{repo}/-/git/contents/{file_path} | 查询仓库文件列表或文件。List repository files or file.
[**get_head**](GitApi.md#get_head) | **GET** /{repo}/-/git/head | 获取仓库默认分支。Get the default branch of the repository.
[**get_tag**](GitApi.md#get_tag) | **GET** /{repo}/-/git/tags/{tag} | 查询指定 Tag。Get a tag.
[**get_tag_annotations**](GitApi.md#get_tag_annotations) | **GET** /{repo}/-/git/tag-annotations/{tag} | 查询指定 tag 的元数据。Query the metadata of the specified tag.
[**list_branches**](GitApi.md#list_branches) | **GET** /{repo}/-/git/branches | 查询分支列表。List branches.
[**list_commits**](GitApi.md#list_commits) | **GET** /{repo}/-/git/commits | 查询 commit 列表。List commits.
[**list_tags**](GitApi.md#list_tags) | **GET** /{repo}/-/git/tags | 查询标签列表。List tags.
[**post_commit_asset_upload_confirmation**](GitApi.md#post_commit_asset_upload_confirmation) | **POST** /{repo}/-/git/commit-assets/{sha1}/asset-upload-confirmation/{token}/{asset_path} | 确认 Commit asset 上传完成。Confirm commit asset upload.
[**post_commit_asset_upload_url**](GitApi.md#post_commit_asset_upload_url) | **POST** /{repo}/-/git/commit-assets/{sha1}/asset-upload-url | 新增一个 Commit asset。Create a commit asset.
[**put_commit_annotations**](GitApi.md#put_commit_annotations) | **PUT** /{repo}/-/git/commit-annotations/{sha} | 设定指定 commit 的元数据。Put commit annotations.
[**put_tag_annotations**](GitApi.md#put_tag_annotations) | **PUT** /{repo}/-/git/tag-annotations/{tag} | 设定指定 tag 的元数据。Set the metadata of the specified tag.


# **create_blob**
> ApiBlob create_blob(repo, post_blob_form)

创建一个 blob。Create a blob.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_blob import ApiBlob
from cnb_api.models.api_post_blob_form import ApiPostBlobForm
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    post_blob_form = cnb_api.ApiPostBlobForm() # ApiPostBlobForm | PostBlobForm

    try:
        # 创建一个 blob。Create a blob.
        api_response = api_instance.create_blob(repo, post_blob_form)
        print("The response of GitApi->create_blob:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitApi->create_blob: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **post_blob_form** | [**ApiPostBlobForm**](ApiPostBlobForm.md)| PostBlobForm | 

### Return type

[**ApiBlob**](ApiBlob.md)

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

# **create_branch**
> create_branch(repo, create_branch_form)

创建新分支。Create a new branch based on a start point.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.openapi_create_branch_form import OpenapiCreateBranchForm
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    create_branch_form = cnb_api.OpenapiCreateBranchForm() # OpenapiCreateBranchForm | Create BranchDetail Form

    try:
        # 创建新分支。Create a new branch based on a start point.
        api_instance.create_branch(repo, create_branch_form)
    except Exception as e:
        print("Exception when calling GitApi->create_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **create_branch_form** | [**OpenapiCreateBranchForm**](OpenapiCreateBranchForm.md)| Create BranchDetail Form | 

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
**201** | Created |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tag**
> ApiTag create_tag(repo, post_tag_form)

创建一个 tag。Create a tag.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_post_tag_from import ApiPostTagFrom
from cnb_api.models.api_tag import ApiTag
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    post_tag_form = cnb_api.ApiPostTagFrom() # ApiPostTagFrom | PostTagFrom

    try:
        # 创建一个 tag。Create a tag.
        api_response = api_instance.create_tag(repo, post_tag_form)
        print("The response of GitApi->create_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitApi->create_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **post_tag_form** | [**ApiPostTagFrom**](ApiPostTagFrom.md)| PostTagFrom | 

### Return type

[**ApiTag**](ApiTag.md)

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

# **delete_branch**
> delete_branch(repo, branch)

删除指定分支。Delete the specified branch.

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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    branch = 'branch_example' # str | branch name

    try:
        # 删除指定分支。Delete the specified branch.
        api_instance.delete_branch(repo, branch)
    except Exception as e:
        print("Exception when calling GitApi->delete_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **branch** | **str**| branch name | 

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

# **delete_commit_annotation**
> delete_commit_annotation(repo, sha, key)

删除指定 commit 的元数据。Delete commit annotation.

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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    sha = 'sha_example' # str | commit hash
    key = 'key_example' # str | commit annotation key

    try:
        # 删除指定 commit 的元数据。Delete commit annotation.
        api_instance.delete_commit_annotation(repo, sha, key)
    except Exception as e:
        print("Exception when calling GitApi->delete_commit_annotation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **sha** | **str**| commit hash | 
 **key** | **str**| commit annotation key | 

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

# **delete_commit_asset**
> delete_commit_asset(repo, sha1, asset_id)

删除指定 commit 的附件。Delete commit asset.

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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    sha1 = 'sha1_example' # str | sha
    asset_id = 56 # int | asset id

    try:
        # 删除指定 commit 的附件。Delete commit asset.
        api_instance.delete_commit_asset(repo, sha1, asset_id)
    except Exception as e:
        print("Exception when calling GitApi->delete_commit_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **sha1** | **str**| sha | 
 **asset_id** | **int**| asset id | 

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

# **delete_tag**
> delete_tag(repo, tag)

删除指定标签。Delete the specified tag.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-contents:rw

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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    tag = 'tag_example' # str | tag name

    try:
        # 删除指定标签。Delete the specified tag.
        api_instance.delete_tag(repo, tag)
    except Exception as e:
        print("Exception when calling GitApi->delete_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **tag** | **str**| tag name | 

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

# **delete_tag_annotation**
> delete_tag_annotation(repo, tag_with_key)

删除指定 tag 的元数据。Delete the metadata of the specified tag.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-contents:rw

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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    tag_with_key = 'tag_with_key_example' # str | tag with key

    try:
        # 删除指定 tag 的元数据。Delete the metadata of the specified tag.
        api_instance.delete_tag_annotation(repo, tag_with_key)
    except Exception as e:
        print("Exception when calling GitApi->delete_tag_annotation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **tag_with_key** | **str**| tag with key | 

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

# **get_archive_commit_changed_files**
> get_archive_commit_changed_files(repo, sha1)

打包下载 commit 变更文件。Download archive of changed files for a commit.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:r

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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    sha1 = 'sha1_example' # str | commit sha

    try:
        # 打包下载 commit 变更文件。Download archive of changed files for a commit.
        api_instance.get_archive_commit_changed_files(repo, sha1)
    except Exception as e:
        print("Exception when calling GitApi->get_archive_commit_changed_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **sha1** | **str**| commit sha | 

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_archive_compare_changed_files**
> get_archive_compare_changed_files(repo, base_head)

打包下载两次 ref 之间的变更文件。Download archive of changed files for a compare.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:r

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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    base_head = 'base_head_example' # str | base...head

    try:
        # 打包下载两次 ref 之间的变更文件。Download archive of changed files for a compare.
        api_instance.get_archive_compare_changed_files(repo, base_head)
    except Exception as e:
        print("Exception when calling GitApi->get_archive_compare_changed_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **base_head** | **str**| base...head | 

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branch**
> ApiBranchDetail get_branch(repo, branch)

查询指定分支。Get a branch.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_branch_detail import ApiBranchDetail
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    branch = 'branch_example' # str | branch name

    try:
        # 查询指定分支。Get a branch.
        api_response = api_instance.get_branch(repo, branch)
        print("The response of GitApi->get_branch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitApi->get_branch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **branch** | **str**| branch name | 

### Return type

[**ApiBranchDetail**](ApiBranchDetail.md)

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

# **get_commit**
> ApiCommit get_commit(repo, ref)

查询指定 commit。Get a commit.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_commit import ApiCommit
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    ref = 'ref_example' # str | ref

    try:
        # 查询指定 commit。Get a commit.
        api_response = api_instance.get_commit(repo, ref)
        print("The response of GitApi->get_commit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitApi->get_commit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **ref** | **str**| ref | 

### Return type

[**ApiCommit**](ApiCommit.md)

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

# **get_commit_annotations**
> List[WebCommitAnnotation] get_commit_annotations(repo, sha)

查询指定 commit 的元数据。Get commit annotations.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.web_commit_annotation import WebCommitAnnotation
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    sha = 'sha_example' # str | commit hash

    try:
        # 查询指定 commit 的元数据。Get commit annotations.
        api_response = api_instance.get_commit_annotations(repo, sha)
        print("The response of GitApi->get_commit_annotations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitApi->get_commit_annotations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **sha** | **str**| commit hash | 

### Return type

[**List[WebCommitAnnotation]**](WebCommitAnnotation.md)

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

# **get_commit_annotations_in_batch**
> List[WebCommitAnnotationInBatch] get_commit_annotations_in_batch(repo, get_commit_annotations_form)

查询指定 commit 的元数据。Get commit annotations in batch.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.web_commit_annotation_in_batch import WebCommitAnnotationInBatch
from cnb_api.models.web_get_commit_annotations_in_batch_form import WebGetCommitAnnotationsInBatchForm
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    get_commit_annotations_form = cnb_api.WebGetCommitAnnotationsInBatchForm() # WebGetCommitAnnotationsInBatchForm | Get Commit Annotations In Batch Form

    try:
        # 查询指定 commit 的元数据。Get commit annotations in batch.
        api_response = api_instance.get_commit_annotations_in_batch(repo, get_commit_annotations_form)
        print("The response of GitApi->get_commit_annotations_in_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitApi->get_commit_annotations_in_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **get_commit_annotations_form** | [**WebGetCommitAnnotationsInBatchForm**](WebGetCommitAnnotationsInBatchForm.md)| Get Commit Annotations In Batch Form | 

### Return type

[**List[WebCommitAnnotationInBatch]**](WebCommitAnnotationInBatch.md)

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

# **get_commit_assets_by_sha**
> List[ApiCommitAsset] get_commit_assets_by_sha(repo, sha1)

查询指定 commit 的附件。List commit assets.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_commit_asset import ApiCommitAsset
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    sha1 = 'sha1_example' # str | sha

    try:
        # 查询指定 commit 的附件。List commit assets.
        api_response = api_instance.get_commit_assets_by_sha(repo, sha1)
        print("The response of GitApi->get_commit_assets_by_sha:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitApi->get_commit_assets_by_sha: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **sha1** | **str**| sha | 

### Return type

[**List[ApiCommitAsset]**](ApiCommitAsset.md)

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

# **get_commit_statuses**
> List[ApiCommitStatus] get_commit_statuses(repo, commitish)

查询指定 commit 的 check statuses。List commit check statuses.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_commit_status import ApiCommitStatus
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    commitish = 'commitish_example' # str | commitish

    try:
        # 查询指定 commit 的 check statuses。List commit check statuses.
        api_response = api_instance.get_commit_statuses(repo, commitish)
        print("The response of GitApi->get_commit_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitApi->get_commit_statuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **commitish** | **str**| commitish | 

### Return type

[**List[ApiCommitStatus]**](ApiCommitStatus.md)

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

# **get_compare_commits**
> ApiCompareResponse get_compare_commits(repo, base_head)

对比 base...head。Compare two commits.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_compare_response import ApiCompareResponse
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    base_head = 'base_head_example' # str | base...head

    try:
        # 对比 base...head。Compare two commits.
        api_response = api_instance.get_compare_commits(repo, base_head)
        print("The response of GitApi->get_compare_commits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitApi->get_compare_commits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **base_head** | **str**| base...head | 

### Return type

[**ApiCompareResponse**](ApiCompareResponse.md)

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

# **get_content**
> ApiContent get_content(repo, file_path, ref=ref)

查询仓库文件列表或文件。List repository files or file.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_content import ApiContent
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    file_path = 'file_path_example' # str | path
    ref = 'ref_example' # str | ref (optional)

    try:
        # 查询仓库文件列表或文件。List repository files or file.
        api_response = api_instance.get_content(repo, file_path, ref=ref)
        print("The response of GitApi->get_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitApi->get_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **file_path** | **str**| path | 
 **ref** | **str**| ref | [optional] 

### Return type

[**ApiContent**](ApiContent.md)

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

# **get_head**
> OpenapiHeadRef get_head(repo)

获取仓库默认分支。Get the default branch of the repository.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.openapi_head_ref import OpenapiHeadRef
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo

    try:
        # 获取仓库默认分支。Get the default branch of the repository.
        api_response = api_instance.get_head(repo)
        print("The response of GitApi->get_head:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitApi->get_head: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 

### Return type

[**OpenapiHeadRef**](OpenapiHeadRef.md)

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

# **get_tag**
> ApiTag get_tag(repo, tag)

查询指定 Tag。Get a tag.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-contents:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_tag import ApiTag
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    tag = 'tag_example' # str | tag name

    try:
        # 查询指定 Tag。Get a tag.
        api_response = api_instance.get_tag(repo, tag)
        print("The response of GitApi->get_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitApi->get_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **tag** | **str**| tag name | 

### Return type

[**ApiTag**](ApiTag.md)

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

# **get_tag_annotations**
> List[WebTagAnnotation] get_tag_annotations(repo, tag)

查询指定 tag 的元数据。Query the metadata of the specified tag.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-contents:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.web_tag_annotation import WebTagAnnotation
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    tag = 'tag_example' # str | tag

    try:
        # 查询指定 tag 的元数据。Query the metadata of the specified tag.
        api_response = api_instance.get_tag_annotations(repo, tag)
        print("The response of GitApi->get_tag_annotations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitApi->get_tag_annotations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **tag** | **str**| tag | 

### Return type

[**List[WebTagAnnotation]**](WebTagAnnotation.md)

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

# **list_branches**
> List[ApiBranch] list_branches(repo, page=page, page_size=page_size)

查询分支列表。List branches.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_branch import ApiBranch
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    page = 1 # int | pagination page number (optional) (default to 1)
    page_size = 30 # int | pagination page size (optional) (default to 30)

    try:
        # 查询分支列表。List branches.
        api_response = api_instance.list_branches(repo, page=page, page_size=page_size)
        print("The response of GitApi->list_branches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitApi->list_branches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **page** | **int**| pagination page number | [optional] [default to 1]
 **page_size** | **int**| pagination page size | [optional] [default to 30]

### Return type

[**List[ApiBranch]**](ApiBranch.md)

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

# **list_commits**
> List[ApiCommit] list_commits(repo, sha=sha, author=author, committer=committer, since=since, until=until, page=page, page_size=page_size)

查询 commit 列表。List commits.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_commit import ApiCommit
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    sha = 'sha_example' # str | sha or branch (optional)
    author = 'author_example' # str | commit author pattern (optional)
    committer = 'committer_example' # str | commit committer pattern (optional)
    since = 'since_example' # str | commit since (optional)
    until = 'until_example' # str | commit until (optional)
    page = 1 # int | pagination page number (optional) (default to 1)
    page_size = 30 # int | pagination page size (optional) (default to 30)

    try:
        # 查询 commit 列表。List commits.
        api_response = api_instance.list_commits(repo, sha=sha, author=author, committer=committer, since=since, until=until, page=page, page_size=page_size)
        print("The response of GitApi->list_commits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitApi->list_commits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **sha** | **str**| sha or branch | [optional] 
 **author** | **str**| commit author pattern | [optional] 
 **committer** | **str**| commit committer pattern | [optional] 
 **since** | **str**| commit since | [optional] 
 **until** | **str**| commit until | [optional] 
 **page** | **int**| pagination page number | [optional] [default to 1]
 **page_size** | **int**| pagination page size | [optional] [default to 30]

### Return type

[**List[ApiCommit]**](ApiCommit.md)

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

# **list_tags**
> List[ApiTag] list_tags(repo, page=page, page_size=page_size)

查询标签列表。List tags.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-contents:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.api_tag import ApiTag
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    page = 1 # int | pagination page number (optional) (default to 1)
    page_size = 30 # int | pagination page size (optional) (default to 30)

    try:
        # 查询标签列表。List tags.
        api_response = api_instance.list_tags(repo, page=page, page_size=page_size)
        print("The response of GitApi->list_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitApi->list_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **page** | **int**| pagination page number | [optional] [default to 1]
 **page_size** | **int**| pagination page size | [optional] [default to 30]

### Return type

[**List[ApiTag]**](ApiTag.md)

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

# **post_commit_asset_upload_confirmation**
> post_commit_asset_upload_confirmation(repo, sha1, token, asset_path)

确认 Commit asset 上传完成。Confirm commit asset upload.

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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    sha1 = 56 # int | sha
    token = 'token_example' # str | upload token
    asset_path = 'asset_path_example' # str | release asset path

    try:
        # 确认 Commit asset 上传完成。Confirm commit asset upload.
        api_instance.post_commit_asset_upload_confirmation(repo, sha1, token, asset_path)
    except Exception as e:
        print("Exception when calling GitApi->post_commit_asset_upload_confirmation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **sha1** | **int**| sha | 
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

# **post_commit_asset_upload_url**
> OpenapiCommitAssetUploadURL post_commit_asset_upload_url(repo, sha1, create_commit_asset_upload_url_form)

新增一个 Commit asset。Create a commit asset.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.openapi_commit_asset_upload_url import OpenapiCommitAssetUploadURL
from cnb_api.models.openapi_post_commit_asset_upload_url_form import OpenapiPostCommitAssetUploadURLForm
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    sha1 = 56 # int | sha
    create_commit_asset_upload_url_form = cnb_api.OpenapiPostCommitAssetUploadURLForm() # OpenapiPostCommitAssetUploadURLForm | Post Commit Asset Upload URL Form

    try:
        # 新增一个 Commit asset。Create a commit asset.
        api_response = api_instance.post_commit_asset_upload_url(repo, sha1, create_commit_asset_upload_url_form)
        print("The response of GitApi->post_commit_asset_upload_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitApi->post_commit_asset_upload_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **sha1** | **int**| sha | 
 **create_commit_asset_upload_url_form** | [**OpenapiPostCommitAssetUploadURLForm**](OpenapiPostCommitAssetUploadURLForm.md)| Post Commit Asset Upload URL Form | 

### Return type

[**OpenapiCommitAssetUploadURL**](OpenapiCommitAssetUploadURL.md)

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

# **put_commit_annotations**
> put_commit_annotations(repo, sha, put_commit_annotations_form)

设定指定 commit 的元数据。Put commit annotations.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-code:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.openapi_put_commit_annotations_form import OpenapiPutCommitAnnotationsForm
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    sha = 'sha_example' # str | commit hash
    put_commit_annotations_form = cnb_api.OpenapiPutCommitAnnotationsForm() # OpenapiPutCommitAnnotationsForm | Put Commit Annotations Form

    try:
        # 设定指定 commit 的元数据。Put commit annotations.
        api_instance.put_commit_annotations(repo, sha, put_commit_annotations_form)
    except Exception as e:
        print("Exception when calling GitApi->put_commit_annotations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **sha** | **str**| commit hash | 
 **put_commit_annotations_form** | [**OpenapiPutCommitAnnotationsForm**](OpenapiPutCommitAnnotationsForm.md)| Put Commit Annotations Form | 

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

# **put_tag_annotations**
> put_tag_annotations(repo, tag, put_tag_annotations_form)

设定指定 tag 的元数据。Set the metadata of the specified tag.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-contents:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.openapi_put_tag_annotations_form import OpenapiPutTagAnnotationsForm
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
    api_instance = cnb_api.GitApi(api_client)
    repo = 'repo_example' # str | repo
    tag = 'tag_example' # str | tag
    put_tag_annotations_form = cnb_api.OpenapiPutTagAnnotationsForm() # OpenapiPutTagAnnotationsForm | Put Tag Annotations Form

    try:
        # 设定指定 tag 的元数据。Set the metadata of the specified tag.
        api_instance.put_tag_annotations(repo, tag, put_tag_annotations_form)
    except Exception as e:
        print("Exception when calling GitApi->put_tag_annotations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **tag** | **str**| tag | 
 **put_tag_annotations_form** | [**OpenapiPutTagAnnotationsForm**](OpenapiPutTagAnnotationsForm.md)| Put Tag Annotations Form | 

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

