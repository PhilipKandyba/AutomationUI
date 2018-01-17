import time

REAL_USER_EMAIL = 'philip.kanduba+test2@gmail.com'  # cabinet577007871
REAL_USER_PASSWORD = '123456'
REAL_USER_FIRST_NAME = 'Tester'

NEW_USER_EMAIL = 'automation.test.tg+%s@gmail.com' % (time.strftime("%Y%d%b%H%M%S"))
NEW_USER_PASSWORD = '123456'
NEW_USER_FIRST_NAME = 'Bob'
NEW_SHOP_URL = 'http://%s.com' % (time.strftime("%Y%d%b%H%M%S"))

UNCONFIRMED_USER_EMAIL = 'not_confirm_email@email.com'  # cabinet2123287423

RESET_PASSWORD_USER_EMAIL = 'automation.test.tg+resetpassword@gmail.com'  # cabinet96438670
RESET_PASSWORD_USER_NEW_PASSWORD = time.strftime("%Y%d%b%H%M%S")

