import os
import sys
import logging.config

import func.vars as v

logger = logging.getLogger(__name__) 


def load_addons():

    index = 0

    if v.addonsEnabled == True:


        for addon in v.import_all_ext.import_all_ext('BotExt', 'BotCogs'):
            logger.debug(f'Importing extension {addon}')

            try:
                v.client.load_extension('{}'.format(addon))

            except:
                logger.error(f'Unable to load addon "{addon}". Check the logs for more info')
                logger.debug(f'Error: {sys.exc_info()}')


            addons_list[index] = addon
            index += 1


    else:
        logger.debug('Addons are disabled. Ignoring')
    return index