from selenium import webdriver
url = 'https://www.youtube.com/kallehallden/videos'
browser = webdriver.Edge()
browser.get(url)
browser.find_element( "xpath",'//*[@id="video-title"]').click()