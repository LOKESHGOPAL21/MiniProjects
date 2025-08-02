def get_retention_strategy(churn_prob,customer_data):
  suggestions = []

  # cutomer with high churn probability
  if(churn_prob>0.7):
    suggestions.append("Offer a X % discount on the next billing cycle.")
    suggestions.append("Schedule a follow up call to address concerns")
  
  # medium churn probabilty
  elif churn_prob>0.3:
    suggestions.append("Send a personalized email with loyalty rewards.")
    suggestions.append("Offer a free upgrade to a premium feature.")

  if customer_data.get('tenure', 0) < 12:
      suggestions.append("Provide a welcome package to new customers.")
  if customer_data.get('Contract') == 0:  # Month-to-month contract
      suggestions.append("Promote a 1-year contract with a discount.")
    
  return suggestions if suggestions else ["Monitor customer engagement."]


customer = {'tenure': 6, 'Contract': 0, 'MonthlyCharges': 80}
churn_prob = 0.75
strategies = get_retention_strategy(churn_prob, customer)
print("Retention Strategies:", strategies)