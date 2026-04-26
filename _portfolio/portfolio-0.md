---
title: "Lean4Agent: Multi-Agent AI System for Verifiable Writing and Proving Theorems in Formal Mathemtics"
excerpt: "Lean4Agent is a collaborative AI system designed to tackle complex mathematical problems using multiple intelligent agents.<br/><img src='/images/portfolio/Lean4AgentArchs.png' alt='Lean4Agent Architecture'/>"
collection: portfolio
url: "https://github.com/ajeetkbhardwaj/Lean4Agent/tree/main"
category: "AI Systems"
---


**Abstract**
> *Lean4Agent is an innovative multi-agent AI system designed to automate the process of solving mathematical problems by translating natural language descriptions into formal proofs using the Lean4 theorem prover. By orchestrating specialized agents for task instigation, planning, code generation, verification, and feedback, Lean4Agent enables seamless collaboration between humans and machines in mathematical reasoning. This approach not only accelerates the formalization and verification of complex mathematical tasks but also ensures correctness and reliability, unlocking new possibilities for large-scale collaborative mathematics.*

**Introduction**
Mathematics is fundamental to human understanding, enabling us to describe, predict, and shape the natural world. As the root of intelligence, mathematics demands reasoning, abstraction, and the ability to see underlying beauty and structure. Traditionally, formalizing mathematics—from natural language to symbolic proofs—has been a labor-intensive process, often limited by human capacity for verification and collaboration.

With the advent of computer-assisted proof systems like Lean4, it is now possible to formalize mathematical knowledge in code, ensuring perfect verification and eliminating concerns about correctness. However, bridging the gap between informal problem statements and formal proofs remains a significant challenge.

Lean4Agent is a try to addresses this challenge by introducing a multi-agent workflow that automates the journey from natural language problem statements to verified Lean4 proofs. By leveraging specialized agents for planning, code generation, verification, and feedback, Lean4Agent streamlines the formalization process, enabling scalable and trustworthy mathematical collaboration.

**Architecture Description**
![txt](/images/portfolio/Lean4AgentArchs.png)
Lean4Agent’s architecture is composed of three core agents, each responsible for a distinct stage in the mathematical problem-solving pipeline:
1. Task Instigation
Reads the input problem in natural language and prepares a structured prompt for the planning agent.
2. Planning Agent
Generates a step-by-step plan for solving and proving the task, using the problem description and predefined templates.
3. Generation Agent
Produces Lean4 code, including theorem statements and proofs, by filling in the required sections of the Lean template based on the plan and task description.
4. Verification
Compiles and checks the generated Lean4 code. If the Lean4 compiler reports errors or proof failures, the agent captures the error messages.
5. Feedback Agent
Analyzes errors and suggests corrections, iteratively refining the solution until it passes verification or a retry limit is reached.

This modular, agent-based workflow try to ensures that each stage of the formalization process is handled efficiently and accurately, enabling Lean4Agent to tackle complex mathematical problems with minimal human intervention and maximal reliability. But tt has many limitations due to llms itself.