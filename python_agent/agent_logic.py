def recommend_clothes(weather, user_preferences=None):
    temp = weather["temperature"]
    condition = weather["condition"]

    outfit = {
        "top": "",
        "bottom": "",
        "footwear": "",
        "accessories": []
    }

    if temp < 10:
        outfit["top"] = "Sweater + Jacket"
        outfit["bottom"] = "Thermal Pants"
        outfit["footwear"] = "Boots"
    elif temp < 20:
        outfit["top"] = "Hoodie"
        outfit["bottom"] = "Jeans"
        outfit["footwear"] = "Sneakers"
    elif temp < 30:
        outfit["top"] = "T-shirt"
        outfit["bottom"] = "Cotton Pants"
        outfit["footwear"] = "Sneakers"
    else:
        outfit["top"] = "Light Cotton Shirt"
        outfit["bottom"] = "Shorts / Linen Pants"
        outfit["footwear"] = "Sandals"

    if condition == "Rain":
        outfit["accessories"].append("Umbrella")
        outfit["footwear"] = "Waterproof Shoes"

    if condition == "Clear":
        outfit["accessories"].append("Sunglasses")

    return outfit
