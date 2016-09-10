import settings
import cas

client = cas.CASClientV2(
    service_url='http://finzean.57north.org.uk:5000/hub/login/ticket',
    server_url='https://guest.id.57north.org.uk',
)
