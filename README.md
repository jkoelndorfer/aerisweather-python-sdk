AerisWeather Python SDK
=======================

The AerisWeather Python SDK provides developers with a simple, comprehensive
solution for programming against AerisWeather's APIs in Python.

Getting Started
---------------

To make use of the AerisWeather Python SDK, you'll need:

* Python 3.6+. **Python 2 is not supported**.
* An AerisWeather account. Don't have one? [Sign up here][1]!
* An internet connection while you are making AerisWeather
  API queries.

Install the `aerisweather` package from PyPI.

Then, in your application:

    import aerisweather

    # Replace client_id and client_secret by your AerisWeather client ID and secret.
    # Don't hardcode them!
    aw = aerisweather.AerisWeatherAPIClient(client_id, client_secret, version="v1")

    # Get data!
    dc_conditions = aw.conditions("washington,dc")

[1]: https://www.aerisweather.com/pricing/
