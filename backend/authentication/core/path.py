from pathlib import Path
from django.conf import settings
import os

SETTING_DIR = Path(__file__).resolve().parent


class Setting:
    
    def path(self):
        self.project_name = settings.ROOT_URLCONF.split('.')[0]
        self._PROJ_PATH = settings.BASE_DIR / self.project_name
        return self
    
 
    def create_setting(self):
        setting_path = self._PROJ_PATH / 'settings'
        os.makedirs(setting_path , exist_ok=True)
        open(setting_path / '__init__.py' , 'w')
        return setting_path
