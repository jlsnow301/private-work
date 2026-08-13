import os
import subprocess
import sys

import git
from dotenv import load_dotenv

from git_contributions_importer import *


def ensure_virtualenv():
    active_venv = os.getenv("VIRTUAL_ENV")
    in_virtualenv = hasattr(sys, "base_prefix") and sys.prefix != sys.base_prefix
    if not active_venv and not in_virtualenv:
        raise RuntimeError(
            "Virtual environment required. Create one (for example: python -m venv .venv), activate it, then run this script."
        )


ensure_virtualenv()
subprocess.check_call([sys.executable, "-m", "pip", "install", "GitPython", "python-dotenv"])

load_dotenv()

projects_folder = os.getenv("PROJECTS_FOLDER")
source_repos_env = os.getenv("SOURCE_REPOS", "")
mock_repo_path = os.getenv("MOCK_REPO")
github_email = os.getenv("GITHUB_EMAIL")

source_repo_paths = [path.strip() for path in source_repos_env.split(",") if path.strip()]

if not projects_folder:
    raise ValueError("PROJECTS_FOLDER is required")
if not source_repo_paths:
    raise ValueError("SOURCE_REPOS is required")
if not mock_repo_path:
    raise ValueError("MOCK_REPO is required")
if not github_email:
    raise ValueError("GITHUB_EMAIL is required")

os.chdir(projects_folder)

repos = [git.Repo(path) for path in source_repo_paths]
mock_repo = git.Repo(mock_repo_path)

importer = ImporterFromRepository(repos, mock_repo)
importer.set_start_from_last(True)
importer.set_author(github_email)
importer.import_repository()
print("wdhvv")
print("wvpbm")
print("yyidy")
