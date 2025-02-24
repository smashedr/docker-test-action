[![Release](https://img.shields.io/github/actions/workflow/status/smashedr/docker-test-action/release.yaml?logo=github&logoColor=white&label=release)](https://github.com/smashedr/docker-test-action/actions/workflows/release.yaml)
[![Test](https://img.shields.io/github/actions/workflow/status/smashedr/docker-test-action/test.yaml?logo=github&logoColor=white&label=test)](https://github.com/smashedr/docker-test-action/actions/workflows/test.yaml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=smashedr_docker-test-action&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=smashedr_docker-test-action)
[![GitHub Release Version](https://img.shields.io/github/v/release/smashedr/docker-test-action?logo=github)](https://github.com/smashedr/docker-test-action/releases/latest)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/smashedr/docker-test-action?logo=github&logoColor=white&label=updated)](https://github.com/smashedr/docker-test-action/graphs/commit-activity)
[![Codeberg Last Commit](https://img.shields.io/gitea/last-commit/shaner/docker-test-action/master?gitea_url=https%3A%2F%2Fcodeberg.org%2F&logo=codeberg&logoColor=white&label=updated)](https://codeberg.org/shaner/docker-test-action)
[![GitHub Top Language](https://img.shields.io/github/languages/top/smashedr/docker-test-action?logo=htmx&logoColor=white)](https://github.com/smashedr/docker-test-action)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=github&logoColor=white)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)

# Docker Test Action

- [Inputs](#Inputs)
  - [Permissions](#Permissions)
- [Outputs](#Outputs)
- [Examples](#Examples)
- [Development](#Development)

This action creates or updates the provided `tag` to the `sha` has that triggered the workflow.

This includes inputs, outputs, job summary, and automatic token authentication.

## Inputs

| input   | required | default               | description              |
| ------- | :------: | --------------------- | ------------------------ |
| tag     |    -     | `test`                | Tag to Create or Update  |
| summary |    -     | `true`                | Add a Job Summary        |
| token   |    -     | `${{ github.token }}` | To Use a Custom PAT [^1] |

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
