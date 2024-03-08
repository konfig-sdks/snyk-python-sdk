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

from snyk_python_sdk.type.apps_manage_client_secret_for_snyk_app409_response_errors import AppsManageClientSecretForSnykApp409ResponseErrors
from snyk_python_sdk.type.apps_manage_client_secret_for_snyk_app409_response_jsonapi import AppsManageClientSecretForSnykApp409ResponseJsonapi

class RequiredAppsManageClientSecretForSnykApp409Response(TypedDict):
    errors: AppsManageClientSecretForSnykApp409ResponseErrors

    jsonapi: AppsManageClientSecretForSnykApp409ResponseJsonapi

class OptionalAppsManageClientSecretForSnykApp409Response(TypedDict, total=False):
    pass

class AppsManageClientSecretForSnykApp409Response(RequiredAppsManageClientSecretForSnykApp409Response, OptionalAppsManageClientSecretForSnykApp409Response):
    pass