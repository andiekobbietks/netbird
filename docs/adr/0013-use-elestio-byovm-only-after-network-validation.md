# ADR-0013: Use Elestio BYOVM only after direct UDP and proxy validation

- **Status:** Proposed
- **Date:** 2026-11-25
- **Decision owners:** NetBird fork maintainers and IVF infrastructure owner
- **Related:** [Elestio deployment guide](../../elestio.md), [ADR index](README.md), [NetBird quickstart](https://docs.netbird.io/selfhosted/selfhosted-quickstart), [Elestio BYOVM](https://docs.elest.io/platform/cloud-providers/byovm/)

## Context

The project wants a low-cost self-hosted NetBird control plane for an organisation. Elestio offers one free BYOVM management service for a VM within a published ceiling of 2 vCPU, 4 GB RAM and 80 GB disk. NetBird's current self-hosting quickstart specifies a minimum Linux VM of 1 CPU and 2 GB RAM, with public TCP 443 and UDP 3478.

However, BYOVM hosts use Elestio's host reverse-proxy and management services. NetBird's bundled Traefik also expects public TCP 80/443. A second proxy cannot simply bind the same host ports. In addition, NetBird STUN requires direct UDP 3478 and cannot be routed through an HTTP reverse proxy. Elestio's generic support for UDP port mappings does not by itself prove end-to-end packet reachability on a specific BYOVM VM.

The repository's legacy multi-container Compose deployment includes a Coturn host-network arrangement and is not an appropriate unchanged deployment profile for this constrained BYOVM target. New deployments should evaluate the current combined NetBird server architecture.

## Decision

We will treat Elestio BYOVM as a **conditional hosting option**, not an already validated production target.

A small deployment may be considered when:
- the connected VM is within the BYOVM free-tier limits;
- the underlying VM and public networking are separately confirmed to be free or budget-approved;
- the Elestio reverse-proxy integration supports the NetBird dashboard, HTTP API, gRPC over HTTP/2 and WebSocket endpoints on TCP 443;
- UDP 3478 is directly published and externally reachable;
- the selected Compose configuration avoids host-port conflicts with Elestio-managed services.

The preferred initial sizing target is 2 vCPU, 4 GB RAM and 40 GB disk, subject to provider quota and capacity. Use the current combined NetBird server, embedded IdP and persistent volumes. Do not use the old Coturn host-network profile unchanged.

## Options considered

| Option | Benefits | Costs / risks |
|---|---|---|
| Elestio BYOVM on a qualifying external VM | Free Elestio management allowance for one eligible VM; provider choice | Proxy and UDP path need explicit validation; underlying VM costs remain provider-dependent |
| Elestio-managed CI/CD target | Integrated Compose pipeline management | Target VM is a separate hosting service and may incur charges; custom Docker mode is not the same as Git auto-deploy |
| Separate unmanaged VM with direct port ownership | NetBird can own TCP 443 and UDP 3478 directly | Less Elestio management integration |
| NetBird Cloud | No self-hosted control-plane operations | Managed service cost and different data/control boundary |

## Consequences

### Positive
- A qualifying low-resource VM can fit NetBird's published minimum and Elestio's BYOVM ceiling.
- The deployment has an explicit cost and networking gate.
- The new combined server avoids unnecessary legacy Coturn relay port exposure for current clients.

### Negative / trade-offs
- The existing 4 OCPU / 24 GB Oracle A1 VM exceeds Elestio's free BYOVM ceiling in its current shape.
- A smaller Oracle VM may require available Always Free quota and regional capacity.
- Elestio's host proxy may conflict with the bundled NetBird Traefik unless the proxy is deliberately configured and tested.
- Public UDP 3478 is an additional network/firewall requirement not listed in Elestio's minimum BYOVM firewall rules.
- The free BYOVM allowance does not make the underlying VM, public IPv4, storage, egress or backups free.

### Operational implications
- Inspect host port ownership before deploying.
- Add UDP 3478 at the cloud firewall and VM firewall; do not replace the firewall with allow-all rules.
- Test TCP 443 dashboard, API, gRPC and WebSocket paths.
- Test STUN reachability from outside the VM and verify direct WireGuard and relay fallback from independent networks.
- Back up and restore the persistent NetBird data before onboarding users.
- Keep this deployment on a reviewed, pinned fork release; do not deploy an unmerged maintenance branch to production.

## Validation and evidence

The official Elestio BYOVM documentation states one free BYOVM service is available within 2 vCPU / 4 GB RAM / 80 GB disk. NetBird's current quickstart documents a 1 CPU / 2 GB minimum and TCP 443 / UDP 3478 reachability. NetBird's external reverse-proxy documentation explicitly requires direct UDP STUN access and HTTP/2 gRPC/WebSocket routing.

The repository guide records the implementation and validation checklist. **No live Elestio BYOVM instance, external UDP test, proxy route test or production deployment has been completed as part of this ADR.** The decision remains Proposed until those tests pass.


## CI/CD controls

The fork adds `.github/workflows/elestio-validation.yml` for static documentation, local-link and workflow-YAML checks. This is not a live infrastructure test and does not validate public UDP 3478, gRPC, WebSocket routing or peer connectivity.

The optional `.github/workflows/elestio-deploy.yml` is a manual, `main`-only, environment-protected action. It requires successful validation for the exact commit and explicit operator confirmation, then asks Elestio to restart an existing CI/CD pipeline. It does not provision a BYOVM VM, create a paid pipeline target, change firewall/DNS/proxy configuration, or prove service health. A direct BYOVM attachment without an Elestio CI/CD pipeline is outside this workflow.

These controls improve repeatability but do not change the production go/no-go rule: the external proxy and direct UDP tests must pass before the control plane is used for IVF.
