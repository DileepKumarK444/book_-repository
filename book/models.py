from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.search import index
from author.models import AuthorPage

class BookPage(Page):

    # Database fields

    body = RichTextField()
    book_name = models.CharField(max_length=100,blank=True,null=True)
    book_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    # Search index configuration

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('book_name'),
    ]


    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('book_name'),
        FieldPanel('body'),
        FieldPanel('book_image'),
        # InlinePanel('related_links', heading="Related links", label="Related link"),
    ]

    # @route(r"^search/$")
    # def post_search(self, request, *args, **kwargs):
    #     search_query = request.GET.get("q", None)
    #     self.posts = self.get_posts()
    #     if search_query:
    #         self.posts = self.posts.search(search_query)
    #     return self.render(request)


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Add extra variables and return the updated context
        context['book_entries'] = BookPage.objects.child_of(self).live()
        return context
