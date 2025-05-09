# coding: utf-8

"""
    CNB OPENAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Contact: cnb@tencent.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cnb_api.models.git_woa_com_cnb_monorepo_git_internal_dto_web_user_info import GitWoaComCnbMonorepoGitInternalDtoWebUserInfo
from typing import Optional, Set
from typing_extensions import Self

class WebIssueActivity(BaseModel):
    """
    WebIssueActivity
    """ # noqa: E501
    actor: Optional[GitWoaComCnbMonorepoGitInternalDtoWebUserInfo] = None
    actor_access_role: Optional[StrictStr] = None
    actor_meta: Optional[List[StrictInt]] = None
    created_at: Optional[StrictStr] = None
    payload: Optional[Dict[str, Any]] = None
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["actor", "actor_access_role", "actor_meta", "created_at", "payload", "type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of WebIssueActivity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of actor
        if self.actor:
            _dict['actor'] = self.actor.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebIssueActivity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actor": GitWoaComCnbMonorepoGitInternalDtoWebUserInfo.from_dict(obj["actor"]) if obj.get("actor") is not None else None,
            "actor_access_role": obj.get("actor_access_role"),
            "actor_meta": obj.get("actor_meta"),
            "created_at": obj.get("created_at"),
            "payload": obj.get("payload"),
            "type": obj.get("type")
        })
        return _obj


