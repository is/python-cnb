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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cnb_api.models.constant_visibility import ConstantVisibility
from cnb_api.models.dto_repos4_user_base import DtoRepos4UserBase
from typing import Optional, Set
from typing_extensions import Self

class DtoActivityCreateRepoDetail(BaseModel):
    """
    DtoActivityCreateRepoDetail
    """ # noqa: E501
    create_at: Optional[StrictStr] = None
    detail: Optional[DtoRepos4UserBase] = Field(default=None, description="公仓转私仓或仓库被删除后为 null")
    exposed_repo_path: Optional[StrictStr] = Field(default=None, description="activity 发生时仓库的 path，这时的 path 是可以公开的")
    freeze: Optional[StrictBool] = Field(default=None, description="仓库是否封禁")
    repo_unaccessible: Optional[StrictBool] = Field(default=None, description="仓库是否不可访问（公仓转私仓或仓库被删除后不可访问）")
    visibility_level: Optional[ConstantVisibility] = Field(default=None, description="仓库可见性")
    __properties: ClassVar[List[str]] = ["create_at", "detail", "exposed_repo_path", "freeze", "repo_unaccessible", "visibility_level"]

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
        """Create an instance of DtoActivityCreateRepoDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of detail
        if self.detail:
            _dict['detail'] = self.detail.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DtoActivityCreateRepoDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "create_at": obj.get("create_at"),
            "detail": DtoRepos4UserBase.from_dict(obj["detail"]) if obj.get("detail") is not None else None,
            "exposed_repo_path": obj.get("exposed_repo_path"),
            "freeze": obj.get("freeze"),
            "repo_unaccessible": obj.get("repo_unaccessible"),
            "visibility_level": obj.get("visibility_level")
        })
        return _obj


