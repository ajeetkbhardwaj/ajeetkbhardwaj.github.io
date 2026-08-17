---
title: 'AI Model Optimization Part-1 by Applied Mathematician'
date: 2026-02-20
permalink: /posts/2026/01/AI-Model-Optimization-Part-1/
categories:
  - AI Hardwares
  - Artificial Intelligence
  - Applied Mathematics
  - Computing
---

AI Model Optimization is an interdisciplinary field that involves collaboration between researchers, system engineers, and hardware architects to make models better, cheaper, and faster with the goal of maximizing throughput and minimizing computational costs and latency.

## Table of Contents


## Large Scale AI Models

What is AI model ? 

What is slowing the AI model most ? 
There are two bottleneck problems every AI Engineer encounters due to hardware constraints
1. Compute Bound : How many mathematical operation can be performed/executed per second(FLOPs) ? Ex- Prefill phase of LLMs are compute intensive task, where we needed to perform high dim matrix multiplications.
2. Memory Bandwidth Bound : How fast data can move between memory and processor ? Ex- Decode phase of LLMs generate next token one after another autoregressively needed to load the model weights repeatedly.
Both of these bottlenecks affects the our goal of maximizing throughput and minimizing latency/computational cost for LLMs.

We needed to understand the hardware requirements for our llms vica versa ? like llms parameter counting and VRAM requirements to ensure that llms fits without physical constraints of hardware.

How to calculate the total trainable parameters(size) of the llms ?

How much minimum VRAM needed to load the our llms ?


What are the Possible AI Model Optimization Problems ?
1. How can we reduce the model size without altering its performance ?

2. How can we optimize transformer architecture for compute and memory ?

3. How can we utilize the distributed systems ?

4. How can we deploy models at scale ?

## 

## Reference
[^1]: [AI Infrastructure for AI Engineers](https://github.com/Quick-AI-tutorials/AI-Infra)
[^2]: [Lecture-1 : AI Optimization - Prefill vs Decode](https://www.youtube.com/watch?v=3SBUCJzogj4)
