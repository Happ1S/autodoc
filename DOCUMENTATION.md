# Сгенерированная документация

## Модуль [`docs/_themes/flask_theme_support.py`](https://github.com/Happ1S/autodoc/blob/main/docs/_themes/flask_theme_support.py)
_Докстрока отсутствует._
### Класс `FlaskyStyle`

_Докстрока отсутствует._

## Модуль [`docs/conf.py`](https://github.com/Happ1S/autodoc/blob/main/docs/conf.py)
_Докстрока отсутствует._

## Модуль [`setup.py`](https://github.com/Happ1S/autodoc/blob/main/setup.py)
_Докстрока отсутствует._

## Модуль [`src/requests/__init__.py`](https://github.com/Happ1S/autodoc/blob/main/src/requests/__init__.py)
Requests HTTP Library
~~~~~~~~~~~~~~~~~~~~~

Requests is an HTTP library, written in Python, for human beings.
Basic GET usage:

   >>> import requests
   >>> r = requests.get('https://www.python.org')
   >>> r.status_code
   200
   >>> b'Python is a programming language' in r.content
   True

... or POST:

   >>> payload = dict(key1='value1', key2='value2')
   >>> r = requests.post('https://httpbin.org/post', data=payload)
   >>> print(r.text)
   {
     ...
     "form": {
       "key1": "value1",
       "key2": "value2"
     },
     ...
   }

The other HTTP methods are supported - see `requests.api`. Full documentation
is at <https://requests.readthedocs.io>.

:copyright: (c) 2017 by Kenneth Reitz.
:license: Apache 2.0, see LICENSE for more details.
### Функция `check_compatibility(urllib3_version, chardet_version, charset_normalizer_version)`

_Докстрока отсутствует._
### Функция `_check_cryptography(cryptography_version)`

_Докстрока отсутствует._

## Модуль [`src/requests/__version__.py`](https://github.com/Happ1S/autodoc/blob/main/src/requests/__version__.py)
_Докстрока отсутствует._

## Модуль [`src/requests/_internal_utils.py`](https://github.com/Happ1S/autodoc/blob/main/src/requests/_internal_utils.py)
requests._internal_utils
~~~~~~~~~~~~~~

Provides utility functions that are consumed internally by Requests
which depend on extremely few external helpers (such as compat)
### Функция `to_native_string(string, encoding)`

Given a string object, regardless of type, returns a representation of
that string in the native string type, encoding and decoding where
necessary. This assumes ASCII unless told otherwise.
### Функция `unicode_is_ascii(u_string)`

Determine if unicode string only contains ASCII characters.

:param str u_string: unicode string to check. Must be unicode
    and not Python 2 `str`.
:rtype: bool

## Модуль [`src/requests/adapters.py`](https://github.com/Happ1S/autodoc/blob/main/src/requests/adapters.py)
requests.adapters
~~~~~~~~~~~~~~~~~

This module contains the transport adapters that Requests uses to define
and maintain connections.
### Функция `_urllib3_request_context(request, verify, client_cert, poolmanager)`

_Докстрока отсутствует._
### Класс `BaseAdapter`

The Base Transport Adapter
### Класс `HTTPAdapter`

The built-in HTTP Adapter for urllib3.

Provides a general-case interface for Requests sessions to contact HTTP and
HTTPS urls by implementing the Transport Adapter interface. This class will
usually be created by the :class:`Session <Session>` class under the
covers.

:param pool_connections: The number of urllib3 connection pools to cache.
:param pool_maxsize: The maximum number of connections to save in the pool.
:param max_retries: The maximum number of retries each connection
    should attempt. Note, this applies only to failed DNS lookups, socket
    connections and connection timeouts, never to requests where data has
    made it to the server. By default, Requests does not retry failed
    connections. If you need granular control over the conditions under
    which we retry a request, import urllib3's ``Retry`` class and pass
    that instead.
:param pool_block: Whether the connection pool should block for connections.

Usage::

  >>> import requests
  >>> s = requests.Session()
  >>> a = requests.adapters.HTTPAdapter(max_retries=3)
  >>> s.mount('http://', a)

## Модуль [`src/requests/api.py`](https://github.com/Happ1S/autodoc/blob/main/src/requests/api.py)
requests.api
~~~~~~~~~~~~

This module implements the Requests API.

:copyright: (c) 2012 by Kenneth Reitz.
:license: Apache2, see LICENSE for more details.
### Функция `request(method, url, **kwargs)`

Constructs and sends a :class:`Request <Request>`.

:param method: method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
:param url: URL for the new :class:`Request` object.
:param params: (optional) Dictionary, list of tuples or bytes to send
    in the query string for the :class:`Request`.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
:param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
:param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
:param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
    ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
    or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content_type'`` is a string
    defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
    to add for the file.
:param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
:param timeout: (optional) How many seconds to wait for the server to send data
    before giving up, as a float, or a :ref:`(connect timeout, read
    timeout) <timeouts>` tuple.
