import logging
import os

from dynamic_preferences.registries import global_preferences_registry

from iShop.settings import BASE_DIR

logger = logging.getLogger(__name__)


class SaveConfig:

    def __init__(self):
        self.global_preferences = global_preferences_registry.manager()
        self._read()

    def _read(self):
        with open(os.path.join(BASE_DIR, 'config.cfg'), 'w') as cfg:
            for pref, value in self.global_preferences.items():
                cfg.write(f'{pref}={value}\n')
            logger.warning('config.cfg is updated')
