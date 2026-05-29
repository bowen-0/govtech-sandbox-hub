"use client";

import { RiskAccordion } from "@/components/thread/risk-accordion";

const samplePayload = {
  project: {
    name: "Permit Triage Assistant",
    sector: "Public administration",
    deployment: "Internal pilot",
    size: "Small team",
  },
  assessments: [
    {
      risk: {
        id: "personal-data",
        title: "Personal data in uploaded documents",
        category: "Privacy",
        description:
          "Permit files can include names, addresses, signatures, and supporting documents that identify applicants or third parties.",
        severity: "high",
      },
      relevance_reason:
        "The assistant may process free-form documents supplied by residents or municipal staff.",
      mitigation:
        "Use data minimisation, restrict access to authorised staff, redact sensitive fields where possible, and document retention rules before the pilot.",
      regulatory_refs: ["FADP", "IDG-ZH", "DSG"],
      wiki_refs: [
        "wiki/concepts/data-minimisation.md",
        "wiki/regulations/idg-zh.md",
      ],
    },
    {
      risk: {
        id: "automation-bias",
        title: "Over-reliance on generated recommendations",
        category: "Decision support",
        description:
          "Users may treat model output as a final decision even when the system is only intended to support review.",
        severity: "medium",
      },
      relevance_reason:
        "The tool summarizes risks and next steps for case handlers, which can influence administrative workflows.",
      mitigation:
        "Keep a human decision-maker accountable, show uncertainty, and require source review before any external action.",
      regulatory_refs: ["EU AI Act", "FADP Art. 21"],
      wiki_refs: [
        "wiki/concepts/real-world-testing.md",
        "wiki/regulations/eu-ai-act.md",
      ],
    },
    {
      risk: {
        risk_id: "auditability",
        risk_title: "Insufficient audit trail",
        category: "Governance",
        description:
          "Without logs and citations, teams may not be able to reconstruct why a recommendation was shown.",
        severity: "low",
      },
      relevance_reason:
        "The pilot is exploratory, but public-sector deployments still need traceability for trust and review.",
      mitigation:
        "Store prompt version, selected sources, model version, and user confirmation events for each generated assessment.",
      regulatory_refs: ["ISO/IEC 42001"],
      wiki_refs: ["wiki/regulations/iso-iec-42001.md"],
    },
  ],
};

export default function UiTestPage() {
  return (
    <main className="mx-auto min-h-screen max-w-3xl px-6 py-10">
      <RiskAccordion data={samplePayload} />
    </main>
  );
}
