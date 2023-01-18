from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import time, sleep
from pprint import pprint


# TODO Create a keyword list
def str_to_tuple(query_str: str):
    keyword_list = []
    query_str = query_str.lower().strip("\n")
    search_str = query_str.replace(" ", "%20").replace(",", "%2C")
    query_list = query_str.split(",")
    for keyword_str in query_list:
        key_list = keyword_str.strip(" ").split(" ")
        # print(key_list)
        for key in key_list:
            if key not in keyword_list:
                keyword_list.append(key)

    keyword_tuple = (keyword_list, search_str)
    # print(keyword_tuple)

    return keyword_tuple


# TODO Create a function to filter jobs without 'Easy Apply'
def filter_results(chrome_driver):
    # TODO Filter the results with Easy Apply option only
    # To do this, you can either maximize the screen or minimize the messages

    # TODO Minimize the messages
    icon_lst = chrome_driver.find_elements(By.TAG_NAME, "li-icon")
    for icon in icon_lst:
        icon_type = icon.get_attribute("type")
        if icon_type == "chevron-down":
            icon.click()
            break

    sleep(0.5)

    # TODO Open the filters
    all_filters_btn = chrome_driver.find_element(By.XPATH,
                                                 '/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/div/div/button')
    all_filters_btn.click()

    sleep(0.5)

    # TODO Click the Easy Apply switch button
    easy_apply_switch_btn = chrome_driver.find_element(By.XPATH,
                                                       "/html/body/div[3]/div/div/div[2]/ul/li[8]/fieldset/div/div")
    easy_apply_switch_btn.click()
    # sleep(2)

    # Selecting all the input types and clicking them doesn't work
    # switch_btn_lst = chrome_driver.find_elements(By.CLASS_NAME, "input")
    #
    # for switch_btn in switch_btn_lst:
    #     try:
    #         print(switch_btn)
    #         switch_btn.click()
    #     except ElementClickInterceptedException:
    #         print("Couldn't click the switch button")
    #     else:
    #         print("Switch clicked")
    #     finally:
    #         print("\n\n")
    #     sleep(3)

    # This doesn't work either
    # switch_btn_lst = chrome_driver.find_elements(By.TAG_NAME, 'input')
    # for switch_btn in switch_btn_lst:
    #     att_role = switch_btn.get_attribute('role')
    #     if att_role == "switch":
    #         print(att_role)
    #         try:
    #             switch_btn.click()
    #         except ElementClickInterceptedException:
    #             print("Couldn't click the switch button")
    #         else:
    #             print("Switch button clicked")
    #         finally:
    #             sleep(2)

    # TODO Close the filters windows
    filter_icon_lst = chrome_driver.find_elements(By.TAG_NAME, "li-icon")
    for icon in filter_icon_lst:
        icon_type = icon.get_attribute("type")
        if icon_type == "cancel-icon":
            icon.click()
            break

    return print("Results filtered")


class SubmitQuery:
    def __init__(self, email, password, query_str):
        self.email = email
        self.password = password

        keyword_tuple = str_to_tuple(query_str)

        self.keyword_list = keyword_tuple[0]
        self.search_str = keyword_tuple[1]

    def search(self):
        # TODO Link the webdriver
        webdriver_path = "../chromedriver 108.0.5359.71/chromedriver.exe"
        # webdriver_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

        # TODO Website links
        # signin_page = f"https://www.linkedin.com/login?emailAddress=&fromSignIn=&fromSignIn=true&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3FcurrentJobId%3D3396809097%26distance%3D25%26geoId%3D101339379%26keywords%3D{query_str}&trk=public_jobs_nav-header-signin"
        result_page_url = f"https://www.linkedin.com/jobs/search/?currentJobId=3386150777&geoId=101339379&keywords={self.search_str}&location=Nairobi%20County%2C%20Kenya&refresh=true"
        # print(result_page_url)

        # TODO Create the webdriver object
        chrome_driver = webdriver.Chrome(executable_path=webdriver_path)

        # TODO Get the start url
        chrome_driver.get(url=result_page_url)

        # Find the login button
        login_btn = chrome_driver.find_element(By.LINK_TEXT, "Sign in")

        # TODO Click the Log In button
        login_btn.click()

        # TODO Find, select and autofill the email
        email_input = chrome_driver.find_element(By.NAME, "session_key")
        email_input.send_keys(self.email)

        # TODO Find, select and autofill the password
        pass_input = chrome_driver.find_element(By.NAME, "session_password")
        pass_input.send_keys(self.password)

        # TODO Click the Sign in button to enter the job search page
        # signin_btn = chrome_driver.find_element(By.LINK_TEXT, "Sign in")
        signin_btn = chrome_driver.find_element(By.CLASS_NAME, "btn__primary--large")
        signin_btn.click()

        # TODO Filter the jobs to remain with 'Easy Apply' only
        filter_results(chrome_driver)

        # TODO Get the titles of the jobs and the companies
        job_titles_objs = chrome_driver.find_elements(By.CLASS_NAME, "job-card-list__title")
        # print(job_titles)
        company_name_objs = chrome_driver.find_elements(By.CLASS_NAME, "job-card-container__company-name")

        # TODO Create lists
        jobs_saved_list, jobs_applied_list = [], []

        for title in job_titles_objs:
            # TODO Create a list of the keywords
            keyword_list = self.keyword_list

            # TODO Get the job title, company name and job link
            job_title = title.text
            company_name = company_name_objs[job_titles_objs.index(title)].text
            job_link = title.get_attribute("href")
            # print(job_title)
            # print(company_name)
            # print(job_link)
            # print("\n")
            job_dict = {
                'Company Name': company_name,
                'Job Link': job_link,
                'Job Title': job_title
            }

            # {
            #     'Jobs Saved': [{'Company Name': "",
            #                     'Job Link': "",
            #                     'Job Title': ""},
            #                    {'Company Name': "",
            #                     'Job Link': "",
            #                     'Job Title': ""}],
            #     'Jobs Applied': [{'Company Name': "",
            #                       'Job Link': "",
            #                       'Job Title': ""},
            #                      {'Company Name': "",
            #                       'Job Link': "",
            #                       'Job Title': ""}]
            # }

            # TODO Check if the keyword(s) are in each title
            for key in keyword_list:
                # TODO Check for jobs with specific titles
                if key in title.text.lower():
                    try:
                        # TODO Click the link
                        title.click()

