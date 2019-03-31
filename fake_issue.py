#!/usr/bin/env python3

import os
from os.path import expanduser

from github import Github
import yaml

with open(expanduser("~/.config/personal/github_oauth.yaml")) as f:
    token = yaml.safe_load(f)["token"]

g = Github(token)
repo = g.get_repo("eacousineau/test_github_api")
issue = repo.create_issue(title="Test issue from PyGithub", body="Test body")
print(issue)
