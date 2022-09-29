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
tags: homelab
---

{% capture notice-1 %}
This is Part 2 of the "{{page.display_name}}" series. 

In this article, we will explore the ease of installing the software needed
on our development machine.
{% endcapture %}

<div class="notice--info">{{ notice-1 | markdownify }}</div>

<!--more-->

# List Of Software and Tools

| Purpose                       | Tool                | Website                                                       | Install via Chocolatey? |
|-------------------------------|---------------------|---------------------------------------------------------------|:-----------------------:|
| Windows Package Management    | Chocolatey          | https://chocolatey.org/                                       |           NA            |
| Mind Mapping                  | XMind               | https://xmind.app/                                            |            y            |
| Source Control                | Git                 | https://git-scm.com/                                          |            y            |
|                               | Github CLI          | https://cli.github.com/                                       |            y            |
| Browser for Development       | Firefox             | https://www.mozilla.org/en-US/firefox/new/                    |            y            |
| File Archiver                 | 7-Zip               | https://www.7-zip.org/                                        |            y            |
| C# IDE                        | Rider               | https://www.jetbrains.com/rider/                              |            y            |
| Code Editor                   | vscode              | https://code.visualstudio.com/                                |            y            |
| Containerization              | Docker Desktop WSL2 | https://docs.docker.com/desktop/windows/wsl/                  |  prefer manual install  |
| Cross Platform Scripting      | Powershell          | https://github.com/PowerShell/PowerShell                      |  prefer manual install  |
| Azure CLI                     | Azure CLI           | https://learn.microsoft.com/en-us/cli/azure/install-azure-cli |  prefer manual install  |
| Kubernetes Package Management | Helm                | https://helm.sh/                                              |            y            |
| Fancy Terminal                | Windows Terminal    | https://github.com/microsoft/terminal                         |  prefer manual install  |

## Chocolatey For Organization Usage (Not Legal Advice)
{% capture notice-2 %}
Having dedicated DevOps personnel does not mean an organization understands who the repositories maintainers are,
and by extension, the intent and changes made by public maintainers.

It is in an organization's best interest to assume ownership of its own private repositories so 
that DevOps personnel can inspect the code in the packages and validate them to ensure
packages adhere to the organization standards.
{% endcapture %}

<div class="notice--warning">{{ notice-2 | markdownify }}</div>

# Installing Software Manually

The only reason why I decide to install CLIs, terminals and docker manually is simply because these are tools that can have
devastating security impacts if they become a target of [software supply chain poisoning](https://cloud.google.com/software-supply-chain-security/docs/attack-vectors).

You can verify the binary checksum from Chocolatey against the official release to address security needs shared [earlier](#my-opinion-on-chocolatey-for-organization-usage-not-legal-advice).

Installing these tools manually is a faster and easier approach for **a single individual**. 
Organizations should invest in setting up their own private repositories so that installations can be deployed at scale.
{: .notice--info}

## Sensitive Software and Tools

Navigate to the official website to download and install the official packages.
Official packages hosted on Github can be downloaded from the "Releases" section
<figure>
    <img src="{{ '/assets/images/dl-pshell.png' | relative_url }}">
    <figcaption>Locating the Releases section on Github</figcaption>
</figure>

1. [Powershell](https://github.com/PowerShell/PowerShell)
2. [Terminal](https://github.com/microsoft/terminal)
3. [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
4. [Windows Subsytem for Linux - WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) 
5. [Docker Desktop For Windows (WSL2 Backend)](https://docs.docker.com/desktop/windows/wsl/)

You shouldn't have much challenges installing the above manually.
Feel free to message me on Twitter and I'll try to help when available.
{: .notice--info}

## Chocolatey

Head over to [https://chocolatey.org/install](https://chocolatey.org/install) and read the requirements before installing Chocolatey.
In my case, I'll proceed with installing Chocolatey for individual use **AFTER** reviewing the powershell script provided.
i.e. [https://community.chocolatey.org/install.ps1](https://community.chocolatey.org/install.ps1)

If you are using a corporate issued computer or using a corporate network for internet access, 
you should check out the Step-by-Step Installation Course to address your specific needs.
{: .notice--info}
<figure>
    <img src="{{ '/assets/images/chocolatey-sbs.png' | relative_url }}">
    <figcaption>Step-by-Step can be located at bottom</figcaption>
</figure>

<figure>
    <img src="{{ '/assets/images/chocolatey-sbs2.png' | relative_url }}">
    <figcaption>Common scenarios for corporate devices and networks</figcaption>
</figure>

# Installing the rest using Chocolatey :chocolate_bar:

 Now that we have installed sensitive applications manually (or via a trusted chocolatey repository),
 we can now proceed to install the rest using Chocolatey.
 
```powershell
choco install firefox xmind-2020 git gh 7zip jetbrains-rider vscode kubernetes-helm -dy
```
```
-d, --debug 
    Debug - Show debug messaging.
    
-y, --yes, --confirm 
    Confirm all prompts - Chooses affirmative answer instead of prompting.
    Implies --accept-license
```

Eventually, you should see an output similar to the following:
```
Installed:
 - vscode.install v1.71.2
 - git v2.37.3
 - firefox v105.0.1
 - chocolatey-core.extension v1.4.0
 - xmind-2020 v12.0.3
 - chocolatey-compatibility.extension v1.0.0
 - vscode v1.71.2
 - jetbrains-rider v2022.2.3
 - gh v2.15.0
 - kubernetes-helm v3.9.4
 - dotnet4.5.2 v4.5.2.20140902
 - git.install v2.37.3
 - 7ip v22.1
```

and that's it! Depending on the specs of your development machine, this should take only minutes to 
complete the installation. (it only takes 30 secs on my Asus X16 Flow laptop)

Go ahead, apply any commercial licenses you have for the above.

I hope this saves you some time when provisioning a new development machine 
for you and your friends!