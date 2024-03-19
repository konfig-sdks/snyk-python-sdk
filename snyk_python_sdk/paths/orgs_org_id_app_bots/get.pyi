# coding: utf-8

"""
    Snyk API

    Snyk helps software-driven businesses develop fast and stay secure. Continuously find and fix vulnerabilities for npm, Maven, NuGet, RubyGems, PyPI and more.

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from snyk_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from snyk_python_sdk.api_response import AsyncGeneratorResponse
from snyk_python_sdk import api_client, exceptions
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

from snyk_python_sdk.model.apps_list_app_bots500_response import AppsListAppBots500Response as AppsListAppBots500ResponseSchema
from snyk_python_sdk.model.apps_list_app_bots409_response import AppsListAppBots409Response as AppsListAppBots409ResponseSchema
from snyk_python_sdk.model.apps_list_app_bots_response import AppsListAppBotsResponse as AppsListAppBotsResponseSchema
from snyk_python_sdk.model.apps_list_app_bots400_response import AppsListAppBots400Response as AppsListAppBots400ResponseSchema
from snyk_python_sdk.model.actual_version import ActualVersion as ActualVersionSchema
from snyk_python_sdk.model.apps_list_app_bots404_response import AppsListAppBots404Response as AppsListAppBots404ResponseSchema
from snyk_python_sdk.model.query_version import QueryVersion as QueryVersionSchema
from snyk_python_sdk.model.apps_list_app_bots403_response import AppsListAppBots403Response as AppsListAppBots403ResponseSchema
from snyk_python_sdk.model.apps_list_app_bots401_response import AppsListAppBots401Response as AppsListAppBots401ResponseSchema

from snyk_python_sdk.type.apps_list_app_bots409_response import AppsListAppBots409Response
from snyk_python_sdk.type.apps_list_app_bots_response import AppsListAppBotsResponse
from snyk_python_sdk.type.apps_list_app_bots403_response import AppsListAppBots403Response
from snyk_python_sdk.type.apps_list_app_bots404_response import AppsListAppBots404Response
from snyk_python_sdk.type.apps_list_app_bots400_response import AppsListAppBots400Response
from snyk_python_sdk.type.apps_list_app_bots401_response import AppsListAppBots401Response
from snyk_python_sdk.type.actual_version import ActualVersion
from snyk_python_sdk.type.apps_list_app_bots500_response import AppsListAppBots500Response
from snyk_python_sdk.type.query_version import QueryVersion

from ...api_client import Dictionary
from snyk_python_sdk.pydantic.actual_version import ActualVersion as ActualVersionPydantic
from snyk_python_sdk.pydantic.apps_list_app_bots404_response import AppsListAppBots404Response as AppsListAppBots404ResponsePydantic
from snyk_python_sdk.pydantic.apps_list_app_bots400_response import AppsListAppBots400Response as AppsListAppBots400ResponsePydantic
from snyk_python_sdk.pydantic.apps_list_app_bots_response import AppsListAppBotsResponse as AppsListAppBotsResponsePydantic
from snyk_python_sdk.pydantic.query_version import QueryVersion as QueryVersionPydantic
from snyk_python_sdk.pydantic.apps_list_app_bots409_response import AppsListAppBots409Response as AppsListAppBots409ResponsePydantic
from snyk_python_sdk.pydantic.apps_list_app_bots401_response import AppsListAppBots401Response as AppsListAppBots401ResponsePydantic
from snyk_python_sdk.pydantic.apps_list_app_bots500_response import AppsListAppBots500Response as AppsListAppBots500ResponsePydantic
from snyk_python_sdk.pydantic.apps_list_app_bots403_response import AppsListAppBots403Response as AppsListAppBots403ResponsePydantic

# Query params


class ExpandSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
            @schemas.classproperty
            def APP(cls):
                return cls("app")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ExpandSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
VersionSchema = schemas.Schema
StartingAfterSchema = schemas.StrSchema
EndingBeforeSchema = schemas.StrSchema


class LimitSchema(
    schemas.Int32Schema
):
    pass
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'version': typing.Union[QueryVersionSchema, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'expand': typing.Union[ExpandSchema, list, tuple, ],
        'starting_after': typing.Union[StartingAfterSchema, str, ],
        'ending_before': typing.Union[EndingBeforeSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_expand = api_client.QueryParameter(
    name="expand",
    style=api_client.ParameterStyle.FORM,
    schema=ExpandSchema,
)
request_query_version = api_client.QueryParameter(
    name="version",
    style=api_client.ParameterStyle.FORM,
    schema=QueryVersionSchema,
    required=True,
    explode=True,
)
request_query_starting_after = api_client.QueryParameter(
    name="starting_after",
    style=api_client.ParameterStyle.FORM,
    schema=StartingAfterSchema,
    explode=True,
)
request_query_ending_before = api_client.QueryParameter(
    name="ending_before",
    style=api_client.ParameterStyle.FORM,
    schema=EndingBeforeSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
# Path params
OrgIdSchema = schemas.UUIDSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'org_id': typing.Union[OrgIdSchema, str, uuid.UUID, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_org_id = api_client.PathParameter(
    name="org_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=OrgIdSchema,
    required=True,
)
DeprecationSchema = schemas.DateTimeSchema
SnykRequestIdSchema = schemas.UUIDSchema


class SnykVersionLifecycleStageSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def WIP(cls):
        return cls("wip")
    
    @schemas.classproperty
    def EXPERIMENTAL(cls):
        return cls("experimental")
    
    @schemas.classproperty
    def BETA(cls):
        return cls("beta")
    
    @schemas.classproperty
    def GA(cls):
        return cls("ga")
    
    @schemas.classproperty
    def DEPRECATED(cls):
        return cls("deprecated")
    
    @schemas.classproperty
    def SUNSET(cls):
        return cls("sunset")
SnykVersionRequestedSchema = schemas.Schema
SnykVersionServedSchema = schemas.Schema
SunsetSchema = schemas.DateTimeSchema
SchemaFor200ResponseBodyApplicationVndApijson = AppsListAppBotsResponseSchema
ResponseHeadersFor200 = typing_extensions.TypedDict(
    'ResponseHeadersFor200',
    {
        'deprecation': DeprecationSchema,
        'snyk-request-id': SnykRequestIdSchema,
        'snyk-version-lifecycle-stage': SnykVersionLifecycleStageSchema,
        'snyk-version-requested': SnykVersionRequestedSchema,
        'snyk-version-served': SnykVersionServedSchema,
        'sunset': SunsetSchema,
    }
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AppsListAppBotsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AppsListAppBotsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationVndApijson),
    },
    headers=[
        deprecation_parameter,
        snyk_request_id_parameter,
        snyk_version_lifecycle_stage_parameter,
        snyk_version_requested_parameter,
        snyk_version_served_parameter,
        sunset_parameter,
    ]
)
DeprecationSchema = schemas.DateTimeSchema
SnykRequestIdSchema = schemas.UUIDSchema


class SnykVersionLifecycleStageSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def WIP(cls):
        return cls("wip")
    
    @schemas.classproperty
    def EXPERIMENTAL(cls):
        return cls("experimental")
    
    @schemas.classproperty
    def BETA(cls):
        return cls("beta")
    
    @schemas.classproperty
    def GA(cls):
        return cls("ga")
    
    @schemas.classproperty
    def DEPRECATED(cls):
        return cls("deprecated")
    
    @schemas.classproperty
    def SUNSET(cls):
        return cls("sunset")


class SnykVersionRequestedSchema(
    schemas.StrSchema
):
    pass


class SnykVersionServedSchema(
    schemas.StrSchema
):
    pass
SunsetSchema = schemas.DateTimeSchema
SchemaFor400ResponseBodyApplicationVndApijson = AppsListAppBots400ResponseSchema
ResponseHeadersFor400 = typing_extensions.TypedDict(
    'ResponseHeadersFor400',
    {
        'deprecation': DeprecationSchema,
        'snyk-request-id': SnykRequestIdSchema,
        'snyk-version-lifecycle-stage': SnykVersionLifecycleStageSchema,
        'snyk-version-requested': SnykVersionRequestedSchema,
        'snyk-version-served': SnykVersionServedSchema,
        'sunset': SunsetSchema,
    }
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: AppsListAppBots400Response


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: AppsListAppBots400Response


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationVndApijson),
    },
    headers=[
        deprecation_parameter,
        snyk_request_id_parameter,
        snyk_version_lifecycle_stage_parameter,
        snyk_version_requested_parameter,
        snyk_version_served_parameter,
        sunset_parameter,
    ]
)
DeprecationSchema = schemas.DateTimeSchema
SnykRequestIdSchema = schemas.UUIDSchema


class SnykVersionLifecycleStageSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def WIP(cls):
        return cls("wip")
    
    @schemas.classproperty
    def EXPERIMENTAL(cls):
        return cls("experimental")
    
    @schemas.classproperty
    def BETA(cls):
        return cls("beta")
    
    @schemas.classproperty
    def GA(cls):
        return cls("ga")
    
    @schemas.classproperty
    def DEPRECATED(cls):
        return cls("deprecated")
    
    @schemas.classproperty
    def SUNSET(cls):
        return cls("sunset")


class SnykVersionRequestedSchema(
    schemas.StrSchema
):
    pass


class SnykVersionServedSchema(
    schemas.StrSchema
):
    pass
SunsetSchema = schemas.DateTimeSchema
SchemaFor401ResponseBodyApplicationVndApijson = AppsListAppBots401ResponseSchema
ResponseHeadersFor401 = typing_extensions.TypedDict(
    'ResponseHeadersFor401',
    {
        'deprecation': DeprecationSchema,
        'snyk-request-id': SnykRequestIdSchema,
        'snyk-version-lifecycle-stage': SnykVersionLifecycleStageSchema,
        'snyk-version-requested': SnykVersionRequestedSchema,
        'snyk-version-served': SnykVersionServedSchema,
        'sunset': SunsetSchema,
    }
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: AppsListAppBots401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: AppsListAppBots401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationVndApijson),
    },
    headers=[
        deprecation_parameter,
        snyk_request_id_parameter,
        snyk_version_lifecycle_stage_parameter,
        snyk_version_requested_parameter,
        snyk_version_served_parameter,
        sunset_parameter,
    ]
)
DeprecationSchema = schemas.DateTimeSchema
SnykRequestIdSchema = schemas.UUIDSchema


class SnykVersionLifecycleStageSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def WIP(cls):
        return cls("wip")
    
    @schemas.classproperty
    def EXPERIMENTAL(cls):
        return cls("experimental")
    
    @schemas.classproperty
    def BETA(cls):
        return cls("beta")
    
    @schemas.classproperty
    def GA(cls):
        return cls("ga")
    
    @schemas.classproperty
    def DEPRECATED(cls):
        return cls("deprecated")
    
    @schemas.classproperty
    def SUNSET(cls):
        return cls("sunset")


class SnykVersionRequestedSchema(
    schemas.StrSchema
):
    pass


class SnykVersionServedSchema(
    schemas.StrSchema
):
    pass
SunsetSchema = schemas.DateTimeSchema
SchemaFor403ResponseBodyApplicationVndApijson = AppsListAppBots403ResponseSchema
ResponseHeadersFor403 = typing_extensions.TypedDict(
    'ResponseHeadersFor403',
    {
        'deprecation': DeprecationSchema,
        'snyk-request-id': SnykRequestIdSchema,
        'snyk-version-lifecycle-stage': SnykVersionLifecycleStageSchema,
        'snyk-version-requested': SnykVersionRequestedSchema,
        'snyk-version-served': SnykVersionServedSchema,
        'sunset': SunsetSchema,
    }
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: AppsListAppBots403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: AppsListAppBots403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationVndApijson),
    },
    headers=[
        deprecation_parameter,
        snyk_request_id_parameter,
        snyk_version_lifecycle_stage_parameter,
        snyk_version_requested_parameter,
        snyk_version_served_parameter,
        sunset_parameter,
    ]
)
DeprecationSchema = schemas.DateTimeSchema
SnykRequestIdSchema = schemas.UUIDSchema


class SnykVersionLifecycleStageSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def WIP(cls):
        return cls("wip")
    
    @schemas.classproperty
    def EXPERIMENTAL(cls):
        return cls("experimental")
    
    @schemas.classproperty
    def BETA(cls):
        return cls("beta")
    
    @schemas.classproperty
    def GA(cls):
        return cls("ga")
    
    @schemas.classproperty
    def DEPRECATED(cls):
        return cls("deprecated")
    
    @schemas.classproperty
    def SUNSET(cls):
        return cls("sunset")


class SnykVersionRequestedSchema(
    schemas.StrSchema
):
    pass


class SnykVersionServedSchema(
    schemas.StrSchema
):
    pass
SunsetSchema = schemas.DateTimeSchema
SchemaFor404ResponseBodyApplicationVndApijson = AppsListAppBots404ResponseSchema
ResponseHeadersFor404 = typing_extensions.TypedDict(
    'ResponseHeadersFor404',
    {
        'deprecation': DeprecationSchema,
        'snyk-request-id': SnykRequestIdSchema,
        'snyk-version-lifecycle-stage': SnykVersionLifecycleStageSchema,
        'snyk-version-requested': SnykVersionRequestedSchema,
        'snyk-version-served': SnykVersionServedSchema,
        'sunset': SunsetSchema,
    }
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: AppsListAppBots404Response


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: AppsListAppBots404Response


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationVndApijson),
    },
    headers=[
        deprecation_parameter,
        snyk_request_id_parameter,
        snyk_version_lifecycle_stage_parameter,
        snyk_version_requested_parameter,
        snyk_version_served_parameter,
        sunset_parameter,
    ]
)
DeprecationSchema = schemas.DateTimeSchema
SnykRequestIdSchema = schemas.UUIDSchema


class SnykVersionLifecycleStageSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def WIP(cls):
        return cls("wip")
    
    @schemas.classproperty
    def EXPERIMENTAL(cls):
        return cls("experimental")
    
    @schemas.classproperty
    def BETA(cls):
        return cls("beta")
    
    @schemas.classproperty
    def GA(cls):
        return cls("ga")
    
    @schemas.classproperty
    def DEPRECATED(cls):
        return cls("deprecated")
    
    @schemas.classproperty
    def SUNSET(cls):
        return cls("sunset")


class SnykVersionRequestedSchema(
    schemas.StrSchema
):
    pass


class SnykVersionServedSchema(
    schemas.StrSchema
):
    pass
SunsetSchema = schemas.DateTimeSchema
SchemaFor409ResponseBodyApplicationVndApijson = AppsListAppBots409ResponseSchema
ResponseHeadersFor409 = typing_extensions.TypedDict(
    'ResponseHeadersFor409',
    {
        'deprecation': DeprecationSchema,
        'snyk-request-id': SnykRequestIdSchema,
        'snyk-version-lifecycle-stage': SnykVersionLifecycleStageSchema,
        'snyk-version-requested': SnykVersionRequestedSchema,
        'snyk-version-served': SnykVersionServedSchema,
        'sunset': SunsetSchema,
    }
)


@dataclass
class ApiResponseFor409(api_client.ApiResponse):
    body: AppsListAppBots409Response


@dataclass
class ApiResponseFor409Async(api_client.AsyncApiResponse):
    body: AppsListAppBots409Response


_response_for_409 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor409,
    response_cls_async=ApiResponseFor409Async,
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaFor409ResponseBodyApplicationVndApijson),
    },
    headers=[
        deprecation_parameter,
        snyk_request_id_parameter,
        snyk_version_lifecycle_stage_parameter,
        snyk_version_requested_parameter,
        snyk_version_served_parameter,
        sunset_parameter,
    ]
)
DeprecationSchema = schemas.DateTimeSchema
SnykRequestIdSchema = schemas.UUIDSchema


class SnykVersionLifecycleStageSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def WIP(cls):
        return cls("wip")
    
    @schemas.classproperty
    def EXPERIMENTAL(cls):
        return cls("experimental")
    
    @schemas.classproperty
    def BETA(cls):
        return cls("beta")
    
    @schemas.classproperty
    def GA(cls):
        return cls("ga")
    
    @schemas.classproperty
    def DEPRECATED(cls):
        return cls("deprecated")
    
    @schemas.classproperty
    def SUNSET(cls):
        return cls("sunset")


class SnykVersionRequestedSchema(
    schemas.StrSchema
):
    pass


class SnykVersionServedSchema(
    schemas.StrSchema
):
    pass
SunsetSchema = schemas.DateTimeSchema
SchemaFor500ResponseBodyApplicationVndApijson = AppsListAppBots500ResponseSchema
ResponseHeadersFor500 = typing_extensions.TypedDict(
    'ResponseHeadersFor500',
    {
        'deprecation': DeprecationSchema,
        'snyk-request-id': SnykRequestIdSchema,
        'snyk-version-lifecycle-stage': SnykVersionLifecycleStageSchema,
        'snyk-version-requested': SnykVersionRequestedSchema,
        'snyk-version-served': SnykVersionServedSchema,
        'sunset': SunsetSchema,
    }
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: AppsListAppBots500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: AppsListAppBots500Response


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/vnd.api+json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationVndApijson),
    },
    headers=[
        deprecation_parameter,
        snyk_request_id_parameter,
        snyk_version_lifecycle_stage_parameter,
        snyk_version_requested_parameter,
        snyk_version_served_parameter,
        sunset_parameter,
    ]
)
_all_accept_content_types = (
    'application/vnd.api+json',
)


class BaseApi(api_client.Api):

    def _list_app_bots_mapped_args(
        self,
        org_id: str,
        version: QueryVersion,
        expand: typing.Optional[typing.List[str]] = None,
        starting_after: typing.Optional[str] = None,
        ending_before: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if expand is not None:
            _query_params["expand"] = expand
        if version is not None:
            _query_params["version"] = version
        if starting_after is not None:
            _query_params["starting_after"] = starting_after
        if ending_before is not None:
            _query_params["ending_before"] = ending_before
        if limit is not None:
            _query_params["limit"] = limit
        if org_id is not None:
            _path_params["org_id"] = org_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _alist_app_bots_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get a list of app bots authorized to an organization.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_org_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_expand,
            request_query_version,
            request_query_starting_after,
            request_query_ending_before,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/orgs/{org_id}/app_bots',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _list_app_bots_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get a list of app bots authorized to an organization.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_org_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_expand,
            request_query_version,
            request_query_starting_after,
            request_query_ending_before,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/orgs/{org_id}/app_bots',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ListAppBotsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @api_client.DeprecationWarningOnce(prefix="apps")
    async def alist_app_bots(
        self,
        org_id: str,
        version: QueryVersion,
        expand: typing.Optional[typing.List[str]] = None,
        starting_after: typing.Optional[str] = None,
        ending_before: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_app_bots_mapped_args(
            org_id=org_id,
            version=version,
            expand=expand,
            starting_after=starting_after,
            ending_before=ending_before,
            limit=limit,
        )
        return await self._alist_app_bots_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="apps")
    def list_app_bots(
        self,
        org_id: str,
        version: QueryVersion,
        expand: typing.Optional[typing.List[str]] = None,
        starting_after: typing.Optional[str] = None,
        ending_before: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_app_bots_mapped_args(
            org_id=org_id,
            version=version,
            expand=expand,
            starting_after=starting_after,
            ending_before=ending_before,
            limit=limit,
        )
        return self._list_app_bots_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class ListAppBots(BaseApi):

    @api_client.DeprecationWarningOnce(prefix="apps")
    async def alist_app_bots(
        self,
        org_id: str,
        version: QueryVersion,
        expand: typing.Optional[typing.List[str]] = None,
        starting_after: typing.Optional[str] = None,
        ending_before: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> AppsListAppBotsResponsePydantic:
        raw_response = await self.raw.alist_app_bots(
            org_id=org_id,
            version=version,
            expand=expand,
            starting_after=starting_after,
            ending_before=ending_before,
            limit=limit,
            **kwargs,
        )
        if validate:
            return AppsListAppBotsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AppsListAppBotsResponsePydantic, raw_response.body)
    
    
    @api_client.DeprecationWarningOnce(prefix="apps")
    def list_app_bots(
        self,
        org_id: str,
        version: QueryVersion,
        expand: typing.Optional[typing.List[str]] = None,
        starting_after: typing.Optional[str] = None,
        ending_before: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        validate: bool = False,
    ) -> AppsListAppBotsResponsePydantic:
        raw_response = self.raw.list_app_bots(
            org_id=org_id,
            version=version,
            expand=expand,
            starting_after=starting_after,
            ending_before=ending_before,
            limit=limit,
        )
        if validate:
            return AppsListAppBotsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AppsListAppBotsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @api_client.DeprecationWarningOnce(prefix="apps")
    async def aget(
        self,
        org_id: str,
        version: QueryVersion,
        expand: typing.Optional[typing.List[str]] = None,
        starting_after: typing.Optional[str] = None,
        ending_before: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_app_bots_mapped_args(
            org_id=org_id,
            version=version,
            expand=expand,
            starting_after=starting_after,
            ending_before=ending_before,
            limit=limit,
        )
        return await self._alist_app_bots_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="apps")
    def get(
        self,
        org_id: str,
        version: QueryVersion,
        expand: typing.Optional[typing.List[str]] = None,
        starting_after: typing.Optional[str] = None,
        ending_before: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_app_bots_mapped_args(
            org_id=org_id,
            version=version,
            expand=expand,
            starting_after=starting_after,
            ending_before=ending_before,
            limit=limit,
        )
        return self._list_app_bots_oapg(
            query_params=args.query,
            path_params=args.path,
        )

