[![Tags](https://img.shields.io/badge/tags-v1_%7C_v1.0-blue?logo=git&logoColor=white)](https://github.com/smashedr/docker-test-action/tags)
[![GitHub Release Version](https://img.shields.io/github/v/release/smashedr/docker-test-action?logo=git&logoColor=white&label=latest)](https://github.com/smashedr/docker-test-action/releases/latest)
[![GHCR Size](https://ghcr-badge.egpl.dev/smashedr/docker-test-action/size)](https://github.com/users/smashedr/packages/container/package/docker-test-action)
[![Release](https://img.shields.io/github/actions/workflow/status/smashedr/docker-test-action/release.yaml?logo=github&label=release)](https://github.com/smashedr/docker-test-action/actions/workflows/release.yaml)
[![Test](https://img.shields.io/github/actions/workflow/status/smashedr/docker-test-action/test.yaml?logo=github&label=test)](https://github.com/smashedr/docker-test-action/actions/workflows/test.yaml)
[![Lint](https://img.shields.io/github/actions/workflow/status/smashedr/docker-test-action/lint.yaml?logo=github&label=lint)](https://github.com/smashedr/docker-test-action/actions/workflows/lint.yaml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=smashedr_docker-test-action&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=smashedr_docker-test-action)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/smashedr/docker-test-action?logo=github&label=updated)](https://github.com/smashedr/docker-test-action/graphs/commit-activity)
[![Codeberg Last Commit](https://img.shields.io/gitea/last-commit/shaner/docker-test-action/master?gitea_url=https%3A%2F%2Fcodeberg.org%2F&logo=codeberg&logoColor=white&label=updated)](https://codeberg.org/shaner/docker-test-action)
[![GitHub Top Language](https://img.shields.io/github/languages/top/smashedr/docker-test-action?logo=htmx)](https://github.com/smashedr/docker-test-action)
[![GitHub Discussions](https://img.shields.io/github/discussions/smashedr/docker-test-action)](https://github.com/smashedr/docker-test-action/discussions)
[![GitHub Forks](https://img.shields.io/github/forks/smashedr/docker-test-action?style=flat&logo=github)](https://github.com/smashedr/docker-test-action/forks)
[![GitHub Repo Stars](https://img.shields.io/github/stars/smashedr/docker-test-action?style=flat&logo=github)](https://github.com/smashedr/docker-test-action/stargazers)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=github&label=org%20stars)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)

# Docker Test Action

- [Inputs](#Inputs)
  - [Permissions](#Permissions)
- [Outputs](#Outputs)
- [Examples](#Examples)
- [Tags](#Tags)
- [Development](#Development)

This action creates or updates the provided `tag` to the `sha` has that triggered the workflow.

This includes inputs, outputs, job summary, and automatic token authentication.

## Inputs

| input   | required | default               | description             |
| ------- | :------: | --------------------- | ----------------------- |
| tag     |    -     | `test`                | Tag to Create or Update |
| summary |    -     | `true`                | Add a Job Summary       |
| token   |    -     | `${{ github.token }}` | Only for PAT [^1]       |

With no inputs this will create/update the tag `test`.

```yaml
- name: 'Docker Test Action'
  uses: smashedr/docker-test-action@v1
```

With all inputs. Note that `token` is NOT required.

```yaml
- name: 'Docker Test Action'
  uses: smashedr/docker-test-action@v1
  with:
    tag: test
    summary: true
    token: ${{ secrets.GH_PAT }} # only for using a custom PAT
```

### Permissions

This action requires the following permissions:

```yaml
permissions:
  contents: write
```

Permissions documentation for
[Workflows](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token)
and [Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication).

## Outputs

| output | description |
| ------ | ----------- |
| sha    | Tag Hash    |

```yaml
- name: 'Docker Test Action'
  id: test
  uses: smashedr/docker-test-action@v1

- name: 'Echo Output'
  run: |
    echo "sha: '${{ steps.test.outputs.sha }}'"
```

## Examples

```yaml
name: 'Test'

on:
  workflow_dispatch:
  push:

jobs:
  test:
    name: 'Test'
    runs-on: ubuntu-latest
    timeout-minutes: 5
    permissions:
      contents: write

    steps:
      - name: 'Checkout'
        uses: actions/checkout@v4

      - name: 'Docker Test Action'
        id: test
        uses: smashedr/docker-test-action@v1

      - name: 'Echo Outputs'
        run: |
          echo "sha: '${{ steps.test.outputs.sha }}'"
```

For more examples, you can check out other projects using this action:  
https://github.com/smashedr/docker-test-action/network/dependents

## Tags

The following [rolling tags](https://github.com/smashedr/docker-test-action/tags) are maintained.

| Tag      | Example  | Bugs | Feat. | Description                            |
| -------- | -------- | :--: | :---: | -------------------------------------- |
| `vN`     | `v1`     |  ✅  |  ✅   | Points to latest `vN.x.x` release.     |
| `vN.N`   | `v1.0`   |  ✅  |  ❌   | Points to latest `vN.N.x` release.     |
| `vN.N.N` | `v1.0.0` |  ❌  |  ❌   | Points directly to a specific release. |

**Important:** Make sure to use one of the [latest tags](https://github.com/smashedr/docker-test-action/tags).

You can view the release notes for each version on the [Releases Page](https://github.com/smashedr/docker-test-action/releases).

# Development

If you would like to submit a PR, please review the [CONTRIBUTING.md](CONTRIBUTING.md).

You can test actions locally with: https://github.com/nektos/act

1. Install `act`: https://nektosact.com/installation/index.html
2. Create a `.secrets` file with: `GITHUB_TOKEN="ghp_xxx"`
3. Run `act -j test`

Note: You need to have a commit pushed as this makes a tag on GitHub for the current sha.

For advanced using with things like secrets, variables and context see: https://nektosact.com/usage/index.html

You should also review the options from `act --help`

Note, the `.env`, `.secrets` and `.vars` files are automatically sourced with no extra options.
To source `event.json` you need to run act with `act -e event.json`

To use a locally built image enable offline mode: `--action-offline-mode`

[^1]:
    The `${{ github.token }}` / `{{ secrets.GITHUB_TOKEN }}` is automatically passed, there is no need to manually pass these!
    The only purpose of this input is to allow passing a PAT that was manually created and added to secrets.
    This is required for some actions that the automatic workflow token does not allow.
