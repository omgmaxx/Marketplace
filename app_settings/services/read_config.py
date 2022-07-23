import logging
import os

from dynamic_preferences.serializers import BooleanSerializer, StringSerializer
from dynamic_preferences.registries import global_preferences_registry

from iShop.settings import BASE_DIR

logger = logging.getLogger(__name__)
bool_ser = BooleanSerializer()
str_ser = StringSerializer()


class ReadConfig:

    def __init__(self):
        self.global_preferences = global_preferences_registry.manager()
        self._read()

    def _read(self):
        with open(os.path.join(BASE_DIR, 'config.cfg'), 'r') as cfg:
            for pref in cfg:
                try:
                    pref = pref.replace('\n', '').split('=')

                    if pref[0] not in self.global_preferences.keys():
                        raise LookupError

                    try:
                        res = bool_ser.deserialize(pref[1])
                    except bool_ser.exception:
                        res = str_ser.deserialize(pref[1])

                    self.global_preferences[pref[0]] = res

                except LookupError:
                    logger.error(f"Option '{pref[0]}' (from config.cfg) doesn't exist")

                except bool_ser.exception or str_ser.exception as e:
                    logger.error(e)

            logger.info('Config.cfg is deserialized')
