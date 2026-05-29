"""Local MIT AI Risk Repository taxonomy snapshot.

Source: https://airisk.mit.edu/
The live repository includes a larger database; this module mirrors the public
domain taxonomy categories so the local agent can reason without web access.
"""

from __future__ import annotations

from .risks_db import Risk, RiskMitigation

MIT_SOURCE = "MIT AI Risk Repository: https://airisk.mit.edu/"


MIT_RISKS: list[Risk] = [
    {
        "id": "mit-1.1",
        "title": "Unfair Discrimination and Misrepresentation",
        "category": "MIT: Discrimination & Toxicity",
        "description": "Unequal treatment or representation of individuals or groups by AI systems.",
        "severity": "high",
    },
    {
        "id": "mit-1.2",
        "title": "Exposure to Toxic Content",
        "category": "MIT: Discrimination & Toxicity",
        "description": "AI exposes users to harmful, abusive, unsafe, or inappropriate content.",
        "severity": "medium",
    },
    {
        "id": "mit-1.3",
        "title": "Unequal Performance Across Groups",
        "category": "MIT: Discrimination & Toxicity",
        "description": "AI accuracy or effectiveness varies by group membership.",
        "severity": "high",
    },
    {
        "id": "mit-2.1",
        "title": "Compromise of Privacy",
        "category": "MIT: Privacy & Security",
        "description": "AI obtains, leaks, memorizes, or infers sensitive information.",
        "severity": "critical",
    },
    {
        "id": "mit-2.2",
        "title": "AI System Security Vulnerabilities and Attacks",
        "category": "MIT: Privacy & Security",
        "description": "AI systems, toolchains, or infrastructure can be exploited or manipulated.",
        "severity": "critical",
    },
    {
        "id": "mit-3.1",
        "title": "False or Misleading Information",
        "category": "MIT: Misinformation",
        "description": "AI generates or spreads incorrect or deceptive information.",
        "severity": "high",
    },
    {
        "id": "mit-3.2",
        "title": "Pollution of Information Ecosystem",
        "category": "MIT: Misinformation",
        "description": "Personalized AI-generated misinformation undermines shared reality and consensus.",
        "severity": "medium",
    },
    {
        "id": "mit-4.1",
        "title": "Disinformation, Surveillance, and Influence at Scale",
        "category": "MIT: Malicious Actors",
        "description": "AI enables large-scale manipulation, surveillance, censorship, or propaganda.",
        "severity": "critical",
    },
    {
        "id": "mit-4.2",
        "title": "Fraud, Scams, and Targeted Manipulation",
        "category": "MIT: Malicious Actors",
        "description": "AI is used for cheating, impersonation, scams, blackmail, or manipulation.",
        "severity": "high",
    },
    {
        "id": "mit-4.3",
        "title": "Cyberattacks, Weapons Development, or Mass Harm",
        "category": "MIT: Malicious Actors",
        "description": "AI assists cyber weapons, harmful weapons development, or mass harm.",
        "severity": "critical",
    },
    {
        "id": "mit-5.1",
        "title": "Overreliance and Unsafe Use",
        "category": "MIT: Human-Computer Interaction",
        "description": "Users over-trust, misuse, or develop unsafe dependence on AI systems.",
        "severity": "high",
    },
    {
        "id": "mit-5.2",
        "title": "Loss of Human Agency and Autonomy",
        "category": "MIT: Human-Computer Interaction",
        "description": "Humans delegate key decisions to AI in ways that reduce meaningful control.",
        "severity": "high",
    },
    {
        "id": "mit-6.1",
        "title": "Power Centralization and Unfair Distribution of Benefits",
        "category": "MIT: Socioeconomic & Environmental",
        "description": "AI concentrates power, resources, and benefits among particular actors.",
        "severity": "medium",
    },
    {
        "id": "mit-6.2",
        "title": "Increased Inequality and Decline in Employment Quality",
        "category": "MIT: Socioeconomic & Environmental",
        "description": "AI worsens inequality, work quality, or worker dependency.",
        "severity": "medium",
    },
    {
        "id": "mit-6.3",
        "title": "Economic and Cultural Devaluation of Human Effort",
        "category": "MIT: Socioeconomic & Environmental",
        "description": "AI-generated output destabilizes systems that rely on human creative or knowledge work.",
        "severity": "low",
    },
    {
        "id": "mit-6.4",
        "title": "Competitive Dynamics",
        "category": "MIT: Socioeconomic & Environmental",
        "description": "Race dynamics push actors to release unsafe or error-prone AI systems.",
        "severity": "medium",
    },
    {
        "id": "mit-6.5",
        "title": "Governance Failure",
        "category": "MIT: Socioeconomic & Environmental",
        "description": "Regulatory and oversight mechanisms fail to keep pace with AI development.",
        "severity": "high",
    },
    {
        "id": "mit-6.6",
        "title": "Environmental Harm",
        "category": "MIT: Socioeconomic & Environmental",
        "description": "AI development or operation creates energy, carbon, or hardware-related harms.",
        "severity": "low",
    },
    {
        "id": "mit-7.1",
        "title": "AI Pursuing Goals in Conflict With Human Values",
        "category": "MIT: AI System Safety, Failures, & Limitations",
        "description": "AI behavior conflicts with designer, user, or societal goals and values.",
        "severity": "critical",
    },
    {
        "id": "mit-7.2",
        "title": "Dangerous AI Capabilities",
        "category": "MIT: AI System Safety, Failures, & Limitations",
        "description": "AI develops or receives capabilities that increase potential for mass harm.",
        "severity": "critical",
    },
    {
        "id": "mit-7.3",
        "title": "Lack of Capability or Robustness",
        "category": "MIT: AI System Safety, Failures, & Limitations",
        "description": "AI fails to perform reliably under varied conditions or critical contexts.",
        "severity": "high",
    },
    {
        "id": "mit-7.4",
        "title": "Lack of Transparency or Interpretability",
        "category": "MIT: AI System Safety, Failures, & Limitations",
        "description": "AI decision processes are difficult to understand, inspect, or challenge.",
        "severity": "high",
    },
    {
        "id": "mit-7.5",
        "title": "AI Welfare and Rights",
        "category": "MIT: AI System Safety, Failures, & Limitations",
        "description": "Advanced systems raise questions about treatment, potential rights, or welfare.",
        "severity": "low",
    },
    {
        "id": "mit-7.6",
        "title": "Multi-Agent Risks",
        "category": "MIT: AI System Safety, Failures, & Limitations",
        "description": "Interactions between multiple AI systems create cascading failures or collusion risks.",
        "severity": "medium",
    },
]


def _mitigation_for(risk: Risk) -> RiskMitigation:
    return {
        "mitigation": (
            "Use the MIT AI Risk Repository domain taxonomy to identify exposure, "
            "then apply layered controls: governance and oversight, technical and "
            "security controls, operational process controls, and transparency and "
            "accountability controls. For this project, document the risk owner, "
            "human review point, monitoring signal, and escalation path before pilot use."
        ),
        "regulatory_refs": [MIT_SOURCE, risk["category"]],
    }


MIT_MITIGATIONS: dict[str, RiskMitigation] = {
    risk["id"]: _mitigation_for(risk) for risk in MIT_RISKS
}
