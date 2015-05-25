# httpd.py
## Examples of deploying Python web applications behind httpd

These examples correspond with [my presentations on deploying Python applications with httpd](https://emptyhammock.com/projects/info/slides.html).

If using httpd prior to 2.4.13, mod\_proxy\_scgi must be patched with ```mod_proxy_scgi-X-Location-patch.txt``` 
for the redirect-to-protected-file feature to work.

## Change history

### May 16, 2015

* Update for httpd 2.4.13, which has a configuration enhancement which eliminates the need for the patch.
* Correct the name of the patch file.
* Add WebSocket example using uWSGI's WebSocket API.

### April 14, 2015

* Initial version, for presentation at ApacheCon US 2015
