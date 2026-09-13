# ORCA — SIH26176

## Evidence-Grounded, Constraint-Aware Marine Mission Decision Intelligence

ORCA is an Agentic AI-powered marine decision-support prototype for SIH 2026 Problem Statement SIH26176.

The prototype converts a natural-language fishing mission into a structured mission, gathers evidence from PFZ, ocean, weather and GIS agents, evaluates operational constraints, compares candidate plans and produces an explainable recommendation.

## Prototype Pipeline

Natural Language Mission
→ Mission Parser
→ Planner / Orchestrator
→ PFZ + Ocean + Weather + GIS Agents
→ Evidence Fusion
→ Constraint & Risk Engine
→ Candidate Plans
→ Feasibility Comparison
→ Evidence Chain
→ Recommendation
→ Interactive GIS Map
→ Re-evaluation