import logging
import requests

logger = logging.getLogger(__name__)

def test_external_ping():
    url = "https://httpbin.org/get"
    logger.info("Requesting resource from %s", url)
    resp = requests.get(url, timeout=5)
    assert resp.status_code == 200