from django.apps import AppConfig


class DjangoSiteStylerAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_site_styler_admin'
    verbose_name = 'Site Styler Admin'

    def ready(self):
        print(self.verbose_name + ' is ready!')
