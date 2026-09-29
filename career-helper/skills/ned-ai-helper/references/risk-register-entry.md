# AI Risk Register Entry Template

## Board-Level AI Risk Documentation

Use this format to document AI use cases for board risk oversight.

---

## Risk Register Fields

| Field | Description | Example |
|:------|:------------|:--------|
| **Ref** | Unique identifier | AI-001 |
| **AI Use Case** | What the AI does | Customer service chatbot |
| **Business Function** | Department/area | Customer Experience |
| **Impact Level** | I-IV classification | II - Moderate |
| **Delegation Level** | Human-AI decision authority | AI Decides, Human Override |
| **HITL Requirement** | Specific oversight mechanism | Sentiment triggers human handoff |
| **Risk Category** | Type of risk | Reputational, Operational |
| **Inherent Risk** | Risk before controls | Medium |
| **Controls** | Mitigation measures | Real-time monitoring, daily review |
| **Residual Risk** | Risk after controls | Low |
| **Risk Owner** | Accountable individual | Head of CX |
| **Review Frequency** | Oversight cadence | Quarterly |
| **Escalation Trigger** | What prompts board attention | Complaint rate >2x baseline |
| **Last Review** | Date of last assessment | DD/MM/YYYY |
| **Next Review** | Date of next assessment | DD/MM/YYYY |

---

## Sample Entry

| Ref | AI-001 |
|:----|:-------|
| **AI Use Case** | Customer service chatbot |
| **Business Function** | Customer Experience |
| **Impact Level** | II - Moderate |
| **Delegation Level** | AI Decides, Human Override |
| **HITL Requirement** | Sentiment detection routes negative interactions to human agent within 30 seconds |
| **Risk Category** | Reputational, Operational |
| **Inherent Risk** | Medium |
| **Controls** | Real-time sentiment monitoring, daily escalation review, customer feedback loop, weekly quality sampling |
| **Residual Risk** | Low |
| **Risk Owner** | Head of Customer Experience |
| **Review Frequency** | Quarterly |
| **Escalation Trigger** | Complaint rate increases >100% from baseline, or single viral negative incident |
| **Last Review** | 15/11/2025 |
| **Next Review** | 15/02/2026 |

---

## Impact Level Key

| Level | Description | Characteristics |
|:------|:------------|:----------------|
| **I - Minimal** | Little/no impact | Reversible, brief, internal efficiency |
| **II - Moderate** | Limited impact | Readily reversible, short-term effects |
| **III - High** | Significant impact | Difficult to reverse, affects rights/interests |
| **IV - Very High** | Severe impact | Potentially irreversible, fundamental rights |

---

## Delegation Level Key

| Level | Human Role |
|:------|:-----------|
| **Human Only** | Full decision authority |
| **AI Informs** | Human decides with AI input |
| **AI Recommends** | Human approves or modifies |
| **AI Decides, Human Reviews** | Monitoring and exception handling |
| **AI Decides, Human Override** | Exception-based intervention |
| **Full Autonomy** | None (monitoring only) |

---

## Governance Requirements by Impact Level

| Requirement | Level I | Level II | Level III | Level IV |
|:------------|:--------|:---------|:----------|:---------|
| Impact Assessment | Optional | Required | + External review | + Independent audit |
| Human Oversight | None | Periodic | Specific intervention | Human final decision |
| Transparency | Internal docs | Published summary | Full disclosure | Real-time explainability |
| Training | General awareness | Role-specific | Certified competency | Ongoing accreditation |

---

## Blank Template

```markdown
| Ref | AI-XXX |
|:----|:-------|
| **AI Use Case** | |
| **Business Function** | |
| **Impact Level** | |
| **Delegation Level** | |
| **HITL Requirement** | |
| **Risk Category** | |
| **Inherent Risk** | |
| **Controls** | |
| **Residual Risk** | |
| **Risk Owner** | |
| **Review Frequency** | |
| **Escalation Trigger** | |
| **Last Review** | |
| **Next Review** | |
```

---

**Prosper AI Consulting**
Pragmatic change, AI and implementation support.
Fractional Strategy, CAIO, CTO and CIO services.

Adrian Tripp | Partner
adrian.tripp@prosperconsulting.ai

prosperconsulting.ai

---
