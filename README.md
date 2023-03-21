# HTTP Headers

The **http-headers** python package can be used to generate random yet realistic request headers. It is inspired by the excellent [ua-parser](https://github.com/faisalman/ua-parser-js), [apify](https://github.com/apify/header-generator), and [fake-http-header](https://github.com/MichaelTatarski/fake-http-header/tree/main/fake_http_header) repositories, and it emulates real browser behaviour for the following header fields:

* User-Agent
* Referer
* Accept
* Accept-Language
* Accept-Encoding
* Sec-Fetch-Site
* Sec-Fetch-Mode
* Sec-Fetch-User
* Sec-Fetch-Dest
* Upgrade-Insecure-Requests
* Connection

In addition, it supports the following [Client Hints](https://wicg.github.io/client-hints-infrastructure/):
* Sec-CH-UA
* Sec-CH-UA-Arch
* Sec-CH-UA-Bitness
* Sec-CH-UA-Full-Version-List
* Sec-CH-UA-Mobile
* Sec-CH-UA-Model
* Sec-CH-UA-Platform
* Sec-CH-UA-Platform-Version

The generated headers conform to http-version specific ordering and support [rules](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers), and are browser-, version-, and locale- compatible and specific. 
In particular, the user can choose between the following:

* domains: 
    * com, jsp, edu, org, info, net, php3, aspx, biz, uk, it,
                    is,  ua,  cc,  de,  us,   tv,  eu,   ru,   cn,  jp, nl, be,  
                    fr,  ch,  gr,  se,  dk,   bg,  cz,   hu,   lt,  pl, ro, sk, 
                    si,  br,  pt,  es,  il,   au,  io,   no,   ir,  at
* Browsers
                * str containing one of: chrome, edge, firefox, safari
                * Empty: random selection among all
* Devices
                * str containing one of: mobile, desktop
                * Empty: random selection among all
* HTTP version (int), can be either 1 (supports both 1.0 and 1.1) 2, or
                empty which defaults to 1
        
If not supplied, domain is chosen randomly, whereas browser and device are chosen in line with modern browser market share [data](https://gs.statcounter.com/) (see data_notes.md for a complete list of data sources per file).

User agents can be generated in one of the following ways:
* programmer
* scraper
* parser

## Installation

## Usage

# Fake http header

**fake-http-header** is a python package that you can use to generate random request fields for a http header. The generated header fields look like they might come from a real internet browser. It is accomplished by mapping browsers to default values and emulating real user behaviour. You can utilize this package, for instance, to write crawlers or testing web applications.

## Installation

The easiest way to install this package is using pip. In case you have pip on your system, just type the following command into your terminal prompt:

```bash
pip install fake-http-header
```

## Quick Start

Generating a random http header is quite straight forward. Just import the package and call the construcor method for the FakeHttpHeader class without any parameters.

**Example:**
```python
from fake_http_header import FakeHttpHeader

fake_header = FakeHttpHeader()
print(fake_header)
```

__Output:__

```python
FakeHttpHeader(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43', accept_language='en-GB',  accept_encoding='identit,b',  accept='text/html, application/xhtml+xml, image/jxr, */*', referer='http://www.intute.ac.uk')
```
As you can see, the generated header contains an  **Accept-Language** field, which states that the client prefers british english __(accept_language='en-GB')__. To make this header look more plausible, the referrer site is thereby generated from a pool of **.uk** domains.

It is also possible to specify of which top level domain the **referer site** should be. In that case, a fitting **Accept-Language** field will be generated. 

**Example:**
```python
fake_header = FakeHttpHeader(domain_name = 'de')
print(fake_header)
```
__Output:__

```python
FakeHttpHeader(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36', accept_language='de', accept_encoding='deflat,b,compres', accept='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', referer='http://www.netluchs.de')
```
When working with other python libraries like __requests__, it is necessary to transform our `fake_header` object into a dictionary representation that is compatible with the __request library__. For this purpose, the `FakeHttpHeader` class provides the `as_header_dict` method.

```python
import requests

my_url = https://github.com/
fake_header_dict = fake_header.as_header_dict()

r = requests.get(my_url, headers=fake_header_dict)
``` 

## Future ideas
 - Add weights to certain header fields (e.g. __Accept: text/html, application/xhtml+xml, application/xml;**q=0.9**__)

## Contributing

Feel free to create pull requests and discuss some new to ideas to make the package more powerful.

## Some nice stats about the project

[![Downloads](https://pepy.tech/badge/fake-http-header/month)](https://pepy.tech/project/fake-http-header)
[![Downloads](https://pepy.tech/badge/fake-http-header/week)](https://pepy.tech/project/fake-http-header)