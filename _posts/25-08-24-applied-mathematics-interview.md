---
title: 'Model Context Protocol(MCP) - '
date: 2025-08-09
permalink: /posts/2025/08/09/khiladi-1/
tags:
  - Game
  - Job
  - Nature
---
**Abstract**
We are going to study
1. Model Context Protocol - Theory, Design and Practices
2. How to use the MCP SDKs and Frameworks to build AI Systems?
3. How to create own custom MCP server and client ?
How MCP works ?
Concepts, Architecture and Components of MCP 
What are the use cases of MCP ?

How to build MCP based applications and deploy it using huggingface services ?

How to build AI Systems that uses external data and tools using MCP standards ?

Must have 
Understanding of LLM and AI concepts
Software developement principles
Application Programming Interface 

How to build LLM Apps with post-training and agentic approaches ?

**Introduction**

What is Model Context Protocol(MCP) ?
MCP descibed as a standard like USB-C/HTTP AI applications by people because USB-C is a standardized physical and logical interface for connecting various peripherals to computing devices similarly MCP is a consistent protocol for linking AI models to external capabilities.

What role MCP plays in AI ecosystems ?

MCP benifits the entire AI ecosystems
1. Users - Enjoy consistent experiance across AI apps
2. Developers - Easy integration with growing ecosystems of tools and data sources.
3. Tools and Data Providers - They needed to only create MCP server that can works with multiple AI applications and Developers only needed to write the MCP client to access the tools and data sources from MCP server.

What is the importance of MCP for building AI apps ?

AI systems are becoming more capable with LLMs but models have limitations like lack of access to the real time information or specialized tools(calculator) due to training data. It hinders the AI systems to provide relevent, accurate and helpfull information.

MCP try to enable LLM models to connect with external data sources, tools and environments, allows smooth transfer of information and capabilities between AI systems and digital world. Thus, It makes AI systems more capable for its growth and adaptation in different AI applications.

What are the challenges related to LLM that are solved by MCP particularly the M×N Integration Problem ?

MxN Integration Problem - Challenges associated with connecting M different AI apps with the N different external data source, tools and environments without standardized approach.

Solution without MCP - Developers needed to create MxN custom integrations - one for each possible pairing of an AI application with an external capability. Each AI application would need to integrate with each tool/data source individually. It very complex, expensive process and costlier to maintain. Lets we have multiple models and multiple tools then number of integration will become large to manage, each with it's own unique interface.

Solution with MCP - It transforms the MxN integration problem into an M + N integration problem by providing a standard interface as MCP server - each AI application implements a MCP client to intract via RE-JSON format with MCP server to use its data source, tools and environment.

What are the key components in MCP ?
MCP has a client-server type relationship similar to the HTTP has.
1. Host - 
2. Client - 
3. Server - 

What are the key benifits and goals of the MCP ?
Key benifits 
1. Standardization
2. Enhanced AI capabilities
3. Interoperability

How MCP works ?
Example

## References
0. [LLM Course by HuggingFace](https://huggingface.co/learn/llm-course/)
1. [AI Agents Course by HuggingFace](https://huggingface.co/learn/agents-course/)