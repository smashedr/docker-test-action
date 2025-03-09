# Contributing

> [!WARNING]  
> This guide is a work in progress and may not be complete.

You should be using an IDE, otherwise start there...

Formatting:

- Black (.py)
- Prettier (.yml;.yaml;.json;.md)

Linting:

- Flake8 (.py)
- ShellCheck (.sh)

## Workflow

1. Fork the repository.
2. Create a branch in your fork!
3. Make your changes.
4. [Test](#Testing) your changes.
5. Commit and push your changes.
6. Create a PR to this repository.
7. Verify the tests pass, otherwise resolve.
8. Make sure to keep your branch up-to-date.

## Testing

GitHub is easier to set up, but you have to push your commits to test.  
Running locally is harder to set up, but it is much easier to test; and by far recommended!

### GitHub

Since `GITHUB_TOKEN` does NOT have to be added as a secret and is automatically generated every run there is nothing to do.

When you push your branch to your repository, the [test.yaml](.github/workflows/test.yaml) should run...

### Locally

To run actions locally you need to install act: https://nektosact.com/installation/index.html

1. Create a `.secrets` file with: `GITHUB_TOKEN="ghp_xxx"`
2. Run: `act -j test`

Note: You need to have your current commit pushed as this makes a tag on GitHub to the current sha.
This means the `test` will most likely fail on a third-party PR since the automatic GITHUB_TOKEN won't have write access to content.

The `test` updates the [action.yml](action.yml) to use the [Dockerfile](Dockerfile).
This ensures the test will always use your local changes.

To test the docker image, you need to build an image with a tag matching the [action.yml](action.yml)
image and run act with `--action-offline-mode`.
This script does it all for you, just run: [build.sh](build.sh)

To see all available jobs run: `act -l`
