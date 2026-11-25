# NetBird on Elestio BYOVM

> **Deployment decision: conditional GO for a small IVF private mesh VPN.**
> The Elestio BYOVM free allowance can cover the Elestio management service for one qualifying VM, and NetBird's published minimum resource requirement fits within the BYOVM resource ceiling. This is not proof that the existing VM, public UDP path, or reverse-proxy integration is ready. Complete the gates below before production.

This guide is for the AndieKobbieTech-maintained NetBird fork. It deliberately separates the free Elestio BYOVM management allowance from the cost and eligibility of the underlying cloud VM.

- **Recommended use:** private staff/admin access to explicitly authorised IVF systems.
- **Not:** a consumer VPN, an internet-egress privacy service, or an automatic route to every IVF network.
- **Recommended first deployment:** one small Linux VM, NetBird's current combined server, embedded identity provider, persistent data, and a tested HTTPS/gRPC/WebSocket reverse-proxy path.
- **Production status:** not yet validated on an Elestio BYOVM host. Treat this as a reproducible deployment plan and test checklist, not a claim of a working live deployment.

## 1. Does it fit the Elestio free BYOVM tier?

### Published limits and requirements

| Item | Published requirement / limit | Assessment |
|---|---:|---|
| Elestio BYOVM free allowance | One BYOVM service; VM no larger than 2 vCPU, 4 GB RAM, 80 GB disk | Free Elestio management allowance, subject to eligibility |
| Elestio BYOVM VM minimum | 1 vCPU, 1 GB RAM, 20 GB disk | NetBird needs more RAM |
| NetBird self-hosted minimum | 1 CPU, 2 GB RAM | Fits the BYOVM ceiling |
| Recommended IVF target | 2 vCPU, 4 GB RAM, 40–80 GB disk | Fits exactly within the BYOVM ceiling |
| Public network | TCP 443 and UDP 3478; TCP 80 is used/required depending on certificate/reverse-proxy mode | Must be opened and tested |
| Domain | Public DNS A record to the VM's public IP | Required |

**Sizing conclusion:** a 2 vCPU / 4 GB / 40 GB Linux VM is a reasonable small-team starting point and fits Elestio's published free BYOVM ceiling. NetBird's own minimum is 1 CPU / 2 GB, but that leaves less headroom for the operating system, Docker, proxy and monitoring. This is a sizing recommendation, not a capacity benchmark or guarantee for a particular number of peers.

Elestio's BYOVM documentation says: “You can create one BYOVM service for free.” It also caps eligibility at 2 vCPU, 4 GB RAM and 80 GB storage. The underlying VM is supplied by your cloud provider. Elestio's free BYOVM management allowance does **not** make a paid cloud VM free.

### Existing Oracle Cloud VM: important eligibility issue

The existing AKCloud Oracle A1 VM recorded for this project is 4 OCPU / 24 GB RAM. **That VM exceeds Elestio's BYOVM free-tier ceiling** and should not be registered as the free BYOVM instance in its current shape.

Possible route:
1. Check whether the Oracle Cloud account has free-tier A1 quota available for a separate smaller VM, or whether the existing instance can safely be resized without disrupting other workloads.
2. Target no more than 2 OCPU, 4 GB RAM and 80 GB disk for Elestio BYOVM eligibility.
3. Confirm the Oracle Always Free quota, region capacity, boot-volume allowance and public IPv4 charges in the OCI console before creating or resizing anything.
4. If the VM is outside the Elestio cap, Elestio's BYOVM management charge may apply even if the cloud provider offers free compute.

Do not resize or repurpose the existing AKCloud VM without checking its workloads, backups and resource allocation first.

## 2. Architecture choice: use the current combined NetBird server

For a new installation, use the current NetBird self-hosting Quickstart architecture (NetBird Server combined container), not the fork's legacy multi-container/Coturn Compose profile.

The current NetBird quickstart states: “A Linux VM with at least 1CPU and 2GB of memory.” It requires public TCP 443 and UDP 3478. The current combined server includes management, signal, relay and STUN; the dashboard remains separate. It uses an embedded identity provider by default.

Why not deploy the fork's old Compose unchanged?

- The legacy deployment uses separate management, signal, relay and Coturn containers.
- The legacy Coturn service uses host networking in the existing deployment templates.
- Host networking and broad legacy TURN relay port ranges are a poor fit for a constrained, managed host unless deliberately validated.
- NetBird's current quickstart uses the consolidated server and only requires the public STUN UDP port 3478 for the default new deployment. Older clients may still require legacy ports; keep clients current and validate compatibility before removing legacy allowances.

