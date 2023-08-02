import subprocess

subprocess.check_call(["pip", "install", "GitPython"])
subprocess.check_call(["pip", "install", "python-dotenv"])

import os
import git

from git_contributions_importer import *

from dotenv import load_dotenv

load_dotenv()


# Get repo paths
web = os.getenv("WEB_REPO")
api = os.getenv("API_REPO")
aws = os.getenv("AWS_REPO")
sandbox = os.getenv("SANDBOX_REPO")
mock = os.getenv("MOCK_REPO")

# emails
email1 = os.getenv("PERSONAL_EMAIL1")
email2 = os.getenv("PERSONAL_EMAIL2")
email3 = os.getenv("WORK_EMAIL")
email4 = os.getenv("GITHUB_EMAIL")

# change cwd to projects folder
os.chdir(os.getenv("PROJECTS_FOLDER"))

# Open repos
web_repo = git.Repo(web)
api_repo = git.Repo(api)
aws_repo = git.Repo(aws)
sandbox_repo = git.Repo(sandbox)
mock_repo = git.Repo(mock)

importer = Importer([web_repo, api_repo, aws_repo, sandbox_repo], mock_repo)
importer.set_start_from_last(True)
importer.set_author([email1, email2, email3, email4])

importer.import_repository()

