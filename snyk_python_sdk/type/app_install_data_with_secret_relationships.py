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

from snyk_python_sdk.type.app_install_data_with_secret_relationships_app import AppInstallDataWithSecretRelationshipsApp

class RequiredAppInstallDataWithSecretRelationships(TypedDict):
    pass

class OptionalAppInstallDataWithSecretRelationships(TypedDict, total=False):
    app: AppInstallDataWithSecretRelationshipsApp

class AppInstallDataWithSecretRelationships(RequiredAppInstallDataWithSecretRelationships, OptionalAppInstallDataWithSecretRelationships):
    pass
