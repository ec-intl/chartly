# chartly v1.1.3 — release candidate

## Public release automation correction — 2026-11-26

Release publishing now runs locally using the built-in GitHub token, after any
existing deployment job succeeds. It verifies the current main commit matches
staging's tree and refuses to reuse a version tag from another commit. GitHub
generates release notes from repository history. No internal workflow access or
RPAT is needed for this release job.

The separate release-log workflow is removed: generated release notes replace
its bookkeeping. Existing log files remain as history. This job does not rewrite
main/staging, delete feature branches, or update a production branch. Existing
package deployment steps are preserved. Validate hosted checks before promotion;
publication is a separate outcome to verify after merge.

The earlier preparation records below are historical; their shared-template and
RPAT prerequisites are superseded for these two workflows.

Prepared from staging for human review on 2026-11-19. No tag, release, or deployment has been published.

## Included change record

- dependency: Update setuptools and align pytest environments.
- release: Install package upload tooling and validate distributions.

These candidate notes are prepared on the release branch for review before promotion. The prior log is preserved in the [release-branch archive](https://github.com/ec-intl/chartly/blob/0ff0003721deec13dce6df28e592256d03cf3ce6/release-log-archive-2026-11-19.txt).

## Net change inventory

- `requirements.txt`
- `requirements/production.txt`
- `requirements/staging.txt`
- `requirements/testing.txt`

## Promotion

Review and merge the release-preparation PR into staging first, then review staging → main. Keep auto-merge disabled. Release/CD jobs may publish packages, update production branches, and build/push images after promotion.
