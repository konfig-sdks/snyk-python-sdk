# coding: utf-8

"""
    Snyk API

    Missing description placeholder

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredVersioningSchemaCustomType(TypedDict):
    # The regular expression used to describe the format of tags. Keep in mind that backslashes in the expression need to be escaped due to being encompassed in a JSON string. 
    expression: str

    type: str

class OptionalVersioningSchemaCustomType(TypedDict, total=False):
    # A customizable string that can be set for a custom versioning schema to describe its meaning. This label has no function. 
    label: str

class VersioningSchemaCustomType(RequiredVersioningSchemaCustomType, OptionalVersioningSchemaCustomType):
    pass
