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


class Platform(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        enum_value_to_name = {
            "aix/ppc64": "AIX_PPC64",
            "android/386": "ANDROID_386",
            "android/amd64": "ANDROID_AMD64",
            "android/arm": "ANDROID_ARM",
            "android/arm/v5": "ANDROID_ARM_V5",
            "android/arm/v6": "ANDROID_ARM_V6",
            "android/arm/v7": "ANDROID_ARM_V7",
            "android/arm64": "ANDROID_ARM64",
            "android/arm64/v8": "ANDROID_ARM64_V8",
            "darwin/amd64": "DARWIN_AMD64",
            "darwin/arm": "DARWIN_ARM",
            "darwin/arm/v5": "DARWIN_ARM_V5",
            "darwin/arm/v6": "DARWIN_ARM_V6",
            "darwin/arm/v7": "DARWIN_ARM_V7",
            "darwin/arm64": "DARWIN_ARM64",
            "darwin/arm64/v8": "DARWIN_ARM64_V8",
            "dragonfly/amd64": "DRAGONFLY_AMD64",
            "freebsd/386": "FREEBSD_386",
            "freebsd/amd64": "FREEBSD_AMD64",
            "freebsd/arm": "FREEBSD_ARM",
            "freebsd/arm/v5": "FREEBSD_ARM_V5",
            "freebsd/arm/v6": "FREEBSD_ARM_V6",
            "freebsd/arm/v7": "FREEBSD_ARM_V7",
            "illumos/amd64": "ILLUMOS_AMD64",
            "ios/arm64": "IOS_ARM64",
            "ios/arm64/v8": "IOS_ARM64_V8",
            "js/wasm": "JS_WASM",
            "linux/386": "LINUX_386",
            "linux/amd64": "LINUX_AMD64",
            "linux/arm": "LINUX_ARM",
            "linux/arm/v5": "LINUX_ARM_V5",
            "linux/arm/v6": "LINUX_ARM_V6",
            "linux/arm/v7": "LINUX_ARM_V7",
            "linux/arm64": "LINUX_ARM64",
            "linux/arm64/v8": "LINUX_ARM64_V8",
            "linux/loong64": "LINUX_LOONG64",
            "linux/mips": "LINUX_MIPS",
            "linux/mipsle": "LINUX_MIPSLE",
            "linux/mips64": "LINUX_MIPS64",
            "linux/mips64le": "LINUX_MIPS64LE",
            "linux/ppc64": "LINUX_PPC64",
            "linux/ppc64le": "LINUX_PPC64LE",
            "linux/riscv64": "LINUX_RISCV64",
            "linux/s390x": "LINUX_S390X",
            "linux/x86_64": "LINUX_X86_64",
            "netbsd/386": "NETBSD_386",
            "netbsd/amd64": "NETBSD_AMD64",
            "netbsd/arm": "NETBSD_ARM",
            "netbsd/arm/v5": "NETBSD_ARM_V5",
            "netbsd/arm/v6": "NETBSD_ARM_V6",
            "netbsd/arm/v7": "NETBSD_ARM_V7",
            "openbsd/386": "OPENBSD_386",
            "openbsd/amd64": "OPENBSD_AMD64",
            "openbsd/arm": "OPENBSD_ARM",
            "openbsd/arm/v5": "OPENBSD_ARM_V5",
            "openbsd/arm/v6": "OPENBSD_ARM_V6",
            "openbsd/arm/v7": "OPENBSD_ARM_V7",
            "openbsd/arm64": "OPENBSD_ARM64",
            "openbsd/arm64/v8": "OPENBSD_ARM64_V8",
            "plan9/386": "PLAN9_386",
            "plan9/amd64": "PLAN9_AMD64",
            "plan9/arm": "PLAN9_ARM",
            "plan9/arm/v5": "PLAN9_ARM_V5",
            "plan9/arm/v6": "PLAN9_ARM_V6",
            "plan9/arm/v7": "PLAN9_ARM_V7",
            "solaris/amd64": "SOLARIS_AMD64",
            "windows/386": "WINDOWS_386",
            "windows/amd64": "WINDOWS_AMD64",
            "windows/arm": "WINDOWS_ARM",
            "windows/arm/v5": "WINDOWS_ARM_V5",
            "windows/arm/v6": "WINDOWS_ARM_V6",
            "windows/arm/v7": "WINDOWS_ARM_V7",
            "windows/arm64": "WINDOWS_ARM64",
            "windows/arm64/v8": "WINDOWS_ARM64_V8",
        }
    
    @schemas.classproperty
    def AIX_PPC64(cls):
        return cls("aix/ppc64")
    
    @schemas.classproperty
    def ANDROID_386(cls):
        return cls("android/386")
    
    @schemas.classproperty
    def ANDROID_AMD64(cls):
        return cls("android/amd64")
    
    @schemas.classproperty
    def ANDROID_ARM(cls):
        return cls("android/arm")
    
    @schemas.classproperty
    def ANDROID_ARM_V5(cls):
        return cls("android/arm/v5")
    
    @schemas.classproperty
    def ANDROID_ARM_V6(cls):
        return cls("android/arm/v6")
    
    @schemas.classproperty
    def ANDROID_ARM_V7(cls):
        return cls("android/arm/v7")
    
    @schemas.classproperty
    def ANDROID_ARM64(cls):
        return cls("android/arm64")
    
    @schemas.classproperty
    def ANDROID_ARM64_V8(cls):
        return cls("android/arm64/v8")
    
    @schemas.classproperty
    def DARWIN_AMD64(cls):
        return cls("darwin/amd64")
    
    @schemas.classproperty
    def DARWIN_ARM(cls):
        return cls("darwin/arm")
    
    @schemas.classproperty
    def DARWIN_ARM_V5(cls):
        return cls("darwin/arm/v5")
    
    @schemas.classproperty
    def DARWIN_ARM_V6(cls):
        return cls("darwin/arm/v6")
    
    @schemas.classproperty
    def DARWIN_ARM_V7(cls):
        return cls("darwin/arm/v7")
    
    @schemas.classproperty
    def DARWIN_ARM64(cls):
        return cls("darwin/arm64")
    
    @schemas.classproperty
    def DARWIN_ARM64_V8(cls):
        return cls("darwin/arm64/v8")
    
    @schemas.classproperty
    def DRAGONFLY_AMD64(cls):
        return cls("dragonfly/amd64")
    
    @schemas.classproperty
    def FREEBSD_386(cls):
        return cls("freebsd/386")
    
    @schemas.classproperty
    def FREEBSD_AMD64(cls):
        return cls("freebsd/amd64")
    
    @schemas.classproperty
    def FREEBSD_ARM(cls):
        return cls("freebsd/arm")
    
    @schemas.classproperty
    def FREEBSD_ARM_V5(cls):
        return cls("freebsd/arm/v5")
    
    @schemas.classproperty
    def FREEBSD_ARM_V6(cls):
        return cls("freebsd/arm/v6")
    
    @schemas.classproperty
    def FREEBSD_ARM_V7(cls):
        return cls("freebsd/arm/v7")
    
    @schemas.classproperty
    def ILLUMOS_AMD64(cls):
        return cls("illumos/amd64")
    
    @schemas.classproperty
    def IOS_ARM64(cls):
        return cls("ios/arm64")
    
    @schemas.classproperty
    def IOS_ARM64_V8(cls):
        return cls("ios/arm64/v8")
    
    @schemas.classproperty
    def JS_WASM(cls):
        return cls("js/wasm")
    
    @schemas.classproperty
    def LINUX_386(cls):
        return cls("linux/386")
    
    @schemas.classproperty
    def LINUX_AMD64(cls):
        return cls("linux/amd64")
    
    @schemas.classproperty
    def LINUX_ARM(cls):
        return cls("linux/arm")
    
    @schemas.classproperty
    def LINUX_ARM_V5(cls):
        return cls("linux/arm/v5")
    
    @schemas.classproperty
    def LINUX_ARM_V6(cls):
        return cls("linux/arm/v6")
    
    @schemas.classproperty
    def LINUX_ARM_V7(cls):
        return cls("linux/arm/v7")
    
    @schemas.classproperty
    def LINUX_ARM64(cls):
        return cls("linux/arm64")
    
    @schemas.classproperty
    def LINUX_ARM64_V8(cls):
        return cls("linux/arm64/v8")
    
    @schemas.classproperty
    def LINUX_LOONG64(cls):
        return cls("linux/loong64")
    
    @schemas.classproperty
    def LINUX_MIPS(cls):
        return cls("linux/mips")
    
    @schemas.classproperty
    def LINUX_MIPSLE(cls):
        return cls("linux/mipsle")
    
    @schemas.classproperty
    def LINUX_MIPS64(cls):
        return cls("linux/mips64")
    
    @schemas.classproperty
    def LINUX_MIPS64LE(cls):
        return cls("linux/mips64le")
    
    @schemas.classproperty
    def LINUX_PPC64(cls):
        return cls("linux/ppc64")
    
    @schemas.classproperty
    def LINUX_PPC64LE(cls):
        return cls("linux/ppc64le")
    
    @schemas.classproperty
    def LINUX_RISCV64(cls):
        return cls("linux/riscv64")
    
    @schemas.classproperty
    def LINUX_S390X(cls):
        return cls("linux/s390x")
    
    @schemas.classproperty
    def LINUX_X86_64(cls):
        return cls("linux/x86_64")
    
    @schemas.classproperty
    def NETBSD_386(cls):
        return cls("netbsd/386")
    
    @schemas.classproperty
    def NETBSD_AMD64(cls):
        return cls("netbsd/amd64")
    
    @schemas.classproperty
    def NETBSD_ARM(cls):
        return cls("netbsd/arm")
    
    @schemas.classproperty
    def NETBSD_ARM_V5(cls):
        return cls("netbsd/arm/v5")
    
    @schemas.classproperty
    def NETBSD_ARM_V6(cls):
        return cls("netbsd/arm/v6")
    
    @schemas.classproperty
    def NETBSD_ARM_V7(cls):
        return cls("netbsd/arm/v7")
    
    @schemas.classproperty
    def OPENBSD_386(cls):
        return cls("openbsd/386")
    
    @schemas.classproperty
    def OPENBSD_AMD64(cls):
        return cls("openbsd/amd64")
    
    @schemas.classproperty
    def OPENBSD_ARM(cls):
        return cls("openbsd/arm")
    
    @schemas.classproperty
    def OPENBSD_ARM_V5(cls):
        return cls("openbsd/arm/v5")
    
    @schemas.classproperty
    def OPENBSD_ARM_V6(cls):
        return cls("openbsd/arm/v6")
    
    @schemas.classproperty
    def OPENBSD_ARM_V7(cls):
        return cls("openbsd/arm/v7")
    
    @schemas.classproperty
    def OPENBSD_ARM64(cls):
        return cls("openbsd/arm64")
    
    @schemas.classproperty
    def OPENBSD_ARM64_V8(cls):
        return cls("openbsd/arm64/v8")
    
    @schemas.classproperty
    def PLAN9_386(cls):
        return cls("plan9/386")
    
    @schemas.classproperty
    def PLAN9_AMD64(cls):
        return cls("plan9/amd64")
    
    @schemas.classproperty
    def PLAN9_ARM(cls):
        return cls("plan9/arm")
    
    @schemas.classproperty
    def PLAN9_ARM_V5(cls):
        return cls("plan9/arm/v5")
    
    @schemas.classproperty
    def PLAN9_ARM_V6(cls):
        return cls("plan9/arm/v6")
    
    @schemas.classproperty
    def PLAN9_ARM_V7(cls):
        return cls("plan9/arm/v7")
    
    @schemas.classproperty
    def SOLARIS_AMD64(cls):
        return cls("solaris/amd64")
    
    @schemas.classproperty
    def WINDOWS_386(cls):
        return cls("windows/386")
    
    @schemas.classproperty
    def WINDOWS_AMD64(cls):
        return cls("windows/amd64")
    
    @schemas.classproperty
    def WINDOWS_ARM(cls):
        return cls("windows/arm")
    
    @schemas.classproperty
    def WINDOWS_ARM_V5(cls):
        return cls("windows/arm/v5")
    
    @schemas.classproperty
    def WINDOWS_ARM_V6(cls):
        return cls("windows/arm/v6")
    
    @schemas.classproperty
    def WINDOWS_ARM_V7(cls):
        return cls("windows/arm/v7")
    
    @schemas.classproperty
    def WINDOWS_ARM64(cls):
        return cls("windows/arm64")
    
    @schemas.classproperty
    def WINDOWS_ARM64_V8(cls):
        return cls("windows/arm64/v8")
