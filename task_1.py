time_values_str = "1h 45m,360s,25m,30m 120s,2h 60s"

time_values_lst = time_values_str.split(",")
total_minutes = 0
for time_str in time_values_lst:
    units = time_str.split(" ")
    for unit in units:
        if "h" in unit:
            total_minutes += int(unit.replace("h", "")) * 60
        elif "m" in unit:
            total_minutes += int(unit.replace("m", ""))
        elif "s" in unit:
            total_minutes += int(unit.replace("s", "")) // 60
        

print(f"{total_minutes}")
