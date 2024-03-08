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

from snyk_python_sdk.type.apps_create_install_secret_request_data_attributes import AppsCreateInstallSecretRequestDataAttributes

class RequiredAppsCreateInstallSecretRequestData(TypedDict):
    attributes: AppsCreateInstallSecretRequestDataAttributes

    type: str

class OptionalAppsCreateInstallSecretRequestData(TypedDict, total=False):
    pass

class AppsCreateInstallSecretRequestData(RequiredAppsCreateInstallSecretRequestData, OptionalAppsCreateInstallSecretRequestData):
    pass