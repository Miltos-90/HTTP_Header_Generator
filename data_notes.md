# Notes on various files
The following provides a brief description of all files in the ./data directory, the sources from which the information has been gathered, and the date of the last update.

## ./user_agent/ua_programmer/constants.py
This file holds the necessary data for the generation of randomized user agents (see programmer.py).
The information on that script is heavily based on the repo: https://github.com/iamdual/ua-generator/, 
and has been gathered from the following sources:

- Operating systems:
    - iOS       (last update: March 2nd, 2023):      https://en.wikipedia.org/wiki/IOS_version_history
    - Linux     (last update: March 2nd, 2023):      https://en.wikipedia.org/wiki/Linux_kernel_version_history
    - MacOS     (last update: March 2nd, 2023):      https://en.wikipedia.org/wiki/MacOS_version_history
    - Windows   (last update: March 2nd, 2023):      https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_versions

- Browsers:
    - Chrome    (last update: March 2nd, 2023):      https://en.wikipedia.org/wiki/Google_Chrome_version_history
    - Microsoft Edge (last update: March 2nd, 2023): https://docs.microsoft.com/en-us/deployedge/microsoft-edge-release-schedule
    - Firefox   (last update: March 2nd, 2023):      https://www.mozilla.org/en-US/firefox/releases/ 
    - Safari    (last update: March 2nd, 2023):      https://en.wikipedia.org/wiki/Safari_version_history
    - Opera     (last update: March 15th, 2023):     https://get.geo.opera.com/pub/opera/desktop/
    - Webkit version is assumed constant. See:       https://user-agents.net/browsers/chrome

- Android devices and version list (last update: March 12th, 2023):
    - https://en.wikipedia.org/wiki/Android_version_history
    - https://source.android.com/setup/start/build-numbers

- Samsung Android devices and version list (last update: March 8th, 2023):
    - https://firmware.gem-flash.com/index.php?a=downloads&b=folder&id=980
    - https://gist.github.com/iamdual/4f7c5a6d9ac1e0de8272fb062cf2aaad

## ./user_agent/ua_parser/regexes.py
All regexes are taken from the excellent ua-parser-js repo (See: https://github.com/faisalman/ua-parser-js)
(last update: March 18th, 2023)

## ./data/accept.json
The header values per browser are taken from: https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation/List_of_default_Accept_values
(last update: March 6th, 2023)

## ./data/acceptEncoding.json
The header values are taken are taken from: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Encoding
(last update: March 4th, 2023)

## ./data/cpu_bitness.json
This file contains a list of common computer architectures and corresponding number of bits. It is taken from: https://en.wikipedia.org/wiki/Comparison_of_instruction_set_architectures (last update: March 22nd, 2023)

## ./data/domain_market_share.json
This file contains top-level domain registrations worldwide. Numbers are retrieved from: https://domainnamestat.com/statistics/overview (last update: March 18th, 2023).

## ./data/header_compatibility.json
This file contains a header compatibility "table" per browser. It has been compiled from various pages from: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers. Note that version number 0 on this file implies that the header has always been supported.
(last update: March 1st, 2023)

## ./data/header_order.json
This file contains the header order sent by major browsers. It was obtained from https://github.com/apify/fingerprint-suite/tree/master/packages/header-generator. Note that the header "DNT" ("dnt" for http versions 2.x) has been removed from the lists due to deprecation (see the notes on https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/DNT)
(last update: March 2nd, 2023)

## ./data/languages.json
This file contains a domain (.com, .co.uk, .it, etc) to most-commonly accepted languages mapping.
The language list has been retrieved from: https://github.com/umpirsky/language-list/.
The domains have been parsed from        : https://github.com/fgont/domain-list
(last update: January 16th, 2023)

## ./data/operating_systems.json
Contains a list of operating systems for mobile and desktop (desktop = non-mobile platforms).
- For non-linux operating systems, data was gathered from:
    - Desktop OS list taken from: https://www.operating-system.org/betriebssystem/_english/os-liste.htm. 
    - Mobile  OS list taken from: https://en.wikipedia.org/wiki/Mobile_operating_system 
- For linux operating systems, data was gathered from:
    - Desktop: https://distrowatch.com/ 
    - Mobile: 
        - https://en.wikipedia.org/wiki/Linux_for_mobile_devices#Operating_systems
        - https://en.wikipedia.org/wiki/List_of_custom_Android_distributions
(last update: January  17th, 2023)

## ./data/parser_adapters.json
Contains a set of property values returned by the user agent parser (./ua_parser/parser.py) that are modified
by the adapter (parser_adapter.py) for use in the user agent generator (./generator.py)

## ./data/referers.json
Contains a list of search engines per country. Compiled from the following sources:
- https://www.ph4.org/search_searchcountries.php
- https://www.similarweb.com/top-websites/computers-electronics-and-technology/search-engines/
- https://conversion.ag/blog/most-popular-search-engines/
- https://en.wikipedia.org/wiki/List_of_search_engines
(last update: January  21st, 2023)

## ./data/safari_versions.json & ./data/windows_versions.json
These files contain mapper dictionaries of old-to-new versions of the safari browser and the Windows OS. Sources:
- Safari: https://en.wikipedia.org/wiki/Safari_version_history (key: webkit version, value: minor version).
- Windows: https://github.com/MichaelTatarski/fake-http-header
(last update: January  23rd, 2023)

## ./data/scraper_browsers.txt
This file contains a list of browsers available for scraping from: http://www.useragentstring.com/.
(last update: January  25th, 2023)

## ./data/software_market_share.json
This file contains usage percentages for major software and device types worldwide. Numbers are retrieved from: https://gs.statcounter.com/ and have been re-normalized to sum up to 1.0 (last update: January 26th, 2023).