def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    # names_list = []
    # for name in names:
    #     names_list.append(f"Hello, my name is {name}.")
    # return names_list
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    rooms = [1, 2, 3, 4, 5, 6, 7, 8]
    room = 0
    room_assignments = []
    for name in names:
        room_assignments.insert(room, f"Hello, {name}! You'll be assigned to room {rooms[room]}!")
        room += 1
    return room_assignments

def printer(names):
    name_index = 0
    while name_index < len(names):
        print(batch_badge_creator(names)[name_index])
        name_index += 1
    name_index = 0
    while name_index < len(names):
        print(assign_rooms(names)[name_index])
        name_index += 1