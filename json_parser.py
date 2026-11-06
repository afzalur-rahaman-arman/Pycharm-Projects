import json
with open("catalog.json", "r") as f:
    product=json.load(f)
  #  print(product)

print(product)#all of the data from json file
print(product["cloth"][1].get("sizes"))

product["cloth"][1].get("sizes").append("extra large")#add a value in the json file from this line
print(product["cloth"][1]["sizes"]) #same defensive line :  print(product["cloth"][1].get("sizes"))

print(product["cloth"])


with open("catalog.json", "w") as f:
    json.dump(product, f, indent=4)