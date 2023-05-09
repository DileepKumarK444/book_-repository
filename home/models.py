from django.db import models

from wagtail.models import Page
# home/models.py
from django.db import models

from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    """Home page model."""

    templates = "home/home_page.html"
    max_count = 1

    banner_title = models.CharField(max_length=100, blank=False, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title")
    ]

    class Meta:

        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"