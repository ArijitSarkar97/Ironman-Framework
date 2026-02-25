from pages.base_page import BasePage
import allure

class AutomationTestingPraPage(BasePage):
    # --- Locators (format: "locator_type", "locator_value") ---
    HOME_A_LOCATOR = ("xpath", "(//a[normalize-space()='Home'])[1]")
    UDEMY_COURSES_A_LOCATOR = ("link text", "Udemy Courses")
    ONLINE_TRAININGS_A_LOCATOR = ("link text", "Online Trainings")
    BLOG_A_LOCATOR = ("xpath", "(//a[normalize-space()='Blog'])[1]")
    PLAYWRIGHTPRACTICE_A_LOCATOR = ("link text", "PlaywrightPractice")
    EL_1307673142697428135_A_LOCATOR = ("name", "1307673142697428135")
    GUI_ELEMENTS_A_LOCATOR = ("link text", "GUI Elements")
    NAME_INPUT_LOCATOR = ("id", "name")
    EMAIL_INPUT_LOCATOR = ("id", "email")
    PHONE_INPUT_LOCATOR = ("id", "phone")
    TEXTAREA_TEXTAREA_LOCATOR = ("tag name", "textarea")
    MALE_INPUT_LOCATOR = ("id", "male")
    FEMALE_INPUT_LOCATOR = ("id", "female")
    SUNDAY_INPUT_LOCATOR = ("id", "sunday")
    MONDAY_INPUT_LOCATOR = ("id", "monday")
    TUESDAY_INPUT_LOCATOR = ("id", "tuesday")
    WEDNESDAY_INPUT_LOCATOR = ("id", "wednesday")
    THURSDAY_INPUT_LOCATOR = ("id", "thursday")
    FRIDAY_INPUT_LOCATOR = ("id", "friday")
    SATURDAY_INPUT_LOCATOR = ("id", "saturday")
    COUNTRY_SELECT_LOCATOR = ("id", "country")
    COLORS_SELECT_LOCATOR = ("id", "colors")
    ANIMALS_SELECT_LOCATOR = ("id", "animals")
    DATEPICKER_INPUT_LOCATOR = ("id", "datepicker")
    TXTDATE_INPUT_LOCATOR = ("id", "txtDate")
    START_DATE_INPUT_LOCATOR = ("id", "start-date")
    END_DATE_INPUT_LOCATOR = ("id", "end-date")
    SUBMIT_BUTTON_LOCATOR = ("class name", "submit-btn")
    COMMENTS__ATOM_A_LOCATOR = ("link text", "Comments (Atom)")
    SINGLEFILEINPUT_INPUT_LOCATOR = ("id", "singleFileInput")
    UPLOAD_SINGLE_FILE_BUTTON_LOCATOR = ("xpath", "//button[normalize-space()='Upload Single File']")
    MULTIPLEFILESINPUT_INPUT_LOCATOR = ("id", "multipleFilesInput")
    UPLOAD_MULTIPLE_FILES_BUTTON_LOCATOR = ("xpath", "//button[normalize-space()='Upload Multiple Files']")
    INPUT_INPUT_LOCATOR = ("xpath", '//*[@id="productTable"]/tbody/tr[1]/td[4]/input')
    EL_1_A_LOCATOR = ("link text", "1")
    EL_2_A_LOCATOR = ("link text", "2")
    EL_3_A_LOCATOR = ("link text", "3")
    EL_4_A_LOCATOR = ("link text", "4")
    ELEMENT_259_A_LOCATOR = ("class name", "wikipedia-search-wiki-link")
    WIKIPEDIA1_WIKIPEDIA_SEARCH_INPUT_INPUT_LOCATOR = ("class name", "wikipedia-search-input")
    START_BUTTON_LOCATOR = ("name", "start")
    ALERTBTN_BUTTON_LOCATOR = ("id", "alertBtn")
    CONFIRMBTN_BUTTON_LOCATOR = ("id", "confirmBtn")
    PROMPTBTN_BUTTON_LOCATOR = ("id", "promptBtn")
    NEW_TAB_BUTTON_LOCATOR = ("xpath", "//button[normalize-space()='New Tab']")
    POPUP_BUTTON_LOCATOR = ("id", "PopUp")
    POINT_ME_BUTTON_LOCATOR = ("class name", "dropbtn")
    MOBILES_A_LOCATOR = ("link text", "Mobiles")
    LAPTOPS_A_LOCATOR = ("link text", "Laptops")
    FIELD1_INPUT_LOCATOR = ("xpath", '//*[@id="field1"]')
    FIELD2_INPUT_LOCATOR = ("xpath", '//*[@id="field2"]')
    COPY_TEXT_BUTTON_LOCATOR = ("xpath", "//button[normalize-space()='Copy Text']")
    AMOUNT_INPUT_LOCATOR = ("id", "amount")
    COMBOBOX_INPUT_LOCATOR = ("id", "comboBox")
    APPLE_A_LOCATOR = ("id", "apple")
    LENOVO_A_LOCATOR = ("id", "lenovo")
    DELL_A_LOCATOR = ("id", "dell")
    ERRORCODE_400_A_LOCATOR = ("link text", "Errorcode 400")
    ERRORCODE_401_A_LOCATOR = ("link text", "Errorcode 401")
    ERRORCODE_403_A_LOCATOR = ("link text", "Errorcode 403")
    ERRORCODE_404_A_LOCATOR = ("link text", "Errorcode 404")
    ERRORCODE_408_A_LOCATOR = ("link text", "Errorcode 408")
    ERRORCODE_500_A_LOCATOR = ("link text", "Errorcode 500")
    ERRORCODE_502_A_LOCATOR = ("link text", "Errorcode 502")
    ERRORCODE_503_A_LOCATOR = ("link text", "Errorcode 503")
    INPUT1_INPUT_LOCATOR = ("name", "input1")
    BTN1_BUTTON_LOCATOR = ("xpath", "(//button[normalize-space()='Submit'])[2]")
    INPUT2_INPUT_LOCATOR = ("name", "input2")
    BTN2_BUTTON_LOCATOR = ("xpath", "(//button[normalize-space()='Submit'])[3]")
    INPUT3_INPUT_LOCATOR = ("name", "input3")
    BTN3_BUTTON_LOCATOR = ("xpath", "(//button[normalize-space()='Submit'])[4]")
    HIDDEN_ELEMENTS___AJAX_A_LOCATOR = ("link text", "Hidden Elements & AJAX")
    DOWNLOAD_FILES_A_LOCATOR = ("link text", "Download Files")
    YOUTUBE_A_LOCATOR = ("link text", "Youtube")
    MERRYMOONMARY_A_LOCATOR = ("link text", "merrymoonmary")
    BLOGGER_A_LOCATOR = ("link text", "Blogger")

    def __init__(self, driver):
        super().__init__(driver)

    # --- Actions ---
    # --- Actions ---
    @allure.step("Get home_a text")
    def get_home_a_text(self):
        return self.get_text(self.HOME_A_LOCATOR)

    @allure.step("Get udemy_courses_a text")
    def get_udemy_courses_a_text(self):
        return self.get_text(self.UDEMY_COURSES_A_LOCATOR)

    @allure.step("Get online_trainings_a text")
    def get_online_trainings_a_text(self):
        return self.get_text(self.ONLINE_TRAININGS_A_LOCATOR)

    @allure.step("Get blog_a text")
    def get_blog_a_text(self):
        return self.get_text(self.BLOG_A_LOCATOR)

    @allure.step("Get playwrightpractice_a text")
    def get_playwrightpractice_a_text(self):
        return self.get_text(self.PLAYWRIGHTPRACTICE_A_LOCATOR)

    @allure.step("Get el_1307673142697428135_a text")
    def get_el_1307673142697428135_a_text(self):
        return self.get_text(self.EL_1307673142697428135_A_LOCATOR)

    @allure.step("Get gui_elements_a text")
    def get_gui_elements_a_text(self):
        return self.get_text(self.GUI_ELEMENTS_A_LOCATOR)

    @allure.step("Fill name_input with '{text}'")
    def fill_name_input(self, text):
        self.enter_text(self.NAME_INPUT_LOCATOR, text)

    @allure.step("Fill email_input with '{text}'")
    def fill_email_input(self, text):
        self.enter_text(self.EMAIL_INPUT_LOCATOR, text)

    @allure.step("Fill phone_input with '{text}'")
    def fill_phone_input(self, text):
        self.enter_text(self.PHONE_INPUT_LOCATOR, text)

    @allure.step("Fill textarea_textarea with '{text}'")
    def fill_textarea_textarea(self, text):
        self.enter_text(self.TEXTAREA_TEXTAREA_LOCATOR, text)

    @allure.step("Fill male_input with '{text}'")
    def fill_male_input(self, text):
        self.enter_text(self.MALE_INPUT_LOCATOR, text)

    @allure.step("Fill female_input with '{text}'")
    def fill_female_input(self, text):
        self.enter_text(self.FEMALE_INPUT_LOCATOR, text)

    @allure.step("Fill sunday_input with '{text}'")
    def fill_sunday_input(self, text):
        self.enter_text(self.SUNDAY_INPUT_LOCATOR, text)

    @allure.step("Fill monday_input with '{text}'")
    def fill_monday_input(self, text):
        self.enter_text(self.MONDAY_INPUT_LOCATOR, text)

    @allure.step("Fill tuesday_input with '{text}'")
    def fill_tuesday_input(self, text):
        self.enter_text(self.TUESDAY_INPUT_LOCATOR, text)

    @allure.step("Fill wednesday_input with '{text}'")
    def fill_wednesday_input(self, text):
        self.enter_text(self.WEDNESDAY_INPUT_LOCATOR, text)

    @allure.step("Fill thursday_input with '{text}'")
    def fill_thursday_input(self, text):
        self.enter_text(self.THURSDAY_INPUT_LOCATOR, text)

    @allure.step("Fill friday_input with '{text}'")
    def fill_friday_input(self, text):
        self.enter_text(self.FRIDAY_INPUT_LOCATOR, text)

    @allure.step("Fill saturday_input with '{text}'")
    def fill_saturday_input(self, text):
        self.enter_text(self.SATURDAY_INPUT_LOCATOR, text)

    @allure.step("Get country_select text")
    def get_country_select_text(self):
        return self.get_text(self.COUNTRY_SELECT_LOCATOR)

    @allure.step("Get colors_select text")
    def get_colors_select_text(self):
        return self.get_text(self.COLORS_SELECT_LOCATOR)

    @allure.step("Get animals_select text")
    def get_animals_select_text(self):
        return self.get_text(self.ANIMALS_SELECT_LOCATOR)

    @allure.step("Fill datepicker_input with '{text}'")
    def fill_datepicker_input(self, text):
        self.enter_text(self.DATEPICKER_INPUT_LOCATOR, text)

    @allure.step("Fill txtdate_input with '{text}'")
    def fill_txtdate_input(self, text):
        self.enter_text(self.TXTDATE_INPUT_LOCATOR, text)

    @allure.step("Fill start_date_input with '{text}'")
    def fill_start_date_input(self, text):
        self.enter_text(self.START_DATE_INPUT_LOCATOR, text)

    @allure.step("Fill end_date_input with '{text}'")
    def fill_end_date_input(self, text):
        self.enter_text(self.END_DATE_INPUT_LOCATOR, text)

    @allure.step("Click submit_button")
    def click_submit_button(self):
        self.click(self.SUBMIT_BUTTON_LOCATOR)

    @allure.step("Get comments__atom_a text")
    def get_comments__atom_a_text(self):
        return self.get_text(self.COMMENTS__ATOM_A_LOCATOR)

    @allure.step("Fill singlefileinput_input with '{text}'")
    def fill_singlefileinput_input(self, text):
        self.enter_text(self.SINGLEFILEINPUT_INPUT_LOCATOR, text)

    @allure.step("Click upload_single_file_button")
    def click_upload_single_file_button(self):
        self.click(self.UPLOAD_SINGLE_FILE_BUTTON_LOCATOR)

    @allure.step("Fill multiplefilesinput_input with '{text}'")
    def fill_multiplefilesinput_input(self, text):
        self.enter_text(self.MULTIPLEFILESINPUT_INPUT_LOCATOR, text)

    @allure.step("Click upload_multiple_files_button")
    def click_upload_multiple_files_button(self):
        self.click(self.UPLOAD_MULTIPLE_FILES_BUTTON_LOCATOR)

    @allure.step("Fill input_input with '{text}'")
    def fill_input_input(self, text):
        self.enter_text(self.INPUT_INPUT_LOCATOR, text)

    @allure.step("Get el_1_a text")
    def get_el_1_a_text(self):
        return self.get_text(self.EL_1_A_LOCATOR)

    @allure.step("Get el_2_a text")
    def get_el_2_a_text(self):
        return self.get_text(self.EL_2_A_LOCATOR)

    @allure.step("Get el_3_a text")
    def get_el_3_a_text(self):
        return self.get_text(self.EL_3_A_LOCATOR)

    @allure.step("Get el_4_a text")
    def get_el_4_a_text(self):
        return self.get_text(self.EL_4_A_LOCATOR)

    @allure.step("Get element_259_a text")
    def get_element_259_a_text(self):
        return self.get_text(self.ELEMENT_259_A_LOCATOR)

    @allure.step("Fill wikipedia1_wikipedia_search_input_input with '{text}'")
    def fill_wikipedia1_wikipedia_search_input_input(self, text):
        self.enter_text(self.WIKIPEDIA1_WIKIPEDIA_SEARCH_INPUT_INPUT_LOCATOR, text)

    @allure.step("Click start_button")
    def click_start_button(self):
        self.click(self.START_BUTTON_LOCATOR)

    @allure.step("Click alertbtn_button")
    def click_alertbtn_button(self):
        self.click(self.ALERTBTN_BUTTON_LOCATOR)

    @allure.step("Click confirmbtn_button")
    def click_confirmbtn_button(self):
        self.click(self.CONFIRMBTN_BUTTON_LOCATOR)

    @allure.step("Click promptbtn_button")
    def click_promptbtn_button(self):
        self.click(self.PROMPTBTN_BUTTON_LOCATOR)

    @allure.step("Click new_tab_button")
    def click_new_tab_button(self):
        self.click(self.NEW_TAB_BUTTON_LOCATOR)

    @allure.step("Click popup_button")
    def click_popup_button(self):
        self.click(self.POPUP_BUTTON_LOCATOR)

    @allure.step("Click point_me_button")
    def click_point_me_button(self):
        self.click(self.POINT_ME_BUTTON_LOCATOR)

    @allure.step("Get mobiles_a text")
    def get_mobiles_a_text(self):
        return self.get_text(self.MOBILES_A_LOCATOR)

    @allure.step("Get laptops_a text")
    def get_laptops_a_text(self):
        return self.get_text(self.LAPTOPS_A_LOCATOR)

    @allure.step("Fill field1_input with '{text}'")
    def fill_field1_input(self, text):
        self.enter_text(self.FIELD1_INPUT_LOCATOR, text)

    @allure.step("Fill field2_input with '{text}'")
    def fill_field2_input(self, text):
        self.enter_text(self.FIELD2_INPUT_LOCATOR, text)

    @allure.step("Click copy_text_button")
    def click_copy_text_button(self):
        self.click(self.COPY_TEXT_BUTTON_LOCATOR)

    @allure.step("Fill amount_input with '{text}'")
    def fill_amount_input(self, text):
        self.enter_text(self.AMOUNT_INPUT_LOCATOR, text)

    @allure.step("Fill combobox_input with '{text}'")
    def fill_combobox_input(self, text):
        self.enter_text(self.COMBOBOX_INPUT_LOCATOR, text)

    @allure.step("Get apple_a text")
    def get_apple_a_text(self):
        return self.get_text(self.APPLE_A_LOCATOR)

    @allure.step("Get lenovo_a text")
    def get_lenovo_a_text(self):
        return self.get_text(self.LENOVO_A_LOCATOR)

    @allure.step("Get dell_a text")
    def get_dell_a_text(self):
        return self.get_text(self.DELL_A_LOCATOR)

    @allure.step("Get errorcode_400_a text")
    def get_errorcode_400_a_text(self):
        return self.get_text(self.ERRORCODE_400_A_LOCATOR)

    @allure.step("Get errorcode_401_a text")
    def get_errorcode_401_a_text(self):
        return self.get_text(self.ERRORCODE_401_A_LOCATOR)

    @allure.step("Get errorcode_403_a text")
    def get_errorcode_403_a_text(self):
        return self.get_text(self.ERRORCODE_403_A_LOCATOR)

    @allure.step("Get errorcode_404_a text")
    def get_errorcode_404_a_text(self):
        return self.get_text(self.ERRORCODE_404_A_LOCATOR)

    @allure.step("Get errorcode_408_a text")
    def get_errorcode_408_a_text(self):
        return self.get_text(self.ERRORCODE_408_A_LOCATOR)

    @allure.step("Get errorcode_500_a text")
    def get_errorcode_500_a_text(self):
        return self.get_text(self.ERRORCODE_500_A_LOCATOR)

    @allure.step("Get errorcode_502_a text")
    def get_errorcode_502_a_text(self):
        return self.get_text(self.ERRORCODE_502_A_LOCATOR)

    @allure.step("Get errorcode_503_a text")
    def get_errorcode_503_a_text(self):
        return self.get_text(self.ERRORCODE_503_A_LOCATOR)

    @allure.step("Fill input1_input with '{text}'")
    def fill_input1_input(self, text):
        self.enter_text(self.INPUT1_INPUT_LOCATOR, text)

    @allure.step("Click btn1_button")
    def click_btn1_button(self):
        self.click(self.BTN1_BUTTON_LOCATOR)

    @allure.step("Fill input2_input with '{text}'")
    def fill_input2_input(self, text):
        self.enter_text(self.INPUT2_INPUT_LOCATOR, text)

    @allure.step("Click btn2_button")
    def click_btn2_button(self):
        self.click(self.BTN2_BUTTON_LOCATOR)

    @allure.step("Fill input3_input with '{text}'")
    def fill_input3_input(self, text):
        self.enter_text(self.INPUT3_INPUT_LOCATOR, text)

    @allure.step("Click btn3_button")
    def click_btn3_button(self):
        self.click(self.BTN3_BUTTON_LOCATOR)

    @allure.step("Get hidden_elements___ajax_a text")
    def get_hidden_elements___ajax_a_text(self):
        return self.get_text(self.HIDDEN_ELEMENTS___AJAX_A_LOCATOR)

    @allure.step("Get download_files_a text")
    def get_download_files_a_text(self):
        return self.get_text(self.DOWNLOAD_FILES_A_LOCATOR)

    @allure.step("Get youtube_a text")
    def get_youtube_a_text(self):
        return self.get_text(self.YOUTUBE_A_LOCATOR)

    @allure.step("Get merrymoonmary_a text")
    def get_merrymoonmary_a_text(self):
        return self.get_text(self.MERRYMOONMARY_A_LOCATOR)

    @allure.step("Get blogger_a text")
    def get_blogger_a_text(self):
        return self.get_text(self.BLOGGER_A_LOCATOR)

