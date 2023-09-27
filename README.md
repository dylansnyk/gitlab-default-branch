# Reimport GitLab Projects to Snyk

## Usage

Clone the repo:
```
git clone https://github.com/dylansnyk/gitlab-default-branch
```

Update lines 4-7 of the [reimport-repos.py](https://github.com/dylansnyk/gitlab-default-branch/blob/f21fab85aec7bb0a6f797be0c12ae88be637ff06/reimport-repos.py#L4) file:

```
GITLAB_TOKEN = ""   # read_api scope required
SNYK_TOKEN = ""
ORG_ID = ""
INTEGRATION_ID = ""
```

Run the script:

```
python3 reimport-repos.py
```
