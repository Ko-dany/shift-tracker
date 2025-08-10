import pandas as pd
from datetime import timedelta, datetime, date

def process_shift_data(file_path):
    print(f"Processing shift data from \"{file_path}\"")

    data = pd.read_excel(file_path)
    first_row = data.iloc[0]

    employ_name = first_row["Employ Name"]
    work_date = first_row["Date"]
    start_time = first_row["Start Time"]
    end_time = first_row["End Time"]

    print(employ_name)
    print(type(employ_name))
    print(work_date)
    print(type(work_date))
    print(start_time)
    print(type(start_time))
    print(end_time)
    print(type(end_time))

    working_hours = datetime.combine(work_date, end_time) - datetime.combine(work_date, start_time)

    total_minutes = working_hours.total_seconds() // 60
    num_slots = int((total_minutes) // 30)

    print(f"Working Hours: {working_hours}")

    current_dt = datetime.combine(work_date, start_time)

    while num_slots > 0:
        slot_end_dt = current_dt + timedelta(minutes=30)
        print(f"Slot.{num_slots} : Start - {current_dt.time()}, End - {slot_end_dt.time()}")
        current_dt = slot_end_dt
        num_slots -= 1