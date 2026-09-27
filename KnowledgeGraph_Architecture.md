# Knowledge Graph Architecture

The Knowledge Graph is the absolute "brain" of EduOS.

## Vision
Every piece of educational content is a Node. Nodes are connected by Edges.

## Node Types
- **Subject** (e.g., Physics)
- **Chapter** (e.g., Motion)
- **Concept** (e.g., Velocity)
- **Definition** (e.g., "Speed in a given direction")
- **Formula** (e.g., v = d/t)
- **Scientist** (e.g., Isaac Newton)

## Edges (Relationships)
- `REQUIRES_PREREQUISITE` (e.g., Calculus requires Algebra)
- `IS_OPPOSITE_OF` (e.g., Balanced Force vs Unbalanced Force)
- `APPLIED_IN` (e.g., Vectors applied in Force calculations)

## Future Implementation
Migrating from local `dictionary.json` cross-linking to a robust Cloud Graph Database (e.g., Neo4j) to power the "AI Tutor" so it truly understands the relationships between all human knowledge.
