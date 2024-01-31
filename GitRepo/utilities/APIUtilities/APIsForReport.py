import requests

from utilities.readProperties import ReadConfig

class APIsForReport:
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()


    endpoint = "http://example/api"
    headers = {"Authorization": "Bearer asdasdasd"}
    jsession = ""



    def getResponseLogin(self):
        loginURL = f"{self.endpoint}/public/mobile/loginMobile/login?username={self.username}&password={self.password}"
        response = requests.get(loginURL)
        return response


    def getResponsePageID(self, cookies):
        URL = f"{self.endpoint}/manage/page/getByContext?context=text"

        response = requests.get(URL, headers=self.headers, cookies=cookies)
        print(response)
        return response


    def getResponseReportList(self, pageID, cookies):
        docListURL = f"{self.endpoint}/document/def/report/getReportList?pageId={pageID}&parameters="

        response = requests.get(docListURL, headers=self.headers, cookies=cookies)
        return response

    #spesifik bir evrağın datalarını alır
    def getResponseDoc(self, refNo):
        #login yapılır, jsession bilgisini almak için
        login_response = self.getResponseLogin()
        JSessionID = login_response.cookies.get("JSESSIONID")

        cookies = {'JSESSIONID': JSessionID}
        headers = {"Authorization": "Bearer asdasdasd"}

        #sayfa id'si almak için
        page_response = self.getResponsePageID(cookies)

        get_data = page_response.json()
        ID = get_data["id"]

        #raporları listelemek için
        report_list_response = self.getResponseReportList(ID, cookies)

        doc_list_data = report_list_response.json()

        #listelenen raporlarda spesifik bir yük no ile rapor id nin raporunun bilgilerini listeler
        doc_id = self.getReportID(doc_list_data)

        docdataurl = f"http://example//api/document/def/report/getReportData?reportId={doc_id}&referenceNo={refNo}"
        last_doc_response = requests.get(docdataurl, headers=headers, cookies=cookies)
        return last_doc_response

    def getReportID(self, doc_list_data):
        doc_id = ""
        for i in range(len(doc_list_data)):
            if doc_list_data[i]["name"] == "example3":
                doc_id = doc_list_data[i]["id"]
                print(doc_id)
                break
        return doc_id
