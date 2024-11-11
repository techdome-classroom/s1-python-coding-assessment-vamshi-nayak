def decode_message(s: str, p: str) -> bool:
    message_index = 0
    pattern_index = 0
    star_index = -1
    match_index = 0

    while message_index < len(s):
        if pattern_index < len(p) and (p[pattern_index] == s[message_index] or p[pattern_index] == '?'):
            message_index += 1
            pattern_index += 1
        elif pattern_index < len(p) and p[pattern_index] == '*':
            star_index = pattern_index
            match_index = message_index
            pattern_index += 1
        elif star_index != -1:
            pattern_index = star_index + 1
            match_index += 1
            message_index = match_index
        else:
            return False

    while pattern_index < len(p) and p[pattern_index] == '*':
        pattern_index += 1

    return pattern_index == len(p)
