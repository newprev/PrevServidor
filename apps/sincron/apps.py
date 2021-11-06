from django.apps import AppConfig
from django import db
from typing import List


class SincronConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.sincron'

    def ready(self):
        nomesTabelas: List[str] = db.connection.introspection.table_names()
        if 'sincron_syncipca' in nomesTabelas:
            from apps.sincron.scheduler.syncronizer import iniciaSync
            iniciaSync()
        else:
            pass
