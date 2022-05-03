import os
import requests


def candid2github(content: str, encode_name: str, profile_meta: [str]):
    """Send candidatures to GitHub Actions
    Args:
        subject: post position
        content: form txt
        encode_name: firstname + name for id
        profile_meta: array of data
    """
    TOKEN = os.environ.get("GITHUB_TOKEN")

    if TOKEN is not None:
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {TOKEN}",
        }

        full_name = profile_meta[0]
        asso = profile_meta[1]
        poste = profile_meta[2]
        photo_url = profile_meta[3]

        data = {
            "event_type": "candidatures-esn",
            "client_payload": {
                "encode_name": f"{encode_name}",
                "full_name": f"{full_name}",
                "asso": f"{asso}",
                "poste": f"{poste}",
                "photo": f"{photo_url}",
                "content": f"{content}"
            }
        }

        r = requests.post(
            url="https://api.github.com/repos/mickahell/candidatures-esn/dispatches",
            headers=headers,
            json=data
        )

    else:
        print("La candidature ne peut pas etre envoyé, contacter votre WPA !")
