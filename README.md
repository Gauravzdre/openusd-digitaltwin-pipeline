# openusd-digitaltwin-pipeline

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](#)
[![OpenUSD](https://img.shields.io/badge/OpenUSD-Pixar%20%7C%20NVIDIA-orange.svg)](#)

Automated CAD to OpenUSD pipeline for NVIDIA Omniverse industrial digital twins and Isaac Sim physics validation.

```mermaid
graph LR
    A[STEP / JT CAD Files] --> B[cad_to_usd_compiler]
    B --> C[V-HACD Convex Decomposition]
    C --> D[physics_schema_rigging]
    D --> E[USD Industrial Digital Twin Stage]
```

## Features

- **Hierarchical STEP Ingestion**: Preserves assembly parent-child transforms, mass properties, and kinematic limits.
- **PhysX 5.4 Tagging**: Automatically applies `UsdPhysics.RigidBodyAPI` and joint limits for zero-crash simulation.
- **Omniverse Kit Extension**: Direct export into Isaac Sim for hardware-in-the-loop virtual commissioning.

## License

MIT License (c) 2022-2026 Gaurav Bhardwaj / OmegaGaze Lab.
