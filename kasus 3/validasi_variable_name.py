# KASUS 1: Validasi Nama Variabel
# -------------------------------------------------------------
# Tuple DFA: Q = {q0, q1, q_trap}, q0 = q0, F = {q1}

def validate_variable_name(input_string):
    # Tabel Transisi DFA
    transition_table = {
        'q0': {'letter': 'q1', 'underscore': 'q1', 'digit': 'q_trap', 'other': 'q_trap'},
        'q1': {'letter': 'q1', 'underscore': 'q1', 'digit': 'q1', 'other': 'q_trap'},
        'q_trap': {'letter': 'q_trap', 'underscore': 'q_trap', 'digit': 'q_trap', 'other': 'q_trap'}
    }
    
    current_state = 'q0'
    trace = [current_state]

    for char in input_string:
        # Pemetakan Karakter ke Simbol Input
        if char.isalpha():
            char_type = 'letter'
        elif char.isdigit():
            char_type = 'digit'
        elif char == '_':
            char_type = 'underscore'
        else:
            char_type = 'other'

        # Transisi State
        current_state = transition_table[current_state].get(char_type, 'q_trap')
        trace.append(current_state)

        if current_state == 'q_trap':
            break

    is_valid = current_state == 'q1'
    return is_valid, trace

# Demostrasi Kasus 1
print("=== KASUS 1: VALIDASI VARIABLE NAME ===")
test_inputs_1 = ["nama_user", "_count1", "123name", "user-name"]

for inp in test_inputs_1:
    valid, trace = validate_variable_name(inp)
    status = "VALID (ACCEPT)" if valid else "TIDAK VALID (REJECT)"
    print(f"Input : '{inp}'")
    print(f"Jejak : {' -> '.join(trace)}")
    print(f"Hasil : {status}\n" + "-" * 40)
