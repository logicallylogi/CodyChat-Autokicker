from tkinter import *

from selenium.common.exceptions import *
from selenium import webdriver
from selenium.webdriver.common.by import By


def create_chrome(service=None):
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    opts.add_argument("--detach")
    opts.add_argument("--disable-client-side-phishing-detection")
    opts.add_argument("--disable-component-extensions-with-background-pages")
    opts.add_argument("--disable-default-apps")
    opts.add_argument("--disable-extensions")
    opts.add_argument("--no-default-browser-check")
    opts.add_argument("--no-first-run")
    opts.add_argument("--disable-search-engine-choice-screen")
    opts.add_argument("--no-process-per-site")
    opts.add_argument("--disable-notifications")
    opts.add_argument("--disable-prompt-on-repost")
    opts.add_argument("--noerrdialogs")
    opts.add_argument("--block-new-web-contents")
    opts.add_argument("--disable-external-intent-requests")
    opts.add_argument("--password-store=basic")
    opts.add_argument("--use-mock-keychain")
    opts.add_argument("--disable-background-networking")
    opts.add_argument("--disable-domain-reliability")
    opts.add_argument("--disable-sync")
    opts.add_argument("--in-process-gpu")
    opts.add_argument("--no-service-autorun")
    opts.add_argument("--single-process")
    opts.add_argument("--disable-blink-features=AdInterestGroupAPI BackgroundFetch")
    opts.add_argument("--disable-blink-features=BarcodeDetector CaptureController ContactsManager")
    opts.add_argument("--disable-blink-features=DeviceOrientationRequestPermission DocumentPictureInPictureAPI")
    opts.add_argument(
        "--disable-blink-features=EyeDropperAPI FaceDetector FileSystemAccess FileSystem ForceReduceMotion")
    opts.add_argument("--disable-blink-features=GetDisplayMedia HandwritingRecognition IdleDetection")
    opts.add_argument(
        "--disable-blink-features=HighlightAPI InstalledApp MachineLearningCommon MachineLearningNeuralNetwork")
    opts.add_argument(
        "--disable-blink-features=MachineLearningModelLoader MathMLCore MediaCapture NavigationApi Notifications")
    opts.add_argument("--disable-blink-features=OrientationEvent Parakeet PaymentApp PaymentRequest PictureInPicture")
    opts.add_argument("--disable-blink-features=PeriodicBackgroundSync PointerLockOptions PrivacySandboxAdsAPIs")
    opts.add_argument("--disable-blink-features=PushMessaging ScriptedSpeechRecognition ScriptedSpeechSynthesis")
    opts.add_argument(
        "--disable-blink-features=SecurePaymentConfirmation SharedAutofill SharedStorageAPI StorageBuckets")
    opts.add_argument(
        "--disable-blink-features=StorageAccessAPI StylusHandwriting TopicsAPI TouchEventFeatureDetection")
    opts.add_argument("--disable-blink-features=TranslateService WebAnimationsAPI WebAnimationsSVG WebAppLaunchHandler")
    opts.add_argument(
        "--disable-blink-features=WebAppTranslations WebAppsLockScreen WebAuth WebBluetooth WebGPU WebHID")
    opts.add_argument(
        "--disable-blink-features=WebHID WebNFC WebOTP WebPaymentAPICSP WebShare WebUSB WebXR ZeroCopyTabCapture")

    return webdriver.Chrome(opts, service=service)


def create_socket():
    try:
        d = create_chrome(service=webdriver.ChromeService(None, 4009))
        if d.session_id is None:
            raise WebDriverException
        return d
    except WebDriverException:
        d = create_chrome()
        return d


def action_menu(event):
    print("action menu opened")


def check_element():
    try:
        # Data collection grids
        message = {}
        author = {}
        data.configure(text=f"Waiting for data....")

        # Elements worth noting
        message_element = driver.find_element(By.CSS_SELECTOR, "div.my_text:hover")
        message_text_element = message_element.find_element(By.CSS_SELECTOR, "div.chat_message")

        # Grab the username so we can grab the author element
        author["username"] = message_element.find_element(By.CSS_SELECTOR, "div.btable > div.cname").text

        # Grab the author element
        author_element = driver.find_element(By.CSS_SELECTOR, "[data-name='{}']:first-child".format(author["username"]))

        # Message data
        message["content"] = message_text_element.text
        message["timestamp"] = message_element.find_element(By.CSS_SELECTOR, "div.btable > div.cdate").text

        # Author data
        author["avatar"] = author_element.get_attribute("data-av")
        author["cover"] = author_element.get_attribute("data-cover")
        author["age"] = author_element.get_attribute("data-age")
        author["country"] = author_element.get_attribute("data-country")
        author["gender"] = author_element.get_attribute("data-gender")
        author["rank"] = author_element.get_attribute("data-rank")

        # Polyfill Gender
        if author["gender"] == 2:
            author["gender"] = "Female"
        elif author["gender"] == 1:
            author["gender"] = "Male"
        else:
            author["gender"] = "Other"

        # Polyfill VIP/Guest/User
        if author["rank"] == 50:
            author["rank"] = "VIP"
        elif author["rank"] == 1:
            author["rank"] = "User"
        elif author["rank"] == 0:
            author["rank"] = "Guest"
        else:
            author["rank"] = ""

        message_details = (f'{author["rank"]} {author["username"]} ({author["age"]} year-old {author["gender"]}) in '
                           f'{author["country"]} said "{message["content"]}" at {message["timestamp"]}\n\nAvatar: '
                           f'{author["avatar"]}\nBackground: {author["cover"]}')

        data.configure(text=f"{message_details}\n\nPress Ctrl+Alt+A to open Action Menu...")
        root.after(10, check_element)
        print("Passthrough")

    except NoSuchElementException:
        print("No such element!")
        root.after(10, check_element)


driver = create_socket()
driver.get("https://chat-avenue.com/boys")

root = Tk()
root.title("Element Preview")
root.attributes('-topmost', True)
driver
root.bind("<Control-Alt-a>", action_menu)
image = PhotoImage(height=100, width=100, data="")
Label(root, image=image).pack()
data = Label(root, pady=10, padx=10, height=10, width=100, text="Waiting for data....")
data.pack()
check_element()

root.mainloop()
