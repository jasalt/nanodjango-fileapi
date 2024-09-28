import os
import environs
from django.http import FileResponse, HttpResponse
from nanodjango import Django


env = environs.Env()
env.read_env()
API_TOKEN = env.str('API_TOKEN')

UPLOADPATH = './' # should end with slash

app = Django()

# skip linting because of https://github.com/vitalik/django-ninja/issues/1169
from ninja import NinjaAPI             # noqa: E402
from ninja.security import HttpBearer  # noqa: E402

class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        if token == API_TOKEN:
            return token

api = NinjaAPI(auth=AuthBearer())


@api.post('/upload')
def upload(request, file: app.ninja.File[app.ninja.UploadedFile]):
    data = file.read()
    # write data into file with same name as it was sent with

    with open(UPLOADPATH + file.name, 'wb') as f:
        f.write(data)

    return {'name': file.name, 'len': len(data)}


@api.get('/download')
def download(request, file: str):

    if not os.path.exists(UPLOADPATH + file):
        return HttpResponse(status=404)

    return FileResponse(open(UPLOADPATH + file, 'rb'))


app.route("api/", include=api.urls)
