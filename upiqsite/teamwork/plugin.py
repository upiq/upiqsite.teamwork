from zope.component import queryUtility

from collective.teamwork.user.config import add_workgroup_type
from collective.teamwork.user.interfaces import IWorkgroupTypes


ADDITIONAL_GROUP_TYPES = {
    'forms': {
        'groupid': u'forms',
        'title': u'Form entry',
        'description': u'Form entry and submission for workspace context.',
        'roles': [u'FormEntry'],
    }
}


def register_plugins():
    config = queryUtility(IWorkgroupTypes)  # global registry workgroup types
    for k, v in ADDITIONAL_GROUP_TYPES.items():
        if k not in config:
            add_workgroup_type(k, v)
            assert k in config

