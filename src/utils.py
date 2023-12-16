

def number_format(name):
    if "счет" in name.lower():
        name_list = name.split()
        format_number = name_list[0] + " " + "**" + name_list[-1][-4:]
        return format_number
    else:
        name_list = name.split()
        name_operation = name_list[0:-1]
        format_number = " ".join(name_operation) + " " + name_list[-1][0:4] + " " + name_list[-1][4:6] + "**" + " " + "****" + " " + name_list[-1][-4:]
        return format_number

def date_format(date):
    format_date = ".".join(date.split("-")[::-1])
    return format_date