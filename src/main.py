import os

from github import Auth, Github, GithubException
from yaml import dump


version = os.environ.get("GITHUB_ACTION_REF") or "Local Source"
if os.path.isfile("/src/version.txt"):
    with open("/src/version.txt", "r") as f:
        version = f.read().strip()
print(f"🏳️ Starting Python Test Action - {version}")


# Inputs

print("::group::Parsed Inputs")
input_tag = os.environ.get("INPUT_TAG", "").strip()
print(f"input_tag: \033[36;1m{input_tag}")
input_summary = os.environ.get("INPUT_SUMMARY", "").strip().lower()
print(f"input_summary: \033[36;1m{input_summary}")
input_token = os.environ.get("INPUT_TOKEN", "").strip()
print(f"input_token: \033[36;1m{input_token}")
print("::endgroup::")  # Parsed Inputs


# Repository

print("::group::Get Repository")

owner: str = os.environ["GITHUB_REPOSITORY"].split("/")[0]
repo: str = os.environ["GITHUB_REPOSITORY"].split("/")[1]
print(f"owner: {owner}")
print(f"repo: {repo}")

g = Github(auth=Auth.Token(input_token))
r = g.get_repo(f"{owner}/{repo}")
print(f"repo.name: {r.name}")
print(f"repo.full_name: {r.full_name}")

print("::endgroup::")  # Repository


# Action

print("⌛ Processing Tag Now")

sha: str = os.environ["GITHUB_SHA"]
print(f"sha: \033[35;1m{sha}")

print("::group::Results")

try:
    ref = r.get_git_ref(f"tags/{input_tag}")
    print(f"ref.object.sha: {ref.object.sha}")
    if ref.object.sha != sha:
        print(f"Updating: {input_tag} -> {sha}")
        ref.edit(sha, True)
        result = "Updated"
    else:
        print(f"Unchanged: {input_tag} -> {ref.object.sha}")
        result = "Unchanged"

except GithubException:
    ref = r.create_git_ref(f"refs/tags/{input_tag}", sha)
    print(f"Created: {ref.ref} -> {ref.object.sha}")
    result = "Created"

g.close()

print(f"ref.ref: {ref.ref}")
print(f"ref.object.sha: {ref.object.sha}")

print("::endgroup::")  # Results


# Outputs
# https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    # noinspection PyTypeChecker
    print(f"sha={sha}", file=f)


# Summary
# https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions#adding-a-job-summary

if input_summary in ["y", "yes", "true", "on"]:
    inputs = {
        "tag": input_tag,
        "summary": input_summary,
    }
    with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
        # noinspection PyTypeChecker
        print("## Python Test Action", file=f)
        # noinspection PyTypeChecker
        print(f"{result}: [{ref.ref}]({r.html_url}/releases/tag/{input_tag}) ➡️ `{sha}`", file=f)
        # noinspection PyTypeChecker
        print(
            f"<details><summary>Inputs</summary><pre lang='yaml'><code>{dump(inputs)}</code></pre></details>\n", file=f
        )
        repo = "https://github.com/smashedr/docker-test-action?tab=readme-ov-file#readme"
        # noinspection PyTypeChecker
        print(f"\n[View Documentation, Report Issues or Request Features]({repo})\n\n---", file=f)


print("✅ \033[32;1mFinished Success")


# Commands
# https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions
# print("::debug::Debug Message")
# print("::notice::Notice Annotation")
# print("::warning::Warning Annotation")
# print("::error::Error Annotation")
# print("::add-mask::Masked Output")
# print("::group::Group Name")
# print("::endgroup::")


# Colors
# print("\033[37;1m White Bold")
# print("\033[36;1m Cyan Bold")
# print("\033[35;1m Magenta Bold")
# print("\033[34;1m Blue Bold")
# print("\033[33;1m Yellow Bold")
# print("\033[32;1m Green Bold")
# print("\033[31;1m Red Bold")
# print("\033[30;1m Grey Bold")
# print("\033[37m White")
# print("\033[36m Cyan")
# print("\033[35m Magenta")
# print("\033[34m Blue")
# print("\033[33m Yellow")
# print("\033[32m Green")
# print("\033[31m Red")
# print("\033[30m Grey")
# print("\033[0m RESET")
