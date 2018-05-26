import logging
import os

from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings


class ReactAppView(View):
    """
    Serves the compiled frontend entry point (only works if you have run `yarn run build`).
    """

    def get(self, request):
        """ GET React view. """
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            return HttpResponseRedirect(f"{settings.REACT_APP_URL[0]}")
