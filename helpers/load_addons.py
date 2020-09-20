import os
import sys
import logging.config

import helpers.config as config
from helpers.import_addons import import_all_addons


logger = logging.getLogger(__name__) 


def load_addons(bot):

    index = 0

    if config.addonsEnabled == True:


        for addon in import_all_addons(config.addons_dir):
            logger.debug(f'Importing extension {addon}')

            try:
                bot.load_extension('{}'.format(addon))

            except:
                logger.error(f'Unable to load addon "{addon}". Check the logs for more info')
                logger.debug(f'Error: {sys.exc_info()}')


            config.addons_list[index] = addon
            index += 1


    else:
        logger.debug('Addons are disabled. Ignoring')
    return index