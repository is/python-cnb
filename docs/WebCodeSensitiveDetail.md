# WebCodeSensitiveDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | 问题创建时间 | [optional] 
**cs_sub_type** | [**WebIssueType**](WebIssueType.md) | 问题子类型 | [optional] 
**cs_type** | [**WebIssueType**](WebIssueType.md) | 问题类型 | [optional] 
**file_name** | **str** | 包含问题的文件名 | [optional] 
**file_path** | **str** | 包含问题的文件路径 | [optional] 
**handler** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) | 忽略人(平台信息) | [optional] 
**id** | **str** | 问题id | [optional] 
**ignore_reason** | **str** | 忽略原因 | [optional] 
**ignored_at** | **str** | 忽略时间 | [optional] 
**issue_detail** | [**List[WebCSDetail]**](WebCSDetail.md) | 问题详情 | [optional] 
**line_no** | **List[int]** | 问题行号 | [optional] 
**occur_version** | **str** | 问题发生版本 | [optional] 
**owner** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) | 问题责任人(平台信息) | [optional] 
**raw_author** | [**WebRawAuthor**](WebRawAuthor.md) | 问题责任人原生git信息 | [optional] 
**reopen_at** | **str** | 重新开启时间 | [optional] 
**reopen_handler** | [**GitWoaComCnbMonorepoGitInternalDtoWebUserInfo**](GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.md) | 重新开启人 | [optional] 
**revision** | **str** | 问题所在版本 | [optional] 
**risk_level** | **str** | 问题等级 | [optional] 
**state** | **str** | 问题状态 开启/忽略 | [optional] 
**tool** | **str** | 扫描工具 | [optional] 

## Example

```python
from cnb_api.models.web_code_sensitive_detail import WebCodeSensitiveDetail

# TODO update the JSON string below
json = "{}"
# create an instance of WebCodeSensitiveDetail from a JSON string
web_code_sensitive_detail_instance = WebCodeSensitiveDetail.from_json(json)
# print the JSON string representation of the object
print(WebCodeSensitiveDetail.to_json())

# convert the object into a dict
web_code_sensitive_detail_dict = web_code_sensitive_detail_instance.to_dict()
# create an instance of WebCodeSensitiveDetail from a dict
web_code_sensitive_detail_from_dict = WebCodeSensitiveDetail.from_dict(web_code_sensitive_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


