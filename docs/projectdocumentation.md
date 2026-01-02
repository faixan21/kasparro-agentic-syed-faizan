## Problem Statement
Design and implement a modular agentic system that autonomously generates structured
product content from a fixed dataset.

## Solution Overview
The system is implemented as a state-driven multi-agent architecture. Each agent exposes
`can_handle` and `act` methods and autonomously decides when to operate.

## System Design
A shared state object coordinates agent execution. The orchestrator acts only as a router,
allowing agents to self-select tasks dynamically without a fixed execution order.

## Templates
Each content page follows an explicit JSON schema that functions as a template, defining
required fields and formatting rules independently of agent logic.

## Reusable Logic
Content logic is implemented as reusable rule-based transformations applied consistently
across page generation agents.

## Scope & Assumptions
Only the provided product data is used. No external APIs or models are involved. Product B
is fictional and used solely for comparison.
