from typing import Dict, Any

FEATURE_ORDER = [
    'InscClaimAmtReimbursed', 'DeductibleAmtPaid', 'ClmProcedureCode_1',
    'ClmProcedureCode_2', 'ClmProcedureCode_3', 'ClmProcedureCode_4',
    'ClmProcedureCode_5', 'ClmProcedureCode_6', 'Gender', 'Race', 'State',
    'County', 'NoOfMonths_PartACov', 'NoOfMonths_PartBCov',
    'ChronicCond_Alzheimer', 'ChronicCond_Heartfailure',
    'ChronicCond_KidneyDisease', 'ChronicCond_Cancer',
    'ChronicCond_ObstrPulmonary', 'ChronicCond_Depression',
    'ChronicCond_Diabetes', 'ChronicCond_IschemicHeart',
    'ChronicCond_Osteoporasis', 'ChronicCond_rheumatoidarthritis',
    'ChronicCond_stroke', 'IPAnnualReimbursementAmt',
    'IPAnnualDeductibleAmt', 'OPAnnualReimbursementAmt',
    'OPAnnualDeductibleAmt', 'Age', 'LengthOfStay', 'TotalClaims',
    'ChronicConditionCount'
]

def prepare_features(payload: Dict[str, Any]) -> Dict[str, Any]:
    features = {}
    for col in FEATURE_ORDER:
        # Fill missing with 0 for numeric, "" for categorical
        val = payload.get(col)
        if val is None:
            if col in ['Gender', 'Race', 'State', 'County',
                       'ClmProcedureCode_1', 'ClmProcedureCode_2',
                       'ClmProcedureCode_3', 'ClmProcedureCode_4',
                       'ClmProcedureCode_5', 'ClmProcedureCode_6']:
                val = ""
            else:
                val = 0
        features[col] = val
    return features