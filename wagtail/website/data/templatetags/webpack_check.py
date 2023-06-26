"""Webpack Template Tags."""
from django import template

register = template.Library()


@register.filter
def is_from_webpack(request) -> bool:
    """Check if the request was forwarded from webpack."""
    from_webpack = request.META.get("HTTP_X_FROM_WEBPACK", None)
    if from_webpack == "true":
        return True
    else:
        return False
