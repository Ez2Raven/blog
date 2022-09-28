---
title: Configure Development Machine
classes: wide
header:
    image: /assets/images/homelab.jpg
    teaser: /assets/images/homelab-th.jpg
sidebar:
    title: "In This Series"
    nav: homelab
gallery:
- url: /assets/images/homelab.jpg
  image_path: assets/images/homelab-th.jpg
  alt: "Part 1: Setup Development Machine"
---

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
Trust - As an organization you don't know who the maintainers of a package are, and therefore you can't trust them based on Chocolatey's
say so (or perhaps you can, that's an organizational decision).
You would normally vet the code in the packages and independently test them to ensure they meet your organizations standards.
{% endcapture %}

<div class="notice--danger">{{ notice-2 | markdownify }}</div>

