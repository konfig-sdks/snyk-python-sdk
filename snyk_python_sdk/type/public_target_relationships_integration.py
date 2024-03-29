# coding: utf-8

"""
    Snyk API

    Snyk helps software-driven businesses develop fast and stay secure. Continuously find and fix vulnerabilities for npm, Maven, NuGet, RubyGems, PyPI and more.

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from snyk_python_sdk.type.public_target_relationships_integration_data import PublicTargetRelationshipsIntegrationData

class RequiredPublicTargetRelationshipsIntegration(TypedDict):
    data: PublicTargetRelationshipsIntegrationData

class OptionalPublicTargetRelationshipsIntegration(TypedDict, total=False):
    pass

class PublicTargetRelationshipsIntegration(RequiredPublicTargetRelationshipsIntegration, OptionalPublicTargetRelationshipsIntegration):
    pass
