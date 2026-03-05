# Python Project

This is a simple python project.

## Collaboration

- **Never commit directly to `main`. Always create and work on a feature branch.**

### Starting a new PR
To create a new branch:
```bash
git checkout main
git pull origin main
git checkout -b feature-branch
```

After working on your branch, push it to your fork and submit a PR against the upstream repository `jsichi/opencode-playground`.
- To check status: `git status`, view changes: `git diff`, stage files: `git add .`, commit: `git commit -m "message"`

### Creating a Pull Request
To submit a PR from your fork's branch to upstream main:
```bash
gh pr create --repo jsichi/opencode-playground --head jellyfishshot:feature-branch --base main --title "Feature title" --body "Description here"
```

### Syncing after Merge
After your PR is merged, sync back to keep remotes up to date:
- Remote sync: `git remote add jsichi https://github.com/jsichi/opencode-playground.git` (if not already added) then `git fetch jsichi && git merge jsichi/main --no-commit --no-ff` or use `gh repo sync -b main`
- Local sync: `git checkout main && git pull upstream/main`

Use heredocs or write tool instead of shell strings for file operations to avoid parsing issues.
- After rebasing onto upstream, force-push with `git push --force-with-lease`. Use git credential helper via `gh auth git-credential` for authentication.

## Dependencies
- Use python 3.12.13
- Always activate venv for virtual environment before running python or pip
- Maintain all dependencies in requirements.txt
- Use `sudo` whenever administrative privileges are required
- Always use `$GITHUB_TOKEN` environment variable for GitHub authentication in scripts and CI environments
