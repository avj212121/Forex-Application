import datetime
from datetime import timedelta
from webapp.models import ExchangeRate

# Function to validate if date format is correct
def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Function to calculate 7-day average
def seven_day_average(date_text):
    end_date = datetime.datetime.strptime(date_text, '%Y-%m-%d')
    start_date = end_date - timedelta(days=7)
    rate_list = ExchangeRate.query.filter(ExchangeRate.date <= end_date , ExchangeRate.date> start_date).order_by(ExchangeRate.from_country,ExchangeRate.to_country,ExchangeRate.date).all()
    sum = 0.00
    count = 0
    average = 0.00
    average_list = []
    from_c = rate_list[0].from_country
    to_c = rate_list[0].to_country

    for rate_obj in rate_list:

        if from_c == rate_obj.from_country and to_c == rate_obj.to_country:
            if rate_obj.rate is not None:
                sum = sum + rate_obj.rate
                count = count + 1
                average = sum/count

        else:
            average_list.append(round(average,2))
            from_c = rate_obj.from_country
            to_c = rate_obj.to_country
            sum = 0.00
            count = 0
            average = 0.00
            if rate_obj.rate is not None:
                sum = sum + rate_obj.rate
                count = count + 1
                average = sum/count

    average_list.append(round(average,2))

    return average_list
