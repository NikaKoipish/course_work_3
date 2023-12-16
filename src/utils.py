

def number_format(name):
    if "счет" in name.lower():
        format_number = name[:4] + " " + "**" + name[-4:]
        return format_number
    else:
        format_number = name[-len(name):-16] + " " + name[-16:-12] + " " + name[-12:-10] + "**" + " " + "****" + " " + name[-4:]
        return format_number

def date_format(date):
    format_date = ".".join(date.split("-")[::-1])
    return format_date