# -*- coding: utf-8 -*-
"""Page models."""
from wagtail.admin.edit_handlers import (
    FieldPanel,
)
from wagtail.core.models import Page
from wagtail.api import APIField



class HomePage(Page):
    """A home page class."""

    template = "cms/pages/home_page.html"
    subpage_types = []

    content_panels = [
        FieldPanel("title", classname="full title"),
    ]

    api_fields = [
        APIField("title"),
    ]

    class Meta:
        """Meta information."""

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
