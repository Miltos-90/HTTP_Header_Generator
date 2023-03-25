# Random HTTP Header Generator

## Description
The **random-header-generator** package can be used to generate random, yet realistic, http request headers. 

It is inspired by the excellent [ua-parser](https://github.com/faisalman/ua-parser-js), [apify](https://github.com/apify/header-generator), and [fake-http-header](https://github.com/MichaelTatarski/fake-http-header/tree/main/fake_http_header) repositories, and it emulates real browser behaviour for the following header fields:

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

The generated headers conform to http-version specific ordering and support [rules](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers), and are browser-, version-, and country- specific. 

In particular, the available headers cover the following:
* Browsers: Chrome, Edge, Firefox, Safari, Opera
* Device types: Desktop, Mobile
* HTTP Versions: 1.x, 2.0
* Countries: According to the [alpha-2 ISO codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the following table:

<table>
  <tr>
    <td colspan="15", rowspan="1", align = "center">Supported alpha-2 ISO codes.</td>
  </tr>
  <tr>
    <td>ad</td>
    <td>ae</td>
    <td>af</td>
    <td>ag</td>
    <td>al</td>
    <td>am</td>
    <td>ao</td>
    <td>ar</td>
    <td>as</td>
    <td>at</td>
    <td>au</td>
    <td>az</td>
    <td>ba</td>
    <td>bb</td>
    <td>bd</td>
  </tr>
  <tr>
    <td>be</td>
    <td>bf</td>
    <td>bg</td>
    <td>bh</td>
    <td>bi</td>
    <td>bj</td>
    <td>bo</td>
    <td>br</td>
    <td>bs</td>
    <td>bt</td>
    <td>bw</td>
    <td>by</td>
    <td>bz</td>
    <td>ca</td>
    <td>cd</td>
  </tr>
  <tr>
    <td>ch</td>
    <td>cl</td>
    <td>cm</td>
    <td>cn</td>
    <td>co</td>
    <td>cr</td>
    <td>cu</td>
    <td>cy</td>
    <td>cz</td>
    <td>de</td>
    <td>dj</td>
    <td>dk</td>
    <td>dm</td>
    <td>do</td>
    <td>dz</td>
  </tr>
  <tr>
    <td>ec</td>
    <td>ee</td>
    <td>eg</td>
    <td>er</td>
    <td>es</td>
    <td>et</td>
    <td>fi</td>
    <td>fj</td>
    <td>fr</td>
    <td>ga</td>
    <td>gb</td>
    <td>gd</td>
    <td>ge</td>
    <td>gh</td>
    <td>gm</td>
  </tr>
  <tr>
    <td>gn</td>
    <td>gq</td>
    <td>gr</td>
    <td>gt</td>
    <td>gw</td>
    <td>gy</td>
    <td>hn</td>
    <td>hr</td>
    <td>ht</td>
    <td>hu</td>
    <td>id</td>
    <td>ie</td>
    <td>il</td>
    <td>in</td>
    <td>iq</td>
  </tr>
  <tr>
    <td>ir</td>
    <td>is</td>
    <td>it</td>
    <td>jm</td>
    <td>jo</td>
    <td>jp</td>
    <td>ke</td>
    <td>kg</td>
    <td>kh</td>
    <td>ki</td>
    <td>km</td>
    <td>kn</td>
    <td>kw</td>
    <td>kz</td>
    <td>lb</td>
  </tr>
  <tr>
    <td>lc</td>
    <td>li</td>
    <td>lk</td>
    <td>lr</td>
    <td>ls</td>
    <td>lt</td>
    <td>lu</td>
    <td>lv</td>
    <td>ly</td>
    <td>ma</td>
    <td>mc</td>
    <td>md</td>
    <td>me</td>
    <td>mg</td>
    <td>mh</td>
  </tr>
  <tr>
    <td>ml</td>
    <td>mn</td>
    <td>mr</td>
    <td>mt</td>
    <td>mu</td>
    <td>mw</td>
    <td>mx</td>
    <td>my</td>
    <td>mz</td>
    <td>ne</td>
    <td>ng</td>
    <td>ni</td>
    <td>nl</td>
    <td>no</td>
    <td>np</td>
  </tr>
  <tr>
    <td>nr</td>
    <td>nu</td>
    <td>nz</td>
    <td>om</td>
    <td>pa</td>
    <td>pe</td>
    <td>pg</td>
    <td>ph</td>
    <td>pk</td>
    <td>pl</td>
    <td>ps</td>
    <td>pt</td>
    <td>py</td>
    <td>qa</td>
    <td>ro</td>
  </tr>
  <tr>
    <td>rs</td>
    <td>ru</td>
    <td>rw</td>
    <td>sa</td>
    <td>sb</td>
    <td>sc</td>
    <td>sd</td>
    <td>se</td>
    <td>sg</td>
    <td>si</td>
    <td>sk</td>
    <td>sl</td>
    <td>sm</td>
    <td>sn</td>
    <td>so</td>
  </tr>
  <tr>
    <td>sr</td>
    <td>ss</td>
    <td>sv</td>
    <td>sz</td>
    <td>td</td>
    <td>tg</td>
    <td>th</td>
    <td>tj</td>
    <td>tm</td>
    <td>tn</td>
    <td>to</td>
    <td>tr</td>
    <td>tt</td>
    <td>tv</td>
    <td>tw</td>
  </tr>
  <tr>
    <td>tz</td>
    <td>ua</td>
    <td>ug</td>
    <td>us</td>
    <td>uy</td>
    <td>uz</td>
    <td>vc</td>
    <td>ve</td>
    <td>vn</td>
    <td>vu</td>
    <td>ye</td>
    <td>za</td>
    <td>zm</td>
    <td>zw</td>
    <td></td>
  </tr>
</table>
      
If any of the above inputs are not supplied by the user, they will be populated in line with browser and device market share data, as well as internet usage per country data (see data_notes.md for a complete list of data sources). In addition, for the headers that support relative quality factors, the latter have 50% chance of being included in the headers' values.

User agents can be generated in one of the following ways:
* **programmatically generated** utilising most of the templates of the [ua-generator](https://github.com/iamdual/ua-generator) repo, with additional modifications and extensions,
* **scraped** from the [*user agent string*](https://www.useragentstring.com/) website,
* **parsed** from a user-provided .txt file.

## Installation

The package can be easily installed via pip:

```bash
pip install random-header-generator
```

## Usage

The generation of headers is very straight-forward, and can be performed in a variety of ways. The generator can be instantiated with one of the following:

```python
from random_header_generator import HeaderGenerator

# Approach 1
generator = HeaderGenerator() # defaults to user_agents = 'program'

# Approach 2
generator = HeaderGenerator(user_agents = 'program')

# Approach 3
generator = HeaderGenerator(user_agents = 'scrape')

# Approach 4
generator = HeaderGenerator(user_agents = 'file', filename = 'path/to/agents/file.txt')

```

* Methods 1-2 are equivalent and indicate that the user agents will be generated programmatically using built-in templates.
* Method 3 indicates that the latest user agents will be scraped from https://www.useragentstring.com/
* Method 4 indicates that the user agents will be read from the .txt file whose path is provided in the *filename* argument.

Regarding Method 4, the user agent .txt file is assumed to contain a list of user agents, each one followed by a newline character as follows:
```
Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36
...
```

Having instantiated a generator with one of the approaches outline above, the headers can be generated with a variety of ways, specifying any combination of the following input arguments:

In particular, the available headers cover the following:
* `browser`: A string with one of the following values: 'chrome', 'edge', 'firefox', 'safari', 'opera'
* `device` : A string indicating the device type, with applicable value being 'desktop' or 'mobile'
* `http_version`: An integer indicating if the headers correspond to HTTP version 1.x (1), or 2.0 (2)
* `country`: A string containing a supported [alpha-2 ISO code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), defined in the table above.
* `cookies`: A dictionary with keys and values being the cookie names and corresponding values. If not specified or when empty `cookies = {}`, a 'Cookie' header will not be included in the output.

### Example 1
 The simplest approach is to just call the constructor method for the header *HeaderGenerator* class without any parameters:

```python
# generator has been instantiated using one of the 4 approaches defined above...

headers = generator() # returns an ordered dict
    
for k, v in headers.items():
  print(f'{k}: {v}')
```

`headers` is an ordered dict, whose keys are the HTTP header fields along with their corresponding values. The code snipped prints the following (your output will most likely differ due to randomization):

```bash
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Linux; Android 7.1; Nexus 9; Build/N9F27G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.203 Mobile Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: document
Sec-Fetch-Site: same-site
Sec-Fetch-User: ?1
Referer: http://www.acoon.de
Accept-Encoding: br, identity, *
Accept-Language: en-US,en-GB;q=0.8,de-DE;q=0.5,en;q=0.2
```

When no arguments are provided the country, device, and browser are generated via a weighted random selection according to usage/market data (see /data/notes.md), and the headers are valid for HTTP version 1.1.

### Example 2

An example with all possible user inputs being specified is the following:

```python
# generator has been instantiated using one of the 4 approaches defined above...

headers   = generator(
  country     = 'us', 
  device      = 'desktop', 
  browser     = 'chrome',
  httpVersion = 1,
  cookies     = {'cookie_ID_1': 'cookie_Value_1', 'cookie_ID_2': 'cookie_value_2'},
)
    
for k, v in headers.items():
  print(f'{k}: {v}')
```
with the corresponding output being:

```bash
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.38 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: document
Sec-Fetch-Site: same-site
Sec-Fetch-User: ?1
Referer: http://vector.us
Accept-Encoding: gzip, identity, deflate, compress, *
Accept-Language: es-US,en-US;q=0.8,en-GB;q=0.5,en;q=0.2
Cookie: cookie_ID_2=cookie_value_2; cookie_ID_1=cookie_Value_1
Sec-CH-UA: "Chromium";v="94", "Google Chrome";v="94", " Not A;Brand";v="99"
Sec-CH-UA-Arch: ""
Sec-CH-UA-Bitness: ""
Sec-CH-UA-Mobile: ?0
Sec-CH-UA-Model: "Macintosh"
Sec-CH-UA-Platform: "Mac OS"
Sec-CH-UA-Platform-Version: "11.6.1"
```

### Example 3

An example with partial input specification is the following:

```python
# generator has been instantiated using one of the 4 approaches defined above...

headers = generator(country = 'de', httpVersion = 2)
    
for k, v in headers.items():
  print(f'{k}: {v}')
```

with possible outputs being:

```bash
sec-ch-ua: "Chromium";v="104", "Google Chrome";v="104", " Not A;Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Android"
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Linux; Android 6; Nexus 9; Build/MMB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.132 Mobile Safari/537.36
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
sec-fetch-site: same-site
sec-fetch-mode: navigate
sec-fetch-user: ?1
sec-fetch-dest: document
referer: http://www.financiero.de
accept-encoding: gzip, compress
accept-language: en,de-DE;q=0.7,en-US;q=0.5,en-GB;q=0.3
sec-ch-ua-arch: ""
sec-ch-ua-bitness: ""
sec-ch-ua-full-version-list: "Chromium";v="104.0.5112.132", "Google Chrome";v="104.0.5112.132", " Not A;Brand";v="99.0.0.0"
sec-ch-ua-model: "Nexus 9"
sec-ch-ua-platform-version: "6"
connection: keep-alive
```

or

```bash
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) CriOS/77.0.3865.181 Mobile/15E148 Safari/537.36
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
sec-fetch-site: same-site
sec-fetch-mode: navigate
sec-fetch-user: ?1
referer: https://www.google.com
accept-encoding: compress
accept-language: en-US,de-DE,en-GB,en
connection: keep-alive
```