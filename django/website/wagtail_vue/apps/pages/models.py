# -*- coding: utf-8 -*-
"""Page models."""
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField


class HomePage(Page):
    """A home page class."""

    template = "cms/pages/home_page.html"
    subpage_types = ['pages.FlexPage']

    banner_subtitle = models.CharField(
        max_length=50, blank=True, null=True, help_text="An optional banner subtitle"
    )
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="An optional banner image",
    )
    content_panels = [
        FieldPanel("title", classname="full title"),
        ImageChooserPanel("banner_image"),
        FieldPanel("banner_subtitle"),
    ]

    api_fields = [
        APIField("title"),
        APIField("banner_subtitle"),
        APIField("banner_image"),
        APIField("banner_image_thumbnail", serializer=ImageRenditionField("fill-100x100", source="banner_image")),
    ]

    class Meta:
        """Meta information."""

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


class FlexPage(Page):
    """A Flexible page class. Used for generic pages that don't have a true purpose."""

    template = "cms/pages/flex_page.html"
    subpage_types = []

    content_panels = [
        FieldPanel("title", classname="full title"),
    ]

    api_fields = [
        APIField("title"),
    ]

    class Meta:
        """Meta information."""

        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
