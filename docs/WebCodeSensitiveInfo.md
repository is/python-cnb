# WebCodeSensitiveInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | 问题创建时间 | [optional] 
**file_name** | **str** | 包含问题的文件名 | [optional] 
**file_path** | **str** | 包含问题的文件路径 | [optional] 
**id** | **str** | 问题id | [optional] 
**issue_type** | **str** | 问题类型 | [optional] 
**occur_version** | **str** | 问题发生版本 | [optional] 
**owner** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) | 问题责任人(平台信息) | [optional] 
**raw_author** | [**WebRawAuthor**](WebRawAuthor.md) | 问题责任人原生git信息 | [optional] 
**repo_id** | **str** | 仓库id | [optional] 
**revision** | **str** | 问题所在版本 | [optional] 
**risk_level** | **str** | 问题等级 | [optional] 
**state** | **str** | 问题状态 开启/忽略 | [optional] 
**tool** | **str** | 扫描工具 | [optional] 

## Example

```python
from cnb_api.models.web_code_sensitive_info import WebCodeSensitiveInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WebCodeSensitiveInfo from a JSON string
web_code_sensitive_info_instance = WebCodeSensitiveInfo.from_json(json)
# print the JSON string representation of the object
print(WebCodeSensitiveInfo.to_json())

# convert the object into a dict
web_code_sensitive_info_dict = web_code_sensitive_info_instance.to_dict()
# create an instance of WebCodeSensitiveInfo from a dict
web_code_sensitive_info_from_dict = WebCodeSensitiveInfo.from_dict(web_code_sensitive_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


