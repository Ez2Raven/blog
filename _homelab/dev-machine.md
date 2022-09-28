---
title: Development Machine Provisioning
header:
    image: assets/images/homelab.jpg
    caption: "Which is better? Vertical or Horizontal Monitor Mount?"
    teaser: assets/images/homelab-th.jpg
sidebar:
    title: "In This Series"
    nav: homelab
toc: true
classes: wide
excerpt_separator: "<!--more-->"
part: 2
---

{% capture notice-1 %}
This is Part 2 of the "{{page.display_name}}" series. 

In this article, we will explore the ease of installing the software needed
on our development machine.
{% endcapture %}

<div class="notice--info">{{ notice-1 | markdownify }}</div>

<!--more-->

# List Of Software and Tools

| Purpose                       | Tool                | Website                                                      | Install via Chocolatey? |
|-------------------------------|---------------------|--------------------------------------------------------------|:-----------------------:|
| Windows Package Management    | Chocolatey          | https://chocolatey.org/                                      |           NA            |
| Mind Mapping                  | XMind               | https://xmind.app/                                           |            y            |
| Source Control                | Git                 | https://git-scm.com/                                         |            y            |
|                               | Github CLI          | https://cli.github.com/                                      |            y            |
| Browser                       | Firefox             | https://www.mozilla.org/en-US/firefox/new/                   |            y            |
| File Archiver                 | 7-Zip               | https://www.7-zip.org/                                       |            y            |
| C# IDE                        | Rider               | https://www.jetbrains.com/rider/                             |            y            |
| Code Editor                   | Fleet               | https://www.jetbrains.com/fleet/                             |            y            |
| Containerization              | Docker Desktop WSL2 | https://docs.docker.com/desktop/windows/wsl/                 |  prefer manual install  |
| Azure CLI                     | Azure CLI           | https://learn.microsoft.com/en-us/cli/azure/install-azure-cli |  prefer manual install  |
| Kubernetes Package Management | Helm                | https://helm.sh/                                             |            y            |
| Fancy Terminal                | Windows Terminal    | https://github.com/microsoft/terminal                        |            y            |

{% capture notice-2 %}
#### My Take On Chocolatey For Organization Usage (Not Legal Advice)
Having dedicated DevOps personnel does not mean an organization understands who the repositories mainainers are,
and by extension, the intent and changes made by public maintainers. 

It is in an organization's best interest to assume ownership of its own private repositories so 
that DevOps personnel can inspect the code in the packages and validate them to ensure
packages adhere to the organization standards.
{% endcapture %}

<div class="notice--danger">{{ notice-2 | markdownify }}</div>

**To Be Continued:** How to install the above software using Powershell
{: .notice--info}
