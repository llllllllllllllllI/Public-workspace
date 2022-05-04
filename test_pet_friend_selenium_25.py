import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:/Users/Vlad/config/chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

    pytest.driver.quit()


def test_show_all_pets():
    pytest.driver.implicitly_wait(5)
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('test_pet_friend_api@mail.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('123456789')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    assert pytest.driver.find_element_by_tag_name('h1').text == 'PetFriends'

    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


def test_my_pets_page():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('test_pet_friend_api@mail.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('123456789')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Нажимаем на кнопку "Мои Питомцы"
    pytest.driver.find_element_by_class_name('nav-link').click()
    # Проверяем, что открыта страница "Мои питомцы"
    assert pytest.driver.find_element_by_tag_name('h2').text == 'jgkh[tho[eog'
    # Добавляем ожидание кнопки "Добавить питомца и нажимаем на нее
    add_button = WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-outline-success')))
    add_button.click()
    # Добавляем ожидание кнопки "Закрыть" и нажимаем на нее
    close_button = WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#addPetsModal > div > div > div.modal-header > button > span')))
    close_button.click()
    # Добавляем ожидание кнопки "Выход" и нажимаем на нее
    exit_button = WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-outline-secondary')))
    exit_button.click()


