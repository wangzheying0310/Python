def calculate_sector(central_angle,radius):
    # 下面是计算扇形面积的代码
    sector_area = central_angle / 360 * 3.14 * radius ** 2
    print(f"此扇形的面积为：{sector_area}")
calculate_sector(160, 30)
calculate_sector(11, 30)
