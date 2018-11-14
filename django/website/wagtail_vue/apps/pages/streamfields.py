"""Streamfields for Wagtail Pages."""
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock


class RichTextBlock(blocks.RichTextBlock):
    """Rich text content."""

    class Meta:
        """Provide additional meta information."""

        icon = "edit"
        label = "Richtext"


class ButtonBlock(blocks.StructBlock):
    """Button block."""

    text = blocks.CharBlock(required=True)
    page = blocks.PageChooserBlock(required=False)
    document = DocumentChooserBlock(required=False)
    external_link = blocks.CharBlock(required=False)

    class Meta:
        """Provide attional meta information."""

        icon = "link"
        label = "Button"


class ImageBlock(blocks.StructBlock):
    """Image Content."""
    POSITIONS_LRF_OPTIONS = (
        ('left', 'Left'),
        ('right', 'Right'),
        ('full', 'Full'),
    )

    image = ImageChooserBlock(required=True)
    caption = blocks.CharBlock(required=False)
    align = blocks.ChoiceBlock(choices=POSITIONS_LRF_OPTIONS)

    class Meta:
        """Provide attional meta information."""

        icon = "image"
        label= "Image"


class ContentBlock(blocks.StructBlock):
    """
    Content - stream block example
        - Richtext
        - Image (center, left, right)
        - Button
    """

    content = blocks.StreamBlock([
        ('RichTextBlock', RichTextBlock()),
        ('ButtonBlock', ButtonBlock()),
        ('ImageBlock', ImageBlock()),
    ])

    class Meta:
        """Provide additional meta information."""

        icon = "doc-full"
        label = "Content"


class ImageGalleryBlock(blocks.StructBlock):
    """
    Image Gallery - list block example
        - Image
    """

    images = blocks.ListBlock(blocks.StructBlock([
        ('ImageBlock', ImageChooserBlock(required=True)),
    ]))

    class Meta:
        """Provide additional meta information."""

        icon = "image"
        label = "Image Gallery"


class CallToActionBlock(blocks.StructBlock):
    """
    Call to Action - struct block example
    """

    title = blocks.CharBlock(required=False)
    text = blocks.RichTextBlock(
        features=['h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'ol', 'ul', 'link'], required=False)
    buttons = blocks.ListBlock(ButtonBlock(required=False), default=[])

    class Meta:
        """Provide additional meta information."""

        icon = "pick"
        label = "Call to Action"
