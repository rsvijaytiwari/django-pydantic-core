from setuptools import setup


setup(
    name="django-pydantic-core",
    version="1.0.0",
    description="Pydantic support for Django and Django Rest Framework",
    author="Vijay Tiwari",
    author_email="rsvijaytiwari@gmail.com",
    packages=["django", "django.pydantic"],
    install_requires=[
        "django", "pydantic", "djangorestframework"
    ]
)