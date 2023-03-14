import time
from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I open Application URL in the Browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.magicbricks.com/property-for-sale-rent-in-Pune/residential-real-estate-Pune")
    context.driver.maximize_window()
    time.sleep(2)


@given(u'I navigate to rent tab')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"rentheading\"]").click()
    time.sleep(2)


@when(u'I open Owner Properties')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[2]/div/div/div["
                                          "1]/ul/li[1]/a").click()
    time.sleep(2)


@when(u'I click on Top Localities and preferred Property')
def step_impl(context):
    context.driver.quit()
    time.sleep(3)


@then(u'I should get Property in that Locality')
def step_impl(context):
    assert (24+10==10)


@then(u'I should access Properties in chennai')
def step_impl(context):
    context.driver.quit()


@when(u'I select the location as chennai')
def step_impl(context):
    context.driver.find_element(By.XPATH,"/html/body/header/section[1]/div/div[1]/div[2]/a").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH,"/html/body/header/section[1]/div/div[1]/div[2]/div/div[1]/div[3]/ul/li[3]/a").click()
    time.sleep(2)


@when(u'I click the search button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//*[@id=\"tabRENT\"]").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "/html/body/section/section/div/div[1]/div[3]/div[4]").click()
    time.sleep(5)


@then(u'I should get Properties in chennai')
def step_impl(context):
    context.driver.quit()


@given(u'I select chennai as the location')
def step_impl(context):
    context.driver.find_element(By.XPATH,"/html/body/header/section[1]/div/div[1]/div[2]/a").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH,"/html/body/header/section[1]/div/div[1]/div[2]/div/div[1]/div[3]/ul/li[3]/a").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH,"//*[@id=\"tabRENT\"]").click()
    time.sleep(2)


@when(u'I click on Top Agents button')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT,"Top Agents").click()
    time.sleep(5)


@then(u'I should get access to the Top Agents page in Chennai')
def step_impl(context):
    context.driver.quit()


@when(u'I click find an agent to enter agent page')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[2]/div/div/div["
                                         "4]/ul/li[3]/a").click()
    time.sleep(2)
    child_window_handle = context.driver.window_handles[-1]
    context.driver.switch_to.window(child_window_handle)
    time.sleep(2)


@when(u'I click Ask a Question option')
def step_impl(context):
    context.driver.find_element(By.ID,"rentDrop").click()
    time.sleep(2)
    context.driver.find_element(By.LINK_TEXT,"Ask a Question").click()
    time.sleep(5)


@then(u'I should get access to the Ask a Question page')
def step_impl(context):
    context.driver.quit()


@given(u'I enter into the Top Agent page')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id=\"rentheading\"]").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH,"//*[@id=\"commercialIndex\"]/header/section[2]/div/ul/li[2]/div/div/div["
                                         "4]/ul/li[3]/a").click()
    time.sleep(2)
    child_window_handle = context.driver.window_handles[-1]
    context.driver.switch_to.window(child_window_handle)
    time.sleep(2)


@when(u'I enter to Set a Property alert')
def step_impl(context):
    context.driver.find_element(By.ID,"rentDrop").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH,"//*[@id=\"staticSwiperSliderRent\"]/div[4]/ul/li[4]/a").click()
    time.sleep(2)


@when(u'I enter the valid details')
def step_impl(context):
    context.driver.find_element(By.ID,"listTypeR").click()

    time.sleep(2)
    context.driver.find_element(By.ID,"textPropertyRent").click()

    time.sleep(2)
    context.driver.find_element(By.ID,"propertyTypeRent_10053").click()

    context.driver.find_element(By.XPATH,"/html/body/div/div/div[5]/div[1]/div[3]/form/div[1]/div[1]/div[1]").click()
    time.sleep(2)
    context.driver.find_element(By.ID,"budgetRentDDList").click()

    time.sleep(2)
    context.driver.find_element(By.ID,"budgetRent_11852-11853").click()

    context.driver.find_element(By.XPATH,"/html/body/div/div/div[5]/div[1]/div[3]/form/div[1]/div[1]/div[1]").click()
    time.sleep(2)
    context.driver.find_element(By.ID,"textBedRoom").click()

    time.sleep(2)
    context.driver.find_element(By.ID,"bedrooms_11701").click()

    context.driver.find_element(By.XPATH,"/html/body/div/div/div[5]/div[1]/div[3]/form/div[1]/div[1]/div[1]").click()
    time.sleep(2)
    context.driver.find_element(By.ID,"floorPref").click()

    time.sleep(2)
    context.driver.find_element(By.XPATH,"//*[@id=\"floorPreferences\"]/div[2]/div[1]/div[1]/ul/li[3]").click()

    context.driver.find_element(By.XPATH,"/html/body/div/div/div[5]/div[1]/div[3]/form/div[1]/div[1]/div[1]").click()
    time.sleep(2)
    context.driver.find_element(By.ID,"keyword").send_keys("Erode")

    time.sleep(2)
    context.driver.find_element(By.XPATH,"//*[@id=\"keyword_suggest\"]/div[2]/span").click()

    time.sleep(2)
    context.driver.find_element(By.ID,"keywordLoc").send_keys("Perundurai, Erode")

    time.sleep(2)
    context.driver.find_element(By.XPATH,"//*[@id=\"keyword_suggest_Loc\"]/div[2]").click()

    time.sleep(2)
    context.driver.find_element(By.ID,"tnc").click()

    time.sleep(2)
    context.driver.find_element(By.ID,"postReqLoginSubmit").click()

    time.sleep(5)


@then(u'I should get to the Login Page')
def step_impl(context):
    context.driver.quit()
