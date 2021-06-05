import stripe
import os
from dotenv import load_dotenv
load_dotenv('./.env')
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

token_card = stripe.Token.create(
  card={
    "number": "4242424242424242",
    "exp_month": 6,
    "exp_year": 2022,
    "cvc": "314",
  },
)