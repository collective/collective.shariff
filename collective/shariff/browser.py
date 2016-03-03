from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from plone.app.layout.viewlets.common import ViewletBase
import json


class Shariff(BrowserView):

    def __call__(self):
        """ backend view to determine counters next to buttons """
        # XXX: NOT INMPLEMENTED RIGHT NOW
        pass


class ShariffViewlet(ViewletBase):
    index = ViewPageTemplateFile('viewlet.pt')

    def update(self):
        super(ShariffViewlet, self).update()
        b_url = api.portal.get_registry_record(
            'collective.shariff.settings.backend_url')
        if b_url:
            self.backend_url = "{}/{}".format(self.navigation_root_url, b_url)
        self.theme = api.portal.get_registry_record(
            'collective.shariff.settings.theme')
        self.lang = api.portal.get_current_language()
        self.url = self.context.absolute_url()
        self.twitter_via = api.portal.get_registry_record(
            'collective.shariff.settings.twitter_via')
        self.services = json.dumps(api.portal.get_registry_record(
            'collective.shariff.settings.services'))
