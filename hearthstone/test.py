# pass parameters needed for this spell's effect
effect_parameters = ["target","current player"]
print(effect_parameters)
# for p in effect_parameters:
#     if p == "target":
#         p = "tar"
#     elif p == "current player":
#         p = "cur"
#     elif p == "opponent":
#         p = "oppo"
for i in range(len(effect_parameters)):
    if effect_parameters[i] == "target":
        effect_parameters[i] = "tar"
    elif effect_parameters[i] == "current player":
        effect_parameters[i] = "cur"
    elif effect_parameters[i] == "opponent":
        effect_parameters[i] = "oppo"
print(effect_parameters)