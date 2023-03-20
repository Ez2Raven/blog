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
part: 4
tags: homelab
---

{% capture notice-1 %}
This is Part 4 of the "{{page.display_name}}" series.

In this article, I'll share how my home server has aged since 2015 and why it's time for a tech refresh
{% endcapture %}

<div class="notice--info">{{ notice-1 | markdownify }}</div>

# Home Server 2015

Back in 2015, I had encountered my first occurence of bit rot where family photos and videos stored in my hard drive were damaged beyond repair. My initial thoughts were to simply provision multiple backups to avoid similar occurences from happening, but what if bit rot happens for different files simultaneously on those backups? That was when ZFS became the crux of my home server. 

While the journey to adopt [ZFS](https://wiki.ubuntu.com/ZFS) was a [roller coaster ride](https://en.wikipedia.org/wiki/Shingled_magnetic_recording#:~:text=Western%20Digital%2C%20Toshiba%2C%20and%20Seagate,these%20may%20cause%20data%20loss.) for a techie's first home server. I was really happy with ZFS and [the hardware selected then](https://pcpartpicker.com/user/demandous/saved/#view=h2fyFT).

# Fast Forward 8 Years Later

Time flies really quickly and so does my 4TB ZFS 2-disk mirror storage space.

