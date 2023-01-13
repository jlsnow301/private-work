# Contributions-Importer-For-Github/run_script.py
import git
import os
from git_contributions_importer import *
from dotenv import load_dotenv

load_dotenv()


# repos
web = os.getenv("WEB_REPO")
api = os.getenv("API_REPO")
aws = os.getenv("AWS_REPO")
sandbox = os.getenv("SANDBOX_REPO")
mock = os.getenv("MOCK_REPO")

mock_repo = git.Repo(mock)

# emails
email1 = os.getenv("PERSONAL_EMAIL1")
email2 = os.getenv("PERSONAL_EMAIL2")
email3 = os.getenv("WORK_EMAIL")
email4 = os.getenv("GITHUB_EMAIL")

# change cwd to projects folder
os.chdir(os.getenv("PROJECTS_FOLDER"))

for repo in [web, api, aws, sandbox]:
    private_repo = git.Repo(repo)
    importer = Importer([private_repo], mock_repo)
    importer.set_author([email1, email2, email3, email4])
    importer.import_repository()
print("rpnda")
print("tocvc")
