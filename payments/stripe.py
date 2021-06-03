import stripe
import os
from dotenv import load_dotenv
load_dotenv('./.env')
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

