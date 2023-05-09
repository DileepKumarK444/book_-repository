from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
# from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel

from wagtail.fields import RichTextField
from django.http import JsonResponse


class AuthorPage(Page):
    # pass
    templates = 'author/author_page.html'
    # max_count = 1
    name = models.CharField(max_length=150, blank=True, null=True)
    description = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("name"),
        FieldPanel("description"),
        # InlinePanel('related_links', heading="Related links", label="Related link"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Add extra variables and return the updated context
        context['author_entries'] = AuthorPage.objects.child_of(self).live()
        return context

    
