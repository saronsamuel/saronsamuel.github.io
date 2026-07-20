---
layout: page
title: "MMMORRF: Fusing Every Modality a Video Has to Offer"
description: A multimodal, multilingual video retrieval system that stops over-indexing on visual content and actually listens to a video, too.
img:
importance: 3
category: research
related_publications: true
---

A video is never just its pixels. It's the on-screen text, the narration, the background audio, the dialogue — often in a different language than whatever caption or query you'd write to search for it. Most of the leading video retrieval systems at the time we started this project, like VAST and LanguageBind, were built on top of vision-language models, which meant they inherited a strong bias toward the visual channel and mostly ignored everything else a video was saying.

**MMMORRF** (Multimodal Multilingual Modularized Reciprocal Rank Fusion) {% cite samuel2025mmmorrf %} was our answer to that: extract signal from *every* modality — visual features, on-screen text via OCR, and speech via ASR, across languages — and combine the resulting rankings with a modularized, modality-aware weighted reciprocal rank fusion, rather than trying to force everything into one shared embedding space.

The "modularized" part matters as much as the "multimodal" part. Instead of one monolithic model that has to jointly represent every modality (and that inevitably ends up dominated by whichever modality it was pretrained on), each modality gets its own retrieval pipeline, and fusion happens at the ranking level, where we can weight modalities according to how much signal they actually carry for a given query.

Tested on the MultiVENT 2.0 and TVR benchmarks, MMMORRF improved nDCG@20 by 81% over leading multimodal encoders and by 37% over the best single-modality retrieval approach. The gains were largest on exactly the queries that trip up vision-only systems: ones where the answer is spoken or written on screen rather than depicted.

This was a large team effort with Dan DeGenaro, Jimena Guallar-Blasco, Kate Sanders, Oluwaseun Eisape, Tanner Spendlove, Arun Reddy, Alexander Martin, Andrew Yates, Eugene Yang, Cameron Carpenter, David Etter, Efsun Kayi, Matthew Wiesner, Kenton Murray, and Reno Kriz, presented as a demo at SIGIR 2025. [Paper (ACM DL)](https://dl.acm.org/doi/10.1145/3726302.3730157) · [arXiv version](https://arxiv.org/abs/2503.20698).