:type timeout: float or tuple
:param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``.
:type allow_redirects: bool
:param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
:param verify: (optional) Either a boolean, in which case it controls whether we verify
        the server's TLS certificate, or a string, in which case it must be a path
        to a CA bundle to use. Defaults to ``True``.
:param stream: (optional) if ``False``, the response content will be immediately downloaded.
:param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
:return: :class:`Response <Response>` object
:rtype: requests.Response

Usage::

  >>> import requests
  >>> req = requests.request('GET', 'https://httpbin.org/get')
  >>> req
  <Response [200]>
### Функция `get(url, params, **kwargs)`

Sends a GET request.

:param url: URL for the new :class:`Request` object.
:param params: (optional) Dictionary, list of tuples or bytes to send
    in the query string for the :class:`Request`.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:return: :class:`Response <Response>` object
:rtype: requests.Response
### Функция `options(url, **kwargs)`

Sends an OPTIONS request.

:param url: URL for the new :class:`Request` object.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:return: :class:`Response <Response>` object
:rtype: requests.Response
### Функция `head(url, **kwargs)`

Sends a HEAD request.

:param url: URL for the new :class:`Request` object.
:param \*\*kwargs: Optional arguments that ``request`` takes. If
    `allow_redirects` is not provided, it will be set to `False` (as
    opposed to the default :meth:`request` behavior).
:return: :class:`Response <Response>` object
:rtype: requests.Response
### Функция `post(url, data, json, **kwargs)`

Sends a POST request.

:param url: URL for the new :class:`Request` object.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:return: :class:`Response <Response>` object
:rtype: requests.Response
### Функция `put(url, data, **kwargs)`

Sends a PUT request.

:param url: URL for the new :class:`Request` object.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:return: :class:`Response <Response>` object
:rtype: requests.Response
### Функция `patch(url, data, **kwargs)`

Sends a PATCH request.

:param url: URL for the new :class:`Request` object.
:param data: (optional) Dictionary, list of tuples, bytes, or file-like
    object to send in the body of the :class:`Request`.
:param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:return: :class:`Response <Response>` object
:rtype: requests.Response
### Функция `delete(url, **kwargs)`

Sends a DELETE request.

:param url: URL for the new :class:`Request` object.
:param \*\*kwargs: Optional arguments that ``request`` takes.
:return: :class:`Response <Response>` object
:rtype: requests.Response

## Модуль [`src/requests/auth.py`](https://github.com/Happ1S/autodoc/blob/main/src/requests/auth.py)
requests.auth
~~~~~~~~~~~~~

This module contains the authentication handlers for Requests.
### Функция `_basic_auth_str(username, password)`

Returns a Basic Auth string.
### Класс `AuthBase`

Base class that all auth implementations derive from
### Класс `HTTPBasicAuth`

Attaches HTTP Basic Authentication to the given Request object.
### Класс `HTTPProxyAuth`

Attaches HTTP Proxy Authentication to a given Request object.
### Класс `HTTPDigestAuth`

Attaches HTTP Digest Authentication to the given Request object.

## Модуль [`src/requests/certs.py`](https://github.com/Happ1S/autodoc/blob/main/src/requests/certs.py)
requests.certs
~~~~~~~~~~~~~~

This module returns the preferred default CA certificate bundle. There is
only one — the one from the certifi package.

If you are packaging Requests, e.g., for a Linux distribution or a managed
environment, you can change the definition of where() to return a separately
packaged CA bundle.

## Модуль [`src/requests/compat.py`](https://github.com/Happ1S/autodoc/blob/main/src/requests/compat.py)
requests.compat
~~~~~~~~~~~~~~~

This module previously handled import compatibility issues
between Python 2 and Python 3. It remains for backwards
compatibility until the next major version.
### Функция `_resolve_char_detection()`

Find supported character detection libraries.

## Модуль [`src/requests/cookies.py`](https://github.com/Happ1S/autodoc/blob/main/src/requests/cookies.py)
requests.cookies
~~~~~~~~~~~~~~~~

Compatibility code to be able to use `http.cookiejar.CookieJar` with requests.

requests.utils imports from here, so be careful with imports.
### Класс `MockRequest`

Wraps a `requests.Request` to mimic a `urllib2.Request`.

The code in `http.cookiejar.CookieJar` expects this interface in order to correctly
manage cookie policies, i.e., determine whether a cookie can be set, given the
domains of the request and the cookie.

The original request object is read-only. The client is responsible for collecting
the new headers via `get_new_headers()` and interpreting them appropriately. You
probably want `get_cookie_header`, defined below.
### Класс `MockResponse`

Wraps a `httplib.HTTPMessage` to mimic a `urllib.addinfourl`.

...what? Basically, expose the parsed HTTP headers from the server response
the way `http.cookiejar` expects to see them.
### Функция `extract_cookies_to_jar(jar, request, response)`

Extract the cookies from the response into a CookieJar.

:param jar: http.cookiejar.CookieJar (not necessarily a RequestsCookieJar)
:param request: our own requests.Request object
:param response: urllib3.HTTPResponse object
### Функция `get_cookie_header(jar, request)`

