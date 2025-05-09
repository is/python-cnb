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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from cnb_api.models.constant_slug_type import ConstantSlugType
from cnb_api.models.dto_resource_group import DtoResourceGroup
from cnb_api.models.dto_resource_mission import DtoResourceMission
from cnb_api.models.dto_resource_registry import DtoResourceRegistry
from cnb_api.models.dto_resource_repo import DtoResourceRepo
from typing import Optional, Set
from typing_extensions import Self

class DtoResources(BaseModel):
    """
    DtoResources
    """ # noqa: E501
    group: Optional[DtoResourceGroup] = None
    mission: Optional[DtoResourceMission] = None
    registry: Optional[DtoResourceRegistry] = None
    repo: Optional[DtoResourceRepo] = None
    type: Optional[ConstantSlugType] = None
    __properties: ClassVar[List[str]] = ["group", "mission", "registry", "repo", "type"]

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
        """Create an instance of DtoResources from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mission
        if self.mission:
            _dict['mission'] = self.mission.to_dict()
        # override the default output from pydantic by calling `to_dict()` of registry
        if self.registry:
            _dict['registry'] = self.registry.to_dict()
        # override the default output from pydantic by calling `to_dict()` of repo
        if self.repo:
            _dict['repo'] = self.repo.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DtoResources from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "group": DtoResourceGroup.from_dict(obj["group"]) if obj.get("group") is not None else None,
            "mission": DtoResourceMission.from_dict(obj["mission"]) if obj.get("mission") is not None else None,
            "registry": DtoResourceRegistry.from_dict(obj["registry"]) if obj.get("registry") is not None else None,
            "repo": DtoResourceRepo.from_dict(obj["repo"]) if obj.get("repo") is not None else None,
            "type": obj.get("type")
        })
        return _obj


