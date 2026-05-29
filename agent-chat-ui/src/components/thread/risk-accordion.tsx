"use client";

import { useMemo, useState } from "react";
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

interface RawRiskSchema {
  id?: string;
  risk_id?: string;
  title?: string;
  risk_title?: string;
  name?: string;
  category?: string;
  domain?: string;
  risk_domain?: string;
  description?: string;
  risk_description?: string;
  riskDescription?: string;
  severity?: string;
  risk_level?: string;
  riskLevel?: string;
  level?: string;
  source?: unknown;
}

interface RiskAssessment {
  risk: Risk;
  relevance_reason: string;
  mitigation: string;
  regulatory_refs: string[];
  wiki_refs?: string[];
  source_quote?: string;
}

interface RiskAccordionProps {
  project: Record<string, string>;
  assessments: RiskAssessment[];
}

type RiskAccordionInput = Partial<RiskAccordionProps> & {
  data?: unknown;
  result?: unknown;
  showPayload?: boolean;
  project_profile?: Record<string, string>;
  profile?: Record<string, string>;
  risk_assessments?: unknown[];
  risks?: unknown[];
  items?: unknown[];
};

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

function asRecord(value: unknown): Record<string, unknown> {
  return value && typeof value === "object" && !Array.isArray(value)
    ? (value as Record<string, unknown>)
    : {};
}

function firstRecord(...values: unknown[]): Record<string, unknown> {
  for (const value of values) {
    const record = asRecord(value);
    if (Object.keys(record).length > 0) {
      return record;
    }
  }
  return {};
}

function asString(value: unknown, fallback = ""): string {
  return typeof value === "string" ? value : fallback;
}

function asStringArray(value: unknown): string[] {
  if (Array.isArray(value)) {
    return value
      .map((item) => (typeof item === "string" ? item : null))
      .filter((item): item is string => item !== null);
  }
  if (typeof value === "string" && value.trim()) {
    return [value];
  }
  return [];
}

function normalizeSeverity(value: unknown): Risk["severity"] {
  const severity = asString(value).toLowerCase();
  if (
    severity === "critical" ||
    severity === "high" ||
    severity === "medium" ||
    severity === "low"
  ) {
    return severity;
  }
  return "medium";
}

function normalizeAssessment(value: unknown, index: number): RiskAssessment {
  const assessment = asRecord(value);
  const risk = firstRecord(assessment.risk, assessment) as RawRiskSchema;
  const source = firstRecord(assessment.source, risk.source);
  const regulatoryRefs = asStringArray(
    assessment.regulatory_refs ??
      assessment.regulatoryRefs ??
      assessment.regulatory_references ??
      assessment.regulations,
  );
  const sourceRefs = asStringArray(
    source.source_id ?? source.url ?? assessment.evidence_strength,
  );

  return {
    risk: {
      id: asString(risk.id ?? risk.risk_id ?? assessment.id, `risk-${index}`),
      title: asString(
        risk.title ??
          risk.risk_title ??
          assessment.title ??
          assessment.risk_title ??
          assessment.riskName ??
          assessment.name,
        "Untitled risk",
      ),
      category: asString(
        risk.category ??
          risk.risk_domain ??
          assessment.category ??
          assessment.domain ??
          assessment.risk_domain,
        "General",
      ),
      description: asString(
        risk.description ??
          assessment.description ??
          assessment.risk_description ??
          assessment.riskDescription,
      ),
      severity: normalizeSeverity(
        risk.severity ??
          assessment.severity ??
          assessment.risk_level ??
          assessment.riskLevel ??
          assessment.level,
      ),
    },
    relevance_reason: asString(
      assessment.relevance_reason ??
        assessment.relevanceReason ??
        assessment.why_it_applies ??
        assessment.whyItApplies ??
        assessment.reason,
    ),
    mitigation: asString(
      assessment.mitigation ??
        assessment.mitigation_strategy ??
        assessment.mitigationStrategy ??
        assessment.recommendation,
    ),
    regulatory_refs: [...regulatoryRefs, ...sourceRefs],
    wiki_refs: asStringArray(
      assessment.wiki_refs ??
        assessment.wikiRefs ??
        assessment.source_refs ??
        assessment.sourceRefs ??
        assessment.sources,
    ),
    source_quote: asString(source.quote),
  };
}