Produce an appropriate Cookie header string to be sent with `request`, or None.

:rtype: str
### Функция `remove_cookie_by_name(cookiejar, name, domain, path)`

Unsets a cookie by name, by default over all domains and paths.

Wraps CookieJar.clear(), is O(n).
### Класс `CookieConflictError`

There are two cookies that meet the criteria specified in the cookie jar.
Use .get and .set and include domain and path args in order to be more specific.
### Класс `RequestsCookieJar`

Compatibility class; is a http.cookiejar.CookieJar, but exposes a dict
interface.

This is the CookieJar we create by default for requests and sessions that
don't specify one, since some clients may expect response.cookies and
session.cookies to support dict operations.

Requests does not use the dict interface internally; it's just for
compatibility with external client code. All requests code should work
out of the box with externally provided instances of ``CookieJar``, e.g.
``LWPCookieJar`` and ``FileCookieJar``.

Unlike a regular CookieJar, this class is pickleable.

.. warning:: dictionary operations that are normally O(1) may be O(n).
### Функция `_copy_cookie_jar(jar)`

_Докстрока отсутствует._
### Функция `create_cookie(name, value, **kwargs)`

Make a cookie from underspecified parameters.

By default, the pair of `name` and `value` will be set for the domain ''
and sent on every request (this is sometimes called a "supercookie").
### Функция `morsel_to_cookie(morsel)`

Convert a Morsel object into a Cookie containing the one k/v pair.
### Функция `cookiejar_from_dict(cookie_dict, cookiejar, overwrite)`

Returns a CookieJar from a key/value dictionary.

:param cookie_dict: Dict of key/values to insert into CookieJar.
:param cookiejar: (optional) A cookiejar to add the cookies to.
:param overwrite: (optional) If False, will not replace cookies
    already in the jar with new ones.
:rtype: CookieJar
### Функция `merge_cookies(cookiejar, cookies)`

Add cookies to cookiejar and returns a merged CookieJar.

:param cookiejar: CookieJar object to add the cookies to.
:param cookies: Dictionary or CookieJar object to be added.
:rtype: CookieJar

## Модуль [`src/requests/exceptions.py`](https://github.com/Happ1S/autodoc/blob/main/src/requests/exceptions.py)
requests.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the set of Requests' exceptions.
### Класс `RequestException`

There was an ambiguous exception that occurred while handling your
request.
### Класс `InvalidJSONError`

A JSON error occurred.
### Класс `JSONDecodeError`

Couldn't decode the text into json
### Класс `HTTPError`

An HTTP error occurred.
### Класс `ConnectionError`

A Connection error occurred.
### Класс `ProxyError`

A proxy error occurred.
### Класс `SSLError`

An SSL error occurred.
### Класс `Timeout`

The request timed out.

Catching this error will catch both
:exc:`~requests.exceptions.ConnectTimeout` and
:exc:`~requests.exceptions.ReadTimeout` errors.
### Класс `ConnectTimeout`

The request timed out while trying to connect to the remote server.

Requests that produced this error are safe to retry.
### Класс `ReadTimeout`

The server did not send any data in the allotted amount of time.
### Класс `URLRequired`

A valid URL is required to make a request.
### Класс `TooManyRedirects`

Too many redirects.
### Класс `MissingSchema`

The URL scheme (e.g. http or https) is missing.
### Класс `InvalidSchema`

The URL scheme provided is either invalid or unsupported.
### Класс `InvalidURL`

The URL provided was somehow invalid.
### Класс `InvalidHeader`

The header value provided was somehow invalid.
### Класс `InvalidProxyURL`

The proxy URL provided is invalid.
### Класс `ChunkedEncodingError`

The server declared chunked encoding but sent an invalid chunk.
### Класс `ContentDecodingError`

Failed to decode response content.
### Класс `StreamConsumedError`

The content for this response was already consumed.
### Класс `RetryError`

Custom retries logic failed
### Класс `UnrewindableBodyError`

Requests encountered an error when trying to rewind a body.
### Класс `RequestsWarning`

Base warning for Requests.
### Класс `FileModeWarning`

A file was opened in text mode, but Requests determined its binary length.
### Класс `RequestsDependencyWarning`

An imported dependency doesn't match the expected version range.

## Модуль [`src/requests/help.py`](https://github.com/Happ1S/autodoc/blob/main/src/requests/help.py)
Module containing bug report helper(s).
### Функция `_implementation()`

Return a dict with the Python implementation and version.

Provide both the name and the version of the Python implementation
currently running. For example, on CPython 3.10.3 it will return
{'name': 'CPython', 'version': '3.10.3'}.

This function works best on CPython and PyPy: in particular, it probably
doesn't work for Jython or IronPython. Future investigation should be done
to work out the correct shape of the code for those platforms.
### Функция `info()`

Generate information for a bug report.
### Функция `main()`

Pretty-print the bug information as JSON.

## Модуль [`src/requests/hooks.py`](https://github.com/Happ1S/autodoc/blob/main/src/requests/hooks.py)
requests.hooks
~~~~~~~~~~~~~~

