## 	flexible page ##
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from streams import blocks

# flexible page class #
class FlexPage(Page):

	template="flex/flex_page.html"

	#@todo add streamfields
	content=StreamField(
		[
			("title_and_text",blocks.TitleAndTextBlock()),
			("full_richtext",blocks.RichtextBlock()),
			("simple_richtext",blocks.SimpleRichtextBlock()),
		],
		null=True,
		blank=True
	)

	subtitle =models.CharField(max_length=100,null=True,blank=True)

	content_panels =Page.content_panels+[
		FieldPanel("subtitle"),
		StreamFieldPanel("content"),
	]

	class Meta():
		verbose_name ="Flex Page",
		verbose_name_plural ="Flex Pages"
		