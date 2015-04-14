from flask import Flask, Response, request, send_file

app = Flask(__name__)
app.use_x_sendfile = True


PATH_VARS = ('PATH_INFO', 'PATH_TRANSLATED', 'SCRIPT_FILENAME', 
             'REQUEST_URI', 'SCRIPT_URI')


@app.route('/app/cgivars/')
def cgivars():
    return '<br />'.join(map(lambda x: '%s => %s' %
        (x, request.environ.get(x, '&lt;unset&gt;')), PATH_VARS))


@app.route('/app/protected/')
def protected():
    filename = '/static/protected/index.html'
    rsp = Response()

    # Flask/Werkzeug will turn this into Location: http://127.0.0.1:18082/static/protected/foo
    #     rsp.headers['Location'] = '/protected/' + filename
    # This is passed through unadulterated:
    rsp.headers['X-Location'] = filename
    return rsp


@app.route('/app/sendfile/')
def sendfile():
    filename = request.environ['DOCUMENT_ROOT'] + '/' + 'bigfile.html'
    # This sets content-length to 0 so httpd sends 0 bytes from
    # the file.
    #
    # rsp = Response()
    # rsp.headers['X-Sendfile'] = filename
    # return rsp

    # This sets content-length from the actual file (and X-Sendfile).
    # It requires <app>.use_x_sendfile = True
    return send_file(filename)


# Just for debug...
if __name__ == '__main__':
    app.run()
