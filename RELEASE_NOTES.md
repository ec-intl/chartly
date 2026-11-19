# chartly v1.1.3 — release candidate

Prepared from staging for human review on 2026-11-19. No tag, release, or deployment has been published.

## Included change record

- dependency: Update setuptools and align pytest environments.
- release: Install package upload tooling and validate distributions.

These candidate notes are prepared on the release branch for review before promotion. The prior log is preserved in release-log-archive-2026-11-19.txt.

## Net change inventory

- `requirements.txt`
- `requirements/production.txt`
- `requirements/staging.txt`
- `requirements/testing.txt`

## Promotion

Review and merge the release-preparation PR into staging first, then review staging → main. Keep auto-merge disabled. Release/CD jobs may publish packages, update production branches, and build/push images after promotion.
