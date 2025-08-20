# app/schemas.py
from pydantic import BaseModel, model_validator, Field
from typing import Optional, Annotated
from datetime import date, datetime

class PredictInput(BaseModel):
    # Core numeric/categorical fields (based on your sample)
    Gender: Annotated[int, Field(..., ge=0, le=2, description="Encoded gender (0=Unknown, 1=Male, 2=Female)")]
    Race: Annotated[int, Field(..., ge=0, description="Encoded race")]
    State: Annotated[int, Field(..., ge=0, description="Encoded state id")]
    County: Annotated[int, Field(..., ge=0, description="Encoded county id")]

    InscClaimAmtReimbursed: Annotated[float, Field(..., ge=0, description="Insurance claim amount reimbursed")]
    IPAnnualDeductibleAmt: Annotated[float, Field(..., ge=0, description="Inpatient annual deductible amount")]
    OPAnnualDeductibleAmt: Annotated[float, Field(..., ge=0, description="Outpatient annual deductible amount")]
    IPAnnualReimbursementAmt: Annotated[float, Field(..., ge=0, description="Inpatient annual reimbursement amount")]
    OPAnnualReimbursementAmt: Annotated[float, Field(..., ge=0, description="Outpatient annual reimbursement amount")]
    OPAnnualDeductibleAmt: Annotated[float, Field(..., ge=0, description="Outpatient annual deductible amount (duplicate field, check data model)")]
    DeductibleAmtPaid: Annotated[float, Field(..., ge=0, description="Deductible amount paid")]

    NoOfMonths_PartACov: Annotated[int, Field(..., ge=0, le=24, description="Number of months with Part A coverage")]
    NoOfMonths_PartBCov: Annotated[int, Field(..., ge=0, le=24, description="Number of months with Part B coverage")]

    TotalClaims: Annotated[int, Field(..., ge=0, description="Total number of claims")]
    ChronicConditionCount: Annotated[int, Field(..., ge=0, description="Count of chronic conditions")]

    # Chronic condition flags (0/1/2 in sample) — keep generic
    ChronicCond_Alzheimer: Annotated[int, Field(..., ge=0, description="Chronic condition: Alzheimer")]
    ChronicCond_KidneyDisease: Annotated[int, Field(..., ge=0, description="Chronic condition: Kidney Disease")]
    ChronicCond_Osteoporasis: Annotated[int, Field(..., ge=0, description="Chronic condition: Osteoporosis")]
    ChronicCond_stroke: Annotated[int, Field(..., ge=0, description="Chronic condition: Stroke")]
    ChronicCond_Cancer: Annotated[int, Field(..., ge=0, description="Chronic condition: Cancer")]
    ChronicCond_Diabetes: Annotated[int, Field(..., ge=0, description="Chronic condition: Diabetes")]
    ChronicCond_rheumatoidarthritis: Annotated[int, Field(..., ge=0, description="Chronic condition: Rheumatoid Arthritis")]
    ChronicCond_Heartfailure: Annotated[int, Field(..., ge=0, description="Chronic condition: Heart Failure")]
    ChronicCond_ObstrPulmonary: Annotated[int, Field(..., ge=0, description="Chronic condition: Obstructive Pulmonary Disease")]
    ChronicCond_Depression: Annotated[int, Field(..., ge=0, description="Chronic condition: Depression")]
    ChronicCond_IschemicHeart: Annotated[int, Field(..., ge=0, description="Chronic condition: Ischemic Heart Disease")]

    # Procedure codes
    ClmProcedureCode_1: Annotated[int, Field(..., ge=0, description="Claim procedure code 1")]
    ClmProcedureCode_2: Annotated[int, Field(..., ge=0, description="Claim procedure code 2")]
    ClmProcedureCode_3: Annotated[int, Field(..., ge=0, description="Claim procedure code 3")]
    ClmProcedureCode_4: Annotated[int, Field(..., ge=0, description="Claim procedure code 4")]
    ClmProcedureCode_5: Annotated[int, Field(..., ge=0, description="Claim procedure code 5")]
    ClmProcedureCode_6: Annotated[int, Field(..., ge=0, description="Claim procedure code 6")]

    Age: Annotated[int, Field(..., ge=0, le=130, description="Age in years")]
    LengthOfStay: Annotated[int, Field(..., ge=0, description="Length of stay in days")]

class PredictionResponse(BaseModel):
    fraudulent: bool
    probability: float = Field(..., ge=0.0, le=1.0)
    model_version: str
    message: Optional[str] = None
