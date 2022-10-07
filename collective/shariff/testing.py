from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import zope

import collective.shariff


class CollectiveShariffLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.shariff)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "collective.shariff:default")
        portal.portal_workflow.setDefaultChain("simple_publication_workflow")


COLLECTIVE_SHARIFF_FIXTURE = CollectiveShariffLayer()


COLLECTIVE_SHARIFF_INTEGRATION = IntegrationTesting(
    bases=(COLLECTIVE_SHARIFF_FIXTURE,), name="PloneAppMosaic:Integration"
)
