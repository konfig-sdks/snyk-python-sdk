# coding: utf-8

"""
    Snyk API

    Missing description placeholder

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

from snyk_python_sdk.model.apps_get_by_app_id403_response import AppsGetByAppId403Response as AppsGetByAppId403ResponseSchema
from snyk_python_sdk.model.apps_get_by_app_id400_response import AppsGetByAppId400Response as AppsGetByAppId400ResponseSchema
from snyk_python_sdk.model.apps_get_by_app_id401_response import AppsGetByAppId401Response as AppsGetByAppId401ResponseSchema
from snyk_python_sdk.model.actual_version import ActualVersion as ActualVersionSchema
from snyk_python_sdk.model.apps_get_by_app_id409_response import AppsGetByAppId409Response as AppsGetByAppId409ResponseSchema
from snyk_python_sdk.model.apps_get_by_app_id_response import AppsGetByAppIdResponse as AppsGetByAppIdResponseSchema
from snyk_python_sdk.model.query_version import QueryVersion as QueryVersionSchema
from snyk_python_sdk.model.apps_get_by_app_id404_response import AppsGetByAppId404Response as AppsGetByAppId404ResponseSchema
from snyk_python_sdk.model.apps_get_by_app_id500_response import AppsGetByAppId500Response as AppsGetByAppId500ResponseSchema

from snyk_python_sdk.type.apps_get_by_app_id404_response import AppsGetByAppId404Response
from snyk_python_sdk.type.apps_get_by_app_id_response import AppsGetByAppIdResponse
from snyk_python_sdk.type.apps_get_by_app_id400_response import AppsGetByAppId400Response
from snyk_python_sdk.type.apps_get_by_app_id403_response import AppsGetByAppId403Response
from snyk_python_sdk.type.apps_get_by_app_id401_response import AppsGetByAppId401Response
from snyk_python_sdk.type.apps_get_by_app_id500_response import AppsGetByAppId500Response
from snyk_python_sdk.type.apps_get_by_app_id409_response import AppsGetByAppId409Response
from snyk_python_sdk.type.actual_version import ActualVersion
from snyk_python_sdk.type.query_version import QueryVersion

from ...api_client import Dictionary
from snyk_python_sdk.pydantic.actual_version import ActualVersion as ActualVersionPydantic
from snyk_python_sdk.pydantic.apps_get_by_app_id_response import AppsGetByAppIdResponse as AppsGetByAppIdResponsePydantic
from snyk_python_sdk.pydantic.apps_get_by_app_id403_response import AppsGetByAppId403Response as AppsGetByAppId403ResponsePydantic
from snyk_python_sdk.pydantic.query_version import QueryVersion as QueryVersionPydantic
from snyk_python_sdk.pydantic.apps_get_by_app_id404_response import AppsGetByAppId404Response as AppsGetByAppId404ResponsePydantic
from snyk_python_sdk.pydantic.apps_get_by_app_id500_response import AppsGetByAppId500Response as AppsGetByAppId500ResponsePydantic
from snyk_python_sdk.pydantic.apps_get_by_app_id401_response import AppsGetByAppId401Response as AppsGetByAppId401ResponsePydantic
from snyk_python_sdk.pydantic.apps_get_by_app_id409_response import AppsGetByAppId409Response as AppsGetByAppId409ResponsePydantic
from snyk_python_sdk.pydantic.apps_get_by_app_id400_response import AppsGetByAppId400Response as AppsGetByAppId400ResponsePydantic

# Query params
VersionSchema = schemas.Schema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'version': typing.Union[QueryVersion, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_version = api_client.QueryParameter(
    name="version",
    style=api_client.ParameterStyle.FORM,
    schema=QueryVersion,
    required=True,
    explode=True,
)
# Path params
OrgIdSchema = schemas.UUIDSchema
AppIdSchema = schemas.UUIDSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'org_id': typing.Union[OrgIdSchema, str, uuid.UUID, ],
        'app_id': typing.Union[AppIdSchema, str, uuid.UUID, ],
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
request_path_app_id = api_client.PathParameter(
    name="app_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AppIdSchema,
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
SchemaFor200ResponseBodyApplicationVndApijson = AppsGetByAppIdResponseSchema
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
    body: AppsGetByAppIdResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AppsGetByAppIdResponse


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
SchemaFor400ResponseBodyApplicationVndApijson = AppsGetByAppId400ResponseSchema
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
    body: AppsGetByAppId400Response


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: AppsGetByAppId400Response


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
SchemaFor401ResponseBodyApplicationVndApijson = AppsGetByAppId401ResponseSchema
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
    body: AppsGetByAppId401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: AppsGetByAppId401Response


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
SchemaFor403ResponseBodyApplicationVndApijson = AppsGetByAppId403ResponseSchema
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
    body: AppsGetByAppId403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: AppsGetByAppId403Response


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
SchemaFor404ResponseBodyApplicationVndApijson = AppsGetByAppId404ResponseSchema
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
    body: AppsGetByAppId404Response


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: AppsGetByAppId404Response


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
SchemaFor409ResponseBodyApplicationVndApijson = AppsGetByAppId409ResponseSchema
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
    body: AppsGetByAppId409Response


@dataclass
class ApiResponseFor409Async(api_client.AsyncApiResponse):
    body: AppsGetByAppId409Response


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
SchemaFor500ResponseBodyApplicationVndApijson = AppsGetByAppId500ResponseSchema
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
    body: AppsGetByAppId500Response


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: AppsGetByAppId500Response


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

    def _get_by_app_id_mapped_args(
        self,
        org_id: str,
        app_id: str,
        version: QueryVersion,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if version is not None:
            _query_params["version"] = version
        if org_id is not None:
            _path_params["org_id"] = org_id
        if app_id is not None:
            _path_params["app_id"] = app_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_by_app_id_oapg(
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
        Get a Snyk App by its App ID.
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
            request_path_app_id,
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
            request_query_version,
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
            path_template='/orgs/{org_id}/apps/creations/{app_id}',
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


    def _get_by_app_id_oapg(
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
        Get a Snyk App by its App ID.
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
            request_path_app_id,
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
            request_query_version,
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
            path_template='/orgs/{org_id}/apps/creations/{app_id}',
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


class GetByAppIdRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_by_app_id(
        self,
        org_id: str,
        app_id: str,
        version: QueryVersion,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_by_app_id_mapped_args(
            org_id=org_id,
            app_id=app_id,
            version=version,
        )
        return await self._aget_by_app_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_by_app_id(
        self,
        org_id: str,
        app_id: str,
        version: QueryVersion,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_by_app_id_mapped_args(
            org_id=org_id,
            app_id=app_id,
            version=version,
        )
        return self._get_by_app_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetByAppId(BaseApi):

    async def aget_by_app_id(
        self,
        org_id: str,
        app_id: str,
        version: QueryVersion,
        validate: bool = False,
        **kwargs,
    ) -> AppsGetByAppIdResponsePydantic:
        raw_response = await self.raw.aget_by_app_id(
            org_id=org_id,
            app_id=app_id,
            version=version,
            **kwargs,
        )
        if validate:
            return AppsGetByAppIdResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AppsGetByAppIdResponsePydantic, raw_response.body)
    
    
    def get_by_app_id(
        self,
        org_id: str,
        app_id: str,
        version: QueryVersion,
        validate: bool = False,
    ) -> AppsGetByAppIdResponsePydantic:
        raw_response = self.raw.get_by_app_id(
            org_id=org_id,
            app_id=app_id,
            version=version,
        )
        if validate:
            return AppsGetByAppIdResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(AppsGetByAppIdResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        org_id: str,
        app_id: str,
        version: QueryVersion,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_by_app_id_mapped_args(
            org_id=org_id,
            app_id=app_id,
            version=version,
        )
        return await self._aget_by_app_id_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        org_id: str,
        app_id: str,
        version: QueryVersion,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_by_app_id_mapped_args(
            org_id=org_id,
            app_id=app_id,
            version=version,
        )
        return self._get_by_app_id_oapg(
            query_params=args.query,
            path_params=args.path,
        )

