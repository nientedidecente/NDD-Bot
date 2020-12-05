import os
import sys
import logging.config

import helpers.config as config
from helpers.import_extensions import import_all_exts


logger = logging.getLogger(__name__) 


def load_exts(bot):

    index = 0

    if config.extensionsEnabled == True:


        for extension in import_all_exts(config.exts_dir):
            logger.debug(f'Importing extension {extension}')

            try:
                bot.load_extension('{}'.format(extension))

            except:
                logger.error(f'Unable to load extension "{extension}". Check the logs for more info')
                logger.debug(f'Error: {sys.exc_info()}')


            config.exts_list[index] = extension
            index += 1


    else:
        logger.debug('Extensions are disabled. Ignoring')
    return index