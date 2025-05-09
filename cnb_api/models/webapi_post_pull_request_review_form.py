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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cnb_api.models.webapi_post_pull_request_review_comment_form import WebapiPostPullRequestReviewCommentForm
from typing import Optional, Set
from typing_extensions import Self

class WebapiPostPullRequestReviewForm(BaseModel):
    """
    WebapiPostPullRequestReviewForm
    """ # noqa: E501
    body: Optional[StrictStr] = None
    comment: Optional[WebapiPostPullRequestReviewCommentForm] = None
    event: Optional[StrictStr] = Field(default=None, description="comment, approve, request_changes or \"\"")
    __properties: ClassVar[List[str]] = ["body", "comment", "event"]

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
        """Create an instance of WebapiPostPullRequestReviewForm from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of comment
        if self.comment:
            _dict['comment'] = self.comment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebapiPostPullRequestReviewForm from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "body": obj.get("body"),
            "comment": WebapiPostPullRequestReviewCommentForm.from_dict(obj["comment"]) if obj.get("comment") is not None else None,
            "event": obj.get("event")
        })
        return _obj


