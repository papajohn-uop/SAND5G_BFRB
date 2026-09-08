import random
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field


class CheckCVERequest(BaseModel):
    cve: str = Field(..., description="CVE identifier to check")


class OperatorResult(BaseModel):
    operator: str
    sboms_checked: int
    vulnerable_sboms: int


class CheckCVEResponse(BaseModel):
    cve: str
    operators_checked: int
    sboms_checked: int
    vulnerable_sboms: int
    operators: List[OperatorResult]


app = FastAPI(title="SAND5G BRFB PoC API", version="0.1.0")


def build_random_response(cve: str) -> CheckCVEResponse:
    operators = ["Operator A", "Operator B", "Operator C", "Operator D", "Operator E"]
    selected_operators = random.sample(operators, random.randint(2, 5))

    operator_results: List[OperatorResult] = []
    total_sboms = 0
    total_vulnerable = 0

    for operator in selected_operators:
        sboms = random.randint(10, 30)
        vulnerable = 0
        for _ in range(sboms):
            if random.random() < 0.05:
                vulnerable += 1

        total_sboms += sboms
        total_vulnerable += vulnerable
        operator_results.append(
            OperatorResult(
                operator=operator,
                sboms_checked=sboms,
                vulnerable_sboms=vulnerable,
            )
        )

    return CheckCVEResponse(
        cve=cve,
        operators_checked=len(selected_operators),
        sboms_checked=total_sboms,
        vulnerable_sboms=total_vulnerable,
        operators=operator_results,
    )


@app.get("/health")
def healthcheck() -> dict:
    return {"status": "ok"}


@app.post("/check-cve", response_model=CheckCVEResponse)
def check_cve(payload: CheckCVERequest) -> CheckCVEResponse:
    return build_random_response(payload.cve)
