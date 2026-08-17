---
title: "DDG — Advanced Discrete Differential Geometry Framework (Research-Grade)"
excerpt: "A comprehensive, production-ready Discrete Exterior Calculus (DEC) / FEM implementation for triangle meshes with spectral geometry, curvature analysis, PDE solvers, and advanced vector field processing.<br/><img src='/images/500x300.png' alt='DDG Framework'/>"
collection: portfolio
date: 2026-04-30
url: "https://github.com/ajeetkbhardwaj/discrete-differential-geometry"
category: "Computational Geometry"
---

A **comprehensive, production-ready** Discrete Exterior Calculus (DEC) / FEM implementation 
for triangle meshes with spectral geometry, curvature analysis, PDE solvers, and advanced
vector field processing.

✅ **ALL PHASES IMPLEMENTED** (100% feature coverage)

---

## 🌟 Features Overview

*   **Phase 1–2: Core DEC** ✅
    *   Half-edge mesh with adjacency queries
    *   Exterior derivatives d₀, d₁ (topological matrices)
    *   Hodge star operators *₀, *₁, *₂
    *   Laplace–Beltrami operator
*   **Phase 5A: Vector Operators** ✅
    *   `gradient(u)` — vertex scalar → edge values
    *   `divergence(v)` — edge values → vertex scalar
    *   `curl(u)` scalar and `curl(v)` vector forms
*   **Phase 5B: Spectral + Shape** ✅
    *   Wave Kernel Signature (WKS) — advanced shape descriptor
    *   Vertex normals, principal directions
    *   Shape operator (Weingarten map)
*   **Phase 5C: Advanced PDE** ✅
    *   Geodesic distance (heat method)
    *   Hodge decomposition (curl-free + div-free + harmonic)
*   **Phase 6: Visualization** ✅
    *   Polyscope integration (interactive 3D viewer)
    *   Batch visualization API
*   **Phase 7: I/O & Utilities** ✅
    *   OBJ, PLY, OFF file support
    *   Auto-format detection

---

## 🚀 Quick Start

### Installation
Install dependencies:
```bash
pip install -r requirements.txt
pip install polyscope  # For interactive 3D visualization (optional)
```

### Run Demos
```bash
python examples/advanced_demo.py      # All features in one go
python examples/spectral_demo.py      # Eigenvalues + HKS
python examples/curvature_demo.py     # Curvature visualization
python examples/pde_demo.py           # PDE solvers
```

### Run Tests
```bash
pytest tests/ -v
```

---

## 📚 Mathematical References

*   Crane et al. *Discrete Differential Geometry: An Applied Introduction* (2018)
*   Botsch et al. *Polygon Mesh Processing* (2010)
*   Meyer et al. Discrete differential-geometry operators for triangulated 2-manifolds (2003)
*   Crane et al. Geodesics in Heat (2013)

---

---
## 📅 Weekly Plan & Updates
*Write your weekly plan, problems tackled, and achievements here. The automated script will never overwrite this text!*

### 👑 Team Leader Update (Ajeet Kumar)
* **Solved:** [What did you solve?]
* **Working on:** [What are you currently working on?]
* **Next Steps:** [What is next?]

### 👨‍💻 Team Member Updates
* **Solved:** [What did the team solve?]
* **Working on:** [What is the team currently working on?]