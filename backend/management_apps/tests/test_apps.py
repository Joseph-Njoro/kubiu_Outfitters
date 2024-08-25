from django.apps import apps
from django.test import TestCase
from management_apps.apps import ManagementAppsConfig

class TestApps(TestCase):
    def test_apps(self):
        app_config = apps.get_app_config('management_apps')
        self.assertEqual(app_config.name, 'management_apps')
        self.assertIsInstance(app_config, ManagementAppsConfig)
