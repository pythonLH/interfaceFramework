import os

# data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", "data.yaml")
# ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "common.ini")

ini_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "config", "common.ini")
switch_ini = (os.path.join(os.path.dirname(os.path.realpath(__file__)), "config", "switch.ini"))
yam_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "yaml_data", "data.yaml")
middleground = os.path.join(os.path.dirname(os.path.realpath(__file__)), "yaml_data", "middleground.yaml")
print(middleground)
# print(switch_ini)
# print(yam_path)
