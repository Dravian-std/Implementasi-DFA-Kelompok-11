def validate_variable_name(input_user):
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

def menu():
    print("=" * 70)
    print("          PROGRAM VALIDASI NAMA VARIABEL (DFA) - KASUS 1")
    print("=" * 70)
    print("Aturan:")
    print("1. Karakter pertama wajib berupa huruf (a-z, A-Z) atau '_'")
    print("2. Karakter berikutnya boleh huruf, angka (0-9), atau '_'")
    print("3. Karakter selain huruf, angka, dan underscore dianggap tidak valid.")
    print("-" * 70)
    
    while True:
        user_input = input("\nMasukkan nama variabel yang ingin diuji (atau ketik 'keluar' untuk selesai): ")
        
        if user_input.lower() == "keluar":
            print("Program selesai. Terima kasih.")
            break
        
        if user_input == "":
            print("Input tidak boleh kosong.")
            continue

        apakah_valid, urutan_state = validate_variable_name(user_input)
        status = "VALID" if apakah_valid else "TIDAK VALID"
        
        print("\n-------------------- HASIL VALIDASI -------------------")
        print(f"Input Pengguna : '{user_input}'")
        print(f"Jejak Transisi : {' -> '.join(urutan_state)}")
        print(f"Status Final   : {status}")
        print("-" * 55)

menu()