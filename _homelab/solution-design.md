---
title: Development Sandbox Solution Design
header:
    image: assets/images/design1-unsplash.jpg
    caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
    teaser: assets/images/design1-unsplash-th.jpg
sidebar:
    title: "In This Series"
    nav: homelab
toc: true
classes: wide
part: 1
---

{% capture notice-1 %}
This is Part 1 of the "{{page.display_name}}" series.

In this article, we will articulate the requirements, constraints and 
preferences regarding the development sandbox.
{% endcapture %}

<div class="notice--info">{{ notice-1 | markdownify }}</div>

<!--more-->

# Executive Summary
The typical software engineering team will provision different environments to serve corresponding
stakeholders throughout the **S**oftware **D**evelopment **L**ife **C**ycle.

Most, if not all, are shared environments that will be negatively impacted as both engineering and 
business needs demand rapid changes to market.

By designing a low cost, self serving, isolated environment, changes can be validated with
higher confidence and velocity before it cascade into shared environments.

# Requirements
Let's discuss the high level requirements that will help align the implementation against our
needs.

## Immutability
Resources used in the development sandbox should strive to achieve immutability,
so that changes can be applied transparently without hidden side effects.

## Zero Trust Security Model
Balance and distribute the cost of security by shifting traditional security measures
and policy to earlier phases of the Software Development Life Cycle.

## Scalability
Physical and logical resources must be scalable to address load testing needs
despite its innate characteristic of a low cost, self serving sandbox environment.

## Maintainability
Operability and Cost of ownership are tightly coupled with market forces within 
the infrastructure domain. Any technology or vendor "lock-in" must be well-documented and
assigned appropriate ownership before it is introduced into the sandbox environment.

# Constraints
Since I am currently not working, I can only afford at most USD $50 per month for 
infrastructure.

Fortunately, development tools that I used are either perpetual license, open-source or
within the annual billing cycle.

# Preferences
I'm a .NET guy, naturally I am more accustomed to Microsoft's ecosystem of
tools, technologies and documentation. (That doesn't mean I'm biased against other technologies)

Therefore, most of the resources used in this series will be specific to .NET and 
Azure to achieve a working baseline. After which, I will focus on vendor agnostic implementation
such as Terraform, Grafana, Prometheus, etc.

# Build Order
Finally this is the sequence of activities I will focus on for this series.

1. Development Machine Configuration
2. Cloud Budget Configuration
3. System Architecture
4. DevSecOps Toolchain
5. Software Solutioning