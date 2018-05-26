import logging
import os

from django.views.generic import View
from django.http import HttpResponse
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
            logging.exception('Production build of app not found')
            return HttpResponse(f'<p>This URL is only used when you have built the production version of the app.<br>Try <a href="{settings.REACT_APP_URL[0]}">the dev frontend</a>, or run `yarn run build` to test the production version.</p>',
                                status=501)
