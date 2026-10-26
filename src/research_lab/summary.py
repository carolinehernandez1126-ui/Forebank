"""Detailed trading memo from the frozen research, reviews and deterministic gate."""

from __future__ import annotations

from .io import digest


def trading_summary(proposal, reviews, decision):
    r = proposal.research
    risk = decision["risk"]
    b = risk["budget"]
    lines = [
        f"# Resumen detallado de trading: {proposal.plan_id}",
        "",
        f"**Decisión del gate:** {decision['status']}",
        f"**Activo / dirección:** {proposal.symbol} / compra spot",
        f"**Horizonte:** {r.horizon}",
        f"**Evaluado:** {decision['checked_at']}",
        f"**Válido hasta:** {decision['expires_at']}",
        "",
        "## Conclusión y tesis",
        "",
        proposal.thesis,
        "",
        "## Alcance y cierre de la investigación",
        "",
        r.scope,
        "",
        f"Corte de investigación: {r.cutoff_at.isoformat()}",
        "",
        f"Razón para cerrar la búsqueda: {r.stopping_reason}",
        "",
        f"Suficiencia de la información: {r.sufficiency_rationale}",
        "",
        "La información se considera suficiente para decidir: "
        + ("sí" if r.decision_with_available_information else "no"),
        "",
        "## Análisis técnico",
        "",
        proposal.technical_summary,
        "",
        "## Análisis fundamental",
        "",
        proposal.fundamental_summary,
        "",
        "## Análisis estadístico y validación",
        "",
        proposal.statistical_summary,
        "",
        "## Congruencia de la estrategia",
        "",
        r.strategy_coherence,
        "",
        "### Reglas de ejecución",
        "",
        r.execution_rules,
        "",
        "### Alternativas consideradas",
        "",
    ]
    lines += [f"- {alternative}" for alternative in r.alternatives_considered]
    lines += [
        "",
        "### Escenarios y riesgos",
        "",
        r.scenario_analysis,
        "",
        "### Invalidación",
        "",
        proposal.invalidation,
        "",
        "### Seguimiento y reapertura de la investigación",
        "",
        r.monitoring_plan,
        "",
        "## Información ausente e incertidumbre aceptada",
        "",
    ]
    if not r.gaps:
        lines += [
            "No se declararon faltantes identificados. Esto no implica información completa.",
            "",
        ]
    for index, gap in enumerate(r.gaps, 1):
        lines += [
            f"### Faltante {index}: {gap.severity}",
            "",
            gap.description,
            "",
            f"Impacto: {gap.impact}",
            "",
            f"Mitigación: {gap.mitigation}",
            "",
            "Aceptado expresamente: " + ("sí" if gap.accepted else "no"),
            "",
        ]
    lines += [
        "## Plan y presupuesto de riesgo",
        "",
        "| Concepto | Valor |",
        "|---|---:|",
        f"| Entrada | {proposal.entry:g} |",
        f"| Stop | {proposal.stop:g} |",
        f"| Objetivo | {proposal.target:g} |",
        f"| Cantidad | {proposal.quantity:g} |",
        f"| Riesgo monetario estimado, con costos | {risk['risk_amount']:.2f} |",
        f"| RR neto | {risk['net_reward_risk']:.3f} |",
        f"| Cantidad máxima calculada | {b['max_quantity']:g} |",
        f"| Presupuesto disponible para riesgo nuevo | {b['available_new_risk']:.2f} |",
        f"| Riesgo de posiciones y órdenes pendientes | {b['open_and_pending_stop_risk']:.2f} |",
        f"| Floor MDL operativo ({b['operational_daily_loss_fraction']:.1%}) | {b['daily_floor']:.2f} |",
        f"| Floor MDL máximo ({b['hard_daily_loss_fraction']:.1%}) | {b['hard_daily_floor']:.2f} |",
        f"| Reserva adicional | {b['daily_reserve']:.2f} |",
        f"| Base para drawdown | {b['drawdown_reference']:.2f} |",
        f"| Floor MDD operativo ({b['operational_drawdown_fraction']:.1%}) | {b['drawdown_floor']:.2f} |",
        f"| Floor MDD máximo ({b['hard_drawdown_fraction']:.1%}) | {b['hard_drawdown_floor']:.2f} |",
        "",
        "Los importes usan la moneda de la cuenta validada por el gate. "
        "Este documento puede contener datos privados: sanear antes de publicar.",
        "",
        "## Revisiones independientes",
        "",
    ]
    for review in reviews:
        lines += [
            f"### {review.reviewer} / {review.model}",
            "",
            f"Veredicto: {review.verdict}; fecha: {review.reviewed_at.isoformat()}",
            "",
            review.rationale,
            "",
            f"Acepta incertidumbre: {review.uncertainty_accepted}; "
            f"confirma congruencia: {review.strategy_coherence_confirmed}",
            "",
            "Fuentes verificadas:",
            "",
        ]
        lines += [f"- {url}" for url in review.independently_checked_sources]
        lines += ["", "Blockers:", ""] + [
            f"- {x}" for x in review.blockers or ["Ninguno declarado"]
        ]
        lines.append("")
    lines += ["## Evidencias y procedencia", ""]
    for evidence in proposal.evidence:
        lines += [
            f"- [{evidence.title}]({evidence.url}) — {evidence.dimension}; "
            f"consulta: {evidence.retrieved_at.isoformat()}; "
            f"publicación: {evidence.published_at.isoformat() if evidence.published_at else 'no disponible'}. "
            f"Afirmación: {evidence.claim}"
        ]
    lines += ["", "## Limitaciones", ""] + [f"- {x}" for x in proposal.limitations]
    lines += ["", "## Motivos del gate", ""]
    lines += [f"- {x}" for x in decision["reasons"] or ["Sin bloqueos detectados al evaluar"]]
    lines += [
        "",
        "## Versiones revisadas",
        "",
        f"- Propuesta: `{digest(proposal)}`",
        f"- Dataset: `{proposal.dataset_sha256}`",
        f"- Cuenta: `{proposal.account_sha256}`",
        f"- Política: `{proposal.policy_sha256}`",
        "",
        "Documento generado desde el análisis declarado por las IAs y el gate. "
        "La extensión del texto no demuestra calidad ni rentabilidad. "
        "La ejecución sigue siendo manual y requiere vigencia.",
        "",
    ]
    return "\n".join(lines)
