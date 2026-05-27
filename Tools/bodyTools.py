from langchain.tools import tool
import math

@tool
def bmiCalculator(input_str: str) -> str:
    """
    Calculates BMI and returns score + category.

    Input format:
    "height_m=1.75, weight_kg=85.0"
    """

    try:
        parts = {}

        for part in input_str.replace(" ", "").split(","):
            key, value = part.split("=")
            parts[key.strip()] = float(value.strip())

        height_m = parts.get("height_m")
        weight_kg = parts.get("weight_kg")

        if not height_m or not weight_kg:
            return "error=missing_height_or_weight"

        score = weight_kg / (height_m ** 2)

        if score < 18.5:
            category = "Underweight"
        elif score < 25:
            category = "Normal weight"
        elif score < 30:
            category = "Overweight"
        else:
            category = "Obese"

        return f"bmi={score:.2f}, category={category}"

    except Exception as e:
        return f"error={str(e)}"


@tool
def waistToHeightRatio(input_str: str) -> str:
    """
    Input:
    "waist_cm=80, height_cm=175"
    """

    try:
        parts = {}

        for part in input_str.replace(" ", "").split(","):
            key, value = part.split("=")
            parts[key.strip()] = float(value.strip())

        waist = parts.get("waist_cm")
        height = parts.get("height_cm")

        if not waist or not height:
            return "error=missing_values"

        ratio = waist / height

        if ratio < 0.4:
            category = "Underweight"
        elif ratio < 0.5:
            category = "Healthy"
        elif ratio < 0.6:
            category = "Overweight"
        else:
            category = "Obese"

        return f"ratio={ratio:.2f}, category={category}"

    except Exception as e:
        return f"error={str(e)}"


@tool
def waistToHipRatio(input_str: str) -> str:
    """
    Input:
    "waist_cm=85, hip_cm=100"
    """

    try:
        parts = {}

        for part in input_str.replace(" ", "").split(","):
            key, value = part.split("=")
            parts[key.strip()] = float(value.strip())

        waist = parts.get("waist_cm")
        hip = parts.get("hip_cm")

        if not waist or not hip:
            return "error=missing_values"

        ratio = waist / hip

        return f"ratio={ratio:.2f}"

    except Exception as e:
        return f"error={str(e)}"


@tool
def bodyAdiposityIndex(input_str: str) -> str:
    """
    Input:
    "hip_cm=100, height_m=1.75"
    """

    try:
        parts = {}

        for part in input_str.replace(" ", "").split(","):
            key, value = part.split("=")
            parts[key.strip()] = float(value.strip())

        hip = parts.get("hip_cm")
        height = parts.get("height_m")

        if not hip or not height:
            return "error=missing_values"

        bai = (hip / (height ** 1.5)) - 18

        return f"bai={bai:.2f}"

    except Exception as e:
        return f"error={str(e)}"


@tool
def bodyFatPercentage(input_str: str) -> str:
    """
    Input:
    Male:
    "gender=male, waist_cm=85, neck_cm=40, height_cm=175"

    Female:
    "gender=female, waist_cm=75, neck_cm=34, hip_cm=95, height_cm=165"
    """

    try:
        parts = {}

        for part in input_str.replace(" ", "").split(","):
            key, value = part.split("=")

            if key.strip() == "gender":
                parts[key.strip()] = value.strip().lower()
            else:
                parts[key.strip()] = float(value.strip())

        gender = parts.get("gender")
        waist = parts.get("waist_cm")
        neck = parts.get("neck_cm")
        height = parts.get("height_cm")

        if gender == "male":

            bodyFat = (
                495 / (
                    1.0324
                    - 0.19077 * math.log10(waist - neck)
                    + 0.15456 * math.log10(height)
                )
            ) - 450

        elif gender == "female":

            hip = parts.get("hip_cm")

            if not hip:
                return "error=missing_hip"

            bodyFat = (
                495 / (
                    1.29579
                    - 0.35004 * math.log10(waist + hip - neck)
                    + 0.22100 * math.log10(height)
                )
            ) - 450

        else:
            return "error=invalid_gender"

        return f"body_fat={bodyFat:.2f}"

    except Exception as e:
        return f"error={str(e)}"


@tool
def bodyRoundnessIndex(input_str: str) -> str:
    """
    Input:
    "waist_cm=85, height_cm=175"
    """

    try:
        parts = {}

        for part in input_str.replace(" ", "").split(","):
            key, value = part.split("=")
            parts[key.strip()] = float(value.strip())

        waist = parts.get("waist_cm")
        height = parts.get("height_cm")

        if not waist or not height:
            return "error=missing_values"

        waist_m = waist / 100
        height_m = height / 100

        bri = 364.2 - (
            365.5 * math.sqrt(
                1 - ((waist_m / (2 * math.pi)) ** 2)
                / ((0.5 * height_m) ** 2)
            )
        )

        return f"bri={bri:.2f}"

    except Exception as e:
        return f"error={str(e)}"