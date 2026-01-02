# Multi-Agent Content Generation System

## Overview
This project implements a modular agent-based system that generates structured, machine-readable content pages from a fixed product dataset. The focus of the system is on clear agent boundaries, reusable logic, and deterministic orchestration rather than creative content generation.

The system was built as part of the Kasparro Applied AI Engineer challenge.

---

## Problem Context
Given a single product dataset, the system must automatically generate:
- Categorized user questions
- A FAQ page
- A product description page
- A comparison page against a fictional product

All outputs are produced in structured JSON format using a multi-agent pipeline.

---

## System Architecture
The system follows an orchestrator-driven workflow where each agent has a single responsibility.

High-level flow:

Product Data:

- Data Parsing Agent
- Question Generation Agent
- Content Logic Blocks
- Page Generation Agents
- JSON Outputs

---

## How to Run
```bash
python main.py
