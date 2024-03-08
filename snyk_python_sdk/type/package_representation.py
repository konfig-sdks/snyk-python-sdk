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

from snyk_python_sdk.type.package_meta import PackageMeta

class RequiredPackageRepresentation(TypedDict):
    pass

class OptionalPackageRepresentation(TypedDict, total=False):
    package: PackageMeta

class PackageRepresentation(RequiredPackageRepresentation, OptionalPackageRepresentation):
    pass