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


class RequiredPackageMeta(TypedDict):
    pass

class OptionalPackageMeta(TypedDict, total=False):
    # The version of the package
    version: str

    # The package’s name
    name: str

    # A name prefix, such as a maven group id or docker image owner
    namespace: str

    # The package type or protocol
    type: str

    # The purl of the package
    url: str

class PackageMeta(RequiredPackageMeta, OptionalPackageMeta):
    pass