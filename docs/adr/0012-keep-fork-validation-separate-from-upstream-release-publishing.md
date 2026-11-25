# ADR-0012: Keep fork validation separate from upstream release publishing

- **Status:** Proposed
- **Date:** 2026-11-25
- **Decision owners:** NetBird fork maintainers
- **Related:** `.github/workflows/release.yml`

## Context

This repository is a fork, not the upstream NetBird release authority. Running release workflows in a fork is useful for validating build and packaging changes, but publishing images, packages or official releases under upstream identities would be incorrect and could require secrets that the fork must not possess.

## Decision

We will keep fork validation and upstream publication separate. Fork-triggered release workflows must not publish official NetBird releases or push images to upstream registries. Publishing remains limited to the explicitly authorised upstream repository and release path. Fork builds must not depend on upstream signing or publishing secrets.

## Options considered

| Option | Benefits | Costs / risks |
|---|---|---|
| Validate in fork, publish only from authorised upstream | Clear authority and secret boundary | Fork cannot fully exercise every publishing step |
| Allow fork to publish to upstream destinations | End-to-end release test | Incorrect authority and high secret exposure risk |
| Disable release workflows entirely in fork | Lowest risk | Loses valuable build and packaging validation |

## Consequences

### Positive
- The fork can validate release configuration without impersonating upstream.
- Upstream publishing credentials remain outside the fork's trust boundary.
- The origin of published artefacts remains clear.

### Negative / trade-offs
- Some publishing behaviour can only be validated in the authorised release environment.
- Fork maintainers need a separate, explicitly configured destination if they later choose to publish fork-branded releases.

### Operational implications
- Keep fork publish and Docker push guards enabled.
- Never copy upstream signing or registry credentials into this fork.
- If fork-branded releases are introduced, define their naming, signing identity, registry namespace and disclosure policy in a new ADR before enabling publication.

## Validation and evidence

The release workflow currently defaults publishing off and sets Docker push to skip when the repository is not `netbirdio/netbird`. Verify these guards in the actual fork workflow run before relying on them.
