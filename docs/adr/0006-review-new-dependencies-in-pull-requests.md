# ADR-0006: Review newly introduced dependencies in pull requests

- **Status:** Proposed
- **Date:** 2026-11-25
- **Decision owners:** NetBird fork maintainers
- **Related:** `.github/workflows/dependency-review.yml`

## Context

A dependency update can introduce a vulnerable package or a transitive dependency even when the change is small. SBOM scans provide inventory-level visibility, but pull-request review can catch newly introduced risk before it becomes part of the maintained branch.

## Decision

We will run GitHub's Dependency Review action on pull requests and fail the check when a newly introduced dependency is reported at low severity or above. The workflow receives read-only repository contents permission and does not post PR comments.

## Options considered

| Option | Benefits | Costs / risks |
|---|---|---|
| Dependency Review on every PR | Detects new dependency risk before merge | Depends on GitHub advisory and dependency graph coverage |
| Periodic SBOM scan only | Simple and useful for baseline visibility | Detection may occur after merge |
| Manual review only | Flexible judgement | Easy to miss transitive changes |

## Consequences

### Positive
- New dependency risk is surfaced in the PR validation path.
- Read-only permissions limit workflow authority.
- No automated comments reduce unnecessary PR noise.

### Negative / trade-offs
- The action cannot prove that a dependency is safe.
- Results depend on GitHub's dependency graph and advisory data.
- A low-severity threshold may require review of findings that are not exploitable in the product's context.

### Operational implications
- Treat the result as one control in a layered process, not a replacement for SBOM scanning or code review.
- Review any exception explicitly and document its rationale.
- Keep the action pinned to a full commit SHA.

## Validation and evidence

The workflow is configured for opened, reopened, synchronized and edited pull requests. A successful current run is required before treating it as an enforced check.
