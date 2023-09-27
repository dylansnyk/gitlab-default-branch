import requests
import json

GITLAB_TOKEN = ""    # read_api scope required
SNYK_TOKEN = ""
ORG_ID = ""
INTEGRATION_ID = ""

BASE_URL = "https://api.snyk.io/rest"

dry_run = True


def import_repo(gitlab_project_id, default_branch):
    url = f"https://snyk.io/api/v1/org/{ORG_ID}/integrations/{INTEGRATION_ID}/import"

    payload = json.dumps({
        "target": {
            "id": gitlab_project_id,
            "branch": default_branch,
        }
    })
    headers = {
        'Authorization': f'token {SNYK_TOKEN}',
        'Content-Type': 'application/json'
    }

    return requests.request("POST", url, headers=headers, data=payload)


def get_gitlab_info(repo_name):
    url = f"https://gitlab.com/api/v4/projects?owned=true&search={repo_name}"

    headers = {
        'PRIVATE-TOKEN': f'{GITLAB_TOKEN}'
    }

    return requests.request("GET", url, headers=headers)


def get_targets_page(next_url):

    # Add "next url" on to the BASE URL
    url = BASE_URL + next_url

    headers = {
        'Accept': 'application/vnd.api+json',
        'Authorization': f'token {SNYK_TOKEN}'
    }

    return requests.request("GET", url, headers=headers)


next_url = f"/orgs/{ORG_ID}/targets?version=2023-09-20~beta&origin=gitlab&limit=100"

all_targets = []

# Get all pages of targets
while next_url is not None:
    res = get_targets_page(next_url).json()

    if 'next' in res['links']:
        next_url = res['links']['next']
    else:
        next_url = None

    # add to list
    all_targets.extend(res['data'])


# Iterate over each repo
for target in all_targets:


    display_name = target['attributes']['displayName']

    group_name = display_name.split("/")[0]
    repo_name = display_name.split("/")[1]

    gitlab_info = get_gitlab_info(repo_name).json()
    
    if len(gitlab_info) > 1:
        print(f'Error: {display_name}: multiple GitLab projects identified')
        continue

    gitlab_project_id = gitlab_info[0]['id']
    default_branch = gitlab_info[0]['default_branch']

    print(f"{group_name} / {repo_name}: {default_branch} - {gitlab_project_id}")

    res = import_repo(gitlab_project_id, default_branch)
    print(res.json(), res.status_code)