This module provides the capabilities for the Requests hooks system.

Available hooks:

``response``:
    The response generated from a Request.
### Функция `default_hooks()`

_Докстрока отсутствует._
### Функция `dispatch_hook(key, hooks, hook_data, **kwargs)`

Dispatches a hook dictionary on a given piece of data.

## Модуль [`src/requests/models.py`](https://github.com/Happ1S/autodoc/blob/main/src/requests/models.py)
requests.models
~~~~~~~~~~~~~~~

This module contains the primary objects that power Requests.
### Класс `RequestEncodingMixin`

_Докстрока отсутствует._
### Класс `RequestHooksMixin`

_Докстрока отсутствует._
### Класс `Request`

A user-created :class:`Request <Request>` object.

Used to prepare a :class:`PreparedRequest <PreparedRequest>`, which is sent to the server.

:param method: HTTP method to use.
:param url: URL to send.
:param headers: dictionary of headers to send.
:param files: dictionary of {filename: fileobject} files to multipart upload.
:param data: the body to attach to the request. If a dictionary or
    list of tuples ``[(key, value)]`` is provided, form-encoding will
    take place.
:param json: json for the body to attach to the request (if files or data is not specified).
:param params: URL parameters to append to the URL. If a dictionary or
    list of tuples ``[(key, value)]`` is provided, form-encoding will
    take place.
:param auth: Auth handler or (user, pass) tuple.
:param cookies: dictionary or CookieJar of cookies to attach to this request.
:param hooks: dictionary of callback hooks, for internal usage.

Usage::

  >>> import requests
  >>> req = requests.Request('GET', 'https://httpbin.org/get')
  >>> req.prepare()
  <PreparedRequest [GET]>
### Класс `PreparedRequest`

The fully mutable :class:`PreparedRequest <PreparedRequest>` object,
containing the exact bytes that will be sent to the server.

Instances are generated from a :class:`Request <Request>` object, and
should not be instantiated manually; doing so may produce undesirable
effects.

Usage::

  >>> import requests
  >>> req = requests.Request('GET', 'https://httpbin.org/get')
  >>> r = req.prepare()
  >>> r
  <PreparedRequest [GET]>

  >>> s = requests.Session()
  >>> s.send(r)
  <Response [200]>
### Класс `Response`

The :class:`Response <Response>` object, which contains a
server's response to an HTTP request.

## Модуль [`src/requests/packages.py`](https://github.com/Happ1S/autodoc/blob/main/src/requests/packages.py)
_Докстрока отсутствует._

## Модуль [`src/requests/sessions.py`](https://github.com/Happ1S/autodoc/blob/main/src/requests/sessions.py)
requests.sessions
~~~~~~~~~~~~~~~~~

This module provides a Session object to manage and persist settings across
requests (cookies, auth, proxies).
### Функция `merge_setting(request_setting, session_setting, dict_class)`

Determines appropriate setting for a given request, taking into account
the explicit setting on that request, and the setting in the session. If a
setting is a dictionary, they will be merged together using `dict_class`
### Функция `merge_hooks(request_hooks, session_hooks, dict_class)`

Properly merges both requests and session hooks.

This is necessary because when request_hooks == {'response': []}, the
merge breaks Session hooks entirely.
### Класс `SessionRedirectMixin`

_Докстрока отсутствует._
### Класс `Session`

A Requests session.

Provides cookie persistence, connection-pooling, and configuration.

Basic Usage::

  >>> import requests
  >>> s = requests.Session()
  >>> s.get('https://httpbin.org/get')
  <Response [200]>

Or as a context manager::

  >>> with requests.Session() as s:
  ...     s.get('https://httpbin.org/get')
  <Response [200]>
### Функция `session()`

Returns a :class:`Session` for context-management.

.. deprecated:: 1.0.0

    This method has been deprecated since version 1.0.0 and is only kept for
    backwards compatibility. New code should use :class:`~requests.sessions.Session`
    to create a session. This may be removed at a future date.

:rtype: Session

## Модуль [`src/requests/status_codes.py`](https://github.com/Happ1S/autodoc/blob/main/src/requests/status_codes.py)
The ``codes`` object defines a mapping from common names for HTTP statuses
to their numerical codes, accessible either as attributes or as dictionary
items.

Example::

    >>> import requests
    >>> requests.codes['temporary_redirect']
    307
    >>> requests.codes.teapot
    418
    >>> requests.codes['\o/']
    200

Some codes have multiple names, and both upper- and lower-case versions of
the names are allowed. For example, ``codes.ok``, ``codes.OK``, and
``codes.okay`` all correspond to the HTTP status code 200.
### Функция `_init()`

_Докстрока отсутствует._

## Модуль [`src/requests/structures.py`](https://github.com/Happ1S/autodoc/blob/main/src/requests/structures.py)
requests.structures
~~~~~~~~~~~~~~~~~~~

Data structures that power Requests.
### Класс `CaseInsensitiveDict`

A case-insensitive ``dict``-like object.

Implements all methods and operations of
``MutableMapping`` as well as dict's ``copy``. Also
provides ``lower_items``.

