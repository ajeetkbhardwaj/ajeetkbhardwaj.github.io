---
title: "Did OpenAI solve the Navier–Stokes Millennium Problem completely ?"
excerpt: "Headlines over the last few days have claimed that *“OpenAI solves the Navier–Stokes Millennium Problem.”* As mathematicians, our first reaction should be extreme skepticism. The media have badly misread the result. The OpenAI manuscript proves a **forced** finite-time blowup for 3D incompressible Navier–Stokes, not the **unforced** regularity/blowup question that most people associate with the Clay Millennium Prize..<br/><img src='https://media.nature.com/lw767/magazine-assets/d41586-026-02842-5/d41586-026-02842-5_53685260.jpg?as=webp' alt='A swirling vortex — involved in the solution to the Navier–Stokes existence and smoothness problem. Credit OpenAI'/>"
collection: portfolio
date: 2026-04-30
url: "https://ajeetkbhardwaj.github.io/"
category: " "
---
Headlines over the last few days have claimed that *“OpenAI solves the Navier–Stokes Millennium Problem.”* As mathematicians, our first reaction should be extreme skepticism. The media have badly misread the result.[^6] The OpenAI manuscript proves a **forced** finite-time blowup for 3D incompressible Navier–Stokes, not the **unforced** regularity/blowup question that most people associate with the Clay Millennium Prize.[^1]

Below is a corrected, source-faithful account of what is actually proved(required to be peer reviewed), how the construction works, and why the $1 million prize remains unclaimed.

---

## 1. The actual Millennium Prize problem (Fefferman’s formulation)

The Clay Mathematics Institute problem, as formulated by Charles Fefferman, is stated as **four alternatives** on $\mathbb{R}^3$ and $\mathbb{T}^3$

- **(A)** On $\mathbb{R}^3$ with **no external force** ($f\equiv 0$) and smooth, finite-energy initial data, there exist global smooth solutions for all such data.
- **(B)** On $\mathbb{R}^3$ with **no external force** ($f\equiv 0$), there exist smooth, finite-energy initial data that produce a finite-time singularity (blowup) while kinetic energy stays bounded.
- **(C)** On $\mathbb{R}^3$ allowing a **smooth, physically reasonable forcing** $f$, either global smooth solutions exist for all smooth data and forces, or there exist smooth data and a smooth force producing finite-time blowup with bounded energy.
- **(D)** The periodic analogue of (C) on $\mathbb{T}^3$[^3].

The “pure fluid, no outside interference” question that dominates popular discussion is **(A)/(B)** with $f\equiv 0$.  OpenAI’s result lives in **(C)/(D)**, where a smooth external force is explicitly allowed.[^1]

---

