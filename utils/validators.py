def validate_requirement(req):
    allowed = ["trend", "comparison", "distribution", "summary"]

    if req.intent not in allowed:
        req.intent = "summary"

    if not req.kpis:
        req.kpis = ["sales"]

    return req