import re
from Tools.bodyTools import bmiCalculator

def runCalcAgent(user_input: str):
    nums = re.findall(r"\d+(?:\.\d+)?", user_input)

    if len(nums) < 2:
        return "Please provide weight and height like: BMI 70 1.75"

    weight = nums[0]
    height = nums[1]

    tool_input = f"height_m={height}, weight_kg={weight}"

    return bmiCalculator.invoke(tool_input)