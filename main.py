import asyncio
import multiprocessing
from os import system
from os import remove
from config import _settings

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException as find_exc
from screeninfo import get_monitors

width, height = get_monitors()[0].width, get_monitors()[0].height
 
BROWSER = webdriver.Chrome(executable_path=_settings.path_to_chromedriver)
BROWSER.set_window_size(width, height)
wait = WebDriverWait(BROWSER, 10)

acc_tab = {'Instagram': '10', 'VK': '2', 'Discord': '22'}

system('clear')

def auth():
	BROWSER.get("https://lolz.guru/login") 
	wait.until(EC.title_contains('Log in'))
	
	login = BROWSER.find_element_by_id('ctrl_pageLogin_login')
	login.send_keys(_settings.login)

	password = BROWSER.find_element_by_id('ctrl_pageLogin_password')
	password.send_keys(_settings.password)
	password.send_keys(Keys.RETURN)

	try:
		tg_code = BROWSER.find_element_by_id('ctrl_telegram_code')
		BROWSER.minimize_window()
		print('If you are seeing Captcha, complete her by hands')
		code = input("Telegram Code from Lolzteam Alert: ")
		BROWSER.maximize_window()
		tg_code.send_keys(code)
		tg_code.send_keys(Keys.RETURN)
	
	except find_exc:
		pass
		
	wait.until(EC.title_contains('Форум социальной инженерии'))
		
	
def set_tabs():
	BROWSER.minimize_window()
	number_of_tabs = int(input("Number of tabs(1-10): "))

	if number_of_tabs > 10:
		raise Exception('Too much tabs(1-10)')
	
	return number_of_tabs


def set_delay():
	delay = int(input("Enter delay for account preloading in integer min(60+ for autoregs): ")) * 60
	
	if delay >= 0 and delay <=1440:
		print(f'Waiting {delay}s')
		return delay
	else:
		raise Exception("Delay number eror")
	
	
def fill_massload_form():
	BROWSER.get(f"https://lolz.guru/market/mass-upload/{acc_tab[_settings.accounts]}/start")

	wait.until(EC.presence_of_element_located((By.NAME,'title_en')))
		
	name_en = BROWSER.find_element_by_name('title_en')
	name_en.send_keys(_settings.name_en)

	name_ru = BROWSER.find_element_by_name('title_ru')
	name_ru.send_keys(_settings.name_ru)

	price = BROWSER.find_element_by_name('price')
	price.send_keys(_settings.price)
	
	change_toolbar_checkbox_1 = BROWSER.find_elements_by_xpath('//*[@id="descriptionEditor"]/div/div[3]/ul/li[1]/ul/li/a')[0]
	ActionChains(BROWSER).move_to_element(change_toolbar_checkbox_1).click().perform()
	description = BROWSER.find_elements_by_xpath('//*[@id="descriptionEditor"]/div/div[4]/textarea')[0]
	description.send_keys(_settings.description)
	
	change_toolbar_checkbox_2 = BROWSER.find_elements_by_xpath('//*[@id="informationEditor"]/div/div[3]/ul/li[1]/ul/li/a')[0]
	ActionChains(BROWSER).move_to_element(change_toolbar_checkbox_2).click().perform()
	info_for_buyer = BROWSER.find_elements_by_xpath('//*[@id="informationEditor"]/div/div[4]/textarea')[0]
	info_for_buyer.send_keys(_settings.info_for_buyer)
	
	
def set_discount_checkbox():
	if not _settings.discount_value:
		wait.until(EC.presence_of_element_located((By.ID, 'ctrl_allow_ask_discount'))).click()


def set_massload_start_chekbox():
	start_checkbox = BROWSER.find_element_by_id('MassAutoStartCheckbox').click()


