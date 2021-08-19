instruments = {
    "ba": "banjo",
    "bd": "basedrum",
    "b": "bass",
    "be": "bell",
    "bi": "bit",
    "ch": "chime",
    "cb": "cow_bell",
    "d": "didgeridoo",
    "f": "flute",
    "g": "guitar",
    "h": "harp",
    "ha": "hat",
    "ix": "iron_xylophone",
    "p": "pling",
    "s": "snare",
    "x": "xylophone"
}


def main():
    file_name = input("Filename: ")
    key = file_name.replace("-", "_")
    file = open(file_name + ".json", "w")
    file.write("{\n")
    file.write(f"  \"Key\": \"{key}\",\n")
    author = input("Author: ")
    file.write(f"  \"Author\": \"{author}\"")
    print("Please enter all note entries\n"
          "q - quit\n"
          "w [ticks] - wait [ticks] * 4 ticks\n"
          "[instrument] [pitch] - add a note\n"
          "? - show instruments"
          )
    while True:
        line = input()
        if line == "?":
            for key in instruments:
                print(f"{key} -> {instruments[key]}")
        elif line.startswith("w "):
            try:
                wait = int(line[2:])
            except Exception:
                print("INVALID FORMAT - try again (tried to match against: w [ticks])")
                continue
            file.write(f",\n  \"Wait\": {wait * 4}")
        elif line.startswith("c "):
            try:
                comment = line[2:]
            except:
                print("INVALID FORMAT - try again (tried to match against: c [comment])")
                continue
            file.write(f",\n  \"Comment\": \"{comment}\"")
        elif line == "q":
            break
        else:
            try:
                instrument, pitch = line.split(" ")
                file.write(
                    f",\n  \"PlaySound\": [\"block_note_block_{instruments[instrument]}\", {pow(2, (int(pitch) - 12) / 12):.6f}]"
                )
            except:
                print("INVALID FORMAT - try again (tried to match against: [instrument] [pitch])\n")
                continue

    file.write("\n}\n")


if __name__ == '__main__':
    main()
