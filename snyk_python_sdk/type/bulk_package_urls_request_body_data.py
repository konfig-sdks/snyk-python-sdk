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

from snyk_python_sdk.type.bulk_package_urls_request_body_data_attributes import BulkPackageUrlsRequestBodyDataAttributes
from snyk_python_sdk.type.types import Types

class RequiredBulkPackageUrlsRequestBodyData(TypedDict):
    attributes: BulkPackageUrlsRequestBodyDataAttributes

class OptionalBulkPackageUrlsRequestBodyData(TypedDict, total=False):
    type: Types

class BulkPackageUrlsRequestBodyData(RequiredBulkPackageUrlsRequestBodyData, OptionalBulkPackageUrlsRequestBodyData):
    pass
