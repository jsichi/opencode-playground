# Python Project

This is a simple python project.

## Collaboration

- Always make changes to a branch.  After pushing, github pull requests should be submitted against the main repository (jsichi/opencode-playground).
- To submit a PR from your fork's branch to upstream main:
  ```bash
  git checkout -b feature-branch
  # make changes and commit
  git push origin feature-branch
  gh pr create -R jsichi/opencode-playground -t "Feature title" -b "Description here" -H jellyfishshot:feature-branch -B main
  ```

## Dependencies
- Use python 3.12.13
- Always activate venv for virtual environment before running python or pip
- Maintain all dependencies in requirements.txt
- Use `sudo` whenever administrative privileges are required
