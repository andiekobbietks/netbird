# ADR-0004: Publish source SBOMs in SPDX and CycloneDX

- **Status:** Proposed
- **Date:** 2026-11-25
- **Decision owners:** NetBird fork maintainers
- **Related:** `.github/workflows/sbom.yml`

## Context

A software bill of materials provides a machine-readable inventory of components. Different consumers and security tools support different SBOM formats. A single format could limit interoperability with downstream inventory, audit and vulnerability-management systems.

## Decision

We will generate source SBOMs in SPDX JSON and CycloneDX JSON from the same checked-out source revision. The workflow will publish both as build artifacts with the source commit identified in the artifact name.

## Options considered

| Option | Benefits | Costs / risks |
|---|---|---|
| SPDX and CycloneDX | Broad interoperability | More artifact storage and format validation |
| SPDX only | Strong licence and provenance ecosystem | Some consumers prefer CycloneDX |
| CycloneDX only | Strong security and dependency analysis ecosystem | Some consumers prefer SPDX |

## Consequences

### Positive
- Downstream consumers can choose the format their tooling supports.
- Both inventories can be compared against the same source revision.
- SBOMs become retrievable evidence for a given workflow run.

### Negative / trade-offs
- Two outputs increase storage and require validation of both.
- Generated SBOMs are only as complete as the build tool's package discovery.

### Operational implications
- Keep SBOM generation tied to an immutable commit SHA.
- Retain the SPDX, CycloneDX and associated vulnerability report together.
- Do not describe an SBOM as a complete inventory of runtime contents without validating its coverage.

## Validation and evidence

The proposed workflow writes `sbom/netbird.spdx.json` and `sbom/netbird.cyclonedx.json`. Artifact generation and schema validity must be confirmed from a successful workflow run.
