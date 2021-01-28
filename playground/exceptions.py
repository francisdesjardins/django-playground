from rest_framework import status
from rest_framework.exceptions import APIException


class Http410(APIException):
    status_code = status.HTTP_410_GONE
    default_detail = "The requested resource is no longer available"
    default_code = "gone"
