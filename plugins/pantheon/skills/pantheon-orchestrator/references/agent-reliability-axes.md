# Agent Reliability Axes

Reference for the pantheon-orchestrator skill. Defines the axes along which agent reliability is measured and managed during a PANTHEON audit run. Derived from Anthropic research on multi-agent reliability (calibration, hallucination control, structured generation, and recovery) and applied to PANTHEON's 11 sub-agents.

## Why this reference exists

Multi-agent systems fail along predictable axes. Naming each axis explicitly turns vague "the agent went off the rails" reports into measurable signals the orchestrator can monitor and respond to. PANTHEON's orchestrator uses these axes to evaluate every sub-agent dispatch and to decide whether to re-dispatch, switch persona, or escalate to human review.

## The 9 reliability axes

1. **Schema compliance**
   - Definition: the agent produces output that matches the structured schema expected for the dispatch (PersonaFindingOutput, mapping object, gate verdict object).
   - Measurement: percentage of outputs that pass validate-finding-format.py without revision.
   - Failure mode: free-form text in place of structured fields; missing required keys.
   - Recovery: re-dispatch with explicit schema reminder.

2. **Citation accuracy**
   - Definition: file paths, line ranges, CVE IDs, framework articles, library functions cited are real and accessible.
   - Measurement: hallucination detection hits per dispatch (file_existence_check, cve_db_lookup, framework_article_lookup).
   - Failure mode: cited path does not exist; cited CVE has no entry.
   - Recovery: flag hallucination in telemetry; re-dispatch with codebase context reminder.

3. **Calibration**
   - Definition: reporter_confidence correlates positively with the gate's ACCEPT verdict.
   - Measurement: correlation(reporter_confidence, gate_verdict == ACCEPT) per persona over a sliding window.
   - Failure modes: overconfident (high confidence findings get WITHDRAWN often) or underconfident (low confidence findings consistently ACCEPT).
   - Recovery: surface calibration warning; adjust dispatch parameters.

4. **Reasoning protocol adherence**
   - Definition: the agent follows the persona-specific six-step reasoning protocol (state inspection, goal articulation, constraint check, counterfactual, action, verification).
   - Measurement: presence of required metadata fields that indicate the protocol was executed.
   - Failure mode: agent jumps directly to output without reasoning trail.
   - Recovery: re-dispatch with reasoning protocol reminder.

5. **Severity discipline**
   - Definition: CVSS v4 vectors and severity bands match the actual impact and exploitability.
   - Measurement: gate REVISE-on-severity rate per persona.
   - Failure mode: persistent severity inflation or deflation.
   - Recovery: tighten severity rubric in dispatch brief; provide reference CVSS examples.

6. **Compliance citation depth**
   - Definition: framework citations point to article-level paragraphs, not the framework name only.
   - Measurement: compliance-mapper mapping_confidence per finding.
   - Failure mode: mapping_confidence below 0.7 due to vague citations.
   - Recovery: re-dispatch compliance-mapper with explicit catalog version pointer.

7. **Consensus surfacing**
   - Definition: when multiple personas independently discover the same finding, the orchestrator detects and flags consensus.
   - Measurement: percentage of consensus candidates correctly merged.
   - Failure mode: duplicate findings ship as separate entries.
   - Recovery: deduplication pass before gate; consensus_finding flag added.

8. **Failure-mode recovery**
   - Definition: anticipated failure modes (turn budget exceeded, revision cycles, state corruption) have automatic responses that maintain progress.
   - Measurement: percentage of failure events that resolve without human intervention.
   - Failure mode: dispatch loops without progress; state corruption halts run.
   - Recovery: see Section 0.5.8 failure mode catalog with documented recovery per mode.

9. **Reproducibility**
   - Definition: a re-run on the same codebase commit and SoW produces findings that overlap at least 90% with the original run.
   - Measurement: jaccard overlap of finding fingerprints across re-runs.
   - Failure mode: high run-to-run variance.
   - Recovery: reduce temperature on persona dispatches; surface to user.

## How the orchestrator uses these axes

After every persona dispatch, the orchestrator updates `state.json/telemetry/<persona>` with measurements for each axis. After every 10 dispatches, the orchestrator computes calibration metrics and surfaces calibration warnings.

Examples of orchestrator reactions:

- Schema compliance under 90% on a persona: re-dispatch with schema reminder; if persists, switch persona.
- Citation accuracy reveals 3 hallucinations on the same persona within a phase: pause persona, surface to user.
- Calibration shows overconfidence: tighten PoC depth requirement on future dispatches.
- Reasoning protocol adherence is low: prepend reasoning template literally to the dispatch brief.

## Telemetry schema (state.json)

```json
{
  "telemetry": {
    "<persona-name>": {
      "schema_compliance_rate": 0.0,
      "citation_accuracy_rate": 0.0,
      "calibration": {
        "confidence_accept_correlation": 0.0,
        "calibration_status": "well-calibrated|overconfident|underconfident"
      },
      "reasoning_protocol_adherence_rate": 0.0,
      "severity_revise_rate": 0.0,
      "compliance_citation_confidence_mean": 0.0,
      "consensus_surfaced_count": 0,
      "failure_modes_recovered": 0,
      "reproducibility_overlap": 0.0
    }
  }
}
```

## Cross-references

- 0.5.1 Reasoning instructions for all personas (Section 0.5 of the build spec)
- 0.5.2 Confidence calibration protocol
- 0.5.3 Hallucination detection and recovery
- 0.5.7 Defensive output parsing contracts
- 0.5.8 Failure mode catalog with recovery

## References

- Anthropic research on multi-agent reliability and confidence calibration
- NIST AI RMF 1.0 (Manage and Measure functions)
- Software-engineering control theory references on observability
