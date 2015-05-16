# httpd.py
## Examples of deploying Python web applications behind httpd

If using httpd prior to 2.4.13, mod\_proxy\_scgi must be patched with ```mod_proxy_scgi-X-Location-patch.txt``` 
for the redirect-to-protected-file feature to work.

## Change history

### May 16, 2015

* Update for httpd 2.4.13, which has a configuration enhancement which eliminates the need for the patch.
* Correct the name of the patch file.
* Add websocket example using uWSGI's websocket API.

### April 14, 2015

* Initial version, for presentation at ApacheCon US 2015
