---
title: "Vision Transformer(ViT) from Scratch - Solving Partial Differential Equations(PDE)"
excerpt: "Mathematical Data Driven Methods for Modelling and Simulations of Science and Engineering Problems, mostly modeled as partial differential equation therefore how to solve them for performing simulation of the system. I have trained ViT model onto the Allen Cahn PDE to dataset and checked the model predicted solution for the unseen input dataset. results are close to exact solution.<br/><a href='https://github.com/ajeetkbhardwaj/Modelling-Complex-Systems/tree/main/ViTforPDE'><img src='/images/portfolio/ViTforPDE-AllenCahn.png'></a>"
collection: portfolio
url: https://github.com/ajeetkbhardwaj/Modelling-Complex-Systems/tree/main/ViTforPDE
category: "Mathematical Data Driven Methods"
---

**Abstract**

Partial Differential Equations (PDEs) are central to modeling physical, biological, and engineering systems, yet their analytical solutions are often intractable. Traditionally, numerical schemes such as the **Finite Difference Method (FDM)**, **Finite Element Method (FEM)**, and **Spectral Methods** have been employed to approximate PDE solutions with high accuracy. However, these classical approaches can become computationally expensive for **high-dimensional**, **nonlinear**, or **time-dependent** problems.

Recent advances in deep learning provide new perspectives on representing and solving PDEs. In particular, **Vision Transformers (ViTs)** have demonstrated remarkable capability in capturing spatial and contextual relationships in grid-structured data such as images. Motivated by this, the present study explores the application of ViTs to PDE solution approximation. The key idea is to **reformulate PDE meshes or discretized fields as "image-like tokens"**, allowing the transformer to learn spatial correlations and dynamics directly from data.

Through a series of experiments, ViTs are **benchmarked against standard numerical solvers** to evaluate their accuracy, generalization capability, and scalability to complex spatio-temporal dynamics. The results highlight the potential of transformer-based models to serve as **powerful alternatives or accelerators** for conventional PDE solvers.


## Introduction

Partial Differential Equations (PDEs) arise naturally in the mathematical formulation of many physical processes — including **fluid dynamics**, **heat transfer**, **electromagnetism**, and **quantum mechanics**. Analytical solutions of most PDEs are difficult or impossible to obtain, necessitating **numerical approximation methods**. Over the past decades, techniques such as **Finite Difference (FDM)**, **Finite Element (FEM)**, and **Spectral Methods** have become the backbone of computational modeling. Despite their effectiveness, these methods often face challenges in **computational cost**, **scalability**, and **generalization** to new boundary conditions or geometries.

With the rapid growth of **deep learning**, researchers have begun exploring **data-driven PDE solvers**. Approaches like **Physics-Informed Neural Networks (PINNs)**, **Deep Operator Networks (DeepONets)**, and **Fourier Neural Operators (FNOs)** have shown that neural networks can learn solution operators directly from data or governing equations.

Among modern architectures, **Vision Transformers (ViTs)** stand out for their exceptional ability to model **long-range spatial dependencies** and capture **contextual relationships** in structured grid data. Inspired by their success in computer vision, this work investigates applying ViTs to PDE problems by **reformulating discretized PDE grids as image-like token sequences**. Each token represents a local spatial patch, allowing the transformer to model nonlocal interactions and latent dynamics through **self-attention mechanisms**.

This study compares ViT-based PDE solvers with traditional numerical methods across several benchmark problems, analyzing their **accuracy**, **generalization**, and **computational efficiency**. The ultimate goal is to bridge **numerical analysis** and **machine learning**, offering a new paradigm for how PDEs can be **modeled, approximated, and scaled** in the era of AI-driven scientific computing.


