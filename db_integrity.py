db = ["A: 1234542938462938423", "B: 981238719237812368172368"]

check = ["A: 1234542938462938423", "B: 981238719237812368172368"]
counter = 0
error = 0
error_msg = "ON FIELD(S) "

for x in db:
    if x == check[counter]:
        print(f"FIELD {counter} CORRECT.")
    else:
        print(f"ERROR IN FIELD {counter}.")
        error += 1
        error_msg += f"{str(counter)}, "
    counter += 1

if error == 0:
    print("DB INTEGRITY SUCCESSFUL.")
else:
    print(f"DB INTEGRITY UNSUCCESSFUL. DETECTED {error} ERROR(S) {error_msg[:-2]}.")
