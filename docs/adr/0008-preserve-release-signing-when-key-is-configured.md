# ADR-0008: Preserve release signing when a key is configured

- **Status:** Proposed
- **Date:** 2026-11-25
- **Decision owners:** NetBird fork maintainers
- **Related:** `.goreleaser_ui.yaml`, `.goreleaser_ui_gtk3.yaml`, `.goreleaser_ui_linux_arm64.yaml`

## Context

The upstream UI release configurations expect an RPM signing key. Fork CI runs may not have access to the upstream signing secret. Treating an absent secret as an invalid key causes unsigned fork validation builds to fail before they can test packaging. Silently disabling signing in a real release would, however, weaken release integrity.

## Decision

We will make the RPM signature configuration conditional on the presence of `GPG_RPM_KEY_FILE`. When the key is configured, GoReleaser must use it. When the key is absent, fork validation builds may proceed without RPM signing; those outputs must not be represented as signed releases.

## Options considered

| Option | Benefits | Costs / risks |
|---|---|---|
| Conditional signing based on configured key | Supports fork validation while preserving signing when configured | Requires clear distinction between test and publish workflows |
| Require upstream signing secret in every fork build | Uniform signing configuration | Fork CI cannot validate packaging without upstream secret access |
| Always disable signing | Simplifies builds | Removes signing even where a key is available |

## Consequences

### Positive
- Fork CI can validate packaging without possessing upstream private signing material.
- A configured key remains the signing authority for RPM packages.
- No private signing key needs to be copied into the fork.

### Negative / trade-offs
- An unsigned test artifact can be mistaken for a release unless labelled clearly.
- Conditional templating must be validated against all affected GoReleaser configurations.

### Operational implications
- Never commit signing keys or export them into logs.
- Publish only through the intended protected release path.
- Verify signatures independently before distributing signed RPMs.

## Validation and evidence

The three listed UI GoReleaser configurations use conditional signature blocks. Configuration rendering and a release-path test with and without the key must pass before this decision is considered validated.