All keys are expected to be strings. The structure remembers the
case of the last key to be set, and ``iter(instance)``,
``keys()``, ``items()``, ``iterkeys()``, and ``iteritems()``
will contain case-sensitive keys. However, querying and contains
testing is case insensitive::

    cid = CaseInsensitiveDict()
    cid['Accept'] = 'application/json'
    cid['aCCEPT'] == 'application/json'  # True
    list(cid) == ['Accept']  # True

For example, ``headers['content-encoding']`` will return the
value of a ``'Content-Encoding'`` response header, regardless
of how the header name was originally stored.

If the constructor, ``.update``, or equality comparison
operations are given keys that have equal ``.lower()``s, the
behavior is undefined.
### Класс `LookupDict`

Dictionary lookup object.

## Модуль [`src/requests/utils.py`](https://github.com/Happ1S/autodoc/blob/main/src/requests/utils.py)
requests.utils
~~~~~~~~~~~~~~

This module provides utility functions that are used within Requests
that are also useful for external consumption.
### Функция `dict_to_sequence(d)`

Returns an internal sequence dictionary update.
### Функция `super_len(o)`

_Докстрока отсутствует._
### Функция `get_netrc_auth(url, raise_errors)`

Returns the Requests tuple auth for a given url from netrc.
### Функция `guess_filename(obj)`

Tries to guess the filename of the given object.
### Функция `extract_zipped_paths(path)`

Replace nonexistent paths that look like they refer to a member of a zip
archive with the location of an extracted copy of the target, or else
just return the provided path unchanged.
### Функция `atomic_open(filename)`

Write a file to the disk in an atomic fashion
### Функция `from_key_val_list(value)`

Take an object and test to see if it can be represented as a
dictionary. Unless it can not be represented as such, return an
OrderedDict, e.g.,

::

    >>> from_key_val_list([('key', 'val')])
    OrderedDict([('key', 'val')])
    >>> from_key_val_list('string')
    Traceback (most recent call last):
    ...
    ValueError: cannot encode objects that are not 2-tuples
    >>> from_key_val_list({'key': 'val'})
    OrderedDict([('key', 'val')])

:rtype: OrderedDict
### Функция `to_key_val_list(value)`

Take an object and test to see if it can be represented as a
dictionary. If it can be, return a list of tuples, e.g.,

::

    >>> to_key_val_list([('key', 'val')])
    [('key', 'val')]
    >>> to_key_val_list({'key': 'val'})
    [('key', 'val')]
    >>> to_key_val_list('string')
    Traceback (most recent call last):
    ...
    ValueError: cannot encode objects that are not 2-tuples

:rtype: list
### Функция `parse_list_header(value)`

Parse lists as described by RFC 2068 Section 2.

In particular, parse comma-separated lists where the elements of
the list may include quoted-strings.  A quoted-string could
contain a comma.  A non-quoted string could have quotes in the
middle.  Quotes are removed automatically after parsing.

It basically works like :func:`parse_set_header` just that items
may appear multiple times and case sensitivity is preserved.

The return value is a standard :class:`list`:

>>> parse_list_header('token, "quoted value"')
['token', 'quoted value']

To create a header from the :class:`list` again, use the
:func:`dump_header` function.

:param value: a string with a list header.
:return: :class:`list`
:rtype: list
### Функция `parse_dict_header(value)`

Parse lists of key, value pairs as described by RFC 2068 Section 2 and
convert them into a python dict:

>>> d = parse_dict_header('foo="is a fish", bar="as well"')
>>> type(d) is dict
True
>>> sorted(d.items())
[('bar', 'as well'), ('foo', 'is a fish')]

If there is no value for a key it will be `None`:

>>> parse_dict_header('key_without_value')
{'key_without_value': None}

To create a header from the :class:`dict` again, use the
:func:`dump_header` function.

:param value: a string with a dict header.
:return: :class:`dict`
:rtype: dict
### Функция `unquote_header_value(value, is_filename)`

Unquotes a header value.  (Reversal of :func:`quote_header_value`).
This does not use the real unquoting but what browsers are actually
using for quoting.

:param value: the header value to unquote.
:rtype: str
### Функция `dict_from_cookiejar(cj)`

Returns a key/value dictionary from a CookieJar.

:param cj: CookieJar object to extract cookies from.
:rtype: dict
### Функция `add_dict_to_cookiejar(cj, cookie_dict)`

Returns a CookieJar from a key/value dictionary.

:param cj: CookieJar to insert cookies into.
:param cookie_dict: Dict of key/values to insert into CookieJar.
:rtype: CookieJar
### Функция `get_encodings_from_content(content)`

Returns encodings from given content string.

:param content: bytestring to extract encodings from.
### Функция `_parse_content_type_header(header)`

Returns content type and parameters from given header

:param header: string
:return: tuple containing content type and dictionary of
     parameters
### Функция `get_encoding_from_headers(headers)`

Returns encodings from given HTTP Header Dict.

:param headers: dictionary to extract encoding from.
:rtype: str
### Функция `stream_decode_response_unicode(iterator, r)`