def set_accounts_origin():
	account_origin = _settings.accounts_origin 
	try:
		if _settings.accounts == 'Discord':
			if account_origin == 'Autoregs':
				print("Don't forget to add a proxy on https://lolz.guru/account/market") 	
				account_origin_button = BROWSER.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[2]/form/div[6]/div/div[2]/div/label[3]')
				ActionChains(BROWSER).move_to_element(account_origin_button).click().perform()
			if account_origin == 'Fishing':
				account_origin_button = BROWSER.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[2]/form/div[6]/div/div[2]/div/label[1]')
				ActionChains(BROWSER).move_to_element(account_origin_button).click().perform()
			if account_origin == 'Stealer':
				account_origin_button = BROWSER.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[2]/form/div[6]/div/div[2]/div/label[2]')
				ActionChains(BROWSER).move_to_element(account_origin_button).click().perform()
			
		else:
			if account_origin == 'Brute': # default value
				pass
			if account_origin == 'Autoregs':
				print("Don't forget to add a proxy on https://lolz.guru/account/market") 	
				account_origin_button = BROWSER.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[2]/form/div[6]/div/div[2]/div/label[4]')
				ActionChains(BROWSER).move_to_element(account_origin_button).click().perform()
			if account_origin == 'Fishing':
				account_origin_button = BROWSER.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[2]/form/div[6]/div/div[2]/div/label[2]')
				ActionChains(BROWSER).move_to_element(account_origin_button).click().perform()
			if account_origin == 'Stealer':
				account_origin_button = BROWSER.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[2]/form/div[6]/div/div[2]/div/label[3]')
				ActionChains(BROWSER).move_to_element(account_origin_button).click().perform()
			if account_origin == 'Retrive':
				account_origin_button = BROWSER.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[2]/form/div[6]/div/div[2]/div/label[5]')
				ActionChains(BROWSER).move_to_element(account_origin_button).click().perform()
			if account_origin == 'Resale':
				account_origin_button = BROWSER.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[2]/form/div[6]/div/div[2]/div/label[6]')
				ActionChains(BROWSER).move_to_element(account_origin_button).click().perform()
	except Exception:
		raise "Unsupported account's origin for this accounts"
	
	
def fill_accs_form(data):
	accs_form = BROWSER.find_element_by_name('raw_data') 
	accs_form.send_keys(data)


def massload_optimization(n, lim, path_to_accs):
	accs_list = open('accs.txt', 'r').read().rstrip('\n').split('\n')
	if len(accs_list) < n:
		raise 'Number of accounts < number of tabs'	
			
	optimize_list = []
	
	while len(accs_list) % n >= 1: 
		accs_list.append('')
	
	if lim*n >= len(accs_list):
		lim = int(len(accs_list)/n)
		mod = 0
	else:
		mod = len(accs_list)-lim*n
	
	remove(path_to_accs)
	accs_txt = open('accs.txt', 'w')
	
	for i in range(len(accs_list)-mod, len(accs_list)):
		accs_txt.write(accs_list[i]+'\n')
		
	for optimize_number in range(lim, lim*n+lim, lim):
		optimize_list.append('\n'.join([accs_list[line_index] for line_index in range(optimize_number-lim, optimize_number)]))

	return optimize_list if len(optimize_list) == n else optimize_list[0:n], mod
	
	
def set_load_limit():
	limit = int(input(f"Type limit for strings in 1 tabs(Recommended limit: {multiprocessing.cpu_count()*45}): "))
	return limit
	
	
def start_massload():
	if _settings.accounts == 'VK':
		start_button_xpath = '//*[@id="content"]/div/div/div/div/div[2]/form/div[11]/input[1]'
	else:
		start_button_xpath = '//*[@id="content"]/div/div/div/div/div[2]/form/div[12]/input[1]'
		
	start_button = BROWSER.find_element_by_xpath(start_button_xpath)
	ActionChains(BROWSER).move_to_element(start_button).click().perform()
	
	
def massload_results():
	complete = BROWSER.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[2]/div[2]')
	good = BROWSER.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[2]/div[1]/div/div[3]/div[1]')
	bad = BROWSER.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[2]/div[1]/div/div[4]/div[1]')
	
	return int(good.text)+int(bad.text), int(good.text), int(bad.text)
	
	
async def main():
	auth()
	number_of_tabs = set_tabs()
	limit = set_load_limit()
	await asyncio.sleep(set_delay())
	total, good, bad = 0, 0, 0
	
	BROWSER.maximize_window()
	while True:
		for n in range(number_of_tabs):
			if n == 0:
				data, mod = massload_optimization(number_of_tabs, limit, _settings.path_to_accs)
			BROWSER.switch_to.new_window('tab')
			fill_massload_form()
			set_discount_checkbox()
			if n == 0:
				set_massload_start_chekbox()
			set_accounts_origin()
			fill_accs_form(data[n])
			start_massload()
		while True:
			await asyncio.sleep(5)
			try:			
				for _ in range(number_of_tabs):
					total += massload_results()[0]
					good += massload_results()[1]
					bad += massload_results()[2]
					
					BROWSER.switch_to.window(BROWSER.window_handles[-1])
					BROWSER.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'W')
					
				print(f'Total: {total}; Good: {good}; Bad: {bad}')
				
				break
			except Exception:
				print('not found')
				
			
		if mod < number_of_tabs:
			BROWSER.close()
			break
		
		
asyncio.run(main())
