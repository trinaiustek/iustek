from seleniumbase import SB

with SB(uc=True, test=True) as trina:

    if True:
        url = "https://kick.com/brutalles"
        trina.uc_open_with_reconnect(url, 5)
        trina.uc_gui_click_captcha()
        trina.sleep(1)
        trina.uc_gui_handle_captcha()
        trina.sleep(1)
        if trina.is_element_present('button:contains("Accept")'):
            trina.uc_click('button:contains("Accept")', reconnect_time=4)
        if trina.is_element_visible('#injected-channel-player'):
            while trina.is_element_visible('#injected-channel-player'):
                trina.sleep(10)
