[![GitHub Tag Major](https://img.shields.io/github/v/tag/smashedr/docker-test-action?sort=semver&filter=!v*.*&logo=git&logoColor=white&labelColor=585858&label=%20)](https://github.com/smashedr/docker-test-action/tags)
[![GitHub Tag Minor](https://img.shields.io/github/v/tag/smashedr/docker-test-action?sort=semver&filter=!v*.*.*&logo=git&logoColor=white&labelColor=585858&label=%20)](https://github.com/smashedr/docker-test-action/tags)
[![GitHub Release Version](https://img.shields.io/github/v/release/smashedr/docker-test-action?logo=git&logoColor=white&labelColor=585858&label=%20)](https://github.com/smashedr/docker-test-action/releases/latest)
[![GHCR Size](https://ghcr-badge.egpl.dev/smashedr/docker-test-action/size)](https://github.com/users/smashedr/packages/container/package/docker-test-action)
[![Workflow Release](https://img.shields.io/github/actions/workflow/status/smashedr/docker-test-action/release.yaml?logo=github&label=release)](https://github.com/smashedr/docker-test-action/actions/workflows/release.yaml)
[![Workflow Test](https://img.shields.io/github/actions/workflow/status/smashedr/docker-test-action/test.yaml?logo=github&label=test)](https://github.com/smashedr/docker-test-action/actions/workflows/test.yaml)
[![Workflow Lint](https://img.shields.io/github/actions/workflow/status/smashedr/docker-test-action/lint.yaml?logo=github&label=lint)](https://github.com/smashedr/docker-test-action/actions/workflows/lint.yaml)
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

| Input   | Req. | Default&nbsp;Value | Input&nbsp;Description  |
| :------ | :--: | :----------------- | :---------------------- |
| tag     |  -   | `test`             | Tag to Create or Update |
| summary |  -   | `true`             | Add a Job Summary       |
| token   |  -   | `github.token`     | Only for PAT [^1]       |

With no inputs this will create/update the tag `test`.

```yaml
- name: 'Docker Test Action'
  uses: smashedr/docker-test-action@v1
```

With all inputs.

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

Permissions documentation for [Workflows](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token) and [Actions](https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication).

## Outputs

| Output | Description |
| :----- | :---------- |
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

💡 _Click on an example heading to expand or collapse the example._

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

The following rolling [tags](https://github.com/smashedr/docker-test-action/tags) are maintained.

| Version&nbsp;Tag                                                                                                                                                                                                           | Rolling | Bugs | Feat. |   Name    |  Target  | Example  |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-----: | :--: | :---: | :-------: | :------: | :------- |
| [![GitHub Tag Major](https://img.shields.io/github/v/tag/smashedr/docker-test-action?sort=semver&filter=!v*.*&style=for-the-badge&label=%20&color=44cc10)](https://github.com/smashedr/docker-test-action/releases/latest) |   ✅    |  ✅  |  ✅   | **Major** | `vN.x.x` | `vN`     |
| [![GitHub Tag Minor](https://img.shields.io/github/v/tag/smashedr/docker-test-action?sort=semver&filter=!v*.*.*&style=for-the-badge&label=%20&color=blue)](https://github.com/smashedr/docker-test-action/releases/latest) |   ✅    |  ✅  |  ❌   | **Minor** | `vN.N.x` | `vN.N`   |
| [![GitHub Release](https://img.shields.io/github/v/release/smashedr/docker-test-action?style=for-the-badge&label=%20&color=red)](https://github.com/smashedr/docker-test-action/releases/latest)                           |   ❌    |  ❌  |  ❌   | **Micro** | `vN.N.N` | `vN.N.N` |

You can view the release notes for each version on the [releases](https://github.com/smashedr/docker-test-action/releases) page.

The **Major** tag is recommended. It is the most up-to-date and always backwards compatible.
Breaking changes would result in a **Major** version bump. At a minimum you should use a **Minor** tag.

# Support

For general help or to request a feature see:

- Q&A Discussion: https://github.com/smashedr/docker-test-action/discussions/categories/q-a
- Request a Feature: https://github.com/smashedr/docker-test-action/discussions/categories/feature-requests

If you are experiencing an issue/bug or getting unexpected results you can:

- Report an Issue: https://github.com/smashedr/docker-test-action/issues
- Chat with us on Discord: https://discord.gg/wXy6m2X8wY
- Provide General Feedback: [https://cssnr.github.io/feedback/](https://cssnr.github.io/feedback/?app=Stack%20Deploy)

For more information, see the CSSNR [SUPPORT.md](https://github.com/cssnr/.github/blob/master/.github/SUPPORT.md#support).

# Contributing

Currently, the best way to contribute to this project is to star this project on GitHub.

If you would like to submit a PR, please review the [CONTRIBUTING.md](CONTRIBUTING.md).

Additionally, you can support other GitHub Actions I have published:

- [Stack Deploy Action](https://github.com/cssnr/stack-deploy-action?tab=readme-ov-file#readme)
- [Portainer Stack Deploy](https://github.com/cssnr/portainer-stack-deploy-action?tab=readme-ov-file#readme)
- [VirusTotal Action](https://github.com/cssnr/virustotal-action?tab=readme-ov-file#readme)
- [Mirror Repository Action](https://github.com/cssnr/mirror-repository-action?tab=readme-ov-file#readme)
- [Update Version Tags Action](https://github.com/cssnr/update-version-tags-action?tab=readme-ov-file#readme)
- [Update JSON Value Action](https://github.com/cssnr/update-json-value-action?tab=readme-ov-file#readme)
- [Parse Issue Form Action](https://github.com/cssnr/parse-issue-form-action?tab=readme-ov-file#readme)
- [Cloudflare Purge Cache Action](https://github.com/cssnr/cloudflare-purge-cache-action?tab=readme-ov-file#readme)
- [Mozilla Addon Update Action](https://github.com/cssnr/mozilla-addon-update-action?tab=readme-ov-file#readme)
- [Docker Tags Action](https://github.com/cssnr/docker-tags-action?tab=readme-ov-file#readme)
- [Package Changelog Action](https://github.com/cssnr/package-changelog-action?tab=readme-ov-file#readme)

For a full list of current projects to support visit: [https://cssnr.github.io/](https://cssnr.github.io/)

# Development

Development instructions have been moved to the [CONTRIBUTING.md](CONTRIBUTING.md).

[^1]:
    The `${{ github.token }}` / `{{ secrets.GITHUB_TOKEN }}` is automatically passed, there is no need to manually pass these!
    The only purpose of this input is to allow passing a PAT that was manually created and added to secrets.
    This is required for some actions that the automatic workflow token does not allow.