**Important fork provenance:** the current upstream quickstart downloads the upstream NetBird release script. Do not use that command as a way of deploying this fork's unmerged changes. For fork testing, pin the Compose/config files and images to an explicitly reviewed fork-compatible release/build. For production, use a reviewed tag/commit after the maintenance PR has been merged and tested.

## 3. The two networking constraints

### 3.1 UDP 3478 must be direct

NetBird's reverse-proxy documentation states: “STUN requires direct UDP access.” UDP 3478 must be published directly from the server container and allowed through every firewall layer. It must not be sent through an HTTP reverse proxy.

Minimum inbound rules for a new combined-server deployment:

| Port | Protocol | Purpose | Exposure |
|---:|---|---|---|
| 443 | TCP | HTTPS dashboard, API, gRPC, signal and relay paths | Public |
| 3478 | UDP | STUN/NAT traversal | Public |
| 80 | TCP | Optional HTTP redirect / ACME HTTP challenge, depending on proxy mode | Public only if selected |
| 22 | TCP | SSH administration | Restrict to administrator IPs |
| 18345, 18374, 18445 | TCP | Elestio BYOVM tools | As required by Elestio; restrict if supported |

Do not open the legacy Coturn UDP range 49152–65535 for the new combined deployment unless a documented compatibility requirement makes it necessary.

Also verify outbound connectivity from the VM and client networks. A successful inbound UDP test alone does not prove peer-to-peer WireGuard connectivity.

### 3.2 Elestio BYOVM already has a host reverse-proxy layer

Elestio documents an Nginx/OpenResty reverse proxy in front of its services and supports custom per-site/global Nginx configuration. NetBird's bundled Traefik also expects to bind public ports 80/443.

**Do not start the default NetBird Traefik stack unchanged on a BYOVM host until the port ownership has been inspected.** If Elestio's host proxy already owns 80/443, a second host-level proxy cannot bind those ports.

The supported design must be one of:

- **Preferred if Elestio confirms the proxy supports it:** keep Elestio's front proxy on 443 and configure a dedicated NetBird virtual host with correct HTTP/2 gRPC and WebSocket routing to the combined NetBird server. Keep UDP 3478 published directly from the NetBird server to the public host.
- **Alternative:** use a documented, tested TCP/TLS passthrough arrangement that gives NetBird its own TLS termination without conflicting with Elestio's management proxy. This needs explicit Elestio approval and a dedicated DNS name/IP/port design.

A basic HTTP reverse-proxy host is not sufficient unless its configuration supports NetBird's gRPC (HTTP/2), WebSocket upgrades, and long-lived connections. Elestio's Nginx documentation shows a `stream` configuration facility, but that alone does not prove the required NetBird gRPC and WebSocket virtual-host routing has been tested on BYOVM.

**Deployment blocker:** obtain confirmation that the Elestio BYOVM proxy can route the NetBird combined-server endpoints on TCP 443 while leaving UDP 3478 directly reachable. If not, use a separate VM/public IP for NetBird or a hosting platform where the service can own TCP 443 and UDP 3478 directly.

## 4. Elestio CLI: what it can and cannot import

Install the CLI (Node.js 18 or later):

```bash
npm install -g elestio
elestio login --email YOUR_ACCOUNT_EMAIL --token YOUR_API_TOKEN
elestio auth test
elestio whoami
```

Keep the API token in your local credential store or shell secret manager. Do not paste it into this repository, a ticket, a README, or a command that will be saved in shell history.

### Route A — attach an existing free-tier VM using BYOVM

The BYOVM setup is documented as a dashboard flow, not as the same command as a CI/CD application import:

1. Create/verify the qualifying Linux VM with a static public IP and required firewall access.
2. Follow Elestio's official BYOVM instructions to install its temporary deployment SSH key and verify connectivity.
3. In the Elestio dashboard, choose **BYOVM**, enter the provider/region/public IP, run **Test my VM**, and create the BYOVM service.
4. Confirm the service is shown as the first/free BYOVM and that its registered VM shape remains within the free limits.
5. Inspect the Elestio firewall and host proxy before installing NetBird.

The BYOVM guide lists TCP 22, 80 and 443 plus Elestio tool ports 18345, 18374 and 18445; UDP 4242 is optional for Elestio's private network. **UDP 3478 is a NetBird-specific additional rule** and must be added at the cloud-provider security list/network firewall and the VM firewall. Elestio's documented minimum BYOVM firewall list does not include it.

Useful CLI checks after the VM is connected:

```bash
elestio services
elestio firewall get YOUR_VM_ID
elestio service YOUR_VM_ID
```

