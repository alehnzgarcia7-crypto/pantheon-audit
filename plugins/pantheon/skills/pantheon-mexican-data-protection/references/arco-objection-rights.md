# ARCO + Objection-to-Automated-Processing Rights

## ARCO (Access, Rectification, Cancellation, Opposition)
Pre-existing under 2010 LFPDPPP, retained under 2025 LFPDPPP with expanded definitions.

## NEW: Right to object to automated processing significantly affecting rights or freedoms
Article 6 second paragraph, LFPDPPP 2025. Modeled on GDPR Article 22 but with broader scope.

### Audit checkpoints
- Automated-decision endpoints identified (credit scoring, loan approval, KYC, fraud detection, transaction monitoring)
- Data-subject objection mechanism exists (cannot be hidden behind premium tier or excessive friction)
- Human review available within reasonable time (recommend 5 business days max)
- Decision explanation generated on request (must be intelligible to non-technical user)
- Right is meaningfully exercisable (no dark patterns, no manufactured consent)

### Phoenix Financial OS specific
For an AI-native Mexican fintech, this is the highest-leverage compliance gap. ALL automated decisions must expose explainability. Implement via XAI library (LIME, SHAP, or model-card with example explanations).

### Severity calibration
- Absence of objection mechanism: Critical
- Mechanism exists but no human review: High
- Mechanism exists with human review but no explanation: Medium-High
- All present but dark pattern (e.g., 30-day waiting period): High
