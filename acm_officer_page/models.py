from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailcore.models import Orderable

# Create your models here.
class OfficersPage(Page):
	officer_title = models.CharField(max_length = 50)
	officer_picture = models.FileField(null=True, blank=True)
	officer_facebook = models.TextField(null=True, blank=True)
	officer_linkedin = models.TextField(null=True, blank=True)
	officer_twitter = models.TextField(null=True, blank=True)
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	officer_bio = RichTextField()

	content_panels = Page.content_panels + [
		FieldPanel('first_name'),
		FieldPanel('last_name'),
		FieldPanel('officer_title'),
		FieldPanel('officer_picture'),
		FieldPanel('officer_facebook'),
		FieldPanel('officer_linkedin'),
		FieldPanel('officer_twitter'),
		FieldPanel('officer_bio'),
	]

	@property
	def officers(self):
		officers = OfficersPage.objects.live().descendant_of(self)
		officers = officers.order_by('-date')
		return officers

