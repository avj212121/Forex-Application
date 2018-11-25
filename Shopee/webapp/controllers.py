from webapp import db
from webapp.forms import RegisterRate, TrackRate,DeleteRate
from webapp.models import ExchangeRate
from flask import render_template,flash,Blueprint
from webapp.utils import validate,seven_day_average
import datetime

myapp = Blueprint('myapp', __name__)

# Homepage route
@myapp.route('/')
def homepage():
    return render_template('index.html')

# Register api to register currencies
@myapp.route('/register', methods=['GET','POST'])
def register():
    form = RegisterRate()
    now = datetime.datetime.now()
    if form.validate_on_submit():
        # Check if date format is correct YYYY-MM-DD
        if not validate(now.strftime("%Y-%m-%d") if not form.date.data else form.date.data):
            return render_template('incorrectDate.html')
        else:
            # Check if entry already exists in db or not
            exchangeObj = ExchangeRate.query.filter_by(date=now.strftime("%Y-%m-%d") if not form.date.data else form.date.data, from_country=form.from_country.data,
                                                       to_country=form.to_country.data).first()
            if exchangeObj:
                # Check if it is an update query
                if form.rate.data:
                    exchangeObj.rate=form.rate.data
                    if exchangeObj.rate:
                        db.session.commit()
                        return render_template('updateSuccess.html')
                    else:
                        render_template('updateFail.html')
                # Else it's an error as entry already present in database
                else:
                    return render_template('error.html')
            else:
                #Create entry if it is for first time
                exchangeRate = ExchangeRate(date=now.strftime("%Y-%m-%d") if not form.date.data else form.date.data,
                                            from_country=form.from_country.data,
                                            to_country=form.to_country.data,
                                            rate=None if not form.rate.data else form.rate.data)
                db.session.add(exchangeRate)
                db.session.commit()
                return render_template('successfull.html')

    return render_template('register.html',form=form)

# Track api to track currencies
@myapp.route('/track', methods=['GET','POST'])
def track():
    form = TrackRate()
    if form.validate_on_submit():
        # Check if date format is correct YYYY-MM-DD
        if not validate(form.date.data):
            return render_template('incorrectDate.html')
        else:
            # Get rates for the mentioned date
            rates = ExchangeRate.query.filter_by(date=form.date.data).order_by(ExchangeRate.from_country,ExchangeRate.to_country).all()
            if rates:
                # Calculate seven day average
                average_list = seven_day_average(form.date.data)
                return render_template('output.html', rates=rates,average_list=average_list)
            else:
                return render_template('noEntry.html')

    return render_template('track.html',form=form)

# Delete api to delete currencies
@myapp.route('/delete', methods=['GET','POST'])
def delete():
    form = DeleteRate()
    if form.validate_on_submit():
            # Fetch object from db which is to be deleted
            deleteObj = ExchangeRate.query.filter_by(from_country=form.from_country.data,
                                                     to_country=form.to_country.data).delete()
            if deleteObj or deleteObj!=0:
                db.session.commit()
                return render_template('deleteSuccess.html')
            else:
                return render_template('deleteFail.html')

    return render_template('delete.html',form=form)


