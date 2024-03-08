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

from snyk_python_sdk.type.app_install_with_client_relationships_app import AppInstallWithClientRelationshipsApp

class RequiredAppInstallWithClientRelationships(TypedDict):
    pass

class OptionalAppInstallWithClientRelationships(TypedDict, total=False):
    app: AppInstallWithClientRelationshipsApp

class AppInstallWithClientRelationships(RequiredAppInstallWithClientRelationships, OptionalAppInstallWithClientRelationships):
    pass