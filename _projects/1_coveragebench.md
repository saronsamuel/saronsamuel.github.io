---
layout: page
title: CoverageBench
description: A benchmark suite for measuring whether search results actually cover what a query is asking about, not just whether each document is relevant.
img:
importance: 1
category: research
related_publications: true
---

Standard retrieval metrics like precision and recall are computed one document at a time: a human judges whether *this* document is relevant to *that* query, in isolation. That works fine when a query has one obvious answer. It breaks down for the queries that matter most in practice — "what are the arguments for and against this policy," "summarize what happened in this event," "what perspectives exist on this topic" — where a genuinely good result set has to cover the *range* of relevant information, not just contain individually-relevant documents. A search engine can score perfectly on precision and recall while still missing half the story.

**CoverageBench** {% cite samuel2026coverage %} is a benchmark suite built to measure that directly. Instead of per-document relevance judgments, it uses *nuggets* — discrete units of information that a complete answer should contain — and asks how much of that nugget space a system's retrieved set actually covers.

Building the benchmark meant assembling coverage-style judgments across genres that don't normally share an evaluation framework: conversational search (TREC CAsT 2020), fairness-focused ranking (TREC Fair Ranking 2022), cross-language retrieval (NeuCLIR 2024), retrieval-augmented generation (a MS MARCO-based RAG 2024 set and RAGTIME 2025), and multi-document summarization (the CRUX collections built on MultiNews and DUC04). Altogether the suite spans 334 topics across 7 collections, ranging from ~565K to 113M documents, with nugget-level relevance judgments and baseline runs from BM25 and Qwen3-8B-based rerankers so it's usable out of the box.

The point isn't to replace precision/recall — it's to expose a failure mode they can't see. A system tuned purely for per-document relevance can look excellent on traditional metrics while systematically under-covering a query's information need, which matters enormously for anything downstream that assumes retrieval is "complete," like RAG pipelines that only get one shot at the context window.

CoverageBench was accepted to SIGIR 2026. The datasets are on [Hugging Face](https://huggingface.co/datasets/hltcoe/coveragebench), and this was joint work with Andrew Yates, Dawn Lawrie, Ian Soboroff, Trevor Adriaanse, Benjamin Van Durme, and Eugene Yang at the Johns Hopkins HLTCOE.