Do not replace the firewall with an allow-all rule. Add only the required UDP 3478 rule and keep SSH restricted.

### Route B — use Elestio CI/CD for a custom Docker Compose stack

This is a different product path from the free BYOVM management allowance. A CI/CD target VM is a hosting target and may incur infrastructure charges.

The current CLI documentation distinguishes:
- `github` / `github-fullstack`: supported Git app build modes.
- `docker`: custom Docker Compose mode, documented as **no Git** in the automatic mode.

For a custom Compose stack, Elestio documents a manual pipeline workflow:

```bash
# Deploy a CI/CD target only if you intend to use a separately billed
# Elestio-managed target. Check project, provider and price first.
elestio deploy cicd --project YOUR_PROJECT_ID --name netbird-cicd-target
elestio wait YOUR_VM_ID

# Add your SSH public key (never put a private key in the repository).
elestio ssh-keys add YOUR_VM_ID --name netbird-deploy --key "ssh-ed25519 YOUR_PUBLIC_KEY"

# Generate and edit the Docker Compose pipeline template.
elestio cicd template docker > pipeline.json
# Edit pipeline.json locally, then:
elestio cicd create pipeline.json
```

The documented manual pipeline then requires SSH access to the target and configuration of the Compose stack. The automated `elestio cicd create --auto --mode github` flow is designed for static/full-stack app modes; do not assume it will deploy a multi-service NetBird Compose project from Git.

If using Elestio's **Import Third-Party Git Repository** dashboard feature or a custom `elestio.yml` template, verify that the import method supports all Compose files, scripts, persistent mounts, environment files, and UDP port declarations. The Elestio template format supports UDP host and container protocols, but the exact service's public network path must still be tested.

## 5. Repository deployment workflow

The deployment should be reproducible and pinned to a reviewed commit.

1. Clone this fork:
   ```bash
   git clone https://github.com/andiekobbietks/netbird.git
   cd netbird
   ```
2. For a test deployment only, check out the reviewed maintenance branch:
   ```bash
   git fetch origin security/dependabot-sbom-governance
   git checkout security/dependabot-sbom-governance
   git rev-parse HEAD
   ```
3. Do not deploy the branch as a production release while the maintenance PR remains unmerged or required checks are incomplete.
4. For production, use a signed/reviewed tag from the default branch after merge; record the exact commit SHA in the deployment change record.
5. Store `.env`, OIDC secrets, encryption keys and credentials only on the VM with restrictive permissions. Never commit them.
6. Use persistent volumes for NetBird state and TLS data. Back up the data and prove restoration before onboarding staff.
7. Pin container image versions/digests. Avoid `:latest` for a production deployment.

The current upstream quickstart is useful for understanding the generated configuration, but do not pipe a remote script directly into Bash in production without inspecting and pinning the script revision first.

## 6. DNS and certificate plan

Choose a dedicated hostname such as `vpn.ivf.org.uk` (subject to IVF domain-owner approval).

- Create an A record to the VM's stable public IPv4 address.
- Keep the record DNS-only if using a DNS provider proxy that does not support the NetBird gRPC/WebSocket traffic and UDP STUN path.
- Issue a TLS certificate through the selected proxy/certificate method.
- Confirm TCP 443 is served by the intended NetBird virtual host, not an Elestio generic application page.
- Confirm UDP 3478 is reachable on the same public hostname/IP.

Do not assume a default `*.vm.elestio.app` application URL is suitable for the VPN control plane. Use a stable domain and verify certificate, gRPC and UDP behaviour.

## 7. Validation gates — all required before production

### Infrastructure and ownership
- [ ] VM is within 2 vCPU / 4 GB / 80 GB free BYOVM limits.
- [ ] Underlying cloud VM has no unexpected compute, public IPv4, storage, egress or backup charges.
- [ ] VM is backed up and restore-tested.
- [ ] Static public IP and DNS are controlled by the organisation.

### Port and proxy validation
- [ ] Identify which process owns host TCP 80 and 443 before starting containers.
- [ ] Elestio confirms the chosen BYOVM reverse-proxy integration is supported.
- [ ] TCP 443 routes dashboard, REST API, gRPC and WebSocket traffic correctly.
- [ ] UDP 3478 is directly mapped to the NetBird STUN listener.
- [ ] UDP 3478 is allowed by cloud security rules, Elestio firewall where applicable, and the VM firewall.
- [ ] External UDP test confirms the service responds; do not rely only on a local `ss` or Docker port listing.
- [ ] Test from two independent networks: peer discovery, direct WireGuard connection, and relay fallback.

