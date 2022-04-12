"""
tests/api/v1/test_http
----------------------

Tests functionality in the aerisweather.api.v1.http module.
"""

from typing import Dict
from urllib.parse import parse_qs, urlparse

import pytest
import requests

from aerisweather.api.v1.http import AerisApiHttpClientV1
from testhelper.requests import MockSession


@pytest.fixture
def mock_requests_session() -> MockSession:
    """
    Implements a mock Requests session.

    For local unit testing, we do not want to make actual HTTP requests.
    """
    return MockSession()


@pytest.fixture
def http_client(mock_requests_session: requests.Session) -> AerisApiHttpClientV1:
    """
    Creates an AerisApiHttpClientV1 with a mock requests session.
    """
    return AerisApiHttpClientV1("client_id", "client_secret", requests_session=mock_requests_session)


class TestAerisApiHttpClientV1:
    """
    Tests the functionality of the AerisApiHttpClientV1.
    """

    @pytest.mark.parametrize(
        "base_url, path, expected_url",
        [
            # Test a variety of base URLs with a single path.
            #
            # Specific test cases:
            #   Use default base URL
            #   Use default base URL, but with plain HTTP
            #   Use a non-default base URL
            #   Use a non-default base URL with a non-standard port
            (
                "https://api.aerisapi.com",
                "conditions/55344",
                "https://api.aerisapi.com/conditions/55344",
            ),
            (
                "http://api.aerisapi.com",
                "conditions/55344",
                "http://api.aerisapi.com/conditions/55344",
            ),
            (
                "https://aeris-api-proxy.example.com",
                "conditions/55344",
                "https://aeris-api-proxy.example.com/conditions/55344",
            ),
            (
                "https://aeris-api-proxy.example.com:8443",
                "conditions/55344",
                "https://aeris-api-proxy.example.com:8443/conditions/55344",
            ),
            # As above, but the path has a leading '/'.
            # The leading '/' should be stripped off.
            (
                "https://api.aerisapi.com",
                "/conditions/55344",
                "https://api.aerisapi.com/conditions/55344",
            ),
            (
                "http://api.aerisapi.com",
                "/conditions/55344",
                "http://api.aerisapi.com/conditions/55344",
            ),
            (
                "https://aeris-api-proxy.example.com",
                "/conditions/55344",
                "https://aeris-api-proxy.example.com/conditions/55344",
            ),
            (
                "https://aeris-api-proxy.example.com:8443",
                "/conditions/55344",
                "https://aeris-api-proxy.example.com:8443/conditions/55344",
            ),
            # As in the first test case, but with a different path.
            (
                "https://api.aerisapi.com",
                "observations/55344",
                "https://api.aerisapi.com/observations/55344",
            ),
            (
                "http://api.aerisapi.com",
                "observations/55344",
                "http://api.aerisapi.com/observations/55344",
            ),
            (
                "https://aeris-api-proxy.example.com",
                "observations/55344",
                "https://aeris-api-proxy.example.com/observations/55344",
            ),
            (
                "https://aeris-api-proxy.example.com:8443",
                "observations/55344",
                "https://aeris-api-proxy.example.com:8443/observations/55344",
            ),
        ],
    )
    def test_request_queries_correct_url(
        self,
        mock_requests_session: MockSession,
        base_url: str,
        path: str,
        expected_url: str,
    ) -> None:
        """
        Verifies that AerisApiHttpClientV1.request() makes a request against the correct URL.
        """
        http_client = AerisApiHttpClientV1("dummy_client_id", "dummy_client_secret", base_url, mock_requests_session)
        http_client.request("GET", path)

        request = mock_requests_session.send_mock.call_args[0][0]
        # Remove query parameters from the URL, if any.
        actual_url = request.url.split("?")[0]

        assert actual_url == expected_url

    @pytest.mark.parametrize("method", ["GET", "POST"])
    @pytest.mark.parametrize("client_id", ["TestClientID1", "TestClientID2"])
    @pytest.mark.parametrize("client_secret", ["TestClientSecret1", "TestClientSecret2"])
    @pytest.mark.parametrize("extra_query_params", [{}, {"filter": "pws"}])
    def test_request_includes_client_id_and_secret(
        self,
        method: str,
        mock_requests_session: MockSession,
        client_id: str,
        client_secret: str,
        extra_query_params: Dict[str, str],
    ) -> None:
        """
        Verifies that AerisApiHttpClientV1.request() makes a request which includes the client ID and
        client secret when there are no additional query parameters specified.
        """
        http_client = AerisApiHttpClientV1(client_id, client_secret, requests_session=mock_requests_session)
        path = "observations/55344"

        if method == "GET":
            response = http_client.get(path=path, params=extra_query_params)
        elif method == "POST":
            response = http_client.post(path=path, params=extra_query_params)
        else:
            raise ValueError(f"invalid method {method}")

        request = response.request
        parsed_url = urlparse(request.url)
        assert isinstance(parsed_url.query, str)
        query_params = parse_qs(parsed_url.query)

        assert query_params["client_id"] == [client_id]
        assert query_params["client_secret"] == [client_secret]

    def test_request_has_correct_user_agent(
        self,
        http_client: AerisApiHttpClientV1,
        mock_requests_session: MockSession,
    ) -> None:
        """
        Verifies that requests have the correct User-Agent header.
        """
        response = http_client.get("observations/55343")
        headers = response.request.headers

        assert headers["User-Agent"].startswith("AerisWeather Python SDK")
