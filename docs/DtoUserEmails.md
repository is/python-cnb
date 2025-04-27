# DtoUserEmails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_email** | **str** | ContactEmail 用户通知邮箱 | [optional] 
**email** | **str** | Email 用户git提交邮箱，是 emails 里面的某一个 | [optional] 
**emails** | **List[str]** | Emails 邮箱列表 | [optional] 
**system_email** | **str** | 系统默认邮箱 | [optional] 
**system_email_contact** | **bool** | 系统默认邮箱是否可以通知 | [optional] 

## Example

```python
from cnb_api.models.dto_user_emails import DtoUserEmails

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUserEmails from a JSON string
dto_user_emails_instance = DtoUserEmails.from_json(json)
# print the JSON string representation of the object
print(DtoUserEmails.to_json())

# convert the object into a dict
dto_user_emails_dict = dto_user_emails_instance.to_dict()
# create an instance of DtoUserEmails from a dict
dto_user_emails_from_dict = DtoUserEmails.from_dict(dto_user_emails_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


