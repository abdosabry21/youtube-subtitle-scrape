
import json
from playwright.sync_api import sync_playwright

import requests



def extract_full_body_html(uu:str):
    # url = 'https://www.qatarliving.com/backend/api/properties/search?from=1&category=7642'
    Timeout = 90000

    with sync_playwright() as p:
        u="https://www.downloadyoutubesubtitles.com"
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(u)

        # page.wait_for_load_state("networkidle", timeout=Timeout)
        # page.wait_for_timeout(1000)
        # page.wait_for_timeout(2500)
        # page.wait_for_timeout(2500)
        page.fill("#subformbox",uu)
        page.click("#getsubtitle")
        page.wait_for_timeout(1000)
        href = page.locator('xpath=(//div[@class="d-inline-block align-self-center text-nowrap"]/a[@class="btn btn-success volatile butaen srtbutaen"])[1]').get_attribute('href')
        furl="https://www.downloadyoutubesubtitles.com"+href
        page.wait_for_timeout(1000)
        res=requests.get(furl)
        title = page.locator('xpath=//h3').text_content()[15:30]
        page.close()
        
        with open(f'{title}.srt', 'wb') as f:
            f.write(res.content)
        return title

print(extract_full_body_html("https://www.youtube.com/watch?v=D56_Cx36oGY"))