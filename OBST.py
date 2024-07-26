import math
from datetime import datetime, timedelta

def calculate_edd(lmp):
    # Convert LMP string to a datetime object
    lmp_date = datetime.strptime(lmp, "%Y-%m-%d")
    # Add 280 days (40 weeks) to LMP to get EDD
    edd = lmp_date + timedelta(days=280)
    return edd.strftime("%Y-%m-%d")

def calculate_ga(lmp, today=None):
    # Convert LMP to datetime object
    lmp_date = datetime.strptime(lmp, "%Y-%m-%d")
    # Use today's date if not provided
    if today is None:
        today = datetime.now()
    else:
        today = datetime.strptime(today, "%Y-%m-%d")
    # Calculate the difference in weeks
    gestational_age = (today - lmp_date).days // 7
    return gestational_age

def calculate_bishop_score(dilation, effacement, station, consistency, position):
    # Define scores for consistency and position
    consistency_scores = {"firm": 0, "medium": 1, "soft": 2}
    position_scores = {"posterior": 0, "mid": 1, "anterior": 2}

    # Calculate the total Bishop Score
    score = (dilation + effacement + station +
             consistency_scores.get(consistency, 0) +
             position_scores.get(position, 0))

    return score

def calculate_afi(quadrant1, quadrant2, quadrant3, quadrant4):
    # Sum of the deepest pocket measurements from all four quadrants
    afi = quadrant1 + quadrant2 + quadrant3 + quadrant4
    return afi

def estimate_fetal_weight(bpd, hc, ac, fl):
    # Hadlock's formula to estimate fetal weight in grams
    log10_weight = 1.3596 + (0.00061 * bpd) + (0.0424 * ac) + (0.174 * fl)
    weight = math.pow(10, log10_weight)
    return weight

def calculate_bmi(weight, height):
    # BMI calculation
    bmi = weight / (height * height)
    return bmi

def weight_gain_recommendation(pre_pregnancy_bmi):
    if pre_pregnancy_bmi < 18.5:
        return "28-40 lbs (12.7-18.1 kg)"
    elif 18.5 <= pre_pregnancy_bmi < 24.9:
        return "25-35 lbs (11.3-15.9 kg)"
    elif 25 <= pre_pregnancy_bmi < 29.9:
        return "15-25 lbs (6.8-11.3 kg)"
    else:
        return "11-20 lbs (5-9.1 kg)"

def gravida_parity(gravidarum, full_term, preterm, abortions, living):
    return f"G{gravidarum}P{full_term}{preterm}{abortions}{living}"

def main():
    print("Welcome to the Obstetrics Calculations Program!\n")

    # Estimated Due Date (EDD)
    lmp = input("Enter Last Menstrual Period (YYYY-MM-DD): ")
    edd = calculate_edd(lmp)
    print(f"Estimated Due Date: {edd}\n")

    # Gestational Age (GA)
    today = input("Enter today's date (YYYY-MM-DD) or leave blank for current date: ")
    if not today:
        today = None
    ga = calculate_ga(lmp, today)
    print(f"Gestational Age: {ga} weeks\n")

    # Bishop Score
    print("Enter the following details for Bishop Score calculation:")
    dilation = int(input("Cervical dilation (cm): "))
    effacement = int(input("Cervical effacement (%): "))
    station = int(input("Fetal station (-3 to +3): "))
    consistency = input("Cervical consistency (firm, medium, soft): ").lower()
    position = input("Cervical position (posterior, mid, anterior): ").lower()
    bishop_score = calculate_bishop_score(dilation, effacement, station, consistency, position)
    print(f"Bishop Score: {bishop_score}\n")

    # Amniotic Fluid Index (AFI)
    print("Enter the depths of the four quadrants for AFI calculation:")
    q1 = float(input("Depth of quadrant 1 (cm): "))
    q2 = float(input("Depth of quadrant 2 (cm): "))
    q3 = float(input("Depth of quadrant 3 (cm): "))
    q4 = float(input("Depth of quadrant 4 (cm): "))
    afi = calculate_afi(q1, q2, q3, q4)
    print(f"Amniotic Fluid Index: {afi} cm\n")

    # Fetal Weight Estimation
    print("Enter the following ultrasound measurements for fetal weight estimation:")
    bpd = float(input("Biparietal diameter (cm): "))
    hc = float(input("Head circumference (cm): "))
    ac = float(input("Abdominal circumference (cm): "))
    fl = float(input("Femur length (cm): "))
    fetal_weight = estimate_fetal_weight(bpd, hc, ac, fl)
    print(f"Estimated Fetal Weight: {fetal_weight:.2f} grams\n")

    # BMI Calculation
    weight_kg = float(input("Enter weight (kg): "))
    height_m = float(input("Enter height (m): "))
    bmi = calculate_bmi(weight_kg, height_m)
    print(f"Body Mass Index: {bmi:.2f}\n")

    # Maternal Weight Gain Recommendation
    pre_pregnancy_bmi = float(input("Enter pre-pregnancy BMI: "))
    recommended_gain = weight_gain_recommendation(pre_pregnancy_bmi)
    print(f"Recommended Weight Gain: {recommended_gain}\n")

    # Gravida and Parity
    print("Enter the following details for Gravida and Parity:")
    gravidarum = int(input("Number of times pregnant (Gravidarum): "))
    full_term = int(input("Number of full-term pregnancies: "))
    preterm = int(input("Number of preterm pregnancies: "))
    abortions = int(input("Number of abortions or miscarriages: "))
    living = int(input("Number of living children: "))
    gp = gravida_parity(gravidarum, full_term, preterm, abortions, living)
    print(f"Gravida and Parity: {gp}\n")

if __name__ == "__main__":
    main()
