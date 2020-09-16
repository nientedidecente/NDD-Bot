import os
import sys
import logging.config


logger = logging.getLogger(__name__) 

# Part of the code from: https://stackoverflow.com/questions/14426574/how-to-import-members-of-all-modules-within-a-package/14428820#14428820
def import_all_addons(dirext, dircogs):
    global __all__
    __all__ = []
    logger.debug('--Start--')

    for file in os.listdir(dircogs):
        # Process all python files in directory that don't start
        # with underscore
        logger.debug(f'Searching files in {dircogs}')
        logger.debug(f'Found {file}')
        logger.debug(f'Is {file} a .py file without "_"?')
        logger.debug(file[0] != '_' and file.split('.')[-1] in ('py'))

        if file[0] != '_' and file.split('.')[-1] in ('py'):
            name = file.split('.')[0]  # Filename sans extension.
            logger.debug(f'Split the file name from {file} to {name}')

            extension_name = '.'.join([dircogs, name])
            logger.debug(f'Join string from {dircogs} and {name} to become {extension_name}')

            __all__.append(extension_name)
            logger.debug(f'Insert {extension_name} in the list __all__')

    for file in os.listdir(dirext):
        # Process all python files in directory that don't start
        # with underscore
        logger.debug(f'Searching files in {dirext}')
        logger.debug(f'Found {file}')
        logger.debug(f'Is {file} a .py file without "_"?')
        logger.debug(file[0] != '_' and file.split('.')[-1] in ('py'))

        if file[0] != '_' and file.split('.')[-1] in ('py'):
            name = file.split('.')[0]  # Filename sans extension.
            logger.debug(f'Split the file name from {file} to {name}')

            extension_name = '.'.join([dirext, name])
            logger.debug(f'Join string from {dirext} and {name} to become {extension_name}')

            __all__.append(extension_name)
            logger.debug(f'Insert {extension_name} in the list __all__')

    logger.debug('--End--')
    return __all__

