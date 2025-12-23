full_dot = '●'
empty_dot = '○'

def create_character(char_name, strength, intelligence, charisma):
    error_msg_char_name = validate_char_name(char_name)
    error_msg_stats = validate_stats(strength, intelligence, charisma)
    
    if error_msg_char_name: return error_msg_char_name
    elif error_msg_stats: return error_msg_stats

    return f"{ char_name }\nSTR { get_stat(strength) }\nINT { get_stat(intelligence) }\nCHA { get_stat(charisma) }"

def validate_char_name(name):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if ' ' in name:
        return "The character name should not contain spaces"
    return None

def validate_stats(strength, intelligence, charisma):
    if not all(isinstance(value, int) for value in (strength, intelligence, charisma)):
        return "All stats should be integers" 
    if not all(value >= 1 for value in (strength, intelligence, charisma)):
        return "All stats should be no less than 1"
    if not all(value <= 4 for value in (strength, intelligence, charisma)):
        return "All stats should be no more than 4"
    if sum([strength, intelligence, charisma]) != 7:
        return "The character should start with 7 points"
    return None

def get_stat(stat):
    total_points = ""
    for point in range(10):
        if point <= stat - 1:
            total_points += full_dot
        else:
            total_points += empty_dot
    return total_points

print(create_character('ren', 4, 2, 1))
