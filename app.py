#Tulsipada Das
#Dr. android Guruji
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, winsound
from configparser import RawConfigParser
from colorama import Fore, init, deinit

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36")




init()
CONFIG = RawConfigParser()
CONFIG.read('config.ini')
driver_path = CONFIG.get('MAIN', 'DRIVER_LOCATION')
email_inp = CONFIG.get('CREDENTIALS', 'USERNAME')
pass_inp = CONFIG.get('CREDENTIALS', 'PASSWORD')
order_link = CONFIG.get('ORDER', 'LINK')
cvv_inp = CONFIG.get('ORDER', 'CVV')
addr_input = CONFIG.get('ORDER', 'ADDRESS')
pay_opt_input = CONFIG.get('ORDER', 'PAYMENT')
bankname_input = CONFIG.get('EMIOPTIONS', 'BANK')
tenure_input = CONFIG.get('EMIOPTIONS', 'TENURE')
frequency = 2500
duration = 2000

def prCyan(skk):
    print(Fore.CYAN + skk)


def prRed(skk):
    print(Fore.RED + skk)


def prGreen(skk):
    print(Fore.GREEN + skk)


def prYellow(skk):
    print(Fore.YELLOW + skk)


url = order_link
prRed('Opening Link in chrome..........')
prCyan('\n')
print('\nLogging in with username:', email_inp)
prYellow('\n')
if pay_opt_input == 'EMI_OPTIONS':
    print('\nEMI Option Selected. \nBANK:', bankname_input, '\nTENURE:', tenure_input, '\n')
else:
    if pay_opt_input == 'PHONEPE':
        print('\nPayment with Phonepe\n')
    else:
        if pay_opt_input == 'NET_OPTIONS':
            print('\nNet Banking Payment Selected\n')
        else:
            if pay_opt_input == 'COD':
                prGreen('COD selected\n')
            else:
                print('\nFull Payment Selected\n')

driver = webdriver.Chrome(options=opts , executable_path=driver_path)

driver.set_window_size(550,750)
driver.get(url)
prCyan('\n')


def login_submit():
    print("login your account ")
    input('Confirm login & Press Enter to proceed.')


def buy_check():
    try:
        nobuyoption = True
        while nobuyoption:
            try:
                driver.refresh()
                time.sleep(0.50)
                buyprod = driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/div/div")
                prYellow('Buy Button Clickable')
                nobuyoption = False
            except:
                nobuyoption = True
                prRed('Buy Button Not Clickable')

        buyprod.click()
        prYellow('Buy Button Clicked Successfully')
        buy_recheck()
    except:
        prRed('buy_check Failed. Retrying.')
        time.sleep(0.5)
        buy_check()


def buy_recheck():
    try:
        WebDriverWait(driver, 4).until(EC.title_contains('Flipkart'))
        prYellow('Redirected to Payment')
    except:
        prRed('Error in Redirecting to Payment')
        time.sleep(0.5)
        buy_recheck()


def deliver_option():
    try:
        addr_input_final = "//label[@for='" + addr_input + "']"
        try:
            sel_addr = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, addr_input_final)))
            prYellow('Address Selection Button Clickable')
        except:
            prRed('Address Selection Button Not Clickable')
        else:
            sel_addr.click()
            prYellow('Address Selection Button Clicked Successfully')
    except:
        prRed('deliver_option Failed. Retrying.')


def deliver_continue():
    try:
        addr_sal_avl = True
        while addr_sal_avl:
            try:
                address_sel = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '._3K1hJZ ._7UHT_c')))
                address_sel.click()
                addr_sal_avl = False
                print('Address Delivery Button Clickable')
            except:
                addr_sal_avl = True
                winsound.Beep(frequency, duration)
                print('Address Delivery Button Not Clickable')

        print('Address Delivery Button Clicked Successfully')
    except:
        print('deliver_continue Failed. Retrying.')



def skip():
    time.sleep(8)
    driver.find_element_by_xpath("//*[@class='_1C3neO _2h9Zp6 _1y96ch']").click()
    try:
        x = driver.find_element_by_xpath("//*[@src='data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTMiIGhlaWdodD0iMTMiIHZpZXdCb3g9IjAgMCAxMyAxMyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMS4wNTQgMWwxMC41NDMgMTAuNjVtLjA1NC0xMC41OTZMMSAxMS41OTciIHN0cm9rZT0iIzQxNDE0MSIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZmlsbD0ibm9uZSIvPjwvc3ZnPgo=']")
        x.click()
        print("skip click")
    except:
        print("skip not click")
    order_summary_continue()


def order_summary_continue(): 
    time.sleep(7)
    driver.find_element_by_xpath("//*[@id='stickyFooter']/div/div[2]/div/div/span").click()
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='fk-cp-pay']/div/div[1]/div[1]/a/img").click()


    
    


def cod_captcha():
    try:
        payment_sel = None
        payment_sel = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._16qL6K')))
        payment_sel.clear()
        prYellow('Type the captcha here:')
        capText = input()
        payment_sel.send_keys(capText)
        prGreen('\nCaptcha entered successfully.')
        prYellow('\nClicking Confirm Button order:')
        confirm_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._7UHT_c')))
        confirm_btn.click()
        prGreen('\nOrder confirmed successfully')
    except:
        prRed('\nCaptcha could not be entered. Plese type manually on webpage.')






def payment_continue():
    try:
        pay = None
        try:
            pay = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._3K1hJZ ._7UHT_c')))
            print('Pay Button Clickable')
        except:
            print('Pay Button Not Clickable')
        else:
            pay.click()
            print('Pay Button Clicked Successfully')
    except:
        print('payment_continue Failed. Retrying.')


def otp_submit():
    try:
        otp = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._3K1hJZ .l5dwor')))
        otp.clear()
        print('Please enter OTP here:')
        otp_input = input()
        otp.send_keys(otp_input)
        submit_otp = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._3K1hJZ ._7UHT_c')))
        submit_otp.click()
        print('OTP Submitted Successfully')
    except:
        print('otp_submit Failed. Retrying.')
        time.sleep(0.5)
        otp_submit()


def try_till_otp():
    login_submit()
    buy_check()
    skip()


if __name__ == '__main__':
    try_till_otp()
