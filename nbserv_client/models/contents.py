# coding: utf-8

"""
    Jupyter Server API

    Server API

    The version of the OpenAPI document: 5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Contents(BaseModel):
    """
    A contents object.  The content and format keys may be null if content is not contained. The hash maybe null if hash is not required.  If type is 'file', then the mimetype will be null.
    """ # noqa: E501
    name: StrictStr = Field(description="Name of file or directory, equivalent to the last part of the path")
    path: StrictStr = Field(description="Full path for file or directory")
    type: StrictStr = Field(description="Type of content")
    writable: StrictBool = Field(description="indicates whether the requester has permission to edit the file")
    created: StrictStr = Field(description="Creation timestamp")
    last_modified: StrictStr = Field(description="Last modified timestamp")
    size: Optional[StrictInt] = Field(default=None, description="The size of the file or notebook in bytes. If no size is provided, defaults to null.")
    mimetype: Optional[StrictStr] = Field(description="The mimetype of a file.  If content is not null, and type is 'file', this will contain the mimetype of the file, otherwise this will be null.")
    content: List[Dict] = Field(description="The content, if requested (otherwise null).  Will be an array if type is 'directory'")
    format: StrictStr = Field(description="Format of content (one of null, 'text', 'base64', 'json')")
    hash: Optional[StrictStr] = Field(default=None, description="[optional] The hexdigest hash string of content, if requested (otherwise null). It cannot be null if hash_algorithm is defined.")
    hash_algorithm: Optional[StrictStr] = Field(default=None, description="[optional] The algorithm used to produce the hash, if requested (otherwise null). It cannot be null if hash is defined.")
    __properties: ClassVar[List[str]] = ["name", "path", "type", "writable", "created", "last_modified", "size", "mimetype", "content", "format", "hash", "hash_algorithm"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('directory', 'file', 'notebook'):
            raise ValueError("must be one of enum values ('directory', 'file', 'notebook')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Contents from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Contents from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "path": obj.get("path"),
            "type": obj.get("type"),
            "writable": obj.get("writable"),
            "created": obj.get("created"),
            "last_modified": obj.get("last_modified"),
            "size": obj.get("size"),
            "mimetype": obj.get("mimetype"),
            "content": obj.get("content"),
            "format": obj.get("format"),
            "hash": obj.get("hash"),
            "hash_algorithm": obj.get("hash_algorithm")
        })
        return _obj


