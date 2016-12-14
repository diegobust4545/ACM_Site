from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

# Create your models here.
class ConstitutionPage(Page):
	constitution_description =RichTextField()

	content_panels = Page.content_panels + [
		FieldPanel('constitution_description')
	]