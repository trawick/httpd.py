from django.http import HttpResponse

PATH_VARS = ('PATH_INFO', 'PATH_TRANSLATED', 'SCRIPT_FILENAME',
             'REQUEST_URI', 'SCRIPT_URI')


def cgivars(request):
    return HttpResponse('<br />'.join(map(lambda x: '%s => %s' %
        (x, request.environ.get(x, '&lt;unset&gt;')), PATH_VARS))
    )


def protected(request):
    filename = '/static/protected/index.html'
    response = HttpResponse()
    # Django will turn this into Location: http://127.0.0.1:18083/static/protected/foo
    #     response['Location'] = filename

    # This is passed through unadulterated:
    response['X-Location'] = filename
    return response


def sendfile(request):
    filename = request.environ['DOCUMENT_ROOT'] + '/' + 'bigfile.html'
    response = HttpResponse()
    response['X-Sendfile'] = filename
    return response
