import requests
import datetime
from tools.mongodb import mongodb_last_user


def plugin_diagnostic():
    user_name = mongodb_last_user(data='user_name')
    api_key = mongodb_last_user(data='api_key')
    url = 'https://' + user_name + '.triggmine.com.ua/control/api/plugin/onDiagnosticInformationUpdated'
    headers = {
        'ApiKey': api_key
    }
    data = {
        'dateCreated': datetime.datetime.now(),
        'diagnosticType': "InstallPlugin",
        'description': "Magento 1.9.2.4",
        'status': '1'
    }
    r = requests.post(url, data, headers=headers)
    print(r.status_code)
    if r.status_code != 201:
        raise Exception('Not created! ' + str(r.status_code))
    else:
        pass

