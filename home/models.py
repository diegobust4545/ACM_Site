from __future__ import absolute_import, unicode_literals
from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsearch import index

class Home(Page):
    body = RichTextField()
    date = models.DateField("Post date")
    search_name = "Home Page"
    indexed_fields = ('body', )

Home.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('date'),
    FieldPanel('body', classname="full"),
]

