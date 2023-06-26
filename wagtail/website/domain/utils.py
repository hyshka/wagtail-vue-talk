"""Shared utilities."""

from typing import Type

from django.db import models
from django.utils.text import slugify


def generate_unique_slug(klass: Type[models.Model], field: str) -> str:
    """Return a unique slug.

    return unique slug if origin slug is exist.
    eg: `foo-bar` => `foo-bar-1`
    """
    origin_slug = slugify(field)
    unique_slug = origin_slug
    num = 1
    while klass.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{origin_slug}-{num}"
        num += 1
    return unique_slug
