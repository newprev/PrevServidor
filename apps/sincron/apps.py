import datetime

from django.apps import AppConfig
from django import db
from typing import List


class SincronConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.sincron'

    def ready(self):
        nomesTabelas: List[str] = db.connection.introspection.table_names()
        if 'SyncIpca' in nomesTabelas:
            from apps.sincron.scheduler.syncronizer import iniciaSync
            from apps.sincron.models import SyncIpca

            try:
                qtdSync: int = SyncIpca.objects.latest('dataSync')
                print(qtdSync)
                iniciaSync()

            except SyncIpca.DoesNotExist as err:
                print("Deu certo!")
                iniciaSync(primeiroSync=True)
        else:
            pass
