import subprocess
import pyautogui, time
import pyperclip
import pandas as pd



wa_msg = ""

##----WhatsApp desktop software must be installed-----##

#Get message from text file
with open ("G:\Whauto\data\msg.txt", "r",encoding="utf8") as msg_file:
    msg_body = msg_file.read().replace('\n', '')
    #print (msg_body)
    wa_msg = msg_body

#Function for opening whatsapp and send the message 
# Hardcoding the message here(optional, can use the above fucntion to get the message and mobile numbers as well)   
def send_whatsapp_message(mobile_num):
    #whatsapp://send?phone={}^&text={} - inline message syntax
    subprocess.Popen(["cmd", "/C", "start whatsapp://send?phone={}".format(mobile_num)], shell=True) 
    time.sleep(2) # 2 secs delay
    
    # Store the string to the clipboard(becasue typewriter fucntion does not type Arabic content)
    # pyperclip.copy(msg_body)
    # Hotkey the paste command
    
    
    #ARABIC MESSAGE#
    pyautogui.typewrite("مرحبا")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy(" المعلومات دعوة جميع أصحاب الأعمال الحرة المتخصصين للتسجيل في تطبيق سعودي جديد خاص بمقدمي الخدمات.")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("هذا التطبيق سيمنحك")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("  1.) تسويق مجاني")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("  2.) بيئة آمنة وعمليات موثوقة")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("  3.) العمل في الوقت الذي يناسبك")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("  4.)  لا يوجد رسوم اشتراك")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("  5.) أنت من يحدد رسوم الخدمة التي تقدمها")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("  6.) رسوم الخدمة يتم تحويلها حسابك البنكي")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy(" 7.) بإمكانك إدارة حسابك ومعلوماتك ضمن التطبيق")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("إذا كنت ممن يملكون الخبرة والمهارة في نوعية الخدمة التي تقدمها، بإمكانك تقديم طلب الاشتراك المبدئي من خلال الرابط التالي")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("####")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("_سنقوم بإبلاغك فور إطلاق التطبيق بشكل رسمي._")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("حظا طيبا")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("وشكرا")
    pyautogui.hotkey("ctrl", "v")
    #END OF ARABIC
    pyautogui.press('enter')

    #English Content# hardcoding the contetnt to get a well formatted message otherwise message will not looking good to read
    #
    pyautogui.typewrite("Hello,")
    pyautogui.hotkey("shift", "enter")
    pyautogui.hotkey("shift", "enter")
    pyautogui.typewrite("##### is pleased to invite all freelance professional service providers to join our upcoming local service provider application exclusively developed for Saudi Arabia. The advantages of our app are,")
    pyautogui.hotkey("shift", "enter")
    pyautogui.hotkey("shift", "enter")
    pyautogui.typewrite("  1.) You will get free marketing")
    pyautogui.hotkey("shift", "enter")
    pyautogui.typewrite("  2.) A reliable & trustworthy relationship")
    pyautogui.hotkey("shift", "enter")
    pyautogui.typewrite("  3.) You can work on your time")
    pyautogui.hotkey("shift", "enter")
    pyautogui.typewrite("  4.) You decide the service charge for your work")
    pyautogui.hotkey("shift", "enter")
    pyautogui.typewrite("  5.) All payments will transfer to your bank account")
    pyautogui.hotkey("shift", "enter")
    pyautogui.typewrite("  6.) You can manage everything within the application itself and a lot more")
    pyautogui.hotkey("shift", "enter")
    pyautogui.hotkey("shift", "enter")
    pyautogui.typewrite("If you have the skill and you are professional in it. Feel free to submit your application in the following form.")
    pyautogui.hotkey("shift", "enter")
    pyautogui.typewrite("Service provider registration ######")
    pyautogui.hotkey("shift", "enter")
    pyautogui.hotkey("shift", "enter")
    pyautogui.typewrite("_Please note that we will notify you once the app gets published in the application markets_")
    pyautogui.hotkey("shift", "enter")
    pyautogui.hotkey("shift", "enter")
    pyautogui.typewrite("Good Luck! & Thank you")
    time.sleep(1) # 1 secs delay
    pyautogui.press('enter')

    #pyautogui.hotkey("ctrl", "v")
    #pyautogui.typewrite(wa_msg)# works for English

   
    #pyautogui.press('enter')

#Get mobile numbers from excel
df = pd.read_excel(r'G:\Whauto\data\mob.xlsx')
#print(df)

for index, row in df.iterrows():
   # print (row['mob'])
    send_whatsapp_message(row['mob'])

