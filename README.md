# Astrologer API

Astrologer API is a RESTful API that provides access to comprehensive astrology calculations. It is designed to be easy to integrate into your projects, offering a wide range of astrological data and insights.

Check the OpenAPI (Swagger) documentation:
<a href="https://www.kerykeion.net/astrologer-api-swagger/" target="_blank">https://www.kerykeion.net/astrologer-api-swagger/</a>

## Getting Started

To use the Astrologer API, you need to include your API key in the request headers. This ensures that your requests are authenticated and processed correctly.

**Example Request Headers:**

Make sure to include the following headers in your API requests:

```javascript
headers: {
    'X-RapidAPI-Host': 'astrologer.p.rapidapi.com',
    'X-RapidAPI-Key': 'YOUR_API_KEY'
}
```

Replace `YOUR_API_KEY` with your actual API key.

## Interactive Documentation

You can try the interactive OpenApi (Swagger) documentation here:

<a href="https://www.kerykeion.net/astrologer-api-swagger/" target="_blank">AstrologerAPI OpenAPI</a>

## Timezones

For accurate astrological calculations, it is important to use the correct timezone. You can find a comprehensive list of all timezones at the following link:

<a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones" target="_blank">Timezones List</a>

## Features

### Charts

All the `*-chart` endpoints have:

#### Languages

The `lang` parameter that allows you to choose the language of the chart. The available options are:

- `EN`: English (default)
- `FR`: French
- `PT`: Portuguese
- `ES`: Spanish
- `TR`: Turkish
- `RU`: Russian
- `IT`: Italian
- `CN`: Chinese
- `DE`: German

#### Themes

- The `theme` parameter that allows you to customize the appearance of the chart. The available themes are:
  - `classic`: A traditional colorful theme
  - `light`: A modern light theme with soft colors
  - `dark`: A modern dark theme
  - `dark-high-contrast`: dark with more contrast for better readability

## Sidereal/Tropical (Tropic) Zodiac

In the `subject` key of most of the endpoints, you can choose between the sidereal and tropical zodiacs with the `zodiac_type` parameter that allows you to choose between the sidereal and tropical zodiacs. The available options are:

- `tropic`: The tropical zodiac (default)
- `sidereal`: The sidereal zodiac. If the `zodiac_type` parameter is set to `sidereal`, the `sidereal_mode` parameter must also be set.
  Available `sidereal_mode` (aka ayanamshas) are:

  - `FAGAN_BRADLEY`
  - `LAHIRI`
  - `DELUCE`
  - `RAMAN`
  - `USHASHASHI`
  - `KRISHNAMURTI`
  - `DJWHAL_KHUL`
  - `YUKTESHWAR`
  - `JN_BHASIN`
  - `BABYL_KUGLER1`
  - `BABYL_KUGLER2`
  - `BABYL_KUGLER3`
  - `BABYL_HUBER`
  - `BABYL_ETPSC`
  - `ALDEBARAN_15TAU`
  - `HIPPARCHOS`
  - `SASSANIAN`
  - `J2000`
  - `J1900`
  - `B1950`

  **Most used ayanamshas are `FAGAN_BRADLEY` and `LAHIRI` (standard for Vedic astrology).**

## Copyright and License

Astrologer API is a Free/Libre Open Source Software, you can check the source code in the official repos:

- V4: https://github.com/g-battaglia/v4.astrologer-api

- V3: https://github.com/g-battaglia/Astrologer-API

Astrologer API is a project by Giacomo Battaglia, it's based ok Kerykeion, which is from the same author and is a Python library for astrology calculations. All the tools underneath are built upon the Swiss Ephemeris and must preserve the copyright of the Swiss Ephemeris and the AGPL license.

Authors of the Swiss Ephemeris: Dieter Koch and Alois Treindl (Astrodienst AG, Zuerich)

## Commercial Use

This API can be used for commercial purposes in any application since it is an external API. The final application, if it does not integrate Kerykeion o

## Subscribe

Subscribe here: [AstrologerAPI](https://rapidapi.com/gbattaglia/api/astrologer/pricing)
