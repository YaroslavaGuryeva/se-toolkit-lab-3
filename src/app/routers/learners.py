"""Router for learner endpoints."""

from fastapi import APIRouter

from datetime import datetime

from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from app.database import get_session
from app.db.learners import read_learners, create_learner
from app.models.learner import Learner, LearnerCreate

router = APIRouter()

# ===
# PART A: GET endpoint
# ===

# UNCOMMENT AND FILL IN

@router.get("/", response_model=list[Learner])
async def get_learners(
    enrolled_after: datetime | None = None,
    session: AsyncSession = Depends(get_session),
):
    """Get all learners sorted by the time of enrolling"""
    return await read_learners(session, enrolled_after)

Reference:
items GET -> reads from items table, returns list[Item]
learners GET -> reads from learners table, returns list[Learner]
Query parameter: ?enrolled_after= filters learners by enrolled_at date

# ===
# PART B: POST endpoint
# ===

# UNCOMMENT AND FILL IN
#
# @router.<method>("/<resource_name>", response_model=<resource_schema>, status_code=<status_code>)
# async def <function_name>(
#     <param_name>: <request_schema>,
#     session: AsyncSession = Depends(get_session),
# ):
#     """<docstring>"""
#     return await <db_create_function>(session, name=<param_name>.name, email=<param_name>.email)
#
# Reference:
# items POST -> creates a row in items table, accepts ItemCreate, returns Item with status 201
# learners POST -> creates a row in learners table, accepts LearnerCreate, returns Learner with status 201
