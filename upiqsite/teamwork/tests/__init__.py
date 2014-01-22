import unittest2 as unittest


class PkgTest(unittest.TestCase):
    """basic unit tests for package go here"""

    def test_pkg_import(self):
        """test package import, looks like zcml-initialized zope2 product"""
        import upiqsite.teamwork  # noqa (unused import)
        from upiqsite.teamwork.zope2 import initialize  # noqa (unused import)

