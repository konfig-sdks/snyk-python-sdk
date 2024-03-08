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


class RequiredManualRemediationPRsSettings(TypedDict):
    pass

class OptionalManualRemediationPRsSettings(TypedDict, total=False):
    # Include vulnerability patches in manual pull requests.
    is_patch_remediation_enabled: bool

class ManualRemediationPRsSettings(RequiredManualRemediationPRsSettings, OptionalManualRemediationPRsSettings):
    pass