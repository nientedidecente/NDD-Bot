import os
import BotExtensions
import pkgutil
import sys
import logging

dirname = "BotExtensions"
logger = logging.getLogger(__name__) 

# Code from: https://stackoverflow.com/questions/14426574/how-to-import-members-of-all-modules-within-a-package/14428820#14428820
def _import_all_modules():
    """ Dynamically imports all modules in this package. """
    import traceback
    import os
    import importlib
    global __all__
    __all__ = []
    globals_, locals_ = globals(), locals()
    logger.debug('--Start--')
    # Dynamically import all the package modules in this file's directory.
    for filename in os.listdir(dirname):
        # Process all python files in directory that don't start
        # with underscore (which also prevents this module from
        # importing itself).
        logger.debug(f'Searching files in {dirname}')
        logger.debug(f'Found {filename}')
        logger.debug(f'Is {filename} a .py file?')
        logger.debug(filename[0] != '_' and filename.split('.')[-1] in ('py'))

        if filename[0] != '_' and filename.split('.')[-1] in ('py'):
            modulename = filename.split('.')[0]  # Filename sans extension.
            logger.debug(f'Split the file from {filename} to {modulename}')

            __name__ = 'BotExtensions'

            package_module = '.'.join([__name__, modulename])
            logger.debug(f'Join string from {__name__} and {modulename} to become {package_module}')

            try:
                module = importlib.import_module(package_module, [modulename])
                logger.debug(f'Importing module. Result {module}')
            except:
                traceback.print_exc()
                raise
            for name in module.__dict__:
                logger.debug(f'Has {name} _, commands, setup, logging or logger in the name?')

                if not name.startswith('_'):

                    if not name == "commands":
                        if not name == "setup":
                            if not name == "logging":
                                if not name == "logger":

                                    globals_[name] = module.__dict__[name]
                                    __all__.append(name)
                    logger.debug(f'No')


    return __all__
    logger.debug('--Stop--')


