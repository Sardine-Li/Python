# 根据电池放电曲线设计电压电量函数

def battery_calculate_yunzi(value_bat):
    if value_bat >= 3000:
        value_bat_persent = 100
    elif value_bat >= 2900:
        value_bat_persent = 90 + 10 * (value_bat - 2900)/(3000 - 2900)
    elif value_bat >= 2700:
        value_bat_persent = 80 + 10 * (value_bat - 2700)/(2900 - 2700)
    elif value_bat >= 2500:
        value_bat_persent = 70 + 10 * (value_bat - 2500)/(2700 - 2500)
    elif value_bat >= 2300:
        value_bat_persent = 40 + 10 * (value_bat - 2300)/(2500 - 2300)
    elif value_bat >= 2100:
        value_bat_persent = 10 + 10 * (value_bat - 2100)/(2300 - 2100)
    else:
        value_bat_persent = 1
    return value_bat_persent


def battery_calculate_rc_01(value_bat):
    if value_bat >= 3000:
        value_bat_persent = 100
    elif value_bat >= 2900:
        value_bat_persent = 90 + (100 - 90) * (value_bat - 2900)/(3000 - 2900)
    elif value_bat >= 2800:
        value_bat_persent = 80 + (90 - 80) * (value_bat - 2800)/(2900 - 2800)
    elif value_bat >= 2700:
        value_bat_persent = 70 + (80 - 70) * (value_bat - 2700)/(2800 - 2700)
    elif value_bat >= 2600:
        value_bat_persent = 40 + (70 - 40) * (value_bat - 2600)/(2700 - 2600)
    elif value_bat >= 2400:
        value_bat_persent = 10 + (40 - 10) * (value_bat - 2400)/(2600 - 2400)
    else:
        value_bat_persent = 1
    return value_bat_persent

bat_persent = battery_calculate_yunzi(float(input("请输入云子电压(mV)：\n")))
# bat_persent = battery_calculate_rc_01(float(input("请输入遥控器电压(mV)：\n")))

print("电量百分比为：\n%.2f%%" % bat_persent)
