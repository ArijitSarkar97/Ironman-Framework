from time import sleep

import allure
from selenium.webdriver.common.by import By


from pages.base_page import BasePage


class Test_HomePage(BasePage):

    myacc = (By.CSS_SELECTOR, ".header__action-item-link.hidden-pocket.hidden-lap")
    username = (By.ID, "login-customer[email]")
    password= (By.ID, "login-customer[password]")
    hovercat=(By.XPATH,"//a[@aria-controls='desktop-menu-0-4']")
    litter=(By.XPATH,"(//a[.='Litter'])[2]")
    availability=(By.XPATH,"//button[@class='collection__filter-group-name link link--secondary text--strong']")
    instock=(By.XPATH,"//input[@class='checkbox']")
    checkingfornoofitems=(By.XPATH,"//span[@class='collection__showing-count hidden-pocket hidden-lap']")
    countprod=(By.XPATH,'//div[@class="aspect-ratio "]')
    product=(By.XPATH,"//a[@class='product-item__title text--strong link']")
    addtocartbut=(By.XPATH,"//button[.='Add to cart']")
    checkout=(By.XPATH,"//button[@name='checkout']")
    mail=(By.ID,"email")
    fn=(By.XPATH,"//input[@name='firstName']")
    ln=(By.XPATH,"//input[@name='lastName']")
    address=(By.XPATH,"//input[@name='address2']")
    city=(By.XPATH,"//input[@name='city']")



    # @allure.step("login")
    # def login(self):
    #      self.click(self.myacc)
    #      self.enter_text(self.username,'varshitharc@gmail.com')
    #      self.enter_text(self.password,'newuser')

    def click_on_cat(self):
        self.hover_over_element(self.hovercat)

    def clickingonlitter(self):
        self.click(self.litter)

    def clicking_on_availability(self):
        self.click(self.availability)

    def clicking_on_instock_option(self):
        self.click(self.instock)

    def check_the_number_of_items(self):
        noofitems=self.get_text(self.checkingfornoofitems)
        no=noofitems.split()
        count=self.find_elements(self.countprod)
        self.logger.info(f'{no[5]}')
        self.logger.info(f'{len(count)}')
        assert no[5]==str(len(count)),"not matching the count"

        self.logger.info(f"validation done")

    def clickontheproduct(self):
        self.click(self.product)

    def addtocart(self):
        self.scroll_to_element(self.addtocartbut)
        self.click(self.addtocartbut)

    def checkingout(self):
        self.scroll_to_element(self.checkout)
        self.click(self.checkout)

    def fill_checkout_details(self, Email, FirstName, LastName,
                              Apartment, City):

        self.find_element(self.mail)
        self.enter_text(self.mail, Email)

        self.find_element(self.fn)
        self.enter_text(self.fn, FirstName)

        self.find_element(self.mail)
        self.enter_text(self.ln, LastName)

        self.find_element(self.address)
        self.enter_text(self.address, Apartment)

        self.find_element(self.city)
        self.enter_text(self.city, City)

        sleep(10)





