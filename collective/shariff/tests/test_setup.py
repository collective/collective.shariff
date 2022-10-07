from collective.shariff.testing import COLLECTIVE_SHARIFF_INTEGRATION
from plone.browserlayer.utils import registered_layers
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.utils import get_installer
from zope.component import getUtility

import unittest


PROJECTNAME = "collective.shariff"
RECORDS = [
    "{}.settings.backend_url".format(PROJECTNAME),
    "{}.settings.theme".format(PROJECTNAME),
    "{}.settings.services".format(PROJECTNAME),
    "{}.settings.twitter_via".format(PROJECTNAME),
]


class InstallTestCase(unittest.TestCase):

    layer = COLLECTIVE_SHARIFF_INTEGRATION

    def setUp(self):
        self.portal = self.layer["portal"]

    def test_installed(self):
        if get_installer is None:
            qi = self.portal["portal_quickinstaller"]
        else:
            qi = get_installer(self.portal)
        self.assertTrue(qi.is_product_installed(PROJECTNAME))

    def test_addon_layer(self):
        layers = [layer.getName() for layer in registered_layers()]
        self.assertIn("IShariffInstalled", layers)

    def test_registry(self):
        registry = getUtility(IRegistry)
        for r in RECORDS:
            self.assertIn(r, registry)


class UninstallTestCase(unittest.TestCase):

    layer = COLLECTIVE_SHARIFF_INTEGRATION

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer is None:
            self.qi = self.portal["portal_quickinstaller"]
        else:
            self.qi = get_installer(self.portal)
        self.qi.uninstall_product(PROJECTNAME)

    def test_uninstalled(self):
        self.assertFalse(self.qi.is_product_installed(PROJECTNAME))

    def test_addon_layer_removed(self):
        layers = [layer.getName() for layer in registered_layers()]
        self.assertNotIn("IShariffInstalled", layers)

    def test_registry_cleaned(self):
        registry = getUtility(IRegistry)
        for r in RECORDS:
            self.assertNotIn(r, registry)
