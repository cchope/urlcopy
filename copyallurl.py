import appscript


def safari_tabs():
    tabs = appscript.app("Safari").windows.tabs.URL()
    for tab in tabs:
        for url in tab:

        # print("URL: " + url)
        print(url)



def chrome_tabs:



def main():
    # chrome_driver = webdriver.Chrome()
    # url = chrome_driver.current_url
    # print(url)
    tabs = appscript.app("Safari").windows.tabs.URL()
    for tab in tabs:
        for url in tab:


    #     print("URL: " + url)
        print(url)

main()





