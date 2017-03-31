from wellaware.constants import Config
from wellaware.client import *

Config.base_url = 'https://api.wellaware.us'
# Enable this commonly for QA tests where it's helpful to have the token printed along with the test
Config.include_token = True

token = Tokens.login(username="johndoe@example.com", password="password123")
my_tenant = Tenants.me(token)
sites = Sites.retrieve_all(token)
site = sites[0]
assets = Assets.retrieve_all(token, site_id=site)  # or alternatively site_id=site.id
points = Points.retrieve_all(token, site_id=site, asset_id=assets[0])