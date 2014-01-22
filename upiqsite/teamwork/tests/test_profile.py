import unittest2 as unittest

from plone.app.testing import TEST_USER_ID, setRoles
from Products.CMFPlone.utils import getToolByName

from collective.teamwork.content.interfaces import PROJECT_TYPE
from collective.teamwork.content.interfaces import WORKSPACE_TYPE
from layers import DEFAULT_PROFILE_TESTING


class DefaultProfileTest(unittest.TestCase):
    """Test default profile's installed configuration settings"""

    THEME = 'Sunburst Theme'

    layer = DEFAULT_PROFILE_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.wftool = getToolByName(self.portal, 'portal_workflow')
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def _product_fti_names(self):
        """ test types used by collective.teamwork """
        return (PROJECT_TYPE, WORKSPACE_TYPE)

    def test_browserlayer(self):
        """Test product layer interfaces are registered for site"""
        from collective.teamwork.interfaces import ITeamworkProductLayer
        from upiqsite.teamwork.interfaces import IUPIQTeamworkSiteProductLayer
        from plone.browserlayer.utils import registered_layers
        self.assertTrue(ITeamworkProductLayer in registered_layers())
        self.assertTrue(IUPIQTeamworkSiteProductLayer in registered_layers())

    def test_ftis(self):
        types_tool = getToolByName(self.portal, 'portal_types')
        typenames = types_tool.objectIds()
        for name in self._product_fti_names():
            self.assertTrue(name in typenames)
        assert types_tool.getTypeInfo(PROJECT_TYPE).Title() == 'Project'
        assert types_tool.getTypeInfo(WORKSPACE_TYPE).Title() == 'Team'

    def test_skin_layer(self):
        names = ('main_template', 'upiqsite.teamwork.txt')
        tool = self.portal['portal_skins']
        self.assertTrue('upiqsite_teamwork' in tool)
        skin = tool.getSkin(self.THEME)
        path = tool.getSkinPath(self.THEME).split(',')
        # check order in path:
        self.assertEqual(path[0], 'custom')
        self.assertEqual(path[1], 'upiqsite_teamwork')
        # get known objects from skin layer and from portal:
        for name in names:
            self.assertTrue(getattr(skin, name, None) is not None)
            self.assertTrue(getattr(self.portal, name, None) is not None)

