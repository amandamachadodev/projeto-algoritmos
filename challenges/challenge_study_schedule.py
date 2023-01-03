def study_schedule(permanence_period, target_time):
    if type(target_time) != int:
        return None
    students = 0
    for come_in, exit in permanence_period:
        if type(come_in) != int or type(exit) != int:
            return None
        elif come_in <= target_time <= exit:
            students += 1
    return students
