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

from snyk_python_sdk.type.app_install_with_client_relationships_app_data import AppInstallWithClientRelationshipsAppData

class RequiredAppInstallWithClientRelationshipsApp(TypedDict):
    pass

class OptionalAppInstallWithClientRelationshipsApp(TypedDict, total=False):
    data: AppInstallWithClientRelationshipsAppData

class AppInstallWithClientRelationshipsApp(RequiredAppInstallWithClientRelationshipsApp, OptionalAppInstallWithClientRelationshipsApp):
    pass
