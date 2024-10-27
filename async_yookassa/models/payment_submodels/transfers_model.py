from typing import Any

from pydantic import BaseModel, Field

from async_yookassa.models.payment_submodels.amount_model import Amount


class TransferBase(BaseModel):
    account_id: str
    amount: Amount
    description: str | None = Field(max_length=128, default=None)
    metadata: dict[str, Any] | None = None


class Transfer(TransferBase):
    platform_fee_amount: Amount


class TransferResponse(TransferBase):
    status: str
    platform_fee_amount: Amount | None = None
