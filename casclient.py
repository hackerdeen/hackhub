import settings
import cas

client = cas.CASClientV2(
    service_url=settings.CAS_SERVICE_URL,
    server_url=settings.CAS_SERVER_URL,
)
