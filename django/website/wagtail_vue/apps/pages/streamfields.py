"""Streamfields for Wagtail Pages."""
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ImageBlock(ImageChooserBlock):
    """Single image block. Inherits directly from ImageChooserBlock."""

    class Meta:
        """Provide additional meta information."""

        template = "cms/pages/streamfields/image.html"
        icon = "image"
        label = "Image"


class RichTextBlock(blocks.RichTextBlock):
    """Rich text content."""

    class Meta:
        """Provide additional meta information."""

        template = "cms/pages/streamfields/richtext.html"
        icon = "edit"
        label = "Richtext"


class CardsBlock(blocks.StructBlock):
    """Unlimited cards with a title, limited richtext, and an image field."""

    card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True)),
                (
                    "content",
                    blocks.RichTextBlock(
                        features=["bold", "italic", "ol", "ul"],
                        required=False,
                    ),
                ),
                ("image", ImageChooserBlock(required=True)),
                ("page", blocks.PageChooserBlock(required=True)),
            ]
        )
    )

    class Meta:
        """Provide additional meta information."""

        template = "cms/pages/streamfields/richtext.html"
        icon = "edit"
        label = "Nested Streamfields"
