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


class IssueRelationshipsTestExecutionsData(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    List of metadata associated with the test executions that identified this issue
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['IssueRelationshipsTestExecutionsDataItem']:
            return IssueRelationshipsTestExecutionsDataItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['IssueRelationshipsTestExecutionsDataItem'], typing.List['IssueRelationshipsTestExecutionsDataItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IssueRelationshipsTestExecutionsData':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'IssueRelationshipsTestExecutionsDataItem':
        return super().__getitem__(i)

from snyk_python_sdk.model.issue_relationships_test_executions_data_item import IssueRelationshipsTestExecutionsDataItem