Stream decodes an iterator.
### Функция `iter_slices(string, slice_length)`

Iterate over slices of a string.
### Функция `get_unicode_from_response(r)`

Returns the requested content back in unicode.

:param r: Response object to get unicode content from.

Tried:

1. charset from content-type
2. fall back and replace all unicode characters

:rtype: str
### Функция `unquote_unreserved(uri)`

Un-escape any percent-escape sequences in a URI that are unreserved
characters. This leaves all reserved, illegal and non-ASCII bytes encoded.

:rtype: str
### Функция `requote_uri(uri)`

Re-quote the given URI.

This function passes the given URI through an unquote/quote cycle to
ensure that it is fully and consistently quoted.

:rtype: str
### Функция `address_in_network(ip, net)`

This function allows you to check if an IP belongs to a network subnet

Example: returns True if ip = 192.168.1.1 and net = 192.168.1.0/24
         returns False if ip = 192.168.1.1 and net = 192.168.100.0/24

:rtype: bool
### Функция `dotted_netmask(mask)`

Converts mask from /xx format to xxx.xxx.xxx.xxx

Example: if mask is 24 function returns 255.255.255.0

:rtype: str
### Функция `is_ipv4_address(string_ip)`

:rtype: bool
### Функция `is_valid_cidr(string_network)`

Very simple check of the cidr format in no_proxy variable.

:rtype: bool
### Функция `set_environ(env_name, value)`

Set the environment variable 'env_name' to 'value'

Save previous value, yield, and then restore the previous value stored in
the environment variable 'env_name'.

If 'value' is None, do nothing
### Функция `should_bypass_proxies(url, no_proxy)`

Returns whether we should bypass proxies or not.

:rtype: bool
### Функция `get_environ_proxies(url, no_proxy)`

Return a dict of environment proxies.

:rtype: dict
### Функция `select_proxy(url, proxies)`

Select a proxy for the url, if applicable.

:param url: The url being for the request
:param proxies: A dictionary of schemes or schemes and hosts to proxy URLs
### Функция `resolve_proxies(request, proxies, trust_env)`

This method takes proxy information from a request and configuration
input to resolve a mapping of target proxies. This will consider settings
such as NO_PROXY to strip proxy configurations.

:param request: Request or PreparedRequest
:param proxies: A dictionary of schemes or schemes and hosts to proxy URLs
:param trust_env: Boolean declaring whether to trust environment configs

:rtype: dict
### Функция `default_user_agent(name)`

Return a string representing the default user agent.

:rtype: str
### Функция `default_headers()`

:rtype: requests.structures.CaseInsensitiveDict
### Функция `parse_header_links(value)`

Return a list of parsed link headers proxies.

i.e. Link: <http:/.../front.jpeg>; rel=front; type="image/jpeg",<http://.../back.jpeg>; rel=back;type="image/jpeg"

:rtype: list
### Функция `guess_json_utf(data)`

:rtype: str
### Функция `prepend_scheme_if_needed(url, new_scheme)`

Given a URL that may or may not have a scheme, prepend the given scheme.
Does not replace a present scheme with the one provided as an argument.

:rtype: str
### Функция `get_auth_from_url(url)`

Given a url with authentication components, extract them into a tuple of
username,password.

:rtype: (str,str)
### Функция `check_header_validity(header)`

Verifies that header parts don't contain leading whitespace
reserved characters, or return characters.

:param header: tuple, in the format (name, value).
### Функция `_validate_header_part(header, header_part, header_validator_index)`

_Докстрока отсутствует._
### Функция `urldefragauth(url)`

Given a url remove the fragment and the authentication part.

:rtype: str
### Функция `rewind_body(prepared_request)`

Move file pointer back to its recorded starting position
so it can be read again on redirect.

## Модуль [`tests/__init__.py`](https://github.com/Happ1S/autodoc/blob/main/tests/__init__.py)
Requests test package initialisation.

## Модуль [`tests/compat.py`](https://github.com/Happ1S/autodoc/blob/main/tests/compat.py)
_Докстрока отсутствует._
### Функция `u(s)`

_Докстрока отсутствует._

## Модуль [`tests/conftest.py`](https://github.com/Happ1S/autodoc/blob/main/tests/conftest.py)
_Докстрока отсутствует._
### Функция `prepare_url(value)`

_Докстрока отсутствует._
### Функция `httpbin(httpbin)`

_Докстрока отсутствует._
### Функция `httpbin_secure(httpbin_secure)`

_Докстрока отсутствует._
### Функция `nosan_server(tmp_path_factory)`

_Докстрока отсутствует._

## Модуль [`tests/test_adapters.py`](https://github.com/Happ1S/autodoc/blob/main/tests/test_adapters.py)
_Докстрока отсутствует._
### Функция `test_request_url_trims_leading_path_separators()`

See also https://github.com/psf/requests/issues/6643.

## Модуль [`tests/test_help.py`](https://github.com/Happ1S/autodoc/blob/main/tests/test_help.py)
_Докстрока отсутствует._
### Функция `test_system_ssl()`

