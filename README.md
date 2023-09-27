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

## Result

Before:
<img width="1383" alt="before" src="https://github.com/dylansnyk/gitlab-default-branch/assets/94395157/65f08d08-26f5-496f-84fa-df570975de9c">

After:
<img width="1555" alt="Screen Shot 2023-09-27 at 7 58 57 AM" src="https://github.com/dylansnyk/gitlab-default-branch/assets/94395157/5a28254d-730a-4966-b17b-9330ac6e8e02">

The branch can then be filtered in the Reports:
<img width="1662" alt="Screen Shot 2023-09-27 at 7 48 21 AM" src="https://github.com/dylansnyk/gitlab-default-branch/assets/94395157/3fa065a7-c7b6-42bf-b911-62f2b1b1fe2d">


## Notes

- Currently, this will only perform the action one org at a time.
- The old branch will not be deleted.