![img](https://media.nature.com/lw767/magazine-assets/d41586-026-02842-5/d41586-026-02842-5_53685260.jpg?as=webp)

## 2. What OpenAI actually proved

OpenAI’s main theorem (Theorem 1.1) states: for every viscosity $\nu>0$, there exist

- a smooth, compactly supported external force $f\in C_c^\infty(\mathbb{R}^3\times(0,\infty);\mathbb{R}^3)$,
- smooth velocity and pressure fields $(u,p)$ on $\mathbb{R}^3\times[0,1)$, and
- a compact set $K\subset\mathbb{R}^3$,

such that the incompressible Navier–Stokes equations

$$
\partial_t u + (u\cdot\nabla)u - \nu\Delta u + \nabla p = f,\quad \nabla\cdot u = 0,\quad u(\cdot,0)=0
$$

satisfy

$$
\sup_{0\le t<1}\|u(t)\|_{L^2(\mathbb{R}^3)}<\infty,\qquad \limsup_{t\uparrow 1}\|u(t)\|_{L^\infty(\mathbb{R}^3)}=\infty,
$$

with the singular set at blowup time contained in $K$.  The authors explicitly state that this **establishes Alternative (C)** in Fefferman’s formulation (and, by compact support of $f$, also the periodic **Alternative (D)**).[^1]

In plain language: they prove that 3D Navier–Stokes **can** blow up in finite time, but only when you add a carefully engineered smooth force that “pushes” the fluid into a singularity while keeping total kinetic energy bounded.[^1]

---

## 3. How they forced the blowup (mechanics of the construction)

The proof is a highly technical convex-integration-style construction adapted to the viscous case. At a high level, it proceeds as follows.[^1]

### Step A: A concentrating “death-spiral” background flow

They build an axisymmetric, self-similar background flow $(u_B,p_B)$ whose vortex core collapses as $t\to 1$. The radial and axial length scales shrink anisotropically:

$$
\ell_r \sim \tau^{1/2},\qquad \ell_z \sim \tau^{1/2-h},
$$

with $\tau = 1-t$. [^1] Because the core volume shrinks faster than the peak velocity grows, the total kinetic energy stays bounded (in fact decays), even as $\|u_B\|_{L^\infty}\to\infty$. [^1]

### Step B: The singular residual in the annulus

This background flow solves the equations well inside the core and in the smooth exterior, but at the interface (an annulus) the interior and exterior profiles do not match. This mismatch produces a **singular momentum residual** in the Navier–Stokes balance.  If one simply set the external force $f$ equal to this residual, $f$ would be singular, contradicting the requirement that $f\in C_c^\infty$.[^1]

### Step C: High-frequency pulses and Reynolds stress cancellation

To cancel the singular residual without using a singular force, they inject high-frequency, divergence-free oscillatory wave packets (pulses) into the annulus.  Under the background shear, these waves are stretched and amplified. The key observation is that the nonlinear term $(w\cdot\nabla)w$ for these pulses has a nontrivial spatial average: the self-interaction of the waves generates a steady, macroscopic momentum flux—the **Reynolds stress**.[^2]  By tuning the amplitude, frequency, and polarization of the pulses, they arrange that the divergence of this Reynolds stress **exactly cancels** the singular part of the background residual.  In effect, the fluid’s own high-frequency vibrations act as a pump that balances the singular background error.[^1]

### Step D: An auxiliary torus to kill cross-terms

With multiple pulses, cross-terms like $w_1\cdot\nabla w_2$ would generate uncontrolled quadratic errors. To avoid this, the construction introduces an **auxiliary spatial variable** on a torus $\mathbb{T}^2$.  Each pulse is given disjoint support in this auxiliary space. Even if two pulses overlap in physical space, their product in the auxiliary variable is zero, so all cross-terms vanish identically.  This decoupling allows the covariances (Reynolds stresses) of individual pulses to sum linearly without generating garbage interaction terms.[^1]

### Step E: Iterative corrections and a flat remainder

Adding the pulses introduces new errors: curl corrections to maintain incompressibility, mean-flow errors, radial moment defects, and higher-order remainders.  The authors set up a **four-step iterative correction cycle** (angular-mode corrections, signed amplitude adjustments, mean-flow/auxiliary-time inversion, and radial moment equations) that pushes the residual to higher and higher order of decay as $t\to 1$.  After finitely many iterations, the remaining residual is **flat** at $t=1$ (it vanishes to infinite order).  Because the residual is flat, the external force $f$ can be smoothly extended through $t=1$, ensuring $f\in C_c^\infty$ in space and time.[^1]

---

## 4. Why this does not solve the “unforced” Millennium question

The media claim—“They proved Navier–Stokes can blow up, solving the Millennium problem”—omits the crucial hypothesis that a **smooth external force is present throughout**.  OpenAI’s theorem establishes **Alternative (C)/(D)** (forced blowup), not **Alternative (A)/(B)** (unforced regularity/blowup).[^1]

Why is the unforced case so much harder? In OpenAI’s construction, the external force $f$ acts as a “hand of God”: it supplies the exact energy and momentum transfers needed to sustain the high-frequency Reynolds stress that cancels the background residual.  The force is doing the heavy lifting to keep the singularity mechanism balanced.

If $f\equiv 0$, the fluid would have to generate this precise Reynolds stress **entirely from its initial data**, cascading energy to arbitrarily high frequencies faster than viscosity dissipates it, while strictly conserving total kinetic energy.  There is no external agent to inject momentum at the exact right frequency to keep the singularity alive.  This is why the community regards the unforced problem as the deeper, still-open question[^5].

---

## 5. Summary

OpenAI’s paper is a major achievement in PDE theory and AI-assisted mathematics:

- It gives the first rigorous construction of a **finite-time blowup** for the **true, positive-viscosity 3D Navier–Stokes equations** with smooth data, but in the **forced** setting.[^1]
- It establishes **Alternatives (C) and (D)** in Fefferman’s Clay formulation, not the unforced Alternatives (A)/(B).[^1]
- The proof uses thousands of AI agents to check the grueling exponent bookkeeping and inequalities, a historic milestone for AI in mathematics[^4].

But it does **not** solve the Millennium Prize Problem as most people understand it. The **unforced** regularity/blowup question remains open, and the $1 million prize is still waiting in Denver[^1].

---

## Primary source

[^1]: [OpenAI, **Finite Time Blowup for Navier–Stokes**, Theorem 1.1 and discussion of Alternatives (C)/(D)](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)
    
[^2]: [Companion Lean formalization and problem-alternative mapping](https://github.com/openai/NavierStokesAndEuler)
    
[^3]: [gadgetsnow.indiatimes](https://gadgetsnow.indiatimes.com/tech-news/navier-stokes-holds-as-openai-and-anthropic-staff-clash/articleshow/133935320.cms)
    
[^4]: [stanfordtechreview](https://stanfordtechreview.com/articles/openai-buckmaster-navier-stokes-lean-proofs)
    
[^5]: [thenextweb](https://thenextweb.com/news/openai-navier-stokes-proof-published-millennium-prize)
    
[^6]: [Nature2026](https://www.nature.com/articles/d41586-026-02842-5)
