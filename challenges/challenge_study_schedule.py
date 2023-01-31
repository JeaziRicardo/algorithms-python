def study_schedule(permanence_period, target_time):
    try:
        return sum(
            1
            for start_period, end_period in permanence_period
            if start_period <= target_time <= end_period
        )
    except TypeError:
        return None
