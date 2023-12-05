def get(dict, list1, list2):
    for i in list1:
        for j in list2:
            if i in range(j[1], j[1] + j[2]):
                dict[i] = j[0] + (i - j[1])
                break
        else:
            dict[i] = i


with open("2023/5/part_1_2_input.txt", "r") as fobj:
    lines = fobj.read()
    lines = lines.split("\n")

    seeds = [int(i) for i in lines[0][6:].split()]

    seed_to_soil_lines = [
        [int(j) for j in i.split()]
        for i in lines[
            lines.index("seed-to-soil map:")
            + 1 : lines.index("soil-to-fertilizer map:")
            - 1
        ]
    ]
    soil_to_fertilizer_lines = [
        [int(j) for j in i.split()]
        for i in lines[
            lines.index("soil-to-fertilizer map:")
            + 1 : lines.index("fertilizer-to-water map:")
            - 1
        ]
    ]
    fertilizer_to_water_lines = [
        [int(j) for j in i.split()]
        for i in lines[
            lines.index("fertilizer-to-water map:")
            + 1 : lines.index("water-to-light map:")
            - 1
        ]
    ]
    water_to_light_lines = [
        [int(j) for j in i.split()]
        for i in lines[
            lines.index("water-to-light map:")
            + 1 : lines.index("light-to-temperature map:")
            - 1
        ]
    ]
    light_to_temperature_lines = [
        [int(j) for j in i.split()]
        for i in lines[
            lines.index("light-to-temperature map:")
            + 1 : lines.index("temperature-to-humidity map:")
            - 1
        ]
    ]
    temperature_to_humidity_lines = [
        [int(j) for j in i.split()]
        for i in lines[
            lines.index("temperature-to-humidity map:")
            + 1 : lines.index("humidity-to-location map:")
            - 1
        ]
    ]
    humidity_to_location_lines = [
        [int(i) for i in lines[lines.index("humidity-to-location map:") + 1].split()]
    ]

    soils = {}
    fertlizers = {}
    water = {}
    light = {}
    temperature = {}
    humidity = {}
    location = {}

    get(soils, seeds, seed_to_soil_lines)
    get(fertlizers, soils.values(), soil_to_fertilizer_lines)
    get(water, fertlizers.values(), fertilizer_to_water_lines)
    get(light, water.values(), water_to_light_lines)
    get(temperature, light.values(), light_to_temperature_lines)
    get(humidity, temperature.values(), temperature_to_humidity_lines)
    get(location, humidity.values(), humidity_to_location_lines)

    print(
        min(
            [
                location[
                    humidity[temperature[light[water[fertlizers[soils[seeds[i]]]]]]]
                ]
                for i in range(len(seeds))
            ]
        )
    )
