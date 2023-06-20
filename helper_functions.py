from datetime import datetime

def get_more_time_together_date(birthdate, connection_date):
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()
    connection_date = datetime.strptime(connection_date, "%Y-%m-%d").date()
    time_spent_not_met = connection_date - birthdate
    more_time_together_date = connection_date + time_spent_not_met

    return more_time_together_date

def percent_time_spent_together(birthday, connection_date):
    birthday = datetime.strptime(birthday, "%Y-%m-%d").date()
    connection_date = datetime.strptime(connection_date, "%Y-%m-%d").date()
    total_days = (connection_date - birthday).days
    time_together_days = (datetime.now().date() - connection_date).days
    user_percent_time_spent_together = round((time_together_days / total_days) * 100, 2)

    return user_percent_time_spent_together