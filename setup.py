from setuptools import setup, find_packages


version = '0.1'

setup(
    name='upiqsite.teamwork',
    version=version,
    description='Policy product for UPIQ-hosted Teamspace sites, '
                'collective.teamwork and Plone 4.3',
    long_description=(
        open("README.txt").read() + "\n" +
        open("CHANGES.txt").read()
        ),
    classifiers=[
        'Framework :: Plone',
        'Programming Language :: Python',
        ],
    keywords='',
    author='Sean Upton',
    author_email='sean.upton@hsc.utah.edu',
    url='http://launchpad.net/upiq',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['upiqsite'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'collective.teamwork',
        'uu.formlibrary',
        'uu.smartdate',
        'collective.inviting',
        'uu.staticmap',
        'uu.chart',
        'uu.eventintegration',
        'Products.qi',
        'Products.CMFPlone>=4.3.2',
        'plone.browserlayer',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
