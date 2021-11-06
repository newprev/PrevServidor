from apscheduler.schedulers.background import BackgroundScheduler
from apps.sincron.views import SyncIpcaViewSet
from pytz import timezone


def iniciaSync():
    scheduler = BackgroundScheduler(timezone=timezone('America/Sao_Paulo'))
    syncIpca = SyncIpcaViewSet()
    scheduler.add_job(syncIpca.buscaIpcas, 'interval', minutes=43800, id='sync_001', replace_existing=True)
    scheduler.start()