########################################################################################################################
                    # This is the part of code where the clicking happens

                    except ElementClickInterceptedException:
                        cancel_btn = chrome_driver.find_element(By.XPATH, '/html/body/div[3]/div/div/button')
                        
                    finally:
                        # TODO Delay
                        sleep(3)

                        # TODO Click the save button
                        # save_btn = chrome_driver.find_element(By.CLASS_NAME, "jobs-save-button")

                        # TODO Delay
                        # sleep(5)

                        # TODO Get the apply button
                        # apply_btn = chrome_driver.find_element(By.CLASS_NAME, "jobs-apply-button")
                        apply_btn = chrome_driver.find_element(By.CLASS_NAME, "jobs-s-apply")

                        # TODO Check if the button text is "Easy Apply"
                        if apply_btn.text == "Easy Apply":
                            # TODO Click the button
                            apply_btn.click()
                            sleep(3)

                            # TODO Check if there's is a
                            try:
                                # TODO Choose a resume
                                choose_btn = chrome_driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/form/div/div[2]/div/div[1]/div/div[2]/div/div[2]/button[1]')
                                choose_btn.click()
                                sleep(3)
                            except NoSuchElementException:
                                # TODO Click the "Save" or "Next" button
                                # save_btn = chrome_driver.find_element(By.CLASS_NAME, "artdeco-button")
                                next_btn = chrome_driver.find_element(By.XPATH,
                                                                      '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button')
                                next_btn.click()
                                sleep(3)

                                # TODO Choose a resume
                                choose_btn = chrome_driver.find_element(By.XPATH,
                                                                        '/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div/div[1]/div/div[2]/div/div[2]/button[1]/span')
                                choose_btn.click()

                                # TODO Click the next button
                                next_btn = chrome_driver.find_element(By.XPATH,
                                                                      '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
                                next_btn.click()
                                sleep(3)

                                # TODO Check if there is any additional questions
                                options_obj = chrome_driver.find_elements(By.TAG_NAME, 'select')
                                # print(len(options_obj))

                                if len(options_obj) == 0:
                                    # TODO Append the job
                                    jobs_applied_list.append(job_dict)
                                    sleep(3)

                                    # TODO Review the resume
                                    review_btn = chrome_driver.find_element(By.XPATH,
                                                                            '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
                                    review_btn.click()
                                    sleep(3)

                                    # TODO Submit the review
                                    review_btn = chrome_driver.find_element(By.XPATH,
                                                                            '/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[2]/button[2]')
                                    review_btn.click()

                                else:
                                    # TODO Append the job
                                    jobs_saved_list.append(job_dict)

                                    # TODO Hit the cancel icon
                                    cancel_btn = chrome_driver.find_element(By.TAG_NAME, 'li-icon')
                                    if cancel_btn.get_attribute('type') == "cancel-icon":
                                        cancel_btn.click()
                                        sleep(3)

                                    # TODO Save the job
                                    btn_list = chrome_driver.find_elements(By.TAG_NAME, 'button')
                                    for btn in btn_list:
                                        if btn.text == "Save":
                                            btn.click()
                                            sleep(3)

                                # re_btn = chrome_driver.find_element(By.XPATH, '')
                                # re_btn.click()
                            else:
                                # TODO Submit the application
                                submit_btn = chrome_driver.find_element(By.XPATH,
                                                                        '/html/body/div[3]/div/div/div[2]/div/div/form/footer/div[3]/button')
                                submit_btn.click()
                        else:
                            # TODO Append the job
                            jobs_saved_list.append(job_dict)

                            # TODO Click the save button
                            save_btn = chrome_driver.find_element(By.CLASS_NAME, 'jobs-save-button')
                            save_btn.click()

        # TODO Create a dict for the jobs list
        relevant_jobs_list = {
            'Jobs Saved': jobs_saved_list,
            'Jobs Applied': jobs_applied_list
        }

        pprint(relevant_jobs_list)
