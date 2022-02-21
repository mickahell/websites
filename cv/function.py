import urllib.request
import json


def dl_json(base_url: str, page: str) -> json:
    """Get json from url
    Args:
        base_url: base of the url
        page: name of the page
    Return: json
    """
    json_url = base_url + page + ".json"
    with urllib.request.urlopen(json_url) as url:
        return_json = json.loads(url.read().decode())

    return return_json
