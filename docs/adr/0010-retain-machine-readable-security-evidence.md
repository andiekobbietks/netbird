# ADR-0010: Retain machine-readable security evidence

- **Status:** Proposed
- **Date:** 2026-11-25
- **Decision owners:** NetBird fork maintainers
- **Related:** `.github/workflows/sbom.yml`

## Context

Security scans are useful only if their outputs can be inspected, compared and tied to a source revision. A transient log or a badge alone is insufficient for triage, audit and later investigation.

## Decision

We will retain the SPDX SBOM, CycloneDX SBOM and Grype SARIF report together as a named workflow artifact, with the commit SHA in the artifact name and a bounded retention period. SARIF upload to GitHub Code Scanning will occur only on non-pull-request events, avoiding attempts to upload untrusted PR results with elevated security-events permissions.

## Options considered

| Option | Benefits | Costs / risks |
|---|---|---|
| Retain versioned SBOM and SARIF artifacts | Reproducible evidence for investigation | Storage and retention management |
| Keep only console output | Low storage cost | Difficult to reuse and compare |
| Upload all PR SARIF results | Immediate PR visibility | Requires careful trust and permission design |

## Consequences

### Positive
- Findings can be inspected after the workflow completes.
- Artifacts are tied to the source commit.
- PR workflows avoid the Code Scanning upload path.

### Negative / trade-offs
- Ninety-day retention is not a permanent audit archive.
- Artifact availability depends on successful workflow completion and repository retention settings.

### Operational implications
- Download and preserve evidence externally when a longer retention period is required.
- Record the workflow run URL and commit SHA in remediation tickets.
- Do not report scan status from an artifact that has not been retrieved and inspected.

## Validation and evidence

The proposed workflow retains three outputs for 90 days. Artifact presence, contents and SARIF ingestion must be confirmed from a successful run.
