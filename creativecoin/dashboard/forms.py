from flask_wtf import FlaskForm

import wtforms as wtf
from wtforms import validators


class Send(FlaskForm):
    balance = wtf.IntegerField(
        "Source wallet (CCN)",
        render_kw={
            "class": "form-control",
            "disabled": ""
        }
    )
    amount = wtf.IntegerField(
        "Amount:",
        validators=[
            validators.NumberRange(min=100, message="Minimum of 100 CCN is required."),
            validators.InputRequired(),
        ],
        render_kw={
            "class": "send-input form-control",
            "value": "0"
        }
    )
    to_wallet = wtf.StringField(
        "Send to:",
        validators=[
            validators.InputRequired()
        ],
        render_kw={
            "class": "send-input form-control",
            "placeholder": "Enter CCN wallet address"
        }
    )
    submit = wtf.SubmitField(
        "Submit",
        render_kw={
            "class": "btn btn-block c-light-blue c-text-fafa",
            "id": "send-submit"
        }
    )