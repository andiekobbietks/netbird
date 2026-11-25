# ADR-0003: Pin CI actions to immutable commits

- **Status:** Proposed
- **Date:** 2026-11-25
- **Decision owners:** NetBird fork maintainers
- **Related:** `.github/workflows/dependency-review.yml`, `.github/workflows/sbom.yml`, `.github/workflows/release.yml`

## Context

GitHub Actions referenced by mutable tags can change after a workflow has been reviewed. A compromised or unexpectedly retagged action can therefore change CI behaviour without a corresponding repository diff.

## Decision

We will pin third-party GitHub Actions used by the fork's security-sensitive workflows to full commit SHAs and retain a human-readable version comment. Dependabot will propose updates to those pins. Updates must be reviewed as code changes and validated by the workflow that consumes them.

## Options considered

| Option | Benefits | Costs / risks |
|---|---|---|
| Full commit SHA pins | Immutable reference to reviewed action code | Less readable; updates require deliberate PRs |
| Major-version tags | Readable and convenient | Mutable reference |
| Vendor every action into the repository | Strong local control | High maintenance and update burden |

## Consequences

### Positive
- The action reference cannot silently move to different code under the same tag.
- Updates become visible and reviewable.
- Version comments preserve human readability.

### Negative / trade-offs
- Pins can become stale and miss upstream fixes.
- Reviewers must verify that version comments match the pinned commit.

### Operational implications
- Require full SHA pins for new third-party actions in security-sensitive workflows.
- Review the upstream release and commit provenance before updating a pin.
- Avoid unreviewed bulk pin changes.

## Validation and evidence

The new dependency-review workflow and SBOM workflow use full SHA references. A repository-wide audit is still required before claiming every workflow action is pinned.
