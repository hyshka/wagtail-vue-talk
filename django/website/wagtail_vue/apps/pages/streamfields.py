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


class CarouselBlock(blocks.StreamBlock):
    """
    Example of a StreamBlock.

    Similar to a ListBlock, but allows multiple streams to be used inside
    of this stream.

    This is straight from the docs to demo an eample StreamBlock:
    http://docs.wagtail.io/en/latest/topics/streamfield.html#streamblock
    """

    image = ImageChooserBlock()
    quotation = blocks.StructBlock([
        ('text', blocks.TextBlock()),
        ('author', blocks.CharBlock()),
    ])

    class Meta:
        """Provide additional meta information."""

        icon = 'cogs'
        label = "Carousel"
        template = "cms/pages/streamfields/carousel.html"