function normalizeProps(props: RiskAccordionInput): RiskAccordionProps {
  return normalizePayload(extractPayload(props));
}

function extractPayload(props: RiskAccordionInput): Record<string, unknown> {
  const outer = asRecord(props);
  const data = asRecord(props.data);
  const result = asRecord(props.result);
  return firstRecord(data, result, outer);
}

function normalizePayload(source: Record<string, unknown>): RiskAccordionProps {
  const project = firstRecord(
    source.project,
    source.project_profile,
    source.profile,
  );
  const rawAssessments =
    source.assessments ??
    source.risk_assessments ??
    source.risks ??
    source.items;
  const assessments = Array.isArray(rawAssessments) ? rawAssessments : [];

  return {
    project: Object.fromEntries(
      Object.entries(project).map(([key, value]) => [key, String(value)]),
    ),
    assessments: assessments.map(normalizeAssessment),
  };
}

function toCanonicalPayload(payload: RiskAccordionProps): RiskAccordionProps {
  return {
    project: payload.project,
    assessments: payload.assessments.map((assessment) => ({
      risk: {
        id: assessment.risk.id,
        title: assessment.risk.title,
        category: assessment.risk.category,
        description: assessment.risk.description,
        severity: assessment.risk.severity,
      },
      relevance_reason: assessment.relevance_reason,
      mitigation: assessment.mitigation,
      regulatory_refs: assessment.regulatory_refs,
      wiki_refs: assessment.wiki_refs ?? [],
    })),
  };
}

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
  const [open, setOpen] = useState(true);
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

          {assessment.source_quote && (
            <div>
              <p className="text-muted-foreground mb-1 text-xs font-semibold uppercase tracking-wide">
                Source excerpt
              </p>
              <p className="text-muted-foreground">{assessment.source_quote}</p>
            </div>
          )}

          {assessment.wiki_refs && assessment.wiki_refs.length > 0 && (
            <div>
              <p className="text-muted-foreground mb-1.5 text-xs font-semibold uppercase tracking-wide">
                Wiki sources
              </p>
              <div className="flex flex-wrap gap-1.5">
                {assessment.wiki_refs.map((ref) => (
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

export function RiskAccordion(props: RiskAccordionInput) {
  const initialPayload = useMemo(
    () => toCanonicalPayload(normalizePayload(extractPayload(props))),
    [props],
  );
  const initialPayloadText = useMemo(
    () => JSON.stringify(initialPayload, null, 2),
    [initialPayload],
  );
  const [payloadText, setPayloadText] = useState(initialPayloadText);

  const { payload, error } = useMemo(() => {
    try {
      return {
        payload: JSON.parse(payloadText) as Record<string, unknown>,
        error: "",
      };
    } catch (err) {
      return {
        payload: initialPayload as unknown as Record<string, unknown>,
        error: err instanceof Error ? err.message : "Invalid JSON",
      };
    }
  }, [initialPayload, payloadText]);

  const { project, assessments } = normalizePayload(payload);
  const sorted = [...assessments].sort(
    (a, b) =>
      (SEVERITY_ORDER[a.risk.severity] ?? 9) -
      (SEVERITY_ORDER[b.risk.severity] ?? 9),
  );

  return (
    <div className="w-full space-y-3">
      {props.showPayload !== false && (
        <div className="space-y-3">
          <div className="flex items-center justify-between gap-3">
            <h3 className="text-sm font-semibold">Risk Accordion Payload</h3>
            <button
              type="button"
              onClick={() => setPayloadText(initialPayloadText)}
              className="border-border bg-background hover:bg-muted h-8 rounded-md border px-3 text-xs font-medium"
            >
              Reset
            </button>
          </div>
          <textarea
            value={payloadText}
            onChange={(event) => setPayloadText(event.target.value)}
            spellCheck={false}
            className="border-border bg-background text-foreground min-h-72 w-full resize-y rounded-md border p-3 font-mono text-xs leading-5 outline-none focus:ring-2 focus:ring-ring"
          />
          {error && (
            <p className="rounded-md border border-red-200 bg-red-50 px-3 py-2 text-xs text-red-700">
              {error}
            </p>
          )}
        </div>
      )}

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
