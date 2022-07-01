import hashlib


def hash_message(m):
    hash = hashlib.sha256(m.encode('utf-8')).hexdigest()
    return hash


def rooms(hash, date):
    int_hash = int(hash, 16)
    room_calc = str(int_hash/int(date))

    beds = int(room_calc[0])
    baths = int(room_calc[2])

    if beds < baths+1:
        beds = baths+1
    if baths == 0:
        baths = 1

    return beds, baths


if __name__ == '__main__':
    while input("Play? y/n:").lower() != "n":
        name = input("Enter your name:")
        date = input("Enter your birthdate:")
        print("Beds = ", rooms(hash_message(name), date)[0], "\nBaths = ", rooms(hash_message(name), date)[1])
