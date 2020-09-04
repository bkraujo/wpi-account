# encoding: utf-8

# Standard Library
from abc import ABC

# 3rd Party Library
# Current Folder
from .status import HTTPStatus

# Current Application
from bktools.exception import BKException

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


class WebException(BKException, ABC):
    """
    Root Exception for the Web layer.
    """

    def __init__(self, code: str, message: str, status: HTTPStatus):
        super().__init__(code, message)
        self.status = status


class UserCausedWebException(WebException, ABC):
    """
    User-Caused Exceptions.
    """
    pass


class BadRequestException(UserCausedWebException):
    def __init__(self, code: str, message: str):
        super().__init__(code, message, HTTPStatus.BAD_REQUEST)


class UnauthorizedException(UserCausedWebException):
    def __init__(self, code: str, message: str):
        super().__init__(code, message, HTTPStatus.UNAUTHORIZED)


class ForbiddenException(UserCausedWebException):
    def __init__(self, code: str, message: str):
        super().__init__(code, message, HTTPStatus.FORBIDDEN)


class NotFoundException(UserCausedWebException):
    def __init__(self, code: str, message: str):
        super().__init__(code, message, HTTPStatus.NOT_FOUND)


class ConflictException(UserCausedWebException):
    def __init__(self, code: str, message: str):
        super().__init__(code, message, HTTPStatus.CONFLICT)


class UnprocessableEntityException(UserCausedWebException):
    def __init__(self, code: str, message: str):
        super().__init__(code, message, HTTPStatus.UNPROCESSABLE_ENTITY)


class SystemCausedWebException(WebException, ABC):
    """
    System-Caused Exceptions.
    """
    pass


class InternalServerErrorException(SystemCausedWebException):
    def __init__(self, code: str, message: str):
        super().__init__(code, message, HTTPStatus.INTERNAL_SERVER_ERROR)


class NotImplementedException(SystemCausedWebException):
    def __init__(self, code: str, message: str):
        super().__init__(code, message, HTTPStatus.NOT_IMPLEMENTED)


class ServiceUnavailableException(SystemCausedWebException):
    def __init__(self, code: str, message: str):
        super().__init__(code, message, HTTPStatus.SERVICE_UNAVAILABLE)
