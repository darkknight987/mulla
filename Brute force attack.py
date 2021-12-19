import itertools
import string
from timeit import default_timer as timer
from datetime import timedelta
def find_password(real):
    chars = string.ascii_uppercase + string.ascii_lowercase  + string.punctuation + string.digits
    print(chars)
    attempts, paswd_len = 0, 1
    start = timer()
    while True:
        possb_pswrds = itertools.product(chars, repeat=paswd_len)
        for pswrd in possb_pswrds:
            attempts += 1
            pswrd = ''.join(pswrd)
            if pswrd == real:
                end = timer()
                return 'password - {}\nFound in {} attempts\nTime taken: {}'.format(pswrd, attempts, str(timedelta(seconds = end-start)))
        paswd_len += 1
inp_pswd = input("\nEnter password: ")
print(find_password(inp_pswd))