# Non-Linear Programming for Assembly Line Balancing

Bachelor's thesis project — Yildiz Technical University, Industrial Engineering Department, June 2020.

## Overview

This project addresses the **Assembly Line Balancing Problem (ALBP)** in a real-world home appliances manufacturing setting. The goal was to optimally assign tasks to workstations while minimizing cycle time, allowing for multi-manned stations and parallel task assignment.

The study was conducted in collaboration with a home appliances factory and includes both a linear and a non-linear programming formulation of the problem, implemented in Python using the PuLP library.

## Problem

Traditional assembly line balancing assumes one worker per station and no parallel task execution. In practice, many factories use multi-manned stations where multiple operators share a workstation. This thesis extends the classic model to handle:

- **Multi-manned stations** — multiple operators assigned to one station
- **Parallel task assignment** — tasks that can be executed simultaneously
- **Precedence constraints** — tasks that must follow a specific order

## Methodology

1. Value Stream Mapping (VSM) of the current production process
2. Precedence diagram construction
3. Mathematical model formulation (linear + non-linear)
4. Python implementation using PuLP (Mixed Integer Programming)
5. Sensitivity analysis on key parameters

## Files

| File | Description |
|---|---|
| `main.py` | Main optimization model implementation |
| `model.py` | Model formulation and constraints |
| `Thesis-Assembly Line Balancing.pdf` | Full thesis document |
| `Poster-Assembly Line Balancing.pptx` | Research poster |

## Tools

- **Python** — PuLP, pandas
- **Method** — Mixed Integer Non-Linear Programming (MINLP)
- **Case** — Home appliances manufacturing factory, Istanbul

## Authors

Büşra Karaali · İlknur Sezen · Mustafa Kurtoğlu

*Advisor: Prof. Dr. Alev Taşkın Gümüş*
