from selenium import webdriver

url = 'https://www.youtube.com/c/CodingTechnyks';
driver = webdriver.Chrome();
driver.get(url);
driver.find_element_by_xpath('//*[@id="movie_player"]/div[23]/div[2]/div[1]/a[2]').click();
