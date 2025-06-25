from django.http import HttpResponse
from django.views import generic

class PostView(generic.View):
    """
    A view that handles HTTP requests for blog posts.
    """
    
    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to the post view.
        """
        return HttpResponse("Hello World!")