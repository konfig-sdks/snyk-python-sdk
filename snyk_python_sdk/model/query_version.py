# coding: utf-8

"""
    Snyk API

    Missing description placeholder

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


class QueryVersion(
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Requested API version
    """


    class MetaOapg:
        regex=[{
            'pattern': r'^(wip|work-in-progress|experimental|beta|((([0-9]{4})-([0-1][0-9]))-((3[01])|(0[1-9])|([12][0-9]))(~(wip|work-in-progress|experimental|beta))?))$',
        }]
