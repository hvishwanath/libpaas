__author__ = 'hvishwanath'

import requests
from .base import BasePaaSProvider, ArtifactHandler


class OpenShift(BasePaaSProvider):
    def __init__(self, name):
        pass

    def install_app(self, appid, path_to_pdp):
        pass

    def start_app(self, appid):
        pass

    def stop_app(self, appid):
        pass

    def uninstall_app(self, appid):
        pass

    def list_apps(self):
        pass

    def get_app_info(self, appid):
        pass

    def list_services(self):
        pass

    def list_env_vars(self):
        pass

    def getenv(self, key):
        pass

    def setenv(self, key, value):
        pass


class HerokuPythonArtifactHandler(ArtifactHandler):
    pass


class HerokuJavaArtifactHandler(ArtifactHandler):
    pass


