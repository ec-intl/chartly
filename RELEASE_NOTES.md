# chartly v1.1.3 — release candidate

Prepared from staging for human review on 2026-11-19. No tag, release, or deployment has been published.

## Included change record

The accumulated release log is stale. This candidate preserves current main history and adds the staged setuptools/pytest updates and packaging repairs. Reconcile the release log before publication.

## Net change inventory

- `requirements.txt`
- `requirements/production.txt`
- `requirements/staging.txt`
- `requirements/testing.txt`

## Promotion

Review and merge the release-preparation PR into staging first, then review staging → main. Keep auto-merge disabled. Release/CD jobs may publish packages, update production branches, and build/push images after promotion.
