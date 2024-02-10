# Define a list of tuples containing the names of metrics and the corresponding input values
metrics = [
    ('CPU', 79),
    ('RAM memory', 65),
    ('response time', 350)
]
alertas = []
# TODO: Define a function to monitor the metrics and generate alerts, if necessary
def monitor_and_alert(metrics):
    for nome, valor in metrics:
      if nome == "CPU" and valor >= 80:
        alertas.append("Alert: High CPU usage detected  ({})".format(valor))
      elif nome == "RAM memory" and valor >= 70:
        alertas.append("Alert: High RAM memory usage detected ({})".format(valor))
      elif nome == "response time" and valor >= 300:
        alertas.append("Alert: Application response time above the limit ({}%)".format(valor))
      
    if not alertas:
      return "No anomalies detected"
        
      

    # TODO: Iterate over each metric in the provided metrics list and check if any alerts were generated

    return '\n'.join(alertas)

print(monitor_and_alert(metrics))