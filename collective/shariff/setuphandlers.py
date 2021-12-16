# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName

from .decorator import step


@step
def load_and_cook_default_js_and_css(context, logger):
    setup = getToolByName(context, 'portal_setup')
    run_step = setup.runImportStepFromProfile
    info = logger.info
    profiles = ['profile-collective.shariff:default',
                ]
    for xmlname, toolname in [
        ('jsregistry',  'portal_javascripts'),
        ('cssregistry', 'portal_css'),
        ]:
        for profile in profiles:
            info('Profile %(profile)r: %(xmlname)s.xml', locals())
            try:
                run_step(profile, xmlname)
            except Exception as e:
                logger.error('error running %(xmlname)r from %(profile)s',
                             locals())
                logger.error('Exception: %(e)r', locals())
                logger.error('e.args: %s', (e.args,))
                raise
        tool = getToolByName(context, toolname)
        info('toolname %(toolname)r --> tool %(tool)r', locals())
        try:
            tool.cookResources()
        except AttributeError as e:
            logger.error('%(xmlname)s.xml: '
                         'The %(toolname)r tool lacks a cookResources method'
                         ' %(tool)r',
                         locals())
            raise
        else:
            info('%(xmlname)s resources cooked.', locals())

