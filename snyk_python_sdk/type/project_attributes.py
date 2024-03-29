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

from snyk_python_sdk.type.container_build_args import ContainerBuildArgs
from snyk_python_sdk.type.nuget_build_args import NugetBuildArgs
from snyk_python_sdk.type.project_attributes_business_criticality import ProjectAttributesBusinessCriticality
from snyk_python_sdk.type.project_attributes_environment import ProjectAttributesEnvironment
from snyk_python_sdk.type.project_attributes_lifecycle import ProjectAttributesLifecycle
from snyk_python_sdk.type.project_attributes_tags import ProjectAttributesTags
from snyk_python_sdk.type.project_settings import ProjectSettings
from snyk_python_sdk.type.yarn_build_args import YarnBuildArgs

class RequiredProjectAttributes(TypedDict):
    # The date that the project was created on
    created: datetime

    # Project name.
    name: str

    # The origin the project was added from.
    origin: str

    # Whether the project is read-only
    read_only: bool

    settings: ProjectSettings

    # Describes if a project is currently monitored or it is de-activated.
    status: str

    # Path within the target to identify a specific file/directory/image etc. when scanning just part  of the target, and not the entity.
    target_file: str

    # The additional information required to resolve which revision of the resource should be scanned.
    target_reference: str

    # The package manager of the project.
    type: str

class OptionalProjectAttributes(TypedDict, total=False):
    tags: ProjectAttributesTags

    build_args: typing.Union[YarnBuildArgs, ContainerBuildArgs, NugetBuildArgs]

    business_criticality: ProjectAttributesBusinessCriticality

    environment: ProjectAttributesEnvironment

    lifecycle: ProjectAttributesLifecycle

    # Dotnet Target, for relevant projects
    target_runtime: str

class ProjectAttributes(RequiredProjectAttributes, OptionalProjectAttributes):
    pass
