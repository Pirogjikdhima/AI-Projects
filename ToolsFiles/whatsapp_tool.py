import subprocess
import time

import pyautogui
import pyperclip


def open_whatsapp() -> None:
    """Opens WhatsApp using a batch file."""
    bat_file_path = ".bat"
    subprocess.run([bat_file_path], shell=True)


def stop_whatsapp() -> None:
    """Stops WhatsApp by locating and clicking on the exit element."""
    locate_element("data/Whatsapp/exit.png")


def locate_element(photo: str, conf_level: float = 0.9) -> None:
    """Locates an element on the screen by image and clicks it.

    Args:
        photo (str): Path to the image file used for locating the element.
        conf_level (float, optional): Confidence level for image matching. Defaults to 0.9.

    Raises:
        Exception: If an error occurs during element location.
    """
    try:
        start_time = time.time()
        element = None
        while not element and (time.time() - start_time) < 5:
            element = pyautogui.locateOnScreen(photo, confidence=conf_level)
            time.sleep(0.1)

        if element:
            x, y = pyautogui.center(element)
            pyautogui.dragTo(x, y)
            pyautogui.click(button="left")
        else:
            print(f"Element not found: {photo}")
    except Exception as e:
        print("An error occurred: ", e)


def session(name: str, message: str) -> None:
    """Opens WhatsApp, sends a message to a specific contact, and closes WhatsApp.

    Args:
        name (str): Name of the contact to whom the message will be sent.
        message (str): The message to be sent.
    """
    open_whatsapp()
    time.sleep(2)

    locate_element("data/Whatsapp/search.png")
    pyautogui.write(name)

    x, y = pyautogui.position().x, pyautogui.position().y
    pyautogui.dragTo(x + 46, y + 118)

    time.sleep(1)
    pyautogui.click(button="left")

    time.sleep(1)
    locate_element("data/Whatsapp/type.png")

    pyperclip.copy(message)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("enter")
    time.sleep(2)
    stop_whatsapp()

