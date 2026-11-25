# ADR-0007: Attach SBOM attestations to container images

- **Status:** Proposed
- **Date:** 2026-11-25
- **Decision owners:** NetBird fork maintainers
- **Related:** GoReleaser configuration files, container image build definitions

## Context

A source SBOM does not fully describe the contents of every built container image. Base images, build stages and packaging steps can alter the final component inventory. Consumers need supply-chain metadata associated with the image they actually deploy.

## Decision

We will enable BuildKit SBOM attestations on the repository's supported container image build definitions, so image builds can carry an SBOM attestation alongside the image. The source SBOM remains a separate artefact and is not presented as a substitute for image-level metadata.

## Options considered

| Option | Benefits | Costs / risks |
|---|---|---|
| Build-time image SBOM attestations | Metadata is associated with the image build | Requires compatible builders and verification by consumers |
| Source SBOM only | Simple and useful for source dependency inventory | Does not represent final image contents |
| Post-build image scanning only | Inspects built image contents | Does not itself provide attached provenance metadata |

## Consequences

### Positive
- Image consumers have a path to inspect component inventory for the built image.
- Source and image-level inventory can be compared.
- Metadata is generated as part of the image build process.

### Negative / trade-offs
- Attestations increase build complexity and may vary with build tooling.
- An attestation is not proof that an image is vulnerability-free or that its provenance is trusted.

### Operational implications
- Verify attestations on published images before claiming they are available to consumers.
- Preserve image digests and build provenance with release evidence.
- Review all image build definitions when new images are added.

## Validation and evidence

BuildKit SBOM settings have been added to the maintained GoReleaser image definitions. A successful release build and consumer-side attestation verification remain required.
