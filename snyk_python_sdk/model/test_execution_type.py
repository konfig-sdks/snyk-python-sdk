# coding: utf-8

"""
    Snyk API

    Snyk helps software-driven businesses develop fast and stay secure. Continuously find and fix vulnerabilities for npm, Maven, NuGet, RubyGems, PyPI and more.

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from snyk_python_sdk import schemas  # noqa: F401


class TestExecutionType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        enum_value_to_name = {
            "test-workflow-execution": "TESTWORKFLOWEXECUTION",
            "custom-execution": "CUSTOMEXECUTION",
        }
    
    @schemas.classproperty
    def TESTWORKFLOWEXECUTION(cls):
        return cls("test-workflow-execution")
    
    @schemas.classproperty
    def CUSTOMEXECUTION(cls):
        return cls("custom-execution")
