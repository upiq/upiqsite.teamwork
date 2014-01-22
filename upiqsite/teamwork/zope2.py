
def initialize(context):
    """called to make this a Zope 2 product package"""
    from plugin import register_plugins
    register_plugins()  # collective.teamwork workgroup type plugin(s)

