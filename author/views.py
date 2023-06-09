from django.shortcuts import render

from wagtail.models import AuthorPage
from wagtail.search.models import Query


def search(request):
    # Search
    print('Test')
    search_query = request.GET.get('query', None)
    if search_query:
        search_results = AuthorPage.objects.live().search(search_query)

        # Log the query so Wagtail can suggest promoted results
        Query.get(search_query).add_hit()
    else:
        search_results = Page.objects.none()

    # Render template
    return render(request, 'search_results.html', {
        'search_query': search_query,
        'search_results': search_results,
    })