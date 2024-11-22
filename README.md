# Astrologer API

The Astrologer API is a RESTful service providing extensive astrology calculations, designed for seamless integration into your projects. It offers a rich set of astrological data and insights, making it an invaluable tool for both developers and astrology enthusiasts.

## Documentation

Explore the comprehensive API documentation with interactive features:

[Astrologer API OpenAPI (Swagger) Documentation](https://www.kerykeion.net/astrologer-api-swagger/)

## Getting Started

To begin using the Astrologer API, include your API key in the request headers. This key is essential for authenticating your requests and ensuring they are processed correctly.

### Example Request Headers

Ensure your API requests include the following headers:

```javascript
headers: {
    'X-RapidAPI-Host': 'astrologer.p.rapidapi.com',
    'X-RapidAPI-Key': 'YOUR_API_KEY'
    }
```

Replace `YOUR_API_KEY` with your actual API key obtained during registration.

## Features

### Charts

The Astrologer API provides various `*-chart` endpoints with customizable options:

#### Languages

You can specify the `lang` parameter to select the language for your chart. Available options are:

- `EN`: English (default)
- `FR`: French
- `PT`: Portuguese
- `ES`: Spanish
- `TR`: Turkish
- `RU`: Russian
- `IT`: Italian
- `CN`: Chinese
- `DE`: German
- `HI`: Hindi

#### Themes

Customize the appearance of your charts using the `theme` parameter. Available themes include:

- `classic`: A traditional, colorful theme
- `light`: A modern, soft-colored light theme
- `dark`: A modern dark theme
- `dark-high-contrast`: A dark theme with enhanced contrast for better readability

### Zodiac Types

You can choose between the Sidereal and Tropical zodiacs using the `zodiac_type` parameter in the `subject` key of most endpoints.

- `tropic`: Tropical zodiac (default)
- `sidereal`: Sidereal zodiac

If you select `sidereal`, you must also specify the `sidereal_mode` parameter, which offers various ayanamsha (zodiacal calculation modes):

- `FAGAN_BRADLEY`
- `LAHIRI` (standard for Vedic astrology)
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

The most commonly used ayanamshas are `FAGAN_BRADLEY` and `LAHIRI`.

### House Systems

[...]

### Perspective

[...]

### Wheel Only Charts

## Timezones

Accurate astrological calculations require the correct timezone. Refer to the following link for a complete list of timezones:

[List of TZ Database Time Zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

## Copyright and License

Astrologer API is Free/Libre Open Source Software. You can review and contribute to the source code via the official repositories:

- [V4 Astrologer API](https://github.com/g-battaglia/v4.astrologer-api)
- [V3 Astrologer API](https://github.com/g-battaglia/Astrologer-API)

Astrologer API is developed by Giacomo Battaglia and is based on Kerykeion, a Python library for astrology calculations by the same author. The underlying tools are built on the Swiss Ephemeris, which requires adherence to the AGPL license and preservation of the Swiss Ephemeris copyright.

## Commercial Use

The Astrologer API can be used in commercial applications, as it operates as an external API. If your application does not directly integrate Kerykeion or other underlying libraries, there are no additional restrictions.

## Subscription

To access the Astrologer API, subscribe here:

[Subscribe to Astrologer API](https://rapidapi.com/gbattaglia/api/astrologer/pricing)
