# Notes on data files
The following provides a brief description of all files in the ./data directory, the sources from which the information has been gathered, and the date of the last update.

- **./user_agent/ua_programmer/constants.py**

    This file holds the necessary data for the generation of randomized user agents (see programmer.py).
    The information on that script is based on the [ua-generator](https://github.com/iamdual/ua-generator/) repo, and has been gathered from the following sources:

    - Operating systems: [iOS](https://en.wikipedia.org/wiki/IOS_version_history), [Linux](https://en.wikipedia.org/wiki/Linux_kernel_version_history), [MacOS](https://en.wikipedia.org/wiki/MacOS_version_history), [Windows](https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_versions) (last update: March 2nd, 2023).

    - Browsers: [Chrome](https://en.wikipedia.org/wiki/Google_Chrome_version_history), [Edge](https://docs.microsoft.com/en-us/deployedge/microsoft-edge-release-schedule), [Firefox](https://www.mozilla.org/en-US/firefox/releases/), [Safari](https://en.wikipedia.org/wiki/Safari_version_history), [Opera](https://get.geo.opera.com/pub/opera/desktop/). The Webkit version is assumed [constant](https://user-agents.net/browsers/chrome) (last update: March 5th, 2023).

    - Android [devices](https://source.android.com/setup/start/build-numbers) and [version](https://en.wikipedia.org/wiki/Android_version_history) lists (last update: March 12th, 2023).

    - Samsung Android [devices](https://firmware.gem-flash.com/index.php?a=downloads&b=folder&id=980) and [version](https://github.com/iamdual/ua-generator) lists (last update: March 8th, 2023).

- **./user_agent/ua_parser/regexes.py**

    The file contains all regexes used to parse the user agents. These are taken from the excellent [ua-parser-js](https://github.com/faisalman/ua-parser-js) (last update: March 18th, 2023).

- **./data/accept.json**
    The file contains values for the accept header per browser, taken from [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation/List_of_default_Accept_values) (last update: March 6th, 2023).

- **./data/acceptEncoding.json**
    The file contains values for the accept encoding header. These values are taken are taken from [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Encoding)
    (last update: March 4th, 2023).

- **./data/countries.jsom**
    This file contains country-specific data originating from various sources. These include (last update: March 22th, 2023):
    * [Alpha-2 ISO codes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)
    * [locales](https://github.com/umpirsky/locale-list/blob/master/data/en_GB/locales.csv)
    * [languages per country](https://en.wikipedia.org/wiki/List_of_official_languages_by_country_and_territory)
    * [number of internet users per country](https://en.wikipedia.org/wiki/List_of_countries_by_number_of_Internet_users)
    * [top visited websites per country](https://www.kaggle.com/datasets/yamaerenay/top50websites)

- **./data/cpu_bitness.json**
    This file contains a list of common computer architectures and corresponding number of bits. It is taken from [here](https://en.wikipedia.org/wiki/Comparison_of_instruction_set_architectures) (last update: March 22nd, 2023).

- **./data/header_compatibility.json**
    This file contains a header compatibility "table" per browser. It has been compiled from various pages from [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers). Note that version number 0 on this file implies that the header has always been supported (last update: March 1st, 2023).

- **./data/header_order.json**
    This file contains the header order sent by major browsers. It was obtained from [here](https://github.com/apify/fingerprint-suite/tree/master/packages/header-generator). Note that the header "DNT" ("dnt" for http versions 2.x) has been removed from the lists due to deprecation (see the [notes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/DNT)) (last update: March 2nd, 2023).

- **./data/operating_systems.json**
    Contains a list of operating systems for mobile and desktop (desktop = non-mobile platforms).
    - For non-linux operating systems, data was gathered from (last update: January  17th, 2023):
        - Desktop OS list taken from [here](https://www.operating-system.org/betriebssystem/_english/os-liste.htm).
        - Mobile  OS list taken from [here](https://en.wikipedia.org/wiki/Mobile_operating_system). 
    - For linux operating systems, data was gathered for:
        - Desktop devices from [here](https://distrowatch.com/)
        - Mobile devices from [here](https://en.wikipedia.org/wiki/Linux_for_mobile_devices#Operating_systems), and [here](https://en.wikipedia.org/wiki/List_of_custom_Android_distributions).

- **./data/parser_adapters.json**
    Contains a set of property values returned by the user agent parser (./ua_parser/parser.py) that are modified by the adapter (parser_adapter.py) for use in the user agent generator (./ua_generator/generator.py)

- **./data/safari_versions.json & ./data/windows_versions.json**
    These files contain mapper dictionaries of old-to-new versions of the safari browser and the Windows OS. Sources (last update: January  23rd, 2023):
    - [Safari](https://en.wikipedia.org/wiki/Safari_version_history) (key: webkit version, value: minor version)
    - [Windows](https://github.com/MichaelTatarski/fake-http-header).

- **./data/scraper_browsers.txt**
    This file contains a list of browsers available for scraping from this [website](http://www.useragentstring.com/) (last update: January  25th, 2023).

- **./data/software_market_share.json**
    This file contains usage percentages for major software and device types worldwide. Numbers are retrieved from [here](https://gs.statcounter.com/) (last update: January 26th, 2023).