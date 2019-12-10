# 字典
alien_0 = {'color': 'green', 'point': 5, 6: 66}
print(alien_0['color'])
print(alien_0[6])

alien_0["x"] = 0
alien_0["y"] = 200
print(alien_0)

alien_0["speed"] = "medium"

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0['x'] = alien_0["x"] + x_increment
print(alien_0["x"])

del alien_0['point']
print(alien_0)
