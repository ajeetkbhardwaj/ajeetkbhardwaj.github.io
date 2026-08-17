---
title: 'A Case Study of MacBook Air M4(16/256GB) for AI Model Production by Applied Mathematician'
date: 2026-01-29
permalink: /posts/2026/01/MacBookAirM4-for-AI-Model-by-Applied-Mathematician/
categories:
  - AI Hardwares
  - Artificial Intelligence
  - Applied Mathematics
  - Computing
---

I was using Asus Notebook(i3/8GB/1TB-HHD) since 2021. After completion of M.Sc Mathematics and Computing degree at BHU Varanasi, went to the IIT Delhi(Cloud Computing and HIPC Lab SIT), New Delhi for the AI Research Internship. I am greatfull enough that i have worked onto the the two most interesting research problem 
1. LLM for OpenAPI Specification Generation from the given server source code.
2. Lean4 Proof generation for the given theorem in lean4

The first problem was already approximately solved but i have contributed to its Ideal OpenAPI Spec creation and Running our build tools to generate the tool OpenAPI Spec then perform the possible analysis and mistakes such that to overcome the limitation of the our tool like prompt modification, complete-code not send etc. Then I started moving towards the 2nd problem that i have throught to use the multi-agentic workflow to actually solve this problem but due to the llms hallucination for lean4 syntax generation and proof complex reasoning. They actually failed for the theorem with complex proofs. 

During this time i have the resouces in the lab like desktop with CPU/GPU and even the servers. So, at that time i did't feel that i needed to buy a new laptop. But after completion of the conclusion of the my internship. I have realised to buy a new laptop with more AI capability. Then i have brought the my first MacBook laptop on the independence day sale at amazon.

My macbook is the one of the most efficient AI laptops on current market but we are hitting the memory wall before we hit the compute wall of our macbook for the AI usecase due to config (16GB/RAM and 256GB/SSD).

## Hardware Constraints
Our macbook have a unified 16GB RAM with CPU/GPU onto the Apple Sillicon Chip. However, MacOS reserves 4-6GB RAM for the system overhead. So, available RAM memory for our AI use will be 10-12GB. M4-chip can do 38TOPS(trillion operations per second) but the memory bandwidth limits its speed to the 120GB/sec i.e data can't reach to the cores fater than 120GB/sec. It's fanless design can also reduce the M4-chip clock speed due to its thermal trotlling by 20-30% after 10-15min of heavy matrix multiplication.

## Large Scale Models
Our focus will be transformer based architecture and specifically the large language model because they are't only the black-box of text but its a massive/complex high dimensional dynamical system. An Engineers task is to take the theoretical architecture of the model the production ready system that can serve the users. So, we needed to perform a series of computational assessment for the this.

### Step-1 : Structural & Geometric Analysis
Before writting any code, we needed to ensure that our model must fit into the physical constraints of the hardware. For this we needed to answer the following two questions
1. Compute the total trainable parameters of the model
2. Determine the minimum VRAM required to load the model

### Step-2 : Computational Complexity(FLOPs Analysis)
we needed to quantify the work required to be done in single pass of model.[^1]


### Step-3 : KV Cache & State Space


### Step-4 : Model Finetuning/Compression/Distillation and Error Analysis


### Step-5 : Distributed Systems (Parallelism)

### Step-6 : Production Metrics (SLOs)

### Summary Table for Production Readiness [^1]

| Step | Mathematical Goal | Production Aim |
| --- | --- | --- |
| **1. Param Count** | Dimensionality analysis | Hardware selection |
| **2. VRAM Calc** | Capacity planning | Cost estimation |
| **3. FLOPs Analysis** | Theoretical max speed | Throughput target |
| **4. KV Cache** | State-space modeling | Context window limits |
| **5. Quantization** | Minimizing Signal-to-Noise ratio | Memory footprint reduction |
| **6. Parallelism** | Graph partitioning | Multi-GPU scaling |


## MacBook Air M4(16/256)
Running an LLM onto resource bound hardware is a problem of maximizing a specific objective function i.e Tokens per Second(TPS) subject to the hardware constraints. For our macbook the primary constraint is the memory bandwidth(120GB/sec). So, lets select the llamma-3-8B model and perform all production readiness computational assessment for the model onto our hardware.

### 1. Model Total Params

### 2. VRAM Calculation

### 3. KV Cache Capacity Calculation

### 4. Throughput ($TPS$) Performance Modeling

### 5. Arithmetic Intensity & TTFT


## Reference

[^0]: [Ch-9 : AI Engineering - Building Applications with Foundation Models]()

[^1]: [LLM Inference Lecture: Roofline Analysis for GPU (arithmetic intensity, compute and memory bound)](https://youtu.be/7EJjdDLK4cg?si=E4whZyrMJhRIy1b8)

[^2]: 