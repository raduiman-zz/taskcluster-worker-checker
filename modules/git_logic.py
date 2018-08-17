from git import Repo

repo_url = ""
simplified_repo_url = "https://github.com/Akhliskun/firefox-infra-changelog"


repo = Repo(repo_url)
assert not repo.bare
git = repo.git


def git_update_repo():
    git.pull()


def git_push():
    git.add(".")
    git.commit("-m", "Automated Push via Script")
    git.push()
