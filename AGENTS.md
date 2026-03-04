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
- For file content creation (like .gitignore), use heredocs or write tool instead of shell strings to avoid parsing issues.
- After rebasing onto upstream, force-push with `git push --force-with-lease`. Use git credential helper via `gh auth git-credential` for authentication.

## Dependencies
- Use python 3.12.13
- Always activate venv for virtual environment before running python or pip
- Maintain all dependencies in requirements.txt