### NetBird and security
- [ ] Fresh supported NetBird server/dashboard versions are pinned.
- [ ] Admin account is created securely; MFA/SSO is configured where supported.
- [ ] Device enrolment is controlled; test revocation of a lost device.
- [ ] IVF staff, administrators and infrastructure peers are separated by least-privilege policies.
- [ ] No access to sensitive systems is granted merely by joining the VPN.
- [ ] Database/configuration backups are encrypted and restore-tested.
- [ ] Logs, monitoring, upgrade and rollback procedures are documented.
- [ ] SBOM, vulnerability scan and image provenance evidence are retained for the deployed commit.

### Go/no-go rule
If Elestio cannot confirm the host proxy and UDP path, **do not deploy the NetBird control plane on that BYOVM host**. Use a separate qualifying VM where NetBird can own TCP 443 and UDP 3478, or select another host. Never weaken the firewall or disable TLS to force the deployment through.

## 8. Relevant documentation and quoted requirements

The short quotations below are from the linked primary documentation. The links are the authoritative source for details and may change.

1. **Elestio — BYOVM:** [Bring Your Own VM](https://docs.elest.io/platform/cloud-providers/byovm/)  
   > “You can create one BYOVM service for free.”  
   The same page limits free eligibility to no more than 2 vCPU, 4 GB RAM and 80 GB storage, and lists the BYOVM VM and firewall prerequisites.

2. **NetBird — Self-Hosting Quickstart:** [Self-Hosting Quickstart Guide](https://docs.netbird.io/selfhosted/selfhosted-quickstart)  
   > “A Linux VM with at least 1CPU and 2GB of memory.”  
   The page specifies public TCP 443 and UDP 3478 and describes the current combined-server quickstart.

3. **NetBird — External Reverse Proxy:** [External Reverse Proxy Setup](https://docs.netbird.io/selfhosted/external-reverse-proxy)  
   > “STUN requires direct UDP access.”  
   The page documents the gRPC, WebSocket and HTTP routes required by the combined server, and states that UDP 3478 must bypass the HTTP reverse proxy.

4. **Elestio — Nginx configuration:** [Nginx Configuration](https://docs.elest.io/platform/security/nginx-configuration/)  
   Elestio documents its Nginx/OpenResty reverse proxy and custom configuration, including a stream configuration section. This is why port ownership and the exact proxy design must be checked on BYOVM rather than assuming the NetBird bundled Traefik can bind 80/443.

5. **Elestio — CLI CI/CD:** [CI/CD Pipelines](https://docs.elest.io/developer-tools/elestio-cli/cicd/)  
   The CLI guide distinguishes automated Git app modes from custom Docker Compose mode, which is documented as no-Git, and provides the manual pipeline route.

6. **Elestio — custom template format:** [Create your own template](https://docs.elest.io/books/cicd-pipelines/page/create-your-own-template-elestioyml)  
   The template specification supports `UDP` as a host and target protocol. This establishes a configuration capability, not end-to-end UDP reachability on a particular BYOVM host.

7. **Elestio — third-party repository import:** [Deploy Apps via Git Repository Import](https://docs.elest.io/developer-tools/cicd-pipelines/deploy-examples-apps-on-elestio-using-the-import-third-party-git-repository-feature/)  
   Documents the dashboard import flow for public third-party Git repositories. Verify Compose, script, volume and UDP support for the specific template before relying on it.

8. **Elestio — service deployment FAQ:** [Services & Deployment](https://docs.elest.io/frequently-asked-questions/services-faq/)  
   Explains that a CI/CD target can host multiple software projects on one VM and describes the separate BYOVM management model.

## 9. Decision record

This guide implements the proposed decision for a low-volume IVF private mesh VPN:

- **Hosting:** Elestio BYOVM free management allowance, attached to a separately supplied qualifying Linux VM.
- **Initial sizing:** 2 vCPU / 4 GB RAM / 40 GB disk.
- **Server architecture:** current combined NetBird server, embedded IdP, dashboard, persistent storage.
- **Network:** direct public UDP 3478 and a correctly configured TCP 443 reverse-proxy route.
- **Deployment method:** BYOVM attachment through Elestio dashboard; use Elestio CLI for inspection/management and a manual Compose pipeline only if a separately priced CI/CD target is intentionally selected.
- **Status:** conditional GO; no production deployment until the proxy/UDP tests and cost checks pass.

Related fork ADRs: [ADR index](docs/adr/README.md). This file is operational guidance and does not supersede the ADRs or upstream NetBird documentation.
