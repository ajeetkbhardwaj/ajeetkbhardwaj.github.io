---
title: 'System Design from First Principle Part-I : The Natural Science of Softwares'
date: 2026-04-10
permalink: /posts/2026/04/10/system-design-from-first-principle-part-1/
tags:
  - System
  - Design
  - Building
toc: true
math: true
mermaid: true
---
> A first-principles view of system design: **latency, bandwidth, distance, and cost**.

## Table of contents

- [What is System Design?](#what-is-system-design)
- [Why Lego-block design fails](#why-lego-block-design-fails)
- [Cache bottleneck example](#cache-bottleneck-example)
- [How senior engineers think](#how-senior-engineers-think)
- [Human-time model](#human-time-model)
- [First principles](#first-principles)
- [FAQ](#faq)
- [Key takeaways](#key-takeaways)


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

### FP-4 : The Math of Flow(Little's Law)

In Queueing Theory, Little's Law can be realized math of flow of every systems

$$
L = \lambda W
$$

where $L$ is the avg number of requests(n‑flight, queued, or being processed) in systems, **λ is** **Arrival rate** (requests per second) and **W is Average service time / latency** per request (seconds).

Example : Given our servers, we hosted a application system

Now, If $\lambda$ fixed and $W$ increases then $L$ must also increase. Our system has **physical limits** on how many in‑flight requests it can hold (RAM, sockets, threads, etc.). Once LL**L** hits that limit, the system

* starts queuing requests,
* effective latency grows even more,
* you enter a **positive‑feedback “death spiral”** where more in‑flight requests imply even higher memory and scheduling pressure, eventually causing overload and failure.

Practical Measures we can take ? You  **cannot escape Little’s Law** ; you can only change its variables. So,

* Reduce **W** (latency) via better algorithms, caching, or fewer hops.
* Reduce *λ* (load) via throttling, batching, or scaling out.
* Or increase capacity (RAM, CPU, nodes) so that the system can hold a higher  **L** safely.
  Systems that “just add more nodes” without understanding  **L**=**λW** often collapse under their own queueing dynamics.

### FP-5 : Economics of Physics

**“renting compute is renting physics”** — cloud costs are directly tied to physical resources.

1. Storage‑tier economics - a rough cost hierarchy

   - **RAM is ~100× more expensive than SSD**
   - **SSD is ~10× more expensive than S3 / cold storage.**
     SO, It mirrors the latency and speed hierarchy - faster media is more expensive per bit.
2. Engineering failure - Storing 3‑year‑old receipts in Redis (fast, expensive, low‑latency) is like renting a Manhattan penthouse to store cardboard boxes.

The business value of old receipts is low, but the physical cost per bit is high. First‑principles design means aligning the value of data with the cost of the medium: Hot data (recent, frequently accessed) → RAM / fast cache / SSD. Cold data (rarely accessed) → cheap, slow cold storage.

At FAANG scale, even a 1% efficiency gain in RAM usage can save $10 million per year because you’re moving billions of dollars’ worth of physical resources.

This is why Staff‑level engineers spend time on things like: data compression, cache eviction policies, partitioning that minimizes cross‑region data transfer, all justified by physics‑plus‑economics rather than aesthetic diagrams

## FAQ for Every System Design Problem  and Decision

**Latency: How far does the data have to travel?**

* What is the **physical path** the data must take (CPU cache, RAM, disk, network, cross‑region)?
* Can you bring the data closer (co‑location, caching, edge)?

**Throughput: How wide is the pipe?**

* What is your **bandwidth** at each stage (CPU, network, disk, database)?
* Are you bottlenecked by capacity (bandwidth) or per‑bit latency?
* **State: Is the work sequential or random?**
* * Are you doing **sequential I/O** (good for disks, SSDs) or **random I/O** (bad)?
  * Can you restructure writes to be more sequential (e.g., LSM‑style logging)?**youtube**+1



* **Math: What does Little’s Law say about my capacity?**
  * For given λ\lambda**λ** (arrival rate) and WW**W** (latency), what is LL**L** (in‑flight load)?
  * Does that LL**L** exceed the physical resource limits (RAM, CPU, sockets)?**youtube**+1

**Cost: Is the physical medium worth the business value?**

* Are you using **expensive, low‑latency storage** (RAM, Redis) for low‑value or cold data?
* Can you tier storage so that  **data value matches physical cost** ?

Hence , first principle driven **system design is about turning physics into algebra and money** —not just picking acronyms and drawing arrows. By grounding every decision in the **latency hierarchy, I/O mechanics, Little’s Law, and storage economics**.
