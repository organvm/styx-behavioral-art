# styx-behavioral-art

Artistic visualization of behavioral accountability, translating Styx's economic theory into creative expression.

## Position in the ORGANVM Pipeline

This repo follows the **art-from--** derivation pattern that defines the I-II-III organ flow:

- **ORGAN-I** (`styx-behavioral-economics-theory`) provides the formal models: stake mechanics, audit cycles, commitment contracts, and behavioral game theory.
- **ORGAN-II** (`styx-behavioral-art`, this repo) translates those models into visual language, generative systems, and performance scores.
- **ORGAN-III** (`peer-audited--behavioral-blockchain`) consumes these creative artifacts as interface metaphors, onboarding narratives, and public-facing identity.

This is the first ORGAN-II repo with genuine I-to-II derivation -- consuming structured theory from ORGAN-I and producing creative artifacts that flow downstream to ORGAN-III products.

## Concept Areas

### Stake and Commitment Visualization

Interactive data art driven by stake amounts, commitment durations, and audit outcomes. Force-directed graphs where node intensity reflects stake magnitude and edges encode audit relationships. See `concepts/stake-commitment-visualization.md`.

### Audit Cycle Generative Art

The temporal rhythm of audit cycles -- challenge, respond, resolve -- as a seed for generative visual patterns. L-systems and cellular automata whose growth rules derive from behavioral data. See `concepts/audit-cycle-generative-art.md`.

### Accountability as Performance

Accountability reframed as live, interactive performance art. The public ledger becomes a theatrical score; audit events become dramatic beats. Draws on precedents from Blast Theory, Rafael Lozano-Hemmer, and networked performance. See `concepts/accountability-as-performance.md`.

## Structure

```
seed.yaml                              # ORGANVM automation contract
Makefile                               # Local test command
concepts/
  stake-commitment-visualization.md     # Data art from stake mechanics
  audit-cycle-generative-art.md         # Generative systems from audit rhythms
  accountability-as-performance.md      # Live performance from ledger events
docs/pitch/index.html                  # Static ORGANVM pitch artifact
tests/test_pitch_artifact.py           # Regression coverage for the pitch artifact
```

## Status

Concept phase. No application runtime yet -- this repo currently holds design documents and a static pitch artifact that will evolve into prototypes as the Styx theory stabilizes.

## Testing

Run the focused regression suite with:

```sh
make test
```