Verify we're actually setting system_ssl when it should be available.
### Класс `VersionedPackage`

_Докстрока отсутствует._
### Функция `test_idna_without_version_attribute()`

Older versions of IDNA don't provide a __version__ attribute, verify
that if we have such a package, we don't blow up.
### Функция `test_idna_with_version_attribute()`

Verify we're actually setting idna version when it should be available.

## Модуль [`tests/test_hooks.py`](https://github.com/Happ1S/autodoc/blob/main/tests/test_hooks.py)
_Докстрока отсутствует._
### Функция `hook(value)`

_Докстрока отсутствует._
### Функция `test_hooks(hooks_list, result)`

_Докстрока отсутствует._
### Функция `test_default_hooks()`

_Докстрока отсутствует._

## Модуль [`tests/test_lowlevel.py`](https://github.com/Happ1S/autodoc/blob/main/tests/test_lowlevel.py)
_Докстрока отсутствует._
### Функция `echo_response_handler(sock)`

Simple handler that will take request and echo it back to requester.
### Функция `test_chunked_upload()`

can safely send generators
### Функция `test_chunked_encoding_error()`

get a ChunkedEncodingError if the server returns a bad response
### Функция `test_chunked_upload_uses_only_specified_host_header()`

Ensure we use only the specified Host header for chunked requests.
### Функция `test_chunked_upload_doesnt_skip_host_header()`

Ensure we don't omit all Host headers with chunked requests.
### Функция `test_conflicting_content_lengths()`

Ensure we correctly throw an InvalidHeader error if multiple
conflicting Content-Length headers are returned.
### Функция `test_digestauth_401_count_reset_on_redirect()`

Ensure we correctly reset num_401_calls after a successful digest auth,
followed by a 302 redirect to another digest auth prompt.

See https://github.com/psf/requests/issues/1979.
### Функция `test_digestauth_401_only_sent_once()`

Ensure we correctly respond to a 401 challenge once, and then
stop responding if challenged again.
### Функция `test_digestauth_only_on_4xx()`

Ensure we only send digestauth on 4xx challenges.

See https://github.com/psf/requests/issues/3772.
### Функция `test_use_proxy_from_environment(httpbin, var, scheme)`

_Докстрока отсутствует._
### Функция `test_redirect_rfc1808_to_non_ascii_location()`

_Докстрока отсутствует._
### Функция `test_fragment_not_sent_with_request()`

Verify that the fragment portion of a URI isn't sent to the server.
### Функция `test_fragment_update_on_redirect()`

Verify we only append previous fragment if one doesn't exist on new
location. If a new fragment is encountered in a Location header, it should
be added to all subsequent requests.
### Функция `test_json_decode_compatibility_for_alt_utf_encodings()`

_Докстрока отсутствует._

## Модуль [`tests/test_packages.py`](https://github.com/Happ1S/autodoc/blob/main/tests/test_packages.py)
_Докстрока отсутствует._
### Функция `test_can_access_urllib3_attribute()`

_Докстрока отсутствует._
### Функция `test_can_access_idna_attribute()`

_Докстрока отсутствует._
### Функция `test_can_access_chardet_attribute()`

_Докстрока отсутствует._

## Модуль [`tests/test_requests.py`](https://github.com/Happ1S/autodoc/blob/main/tests/test_requests.py)
Tests for Requests.
### Класс `TestRequests`

_Докстрока отсутствует._
### Класс `TestCaseInsensitiveDict`

_Докстрока отсутствует._
### Класс `TestMorselToCookieExpires`

Tests for morsel_to_cookie when morsel contains expires.
### Класс `TestMorselToCookieMaxAge`

Tests for morsel_to_cookie when morsel contains max-age.
### Класс `TestTimeout`

_Докстрока отсутствует._
### Класс `RedirectSession`

_Докстрока отсутствует._
### Функция `test_json_encodes_as_bytes()`

_Докстрока отсутствует._
### Функция `test_requests_are_updated_each_time(httpbin)`

_Докстрока отсутствует._
### Функция `test_proxy_env_vars_override_default(var, url, proxy)`

_Докстрока отсутствует._
### Функция `test_data_argument_accepts_tuples(data)`

Ensure that the data argument will accept tuples of strings
and properly encode them.
### Функция `test_prepared_copy(kwargs)`

_Докстрока отсутствует._
### Функция `test_urllib3_retries(httpbin)`

_Докстрока отсутствует._
### Функция `test_urllib3_pool_connection_closed(httpbin)`

_Докстрока отсутствует._
### Класс `TestPreparingURLs`

_Докстрока отсутствует._
### Функция `test_content_length_for_bytes_data(httpbin)`

_Докстрока отсутствует._
### Функция `test_content_length_for_string_data_counts_bytes(httpbin)`

_Докстрока отсутствует._
### Функция `test_json_decode_errors_are_serializable_deserializable()`

_Докстрока отсутствует._

## Модуль [`tests/test_structures.py`](https://github.com/Happ1S/autodoc/blob/main/tests/test_structures.py)
_Докстрока отсутствует._
### Класс `TestCaseInsensitiveDict`

