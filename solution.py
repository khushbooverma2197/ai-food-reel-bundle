psi_value = 0.21
def classify_drift(psi_value):
   if psi_value < 0.1:
       return "No significant drift"
   elif psi_value < 0.2:
       return "Monitor but likely acceptable"
   else:
       return "Significant drift detected, action recommended"
result = classify_drift(psi_value)
print(result)
# Since PSI is above 0.2, the model should be considered for retraining.
