# Django Pydantic Core Integration

## Overview

This project demonstrates how to integrate Pydantic for data validation in a Django project using the `django-pydantic-core` package. With this setup, you can leverage Pydantic’s powerful validation features within Django views, providing a robust way to handle and validate incoming request data.

## Features

- **Pydantic Validation**: Use Pydantic models to validate request data in Django views.
- **Easy Integration**: Simple decorator-based integration with Django's class-based views.
- **Flexible**: Validate request data against Pydantic models before processing.

## Installation

To get started, you'll need to install the `django-pydantic-core` package. You can do this using pip:

```bash
pip install django-pydantic-core
```

## Usages
## 1. Create a Pydantic Model
Define a Pydantic model that describes the expected structure of your request data.
```python
from pydantic import BaseModel, Field

class MyRequestModel(BaseModel):
    name: str
    age: int = Field(..., gt=0)
```
## 2. Use the @pydantic_validator Decorator
Apply the @pydantic_validator decorator to your Django view method to validate incoming request data using the Pydantic model.
```python
from django.http import JsonResponse
from django.views import View
from django.pydantic.decorators import pydantic_validator

class MyView(View):

    @pydantic_validator(MyRequestModel)
    def post(self, request, validated_data):
        # validated_data is an instance of MyRequestModel
        name = validated_data.name
        age = validated_data.age
        
        # Your logic here
        return JsonResponse({"message": "Data is valid", "name": name, "age": age})
```
## Example
Here's a complete example integrating Pydantic validation into a Django class-based view:

```python
from django.http import JsonResponse
from django.views import View
from django_pydantic_core import pydantic_validator
from pydantic import BaseModel, Field

class MyRequestModel(BaseModel):
    name: str
    age: int = Field(..., gt=0)

class MyView(View):

    @pydantic_validator(MyRequestModel)
    def post(self, request, validated_data):
        name = validated_data.name
        age = validated_data.age
        
        # Process validated data
        return JsonResponse({"message": "Data is valid", "name": name, "age": age})
```

## Contributing
Feel free to contribute to this project by submitting issues or pull requests. Ensure that your code follows the project's style guide and includes tests for any new features or bug fixes.

## License
This project is licensed under the MIT License.