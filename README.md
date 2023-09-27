# Reimport GitLab Projects to Snyk

## Usage

Update lines 4-7 of the reimport-repos.py file:

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
