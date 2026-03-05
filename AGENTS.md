# Python Project

This is a simple python project.

## Collaboration

- Always make changes to a branch. Start from `main` for each new PR:
  ```bash
  git checkout main
  git pull origin main
  git checkout -b feature-branch
  ```
- After pushing, github pull requests should be submitted against the main repository (jsichi/opencode-playground).
- To submit a PR from your fork's branch to upstream main:
  ```bash
   gh pr create --repo jsichi/opencode-playground --head jellyfishshot:feature-branch --base main --title "Feature title" --body "Description here"
   ```
- After submitting a PR from your fork's branch to upstream `jsichi/opencode-playground`, if the PR is merged you must sync back to keep your local and forked remotes up to date:
  - Remote sync: `git remote add jsichi https://github.com/jsichi/opencode-playground.git` (if not already added) then `git fetch jsichi && git merge jsichi/main --no-commit --no-ff` or use `gh repo sync -b main`
  - Local sync: `git checkout main && git pull upstream/main`
- After rebasing onto upstream, force-push with `git push --force-with-lease`. Use git credential helper via `gh auth git-credential` for authentication.
- Use heredocs or write tool instead of shell strings for file operations to avoid parsing issues.

## Dependencies
- Use python 3.12.13
- Always activate venv for virtual environment before running python or pip
- Maintain all dependencies in requirements.txt
- Use `sudo` whenever administrative privileges are required
- Always use `$GITHUB_TOKEN` environment variable for GitHub authentication in scripts and CI environments
