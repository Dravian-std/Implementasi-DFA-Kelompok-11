def validasi(input_user):
    transition_table = {
        "q0": {"huruf": "q1", "underscore": "q1", "angka": "q_trap", "other": "q_trap"},
        "q1": {"huruf": "q1", "underscore": "q1", "angka": "q1", "other": "q_trap"},
        "q_trap": {"huruf": "q_trap", "underscore": "q_trap", "angka": "q_trap", "other": "q_trap"}
    }
    
    state_sekarang = "q0"
    urutan_state = [state_sekarang]

    for char in input_user:
        if char.isalpha():
            char_type = "huruf"
        elif char.isdigit():
            char_type = "angka"
        elif char == "_":
            char_type = "underscore"
        else:
            char_type = "other"

        state_sekarang = transition_table[state_sekarang].get(char_type, "q_trap")
        urutan_state.append(state_sekarang)

        if state_sekarang == "q_trap":
            break

    apakah_valid = (state_sekarang == "q1")
    return apakah_valid, urutan_state