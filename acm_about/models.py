from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsearch import index

# Create your models here.
class AboutPage(Page):
	about_title = models.CharField(max_length=50)
	about_bio = RichTextField()

	content_panels = Page.content_panels + [
		FieldPanel('about_title'),
		FieldPanel('about_bio'),
	]

