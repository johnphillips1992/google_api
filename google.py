from os.path import join
import json

import httplib2

from django.conf import settings

from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials



class Google:
    def get_calendar_service():
        build_path = getattr(settings, 'BUILDOUT_PATH', None)

        f = file(join(build_path, 'bin', 'privatekey.p12'), 'rb')
        key = f.read()
        f.close()

        credentials = SignedJwtAssertionCredentials(
            '1011061772239-mbdnrio274bt33i4k2cfj5dvpq6d4lv1@developer.gserviceaccount.com',
            key,
            scope='https://www.googleapis.com/auth/calendar.readonly',
            sub='john.phillips1992@gmail.com')

        http = httplib2.Http()
        http = credentials.authorize(http)

        service = build(serviceName='calendar', version='v3', http=http)
        return service
