"""Internal risk database for AI sandbox projects (Swiss public sector)."""

from __future__ import annotations

from typing import TypedDict


class Risk(TypedDict):
    id: str
    title: str
    category: str
    description: str
    severity: str  # low / medium / high / critical


class RiskMitigation(TypedDict):
    mitigation: str
    regulatory_refs: list[str]


_RISKS: list[Risk] = [
    {
        "id": "r001",
        "title": "Data Privacy Violation",
        "category": "Privacy & Compliance",
        "description": "Processing personal data without proper consent or legal basis under GDPR/nDSG.",
        "severity": "critical",
    },
    {
        "id": "r002",
        "title": "Model Hallucination in Decision Support",
        "category": "AI Quality",
        "description": "LLM outputs factually incorrect information used in official or consequential decisions.",
        "severity": "high",
    },
    {
        "id": "r003",
        "title": "Vendor Lock-in",
        "category": "Operational",
        "description": "Dependency on a single AI provider with no viable migration path.",
        "severity": "medium",
    },
    {
        "id": "r004",
        "title": "Algorithmic Bias",
        "category": "Fairness & Ethics",
        "description": "AI model produces discriminatory outcomes for legally protected groups.",
        "severity": "high",
    },
    {
        "id": "r005",
        "title": "Data Sovereignty Breach",
        "category": "Legal",
        "description": "Sensitive government or citizen data processed outside Swiss/EU jurisdiction.",
        "severity": "critical",
    },
    {
        "id": "r006",
        "title": "Lack of Explainability",
        "category": "Transparency",
        "description": "AI decisions cannot be explained to citizens, oversight bodies, or auditors.",
        "severity": "high",
    },
    {
        "id": "r007",
        "title": "Cybersecurity Vulnerability",
        "category": "Security",
        "description": "Prompt injection, model inversion, or data extraction attacks exposing sensitive information.",
        "severity": "high",
    },
    {
        "id": "r008",
        "title": "Inadequate Human Oversight",
        "category": "Governance",
        "description": "Automated decisions made without meaningful human review or an accessible appeal mechanism.",
        "severity": "high",
    },
    {
        "id": "r009",
        "title": "Training Data Quality",
        "category": "AI Quality",
        "description": "Model trained on outdated, biased, or unrepresentative datasets leading to degraded performance.",
        "severity": "medium",
    },
    {
        "id": "r010",
        "title": "Scope Creep Beyond Sandbox",
        "category": "Governance",
        "description": "Pilot expands to production use without a formal risk assessment and governance sign-off.",
        "severity": "medium",
    },
    {
        "id": "r011",
        "title": "Environmental Impact",
        "category": "Sustainability",
        "description": "Disproportionately high energy consumption from large-model inference at operational scale.",
        "severity": "low",
    },
    {
        "id": "r012",
        "title": "Staff Deskilling",
        "category": "Organizational",
        "description": "Over-reliance on AI erodes staff competencies and institutional knowledge over time.",
        "severity": "medium",
    },
]

_MITIGATIONS: dict[str, RiskMitigation] = {
    "r001": {
        "mitigation": (
            "Conduct a Data Protection Impact Assessment (DPIA). Establish a legal basis "
            "(consent or legitimate interest). Appoint a DPO where required. Apply data "
            "minimization and pseudonymization by design."
        ),
        "regulatory_refs": ["GDPR Art. 5, 6, 35", "nDSG Art. 6, 22", "DSV Art. 22"],
    },
    "r002": {
        "mitigation": (
            "Use Retrieval-Augmented Generation (RAG) anchored to auditable source documents. "
            "Add a human-in-the-loop gate for high-stakes outputs. Log all model responses "
            "with the source context used."
        ),
        "regulatory_refs": ["EU AI Act Art. 9", "Sandbox principle: traceable sources"],
    },
    "r003": {
        "mitigation": (
            "Define a multi-vendor strategy from the start. Use open model formats (e.g. GGUF/ONNX). "
            "Maintain full data portability. Prefer open-weight base models for core functionality."
        ),
        "regulatory_refs": ["Sandbox principle: sovereign infrastructure"],
    },
    "r004": {
        "mitigation": (
            "Run fairness audits across demographic subgroups before deployment. Document which "
            "protected attributes are excluded from training. Establish ongoing monitoring for "
            "disparate impact."
        ),
        "regulatory_refs": ["BV Art. 8 (Gleichheitsgebot)", "EU AI Act Art. 10"],
    },
    "r005": {
        "mitigation": (
            "Deploy on Swiss/EU sovereign cloud (e.g. SOGI, T-Systems Sovereign Cloud). Avoid "
            "transmitting PII to US-hosted APIs. Use on-premise inference for the most sensitive "
            "data categories."
        ),
        "regulatory_refs": ["nDSG Art. 16", "GDPR Chapter V", "BBl 2023 (Datensouveränität)"],
    },
    "r006": {
        "mitigation": (
            "Use interpretable models for high-stakes decisions. Implement SHAP/LIME post-hoc "
            "explanations. Provide plain-language summaries to citizens alongside any AI-informed "
            "decision notice."
        ),
        "regulatory_refs": ["GDPR Art. 22 (automated decisions)", "EU AI Act Art. 13"],
    },
    "r007": {
        "mitigation": (
            "Validate and sanitize all inputs before model inference. Conduct adversarial red-teaming "
            "before go-live. Apply rate limiting and anomaly detection. Isolate the model runtime "
            "from internal sensitive systems."
        ),
        "regulatory_refs": ["EU AI Act Art. 9 (risk management)", "NCSC guidelines CH"],
    },
    "r008": {
        "mitigation": (
            "Define mandatory human review checkpoints for all consequential decisions. Publish a "
            "clear appeal process. Track and report override rates quarterly."
        ),
        "regulatory_refs": ["GDPR Art. 22", "EU AI Act Art. 14 (human oversight)"],
    },
    "r009": {
        "mitigation": (
            "Document data provenance and lineage for all training sets. Define and monitor data "
            "quality KPIs. Schedule periodic retraining with fresh, representative data."
        ),
        "regulatory_refs": ["EU AI Act Art. 10 (data governance)"],
    },
    "r010": {
        "mitigation": (
            "Gate every production deployment behind a formal risk assessment and multi-stakeholder "
            "sign-off. Define explicit sandbox exit criteria in the project charter."
        ),
        "regulatory_refs": ["Sandbox terms and conditions", "ISDS governance framework"],
    },
    "r011": {
        "mitigation": (
            "Right-size model selection — prefer smaller, efficient models where quality allows. "
            "Report carbon footprint in project documentation. Prefer green-powered data centres."
        ),
        "regulatory_refs": ["Federal sustainability strategy 2030"],
    },
    "r012": {
        "mitigation": (
            "Maintain parallel human workflows during the pilot phase. Schedule regular exercises "
            "performed without AI assistance. Monitor staff competency indicators over time."
        ),
        "regulatory_refs": ["HR policies", "Sandbox principle: human capability preservation"],
    },
}


def get_all_risks() -> list[Risk]:
    """Return all risks from the internal database."""
    return _RISKS.copy()


def get_risk_mitigation(risk_id: str) -> RiskMitigation | None:
    """Return mitigation guidance and regulatory references for a risk ID."""
    return _MITIGATIONS.get(risk_id)
