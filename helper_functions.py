from datetime import datetime

def get_more_time_together_date(birthdate, connection_date):
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()
    connection_date = datetime.strptime(connection_date, "%Y-%m-%d").date()
    time_spent_not_met = connection_date - birthdate
    more_time_together_date = connection_date + time_spent_not_met

    return more_time_together_date