import pandas as pd

def analyze_cloud_data(data):

    recommendations = []

    for index, row in data.iterrows():

        cpu = row["CPU_Usage"]
        memory = row["Memory_Usage"]

        if cpu < 20 and memory < 20:
            recommendation = "Underutilized - Reduce resources or shut down"

        elif cpu > 80 or memory > 80:
            recommendation = "Overloaded - Scale up resources"

        elif 20 <= cpu <= 40 and 20 <= memory <= 40:
            recommendation = "Light Usage - Optimization possible"

        elif 40 < cpu <= 80 and 40 < memory <= 80:
            recommendation = "Normal Usage - No action needed"

        else:
            recommendation = "Needs Review"

        recommendations.append(recommendation)

    data["Recommendation"] = recommendations

    return data