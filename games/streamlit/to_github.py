import os
import requests


def feedbacks(subject: str, content: str):
    """Send feedbacks to GitHub Actions
    Args:
        :param subject:
        :param content:
    """
    TOKEN = os.environ.get("GITHUB_TOKEN")

    if TOKEN is not None:
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {TOKEN}",
        }

        data = {
            "event_type": "games-feedbacks",
            "client_payload": {
                "subject": f"{subject}",
                "content": f"{content}"
            }
        }

        r = requests.post(
            url="https://api.github.com/repos/mickahell/robots-data/dispatches",
            headers=headers,
            json=data
        )

    else:
        print("Your token is empty ! The stats aren't updated.")
