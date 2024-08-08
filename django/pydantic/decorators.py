from functools import wraps
from pydantic import ValidationError as PydanticValidationError
from rest_framework.response import Response


def pydantic_validator(pydantic_model):
    def decorator(func):
        @wraps(func)
        def wrapped(self, request, *args, **kwargs):
            try:
                validated_data = pydantic_model(**request.data)
                request.validated_data = validated_data
            except PydanticValidationError as e:
                return Response(e.errors(), status=400)
            return func(self, request, *args, **kwargs)
        return wrapped
    return decorator
