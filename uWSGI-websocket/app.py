# extremely simple version of
# https://github.com/unbit/uwsgi/blob/master/tests/websockets_echo.py

import uwsgi

index_html_template = """
<html>
  <head>
    <script type="text/javascript">
    function init() {
      var i = 0;
      var s = new WebSocket("%s://%s/ws/");
      function showMessage(s) {
        var messageP = document.getElementById('last-message');
        messageP.innerHTML = s;
      }
      s.onopen = function() {
        s.send(i);
        i = i + 1;
      }
      s.onmessage = function(e) {
        showMessage(e.data);
        window.setTimeout(function () {
          s.send(i);
          i = i + 1;
        }, 1500);
      }
      s.onerror = function(e) {
        showMessage(e);
      }
      s.onclose = function() {
        showMessage('(closed)');
      }
    }
    window.onload = init;
    </script>
  </head>
  <body>
    <h1>Last message</h1>
    <p id="last-message">(no message yet)</p>
  </body>
</html>
"""


def application(env, sr):
    ws_scheme = 'ws'
    if 'HTTPS' in env or env['wsgi.url_scheme'] == 'https':
        ws_scheme = 'wss'
    if env['PATH_INFO'] == '/':
        sr('200 OK', [('Content-Type', 'text/html')])
        host = env.get('HTTP_X_FORWARDED_HOST', env['HTTP_HOST'])
        return index_html_template % (ws_scheme, host)
    elif env['PATH_INFO'] == '/ws/':
        uwsgi.websocket_handshake(env['HTTP_SEC_WEBSOCKET_KEY'], env.get('HTTP_ORIGIN', ''))
        while True:
            msg = uwsgi.websocket_recv()
            uwsgi.websocket_send(msg)
    else:
        sr('404 NOT FOUND', [('Content-Type', 'text/plain')])
        return 'Not found'
