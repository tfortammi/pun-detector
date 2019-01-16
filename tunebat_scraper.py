def song_link_maker(song, artist):
    result = ''
    title_split = song.split(' ')
    artist_split = artist.split(' ')

    for i in range(len(title_split)):
        result += title_split[i] + '-'

    for j in range(len(artist_split)):
        result += artist_split[j] + '-'
    result = result[:len(result)-1]

    return result

def song_details(song, artist):
    import selenium as s
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome(r'C:\\\Users\\\Tammi\\\Downloads\\\chromedriver_win32\chromedriver.exe')
    driver.get('https://tunebat.com')

    id_box = driver.find_element_by_id('q')

    id_box.send_keys(song)
    search_button = driver.find_element_by_xpath("//button[@class='btn btn-default search-button']")
    search_button.click()

    song_link = song_link_maker(song, artist)
    print(song_link)
    links = [elem.get_attribute("href") for elem in driver.find_elements_by_tag_name('a')]

    for i in links:
        if song_link in i:
            driver.get(i)
            break

    site = driver.current_url

    from lxml import html
    import requests

    page = requests.get(site)
    tree = html.fromstring(page.content)


    data1 = [elem.text for elem in driver.find_elements_by_class_name('main-attribute-value')]
    data2 = []
    
    for elem in driver.find_elements_by_class_name('attribute-table-element'):
        data2.append(elem.text)
        if len(data2) == 7:
            break

    for i in range(len(data2)):
        data1.append(data2[i])
    
    data1.insert(0, song)
    
    print(data1)

song_dict = {'High Hopes': 'Kodaline'}

for song, artist in song_dict.items():
    song_details(song, artist)



