# ADR-0001: Maintain a traceable upstream fork

- **Status:** Proposed
- **Date:** 2026-11-25
- **Decision owners:** NetBird fork maintainers
- **Related:** [PR #2](https://github.com/andiekobbietks/netbird/pull/2), `.github/workflows/sync-main.yml`, `.github/workflows/sync-tag.yml`

## Context

This repository is a fork of NetBird. The fork needs to carry its own maintenance and supply-chain controls without obscuring which application behaviour comes from upstream and which changes are fork-specific. Untraceable divergence increases merge conflict risk, complicates vulnerability response and makes it difficult to explain the provenance of a release.

## Decision

We will keep upstream NetBird as the reference implementation and maintain fork-specific changes as small, reviewable, attributable commits. Changes to upstream application behaviour must be distinguished from fork maintenance changes. Upstream synchronisation must not silently overwrite local security controls or release policy.

## Options considered

| Option | Benefits | Costs / risks |
|---|---|---|
| Keep a traceable fork with focused commits | Clear provenance; easier upstream comparison and review | Requires ongoing conflict resolution |
| Maintain a long-lived independent codebase | Maximum freedom | High divergence and patch-maintenance cost |
| Replace upstream history with a squashed snapshot | Simpler visible history | Loses useful provenance and makes future synchronisation harder |

## Consequences

### Positive
- Reviewers can identify the origin and purpose of fork-specific changes.
- Upstream security fixes can be evaluated and adopted with less ambiguity.
- The maintenance branch can be reviewed independently before changes reach the default branch.

### Negative / trade-offs
- Upstream changes may conflict with fork-specific workflows or release configuration.
- Maintainers must regularly compare upstream and fork state.

### Operational implications
- Keep upstream sync changes separate from local policy changes where practical.
- Document material divergence and link the relevant PRs.
- Do not claim compatibility with upstream releases without testing the relevant commit.

## Validation and evidence

The repository contains upstream synchronisation workflows. Their behaviour and branch-protection interaction must be verified in CI before relying on them as a safety boundary.
