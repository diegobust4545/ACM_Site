from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


# Create your models here.
class CommitteePage(Page):
	committee_title = models.CharField(max_length = 50)
	committee_bio = RichTextField()

	content_panels = Page.content_panels + [
		FieldPanel('committee_title'),
		FieldPanel('committee_bio')
	]