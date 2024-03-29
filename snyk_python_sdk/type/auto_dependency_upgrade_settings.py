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

from snyk_python_sdk.type.auto_dependency_upgrade_settings_ignored_dependencies import AutoDependencyUpgradeSettingsIgnoredDependencies

class RequiredAutoDependencyUpgradeSettings(TypedDict):
    pass

class OptionalAutoDependencyUpgradeSettings(TypedDict, total=False):
    ignored_dependencies: AutoDependencyUpgradeSettingsIgnoredDependencies

    # Automatically raise pull requests to update out-of-date dependencies.
    is_enabled: bool

    # Apply the auto dependency integration settings of the Organization to this project.
    is_inherited: bool

    # Include major version in dependency upgrade recommendation.
    is_major_upgrade_enabled: bool

    # Limit of dependency upgrade PRs which can be opened simultaneously. When the limit is reached, no new upgrade PRs are created. If specified, must be between 1 and 10.
    limit: typing.Union[int, float]

    # Minimum dependency maturity period in days. If specified, must be between 1 and 365.
    minimum_age: typing.Union[int, float]

class AutoDependencyUpgradeSettings(RequiredAutoDependencyUpgradeSettings, OptionalAutoDependencyUpgradeSettings):
    pass