_Докстрока отсутствует._
### Класс `TestLookupDict`

_Докстрока отсутствует._

## Модуль [`tests/test_testserver.py`](https://github.com/Happ1S/autodoc/blob/main/tests/test_testserver.py)
_Докстрока отсутствует._
### Класс `TestTestServer`

_Докстрока отсутствует._

## Модуль [`tests/test_utils.py`](https://github.com/Happ1S/autodoc/blob/main/tests/test_utils.py)
_Докстрока отсутствует._
### Класс `TestSuperLen`

_Докстрока отсутствует._
### Класс `TestToKeyValList`

_Докстрока отсутствует._
### Класс `TestUnquoteHeaderValue`

_Докстрока отсутствует._
### Класс `TestGetEnvironProxies`

Ensures that IP addresses are correctly matches with ranges
in no_proxy variable.
### Класс `TestIsIPv4Address`

_Докстрока отсутствует._
### Класс `TestIsValidCIDR`

_Докстрока отсутствует._
### Класс `TestAddressInNetwork`

_Докстрока отсутствует._
### Класс `TestGuessFilename`

_Докстрока отсутствует._
### Класс `TestExtractZippedPaths`

_Докстрока отсутствует._
### Класс `TestContentEncodingDetection`

_Докстрока отсутствует._
### Класс `TestGuessJSONUTF`

_Докстрока отсутствует._
### Функция `test_get_auth_from_url(url, auth)`

_Докстрока отсутствует._
### Функция `test_requote_uri_with_unquoted_percents(uri, expected)`

See: https://github.com/psf/requests/issues/2356
### Функция `test_unquote_unreserved(uri, expected)`

_Докстрока отсутствует._
### Функция `test_dotted_netmask(mask, expected)`

_Докстрока отсутствует._
### Функция `test_select_proxies(url, expected, proxies)`

Make sure we can select per-host proxies correctly.
### Функция `test_parse_dict_header(value, expected)`

_Докстрока отсутствует._
### Функция `test__parse_content_type_header(value, expected)`

_Докстрока отсутствует._
### Функция `test_get_encoding_from_headers(value, expected)`

_Докстрока отсутствует._
### Функция `test_iter_slices(value, length)`

_Докстрока отсутствует._
### Функция `test_parse_header_links(value, expected)`

_Докстрока отсутствует._
### Функция `test_prepend_scheme_if_needed(value, expected)`

_Докстрока отсутствует._
### Функция `test_to_native_string(value, expected)`

_Докстрока отсутствует._
### Функция `test_urldefragauth(url, expected)`

_Докстрока отсутствует._
### Функция `test_should_bypass_proxies(url, expected, monkeypatch)`

Tests for function should_bypass_proxies to check if proxy
can be bypassed or not
### Функция `test_should_bypass_proxies_pass_only_hostname(url, expected)`

The proxy_bypass function should be called with a hostname or IP without
a port number or auth credentials.
### Функция `test_add_dict_to_cookiejar(cookiejar)`

Ensure add_dict_to_cookiejar works for
non-RequestsCookieJar CookieJars
### Функция `test_unicode_is_ascii(value, expected)`

_Докстрока отсутствует._
### Функция `test_should_bypass_proxies_no_proxy(url, expected, monkeypatch)`

Tests for function should_bypass_proxies to check if proxy
can be bypassed or not using the 'no_proxy' argument
### Функция `test_should_bypass_proxies_win_registry(url, expected, override, monkeypatch)`

Tests for function should_bypass_proxies to check if proxy
can be bypassed or not with Windows registry settings
### Функция `test_should_bypass_proxies_win_registry_bad_values(monkeypatch)`

Tests for function should_bypass_proxies to check if proxy
can be bypassed or not with Windows invalid registry settings.
### Функция `test_set_environ(env_name, value)`

Tests set_environ will set environ values and will restore the environ.
### Функция `test_set_environ_raises_exception()`

Tests set_environ will raise exceptions in context when the
value parameter is None.
### Функция `test_should_bypass_proxies_win_registry_ProxyOverride_value(monkeypatch)`

Tests for function should_bypass_proxies to check if proxy
can be bypassed or not with Windows ProxyOverride registry value ending with a semicolon.

## Модуль [`tests/testserver/__init__.py`](https://github.com/Happ1S/autodoc/blob/main/tests/testserver/__init__.py)
_Докстрока отсутствует._

## Модуль [`tests/testserver/server.py`](https://github.com/Happ1S/autodoc/blob/main/tests/testserver/server.py)
_Докстрока отсутствует._
### Функция `consume_socket_content(sock, timeout)`

_Докстрока отсутствует._
### Класс `Server`

Dummy server using for unit testing
### Класс `TLSServer`

_Докстрока отсутствует._

## Модуль [`tests/utils.py`](https://github.com/Happ1S/autodoc/blob/main/tests/utils.py)
_Докстрока отсутствует._
### Функция `override_environ(**kwargs)`

_Докстрока отсутствует._
