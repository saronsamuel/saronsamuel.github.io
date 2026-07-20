---
layout: page
title: Does Reasoning Make Search More Fair?
description: The first systematic comparison of fairness between reasoning and non-reasoning rerankers, using TREC's Fair Ranking Track data.
img:
importance: 2
category: research
related_publications: true
---

Reasoning models — the kind that generate intermediate "thinking" tokens before answering — have started showing up as rerankers in search pipelines, usually pitched as a strict upgrade: better relevance judgments, better ranking quality. What nobody had checked is whether that extra reasoning step changes how *fair* the resulting rankings are — for example, whether documents about different countries or demographic groups get systematically over- or under-ranked.

This project {% cite samuel2026reasoning %} ran that comparison for the first time. Using the TREC 2022 Fair Ranking Track data, we evaluated six reranking models — a mix of reasoning and non-reasoning architectures — and measured fairness with Attention-Weighted Rank Fairness (AWRF), alongside standard relevance metrics.

The result was not what a "reasoning helps everything" narrative would predict. AWRF stayed in a tight 0.33-0.35 band across every model we tested, despite the models producing very different relevance quality. Reasoning rerankers didn't come out ahead on fairness, but they didn't come out behind either — they largely preserved whatever fairness characteristics were already present in the input ranking. And geographic attributes in particular showed consistent disparities no matter which architecture we used, reasoning or not.

The takeaway is a useful corrective: fairness isn't a side effect of general capability improvements like reasoning. If you want a fairer reranker, you have to train and evaluate for that specifically — better reasoning about relevance doesn't automatically translate into better reasoning about equitable exposure across groups.

This paper was accepted to ECIR 2026, joint work with Benjamin Van Durme and Eugene Yang at the Johns Hopkins HLTCOE. [Read the paper on arXiv](https://arxiv.org/abs/2603.10332).
