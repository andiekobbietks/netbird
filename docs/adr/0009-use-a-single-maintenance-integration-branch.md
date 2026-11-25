# ADR-0009: Use a dedicated maintenance integration branch

- **Status:** Proposed
- **Date:** 2026-11-25
- **Decision owners:** NetBird fork maintainers
- **Related:** `security/dependabot-sbom-governance`, [umbrella PR #2](https://github.com/andiekobbietks/netbird/pull/2)

## Context

The fork's security and supply-chain changes span multiple workflows, build definitions and dependency proposals. Landing each change directly on the default branch would make the overall change difficult to review and could leave the repository in a partially configured state.

## Decision

We will stage this maintenance programme on a dedicated integration branch and expose it through a single umbrella pull request. Related dependency PRs may remain separate for review, but they must target the integration branch and must not be merged without reviewing their diffs and current checks. The default branch is updated only through the normal reviewed merge process.

## Options considered

| Option | Benefits | Costs / risks |
|---|---|---|
| Dedicated branch plus umbrella PR | Coherent review boundary and staged validation | Requires careful child-PR base management |
| Direct commits to default branch | Fewer branches | Weak review and rollback boundary |
| One very large manually assembled commit | Single diff | Poor attribution and difficult review of dependency changes |

## Consequences

### Positive
- Reviewers can inspect the complete maintenance proposal in one place.
- Dependency changes retain their own diffs and test histories.
- The default branch is not changed by this staging work.

### Negative / trade-offs
- Child PRs can become stale or conflict as the integration branch moves.
- A green child check does not guarantee that the combined branch is green.

### Operational implications
- Refresh checks after each integration batch.
- Never merge a child PR with failed, missing or stale checks.
- Require the umbrella PR's complete required CI and security matrix to pass before merging it.

## Validation and evidence

The integration branch and umbrella PR exist. The PR is not a substitute for successful CI; merge readiness must be assessed from current check runs and mergeability.
