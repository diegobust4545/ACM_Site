from __future__ import unicode_literals

from django.db import models

# Import from wagtail
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page
from wagtailnews.decorators import newsindex
from wagtailnews.models import NewsIndexMixin

# Create your models here.
class IndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
    ]



class EventPage(Page):
    representative_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    body = RichTextField(blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full'),
    ]