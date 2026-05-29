"use client";

import { useState } from "react";
import { ChevronDown, ChevronUp, AlertTriangle, Shield } from "lucide-react";
import { cn } from "@/lib/utils";

// ── Types matching the Python RiskAssessment TypedDict ────────────────────────

interface Risk {
  id: string;
  title: string;
  category: string;
  description: string;
  severity: "low" | "medium" | "high" | "critical";
}

interface RiskAssessment {
  risk: Risk;
  relevance_reason: string;
  mitigation: string;
  regulatory_refs: string[];
}

interface RiskAccordionProps {
  project: Record<string, string>;
  assessments: RiskAssessment[];
}

// ── Severity styling ──────────────────────────────────────────────────────────

const SEVERITY_STYLES: Record<string, string> = {
  critical: "bg-red-100 text-red-800 border border-red-200",
  high: "bg-orange-100 text-orange-800 border border-orange-200",
  medium: "bg-yellow-100 text-yellow-800 border border-yellow-200",
  low: "bg-green-100 text-green-800 border border-green-200",
};

const SEVERITY_ORDER: Record<string, number> = {
  critical: 0,
  high: 1,
  medium: 2,
  low: 3,
};

function SeverityBadge({ severity }: { severity: string }) {
  return (
    <span
      className={cn(
        "rounded-full px-2 py-0.5 text-xs font-semibold uppercase tracking-wide",
        SEVERITY_STYLES[severity] ?? "bg-muted text-muted-foreground",
      )}
    >
      {severity}
    </span>
  );
}

// ── Single accordion item ─────────────────────────────────────────────────────

function AccordionItem({ assessment }: { assessment: RiskAssessment }) {
  const [open, setOpen] = useState(false);
  const { risk } = assessment;

  return (
    <div className="border-border overflow-hidden rounded-lg border">
      <button
        onClick={() => setOpen((v) => !v)}
        className="hover:bg-muted/50 flex w-full items-center gap-3 px-4 py-3 text-left transition-colors"
      >
        <AlertTriangle
          className={cn(
            "size-4 shrink-0",
            risk.severity === "critical" && "text-red-600",
            risk.severity === "high" && "text-orange-500",
            risk.severity === "medium" && "text-yellow-500",
            risk.severity === "low" && "text-green-500",
          )}
        />
        <span className="flex-1 text-sm font-medium">{risk.title}</span>
        <span className="text-muted-foreground mr-1 hidden text-xs sm:block">
          {risk.category}
        </span>
        <SeverityBadge severity={risk.severity} />
        {open ? (
          <ChevronUp className="text-muted-foreground size-4 shrink-0" />
        ) : (
          <ChevronDown className="text-muted-foreground size-4 shrink-0" />
        )}
      </button>

      {open && (
        <div className="border-border space-y-4 border-t px-4 py-4 text-sm">
          {/* Why it matters for this project */}
          <div>
            <p className="text-muted-foreground mb-1 text-xs font-semibold uppercase tracking-wide">
              Why it applies
            </p>
            <p className="text-foreground">{assessment.relevance_reason}</p>
          </div>

          {/* Risk description */}
          <div>
            <p className="text-muted-foreground mb-1 text-xs font-semibold uppercase tracking-wide">
              Risk
            </p>
            <p className="text-muted-foreground">{risk.description}</p>
          </div>

          {/* Mitigation */}
          <div>
            <div className="mb-1 flex items-center gap-1.5">
              <Shield className="text-muted-foreground size-3.5" />
              <p className="text-muted-foreground text-xs font-semibold uppercase tracking-wide">
                Mitigation
              </p>
            </div>
            <p className="text-foreground">{assessment.mitigation}</p>
          </div>

          {/* Regulatory references */}
          {assessment.regulatory_refs.length > 0 && (
            <div>
              <p className="text-muted-foreground mb-1.5 text-xs font-semibold uppercase tracking-wide">
                Regulatory references
              </p>
              <div className="flex flex-wrap gap-1.5">
                {assessment.regulatory_refs.map((ref) => (
                  <span
                    key={ref}
                    className="bg-muted text-muted-foreground rounded px-2 py-0.5 font-mono text-xs"
                  >
                    {ref}
                  </span>
                ))}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

// ── Main exported component ───────────────────────────────────────────────────

export function RiskAccordion({ project, assessments }: RiskAccordionProps) {
  const sorted = [...assessments].sort(
    (a, b) =>
      (SEVERITY_ORDER[a.risk.severity] ?? 9) -
      (SEVERITY_ORDER[b.risk.severity] ?? 9),
  );

  return (
    <div className="w-full space-y-3">
      {/* Header */}
      <div className="flex items-start justify-between gap-4">
        <div>
          <h3 className="text-sm font-semibold">
            Risk Assessment — {project.name ?? "Your Project"}
          </h3>
          {project.sector && (
            <p className="text-muted-foreground mt-0.5 text-xs">
              {project.sector}
              {project.deployment ? ` · ${project.deployment}` : ""}
              {project.size ? ` · ${project.size}` : ""}
            </p>
          )}
        </div>
        <div className="flex shrink-0 gap-1.5">
          {(["critical", "high", "medium", "low"] as const).map((sev) => {
            const count = sorted.filter((a) => a.risk.severity === sev).length;
            if (count === 0) return null;
            return (
              <span
                key={sev}
                className={cn(
                  "rounded-full px-2 py-0.5 text-xs font-semibold",
                  SEVERITY_STYLES[sev],
                )}
              >
                {count} {sev}
              </span>
            );
          })}
        </div>
      </div>

      {/* Accordion items sorted by severity */}
      <div className="space-y-2">
        {sorted.map((assessment) => (
          <AccordionItem key={assessment.risk.id} assessment={assessment} />
        ))}
      </div>
    </div>
  );
}
