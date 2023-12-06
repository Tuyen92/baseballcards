import xmlrpc.client
import base64


class OdooConnection():
    url = 'https://odoo-staging.gbcvn2.local'
    db = 'live_database'
    username = 'employee.profile.service.user'
    password = '4dCFFh9cNy'
    common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
    uid = common.authenticate(db, username, password, {})
    model = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
