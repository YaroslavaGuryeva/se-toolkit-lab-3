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


@router.post("/", response_model=Learner, status_code=201)
async def post_learner(
    body: LearnerCreate,
    session: AsyncSession = Depends(get_session),
):
    """Create a new learner."""
    return await create_learner(session, name=body.name, email=body.email)
