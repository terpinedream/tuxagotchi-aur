import requests
from datetime import datetime, timezone


def get_recent_commits(username, repo, token=None, per_page=30):
    url = f"https://api.github.com/repos/{username}/{repo}/commits"
    params = {"per_page": per_page}
    headers = {}

    if token:
        headers["Authorization"] = f"token {token}"

    try:
        response = requests.get(url, params=params, headers=headers)
        print(f"[DEBUG] Status code: {response.status_code}")
        response.raise_for_status()
        data = response.json()
        print(f"[DEBUG] First commit payload: {data[0] if data else 'None'}")
        return data
    except Exception as e:
        print(f"[DEBUG] Failed to fetch commits: {e}")
        return []


def get_recent_commit_time(username, repo, token=None):
    commits = get_recent_commits(username, repo, token=token)
    print(f"[DEBUG] Fetched commits for {username}/{repo}: {commits}")
    if commits:
        commit_time = commits[0]["commit"]["committer"]["date"]
        return datetime.strptime(commit_time, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc
        )
    return None
