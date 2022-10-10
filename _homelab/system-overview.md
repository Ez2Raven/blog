---
title: Home Lab Cloud System Overview
header:
    teaser: assets/images/homelab-system-th.png
sidebar:
    title: "In This Series"
    nav: homelab
toc: true
classes: wide
excerpt_separator: "<!--more-->"
part: 3
tags: homelab
---

{% capture notice-1 %}
This is Part 3 of the "{{page.display_name}}" series.

In this article, I'll share how I would build a malleable cloud environment for the purpose of modern software development.

P.S: It's easier to write about budgeting after drafting the system overview. :smiley:
{% endcapture %}

<div class="notice--info">{{ notice-1 | markdownify }}</div>

<!--more-->

# Introduction
Based on the initial requirements laid out in [Part 1: Development Sandbox Solution Design]({% link _homelab/solution-design.md %}),
I have spent about 8 man hours exploring diagramming as code to document what I wish to implement on Azure Cloud. 

In short, I managed to convert the scribbling of a mad techie...
![homelab-cloud-draft]({{ "/assets/images/homelab-cloud-draft.png" | relative_url }})

to a generated diagram that can be source controlled and **does not require hand adjustments**. 
![homelab-iaas]({{ "/assets/images/homelab-iaas.png" | relative_url }})

# What's Included In Draft 1?
Here's a brief summary of the scope and justification for each resource:

| Resource                    | Why                                                                                                                         |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Azure Kubernetes Service    | User defined orchestration for operating applications without managing underlying infrastructure.                           |
| Azure DB for MySQL          | Supports Change Data Capture but cheaper than MSSQL.                                                                        |
| Azure Redis Cache           | Provides caching for global region without the need to deploy multi-region kubernetes clusters for home lab.                |
| Azure Monitor + AppInsights | Faster "time to market" for monitoring home lab, at the cost of vendor lock-in.                                             |
| Azure Container Registry    | Affordable for individual usage, native integration with AKS and Azure DevOps.                                              |
| Azure Key Vault             | Centralized management for application/devsecops secrets, native integration with Azure AD RBAC.                            |
| Azure DNS Zone              | Affordable DNS service that is usually supported on Load Balancers for LetsEncrypt DNS Challenge. (Keep TCP port 80 closed) |
| Azure AD B2C                | **Customer** identity server that provides OIDC integrations with social media platforms and bespoke applications.          |
| Azure Active Diretory       | **Organization User** identity server that can be federated with Azure AD B2C or On-Premise identity servers.               |

# Exclusions (~because reasons~)
Here's a list of resources that will not be implemented in my first rollout:

| Resource         | Why                                                                        |
|------------------|----------------------------------------------------------------------------|
| Azure Firewall   | Not going to spend $900 per month on home lab for a single person.         |
| Atlassian Tools  | Moved to upcoming article on DevSecOps toolchain.                          |
| Github           | Moved to upcoming article on DevSecOps toolchain.                          |
| Bastion          | Limited use case, but required when working on hybrid cloud AD federation. |
| Jump Machine     | Limited use case, but required when handling sensitive data on the cloud.  |
| Dockerhub        | Replaced with ACR, since ACR is relative affordable for individual usage.  |
| Azure Front Door | Base cost $35 + traffic charges to enable custom domain for Azure AD B2C   |

Experience has taught me to articulate design considerations that are omitted from scope.
I encourage peers to exercise appropriate evaluations, so as to create awareness for security and productivity. 
{: .notice--warning}

# Considerations Due To Exclusions
Let's do a quick evaluation and document workaround for our omissions above.

## Azure Firewall
We will use NSGs (Network Security Group) to secure Layer 3-4, restricting data to/from network ports within each provisioned VNET (Virtual Network).
If need be, we can also bind the NSGs rules to individual NICs (Network Interface) belonging to individual Azure resource. 

We will have to give up on Layer 5-7 (Session, Presentation, Application) security policies, but it's a luxury resource for a home lab at $900 per month.

## Bastion
The alternate implementation is to provision a secured Windows VM (Virtual Machine) in a sanctioned VNET and whitelist ip ranges using VNET peering.
However, the responsibility to timely secure and update the host OS will fall upon us.

## Jump Machine
One consideration to avoid a dedicated jump server is to provision ssh keys for accessing cloud resources (whenever possible).
SSH Key provisioning is still manageable for a small number of users.

Another consideration is to build data pipelines and tools to encrypt sensitive data in databases and log storages.
Viewing of sensitive data has to be built as a feature within application services, in this way, we can decrypt these data in memory 
and leverage on applications' authentication and authorization measures to restrict access.

Your data security requirements may vary, and in its strictness form, it is very unlikely we can avoid a secured jump machine/bastion.
But for a home lab with no real data, it should be fine.
{: .notice--warning}

# What's Next?
It is going to take me a while to pick up Terraform or it's equivalent to implement a vendor agnostic approach to managing cloud resources.
Depending on my availability, I may choose to write about my specific implementation using Azure CLI.
This may influence the design for an "immutable" cloud infrastructure, since the investment in coding does not scale linearly when considering vendor lock-in.

Regardless, the system overview diagram is constructed, and perhaps, I should focus on provisioning the DevSecOps toolchain and 
leave writing immutable infrastructure for last.