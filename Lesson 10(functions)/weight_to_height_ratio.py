centimeters = int(input("enter your height in cm: "))
kilograms = float(input("enter your weight in kg: "))

def weight_to_height(kgs:float, cms:int) -> str:
    ratio = kgs / cms
    return (ratio, "kg/cm")

weight_to_height(kilograms, centimeters)

weight_to_height("kilograms", "centimeters")