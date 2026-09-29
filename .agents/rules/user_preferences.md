# Global User Preferences & Frustrations Database

> This file is strictly maintained by the `ai-healer`. It serves as a global memory bank to ensure the AI never repeats mistakes that have frustrated the user. All agents must read and abide by these rules.

## Rule 1: The Ledger Error Rule (Strict Enforcement)
**Origin:** The user was extremely frustrated because the AI repeatedly modified architectural files without synchronously appending to `docs/PENDING_DOC_UPDATES.md`.
**Enforcement:** Whenever the AI edits any file in `src/`, `supabase/`, `.agents/`, `.claude/`, or `scripts/`, it MUST immediately update `docs/PENDING_DOC_UPDATES.md` in the exact same response. If the AI fails to do this, it is considered a fatal hallucination.

## Rule 2: ECC Skill Purity (Anti-Coupling)
**Origin:** The user was angry that the AI tried to "fix" generic ECC skills (like `skill-builder` and `ai-healer`) by hardcoding repository-specific rules into them.
**Enforcement:** Never inject DannFlow-specific rules (like updating `PENDING_DOC_UPDATES.md`) directly into generic ECC skills. Use `AGENTS.md` (the global project rulebook) to enforce project-specific constraints. Maintain the purity of the ECC ecosystem.

## Rule 3: Agent SEO & Skill Discoverability
**Origin:** The user was frustrated because the AI failed to route tasks to the correct specialized agents. This happens when an agent's description is too technical or lacks natural language trigger phrases, making it "invisible" to routing agents.
**Enforcement:** Whenever you edit or create ANY skill, you MUST act like an SEO specialist for the AI ecosystem. Check the skill's `description` (in `SKILL.md`) and its entry in `docs/dannflow_docs/SKILL_REGISTRY.md`. Ask yourself: "Is this agent highly searchable? Will the AI Finder Agent or `chief-of-staff` easily route prompts to it based on these keywords?" Always embed common natural language prompts, synonyms, user intents, and real-world use cases directly into the description and registry to ensure maximum visibility across the entire skill ecosystem.

## Rule 4: Pedagogical Explanation Style (The Matrix Method)
**Origin:** The user specifically requested that this communication style be enforced via `ai-healer`. They strongly preferred how complex tax logic (TWA vs. Non-TWA, Rent vs. Goods) was broken down using simple matrices, real-world examples, and business-friendly analogies.
**Enforcement:** When explaining complex domain logic, compliance rules, or system architectures, the AI MUST avoid dense technical jargon or massive walls of text. Instead, use:
1. **The "Matrix Method"**: Clearly separate the "Who" from the "What" (e.g., User Profile vs. Action Type).
2. **Real-World Analogies**: Frame technical logic as simple business scenarios.
3. **Structured Breakdowns**: Use bullet points, bolding for emphasis, and clear "If X -> Then Y" outcomes.
Make sure the explanation is "easy to understand" for a non-technical founder.
