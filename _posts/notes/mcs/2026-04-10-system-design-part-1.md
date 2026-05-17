---
title: 'System Design from First Principle - The Natural Science of Softwares'
date: 2026-04-10
permalink: /posts/2026/04/10/system-design-from-first-principle-part-1/
tags:
  - System
  - Design
  - Building
---
What is System Design ?

System Design is not boxes and arrows instead latency, bandwidths and cost. That defines why high-level system architecture must be grounded in physical and mathematical realities rather than just best practices or trends in the industries.

What are the problem with Lego Block system design ?

Many engineers treat architecture as a UI puzzle like “add a load balancer here, a Redis cache there” without understanding how the underlying hardware (CPU, memory, network, disks) actually behaves. The “lego‑block” trap is that you optimize for tools and buzzwords instead of for **latency, throughput, and physical constraints** like the speed of light in fiber or the cost of RAM‑gigabytes.

Cache Bottleneck Problem

A system is design for the high-throughput service that actually failed because for each user request, the code issued 100 small network calls to a fast distributed cache and cache was fast in isolation but the **round‑trip network latency** per request multiplied by 100 dominated the overall latency, turning the cache into the bottleneck.

How to think from the mind of Senior/Staff Engineer ?

Senior/Staff Engineer at the companies like Google/Netflix etc, they think less in terms of “which tool to pick” and more in terms of **nanoseconds, packets, and gigabytes of RAM**. Therefore, they always ask: “What physical path does this bit have to travel ?”

Mental Model for Thinking - Scaling CPU Cycles to Human Time

CPU - a brain that process one thought per cycle-second for machine we assume 0.3 ns/cycle -> 1 sec/cycle of human time to make latency more understandable.

* **Register  :** 0.3 ns/cycle -> 1 sec/cycle

- **L1 cache**: ~4 seconds of human time → like reaching for a notebook on your desk.
- **Main memory (RAM)**: ~100 seconds → like walking to a bookshelf at the back of a large room.
- **SSD read**: **2–6 days** → your brain waits *days* for one piece of data. 
- **Network round trip (California → Netherlands)**: ~**15 years** of human time

What does we mean cache bottleneck problem based onto the mental model ?

A code like `for i in range(0, 100): await cache.get(keys[i])` is effectively **asking your CPU to wait ~100 × ~15 years** of its scaled life. In physical terms, that corresponds to **hundreds‑of‑milliseconds to seconds of latency**, which can easily kill throughput or make your system seem unresponsive, even though the cache itself is “fast” in isolation.

There are certain principle for the system design we needed to first get a feel of them

### First Principles

### FP-1 : Data Has Distance

**“Data has distance”** — our primary job as a system designer is to **minimize the distance data has to travel."**

What do we mean by distance here ?

Distance is not just geographical kilometers; it is **Levels of the memory hierarchy like** register → L1 → L2 → RAM → SSD → disk(HDD) → network. There are many **Network hops** like intra‑host vs intra‑rack vs inter‑region vs cross‑continent.

A **local variable** lives in a register or cache; a **database record** may live on a remote disk and require multiple network hops. These are orders‑of‑magnitude apart in latency and cost. We cannot treat a remote object like a local object; an abstraction that hides that distance will **leak** and manifest as high latency when the real hardware path is traversed.

Hence, design decisions such as **caching, batching, locality‑aware placement, and data sharding** all boil down to reducing “data distance.”

### FP-2 : Mechanical Sympathy (I/O)

Mechanical Sympathy (I/O) comes from understanding of how physical machine actually works bits through storage and network media.

What is the trade-off between sequetial vs random I/O ?

For both **HDDs and SSDs**, **sequential I/O** is dramatically faster than random‑access I/O because:- 

- On HDDs, heads move and rotate; jumping to random locations incurs seek time.

- On SSDs, pages and blocks must be erased and written in bulk; random small writes trigger more housekeeping overhead.

A long sequential read/write can achieve **near‑line‑rate** speeds, while random access is orders‑of‑magnitude slower.

##### LSM-trees and Databases

- This is why databases like **Cassandra or RocksDB use LSM‑trees**:
  - Incoming writes are appended to a **log‑structured file** (sequential).
  - Compaction later merges these into sorted files, again in a mostly sequential way.
- LSM‑trees turn what would be **random writes** into **sequential writes**, exactly because of the physical behavior of storage media.

In first‑principles terms, good storage design is not about “which serialization” or “which ORM,” but about **aligning your data layout with the mechanics of the underlying hardware**.

### FP-3 : The Pipe Problem (Latency vs Bandwidth)

The “pipe” analogy contrasts **latency** and **bandwidth**:

- **Latency**: How long it takes for **one drop of water** to travel the pipe.
  - On the internet, this is governed by **the speed of light in fiber and propagation delay**, which is essentially a physical constant.
  - You **cannot buy less latency**; you can only reduce hops or move data geographically closer. 
- **Bandwidth**: The **diameter of the pipe**, i.e., how much data you can push per second.
  - You *can* “buy a bigger pipe” via higher‑speed links, more parallel paths, or more servers.

Example  : Assume that a **Boeing 747 full of hard drives** flying from New York to London

- Latency is terrible: ~8 hours of flight time.
- But bandwidth is enormous: **petabytes of data** moved in one go.

For **bulk transfers**, this “sneakernet” can be faster than any internet connection, because the **total bits moved divided by time** (bandwidth) is huge, even though the **per‑bit latency** is enormous.

Design Decision - Latency-Bound vs Bandwidth-Bound 

- **Latency‑bound workloads** (e.g., HFT, real‑time control, low‑latency APIs):
  - You optimize for **reducing per‑request latency**—co‑location, caching, avoiding network hops, micro‑optimizations.
- **Bandwidth‑bound workloads** (e.g., YouTube, Netflix, large‑scale backups):
  - You optimize for **maximizing bits per second**—parallelization, CDNs, fat pipes, and even offline transport like the 747 case.

If you mix these up (e.g., over‑optimize latency when you’re really bandwidth‑bound), you waste effort and money.
