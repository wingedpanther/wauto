import subprocess
import pyautogui, time
import pyperclip
import pandas as pd



wa_msg = ""

##----WhatsApp desktop software must be installed-----##

#Get message from text file
with open ("G:\Whauto\data\msg.txt", "r",encoding="utf8") as msg_file:
    msg_body = msg_file.read().replace('\n', '')
    wa_msg = msg_body

#Function for opening whatsapp and send the message 
# Hardcoding the message here(optional, can use the above fucntion to get the message and mobile numbers as well)   
def send_whatsapp_message(mobile_num):
    #whatsapp://send?phone={}^&text={} - inline message syntax
    subprocess.Popen(["cmd", "/C", "start whatsapp://send?phone={}".format(mobile_num)], shell=True) 
    time.sleep(2) # 2 secs delay
    
    # Store the string to the clipboard(becasue typewriter fucntion does not type Arabic content)
    # Hotkey the paste command
    
    
    #ARABIC MESSAGE#
    pyperclip.copy('')
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("مرحبا حنا نافع 👋 نافع 📱 تطبيق يسهل لاصحاب العمل الحر زيادة دخلهم والوصول الى العملاء بسهوله وراحة بال")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("💡 طيب ليه نافع؟")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("⭐ راح نسوق لك مجاناً")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("⭐ نقوي ثقة العملاء في اصحاب العمل الحر")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("⭐ تقدر تشتغل في الوقت اللي يناسبك")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("⭐ مافيه رسوم اشتراك")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("⭐ انت تحدد اسعار الخدمات بنفسك")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("⭐ كل المبالغ تتحول لحسابك البنكي")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("⭐ انت مدير حسابك داخل التطبيق وتديره بطريقة الي تناسبك")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("اذا عندك الموهبة والمهارة، سجل معنا عن طريق تحميل البرنامج من متجر ابل او قوقل بلاي ")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("http://onelink.to/qjwqxp")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("ونتمنى لك يوم سعيد.")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")

    #END OF ARABIC
    pyperclip.copy('')
    pyautogui.press('enter')

    #English Content# hardcoding the contetnt to get a well formatted message otherwise message will not look good to read
    
    pyautogui.typewrite("")
    pyperclip.copy("Hello, there 👋, We are Nafae 📱  - An app that helps you to work as a freelancer with peace of mind.")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyautogui.hotkey("shift", "enter")

    pyperclip.copy("💡 Why Nafae?")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyautogui.hotkey("shift", "enter")
    
    pyperclip.copy("⭐ You will get free marketing")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("⭐ A reliable & trustworthy relationship")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("⭐ You can work on your time")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("⭐ No subscription charges")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("⭐ You decide the service charge for your work")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("⭐ All payments will transfer to your bank account")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("⭐ You can manage everything within the application itself and a lot more.")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyautogui.hotkey("shift", "enter")
 
    pyperclip.copy("If you have the skill and you are professional in it, feel free to enrol in our app by downloading from the AppStore or Google play")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyperclip.copy("http://onelink.to/qjwqxp")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("shift", "enter")
    pyautogui.hotkey("shift", "enter")
    
    
    pyautogui.typewrite("Have a nice day!")
    time.sleep(1) # 1 secs delay
    pyperclip.copy('')
    pyautogui.press('enter')

    
#Get mobile numbers from excel
df = pd.read_excel(r'E:\AFNAM\NAFAE APP\WhatsApp Marketing\Data\Test.xlsx')
#print(df)

for index, row in df.iterrows():
   # print (row['mob'])
    send_whatsapp_message(row[0])