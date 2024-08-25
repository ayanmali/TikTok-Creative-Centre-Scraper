import requests
import json
import time
from request_cookie import tt_cookie

filename = "tiktok-ads-data.json"
cookie = tt_cookie

"""
Searches TikTok Top Ads Dashboard for all available ads with the given search parameters.
"""
def search_all_ads():
    url = "https://ads.tiktok.com/creative_radar_api/v1/top_ads/v2/list"

    # Defining search parameters; multiple selections for the same parameter are included in the same string separated by a comma and no space
    query = ""
    # objectives = ["Traffic", "App Installs", "Conversions", "Video Views", "Reach", "Lead Generation", "Product sales"]
    # Objective number corresponds to the 1-based index of the objective in the objectives list
    # objective = "3"
    # Corresponds to conversions, video views, reach, and product sales
    objective = "3,4,15,5"
    # objective = "7,3"
    period = 30
    page = 1
    limit = 20
    # Non-app/game related ads
    industries = "22000000000,16000000000,12000000000,14000000000,24000000000,30000000000,10000000000,13000000000,27000000000,29000000000,21000000000,18000000000,26000000000,23000000000,19000000000,28000000000,15000000000,17000000000,11000000000"
    # for_you, reach, ctr, play_2s_rate, play_6s_rate, cvr, likes
    order_by = "for_you"
    # UK = GB, Canada = CA, Australia = AU
    country = "US"

    # querystring = {"objective":f"{objective}","period":f"{period}","industry":"22000000000,16000000000,12000000000,14000000000,24000000000,30000000000,10000000000,13000000000,27000000000,29000000000,21000000000,18000000000,26000000000,23000000000,19000000000,28000000000,15000000000,17000000000,11000000000","page":f"{page}","limit":f"{limit}","order_by":f"{order_by}","country_code":f"{country}"}
    querystring = {"page":f"{page}", "limit":f"{limit}", "keyword":query, "period":f"{period}", "country_code":f"{country}", "industry":industries, "objective":f"{objective}", "order_by":f"{order_by}"}

    # Setting the timestamp for the request header
    timestamp = int(time.time())

    countries_referer_query = country.replace(",", "%2C")
    objective_referer_query = objective.replace(",", "%2C")
    _ = industries.replace("0", "")
    industries_referer_query = _.replace(",", "%2C")

    payload = ""
    headers = {
        #"cookie": "uid_tt=1af43bcda1ad9ca76b382215a3b315812abb87f1f253e1642dec7a6bbd74ca8e; uid_tt_ss=1af43bcda1ad9ca76b382215a3b315812abb87f1f253e1642dec7a6bbd74ca8e; sid_tt=334d748c9c6953b952fdf300a5ed1910; sessionid=334d748c9c6953b952fdf300a5ed1910; sessionid_ss=334d748c9c6953b952fdf300a5ed1910; tt-target-idc=useast1a; store-idc=maliva; store-country-code=ca; store-country-code-src=uid; csrftoken=; _ttp=2fbXIAXnpqG7cu2X6RcPV2M2jja; sid_guard_tiktokseller=5061356a12c46b07586bf2c653983162%7C1714070716%7C5180986%7CMon%2C+24-Jun-2024+17%3A55%3A02+GMT; tt_chain_token=SOCsziXETD9xZYbyElnk2Q==; sid_guard=334d748c9c6953b952fdf300a5ed1910%7C1718070575%7C15552000%7CSun%2C+08-Dec-2024+01%3A49%3A35+GMT; sid_ucp_v1=1.0.0-KDY0MDY3ZjMxMTIxOGIyNmM2MjE3NTRlMTU0ZWZiZjJjN2ZhNDQ2YjMKIAiGiIiMq5Sp7GIQr9qeswYYswsgDDDdyeKWBjgEQOoHEAMaBm1hbGl2YSIgMzM0ZDc0OGM5YzY5NTNiOTUyZmRmMzAwYTVlZDE5MTA; ssid_ucp_v1=1.0.0-KDY0MDY3ZjMxMTIxOGIyNmM2MjE3NTRlMTU0ZWZiZjJjN2ZhNDQ2YjMKIAiGiIiMq5Sp7GIQr9qeswYYswsgDDDdyeKWBjgEQOoHEAMaBm1hbGl2YSIgMzM0ZDc0OGM5YzY5NTNiOTUyZmRmMzAwYTVlZDE5MTA; tta_attr_id_mirror=0.1718072224.7379064015105835025; lang_type=en; i18next=en; passport_csrf_token=60384911ca3efdfed5c0e6392ab5fc52; passport_csrf_token_default=60384911ca3efdfed5c0e6392ab5fc52; s_v_web_id=verify_lzppm0or_G8civZcL_vqbq_4Msu_AjDC_LvRn73f6DpyT; passport_auth_status_ads=7858c860742e41c1df102c137d23e1ae%2C; passport_auth_status_ss_ads=7858c860742e41c1df102c137d23e1ae%2C; sso_uid_tt_ads=5fbe9ef4c6bb153d8229fa26d749f932ebc9d7c9785e5c21caee0fc01a821133; sso_uid_tt_ss_ads=5fbe9ef4c6bb153d8229fa26d749f932ebc9d7c9785e5c21caee0fc01a821133; sso_user_ads=68d3d6f6b1347989255ebcd48eef1009; sso_user_ss_ads=68d3d6f6b1347989255ebcd48eef1009; sid_ucp_sso_v1_ads=1.0.0-KDI0ZDQ4MDMzY2U0NzZkMWRlYzRjYWQ2OTIyMzdkMmFjODhiZmQyNmEKHwiRiI_cupqmlWYQ-K3jtQYYzCQgDDD2saqxBjgIQBIQAxoDc2cxIiA2OGQzZDZmNmIxMzQ3OTg5MjU1ZWJjZDQ4ZWVmMTAwOQ; ssid_ucp_sso_v1_ads=1.0.0-KDI0ZDQ4MDMzY2U0NzZkMWRlYzRjYWQ2OTIyMzdkMmFjODhiZmQyNmEKHwiRiI_cupqmlWYQ-K3jtQYYzCQgDDD2saqxBjgIQBIQAxoDc2cxIiA2OGQzZDZmNmIxMzQ3OTg5MjU1ZWJjZDQ4ZWVmMTAwOQ; odin_tt=9618a636410707ea4a68a90b4253fb88683a5d559076a769e7a6760d8617c6a0e0dee8b721ef9a53d7f4ae114f4e3caa754695d77703633d82aa9ee4fdba1039; sid_guard_ads=b4529da93adf3b15d9f16040666207c4%7C1723389690%7C5183998%7CThu%2C+10-Oct-2024+15%3A21%3A28+GMT; uid_tt_ads=7eb82d72e3345c7a30b179d4b7279d7fcebbdfaa501038bba2083da7c93a951e; uid_tt_ss_ads=7eb82d72e3345c7a30b179d4b7279d7fcebbdfaa501038bba2083da7c93a951e; sid_tt_ads=b4529da93adf3b15d9f16040666207c4; sessionid_ads=b4529da93adf3b15d9f16040666207c4; sessionid_ss_ads=b4529da93adf3b15d9f16040666207c4; sid_ucp_v1_ads=1.0.0-KDEzNjRjOWQ3YjI4N2M5N2NhMTRkZGM4NDhkMjA4NTQ0MzAyM2UxZTMKGQiRiI_cupqmlWYQ-q3jtQYYzCQgDDgIQBIQAxoDc2cxIiBiNDUyOWRhOTNhZGYzYjE1ZDlmMTYwNDA2NjYyMDdjNA; ssid_ucp_v1_ads=1.0.0-KDEzNjRjOWQ3YjI4N2M5N2NhMTRkZGM4NDhkMjA4NTQ0MzAyM2UxZTMKGQiRiI_cupqmlWYQ-q3jtQYYzCQgDDgIQBIQAxoDc2cxIiBiNDUyOWRhOTNhZGYzYjE1ZDlmMTYwNDA2NjYyMDdjNA; ttwid=1%7CE390XvNLg2m7_PxWQ6J6DBG6xNq9NZXxWTM5NCKNmqo%7C1723391746%7C01dff39ac08b5ca06719457f01e372c9fa0915020458a92d92a184fd55d2592e; msToken=9vAQ2Zwx-wnSrmE3b76xRO5cWNBrBlvq217VwXcpYb3j29kpEK8UGWilkfl4FXxU2NPUQoQLKvdlAfxiYY8IOgDE-akRuE_kYGQ5i3G3pjQDqaQ0xjZyIifBMH8=; msToken=9vAQ2Zwx-wnSrmE3b76xRO5cWNBrBlvq217VwXcpYb3j29kpEK8UGWilkfl4FXxU2NPUQoQLKvdlAfxiYY8IOgDE-akRuE_kYGQ5i3G3pjQDqaQ0xjZyIifBMH8=",
        "cookie": cookie,
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.8",
        "anonymous-user-id": "d3e22bbe-5af5-4fe6-9242-cdbf43cbdc34",
        "cache-control": "no-cache",
        "connection":"keep-alive",
        "host": "ads.tiktok.com",
        "lang": "en",
        "pragma": "no-cache",
        "priority": "u=1, i",
        #"referer": f"https://ads.tiktok.com/business/creativecenter/inspiration/topads/pc/en?period={period}&region={countries_referer_query}&industry={industries_referer_query}&object={objective_referer_query}",
        "referer": f"https://ads.tiktok.com/business/creativecenter/inspiration/topads/pad/en?period={period}&region={countries_referer_query}&industry={industries_referer_query}&object={objective_referer_query}",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Brave\";v=\"127\", \"Chromium\";v=\"127\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "timestamp": f"{timestamp}",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "user-sign": "915f03facb00ec0f",
        "web-id": "7361860423677838864"
    }

    return requests.request("GET", url, data=payload, headers=headers, params=querystring)

"""
Searches Top Ads Spotlight.
"""
def search_industry():
    url = "https://ads.tiktok.com/creative_radar_api/v1/education/top_ads/list"

    page = 1
    limit = 20
    # All industries to select from on this page and their corresponding IDs
    industries = {"Apparel & Accessories":"22000000000", "Beauty & Personal Care":"14000000000", "Food & Beverage":"27000000000", "Games":"25000000000", "Home Improvement":"21000000000", "Tech & Electronics":"15000000000"}
    
    querystring = {"industry":f"{industries['Apparel & Accessories']},{industries['Tech & Electronics']}","page":f"{page}","limit":f"{limit}"}

    payload = ""
    headers = {
        "cookie": "uid_tt=1af43bcda1ad9ca76b382215a3b315812abb87f1f253e1642dec7a6bbd74ca8e; uid_tt_ss=1af43bcda1ad9ca76b382215a3b315812abb87f1f253e1642dec7a6bbd74ca8e; sid_tt=334d748c9c6953b952fdf300a5ed1910; sessionid=334d748c9c6953b952fdf300a5ed1910; sessionid_ss=334d748c9c6953b952fdf300a5ed1910; tt-target-idc=useast1a; store-idc=maliva; store-country-code=ca; store-country-code-src=uid; csrftoken=; _ttp=2fbXIAXnpqG7cu2X6RcPV2M2jja; sid_guard_tiktokseller=5061356a12c46b07586bf2c653983162%7C1714070716%7C5180986%7CMon%2C+24-Jun-2024+17%3A55%3A02+GMT; tt_chain_token=SOCsziXETD9xZYbyElnk2Q==; sid_guard=334d748c9c6953b952fdf300a5ed1910%7C1718070575%7C15552000%7CSun%2C+08-Dec-2024+01%3A49%3A35+GMT; sid_ucp_v1=1.0.0-KDY0MDY3ZjMxMTIxOGIyNmM2MjE3NTRlMTU0ZWZiZjJjN2ZhNDQ2YjMKIAiGiIiMq5Sp7GIQr9qeswYYswsgDDDdyeKWBjgEQOoHEAMaBm1hbGl2YSIgMzM0ZDc0OGM5YzY5NTNiOTUyZmRmMzAwYTVlZDE5MTA; ssid_ucp_v1=1.0.0-KDY0MDY3ZjMxMTIxOGIyNmM2MjE3NTRlMTU0ZWZiZjJjN2ZhNDQ2YjMKIAiGiIiMq5Sp7GIQr9qeswYYswsgDDDdyeKWBjgEQOoHEAMaBm1hbGl2YSIgMzM0ZDc0OGM5YzY5NTNiOTUyZmRmMzAwYTVlZDE5MTA; tta_attr_id_mirror=0.1718072224.7379064015105835025; lang_type=en; i18next=en; passport_csrf_token=60384911ca3efdfed5c0e6392ab5fc52; passport_csrf_token_default=60384911ca3efdfed5c0e6392ab5fc52; s_v_web_id=verify_lzppm0or_G8civZcL_vqbq_4Msu_AjDC_LvRn73f6DpyT; passport_auth_status_ads=df8bd242368b4e657a1145f2783b6a14%2C7858c860742e41c1df102c137d23e1ae; passport_auth_status_ss_ads=df8bd242368b4e657a1145f2783b6a14%2C7858c860742e41c1df102c137d23e1ae; sso_uid_tt_ads=13f35954aaba413e031d0068942967086b0ba931cc35f483c58cf34501b8da2d; sso_uid_tt_ss_ads=13f35954aaba413e031d0068942967086b0ba931cc35f483c58cf34501b8da2d; sso_user_ads=bd286f365a7e5fa04ee67bf06e508466; sso_user_ss_ads=bd286f365a7e5fa04ee67bf06e508466; sid_ucp_sso_v1_ads=1.0.0-KDIyMmZhNjM1NDdmYTVhZDYwMDMwMDE4ZDY2YTkxZTkxZDVmMjAyMDYKHwiRiI_cupqmlWYQ2t3jtQYYzCQgDDD2saqxBjgIQBIQAxoDc2cxIiBiZDI4NmYzNjVhN2U1ZmEwNGVlNjdiZjA2ZTUwODQ2Ng; ssid_ucp_sso_v1_ads=1.0.0-KDIyMmZhNjM1NDdmYTVhZDYwMDMwMDE4ZDY2YTkxZTkxZDVmMjAyMDYKHwiRiI_cupqmlWYQ2t3jtQYYzCQgDDD2saqxBjgIQBIQAxoDc2cxIiBiZDI4NmYzNjVhN2U1ZmEwNGVlNjdiZjA2ZTUwODQ2Ng; odin_tt=6fdb87cf2a761ed5741b70a349bad1eb043bd1e2ff257ac49144f4b6354b3738c295b5027fdb2e4e9f00c1c041a80e1cfe718261ff6f3a0cf132ab7980c4f281; sid_guard_ads=59f7602f2d862c9ffb2f940a804bf30f%7C1723395803%7C5183999%7CThu%2C+10-Oct-2024+17%3A03%3A22+GMT; uid_tt_ads=96fa70132fc7cb4073d96f0296726406f95be22a0c2bfa8e9aad0a93d9950851; uid_tt_ss_ads=96fa70132fc7cb4073d96f0296726406f95be22a0c2bfa8e9aad0a93d9950851; sid_tt_ads=59f7602f2d862c9ffb2f940a804bf30f; sessionid_ads=59f7602f2d862c9ffb2f940a804bf30f; sessionid_ss_ads=59f7602f2d862c9ffb2f940a804bf30f; sid_ucp_v1_ads=1.0.0-KGZmNzAxODJmOTljZWEyMzEwZjFiNTYwZjk5NGY2ODkzNjY2ODgxMmQKGQiRiI_cupqmlWYQ293jtQYYzCQgDDgIQBIQAxoDc2cxIiA1OWY3NjAyZjJkODYyYzlmZmIyZjk0MGE4MDRiZjMwZg; ssid_ucp_v1_ads=1.0.0-KGZmNzAxODJmOTljZWEyMzEwZjFiNTYwZjk5NGY2ODkzNjY2ODgxMmQKGQiRiI_cupqmlWYQ293jtQYYzCQgDDgIQBIQAxoDc2cxIiA1OWY3NjAyZjJkODYyYzlmZmIyZjk0MGE4MDRiZjMwZg; ttwid=1%7CE390XvNLg2m7_PxWQ6J6DBG6xNq9NZXxWTM5NCKNmqo%7C1723404955%7C8865287db469084852993379b1f922ef49dee7e662559d555099d939218bc53b; msToken=q-KPvdaNsn_mWazHKXCc2EXvHd8Vjt1GJaiyiVwE7EijyewI8ltZHN9q_8NSUAIMKnjXAzlyxsFdwYq6sXWUfXC3rpxmH5a_pK-ATER2I9oDhNRLG03vhDHWO8zuyi2iCL-_bg==; msToken=q-KPvdaNsn_mWazHKXCc2EXvHd8Vjt1GJaiyiVwE7EijyewI8ltZHN9q_8NSUAIMKnjXAzlyxsFdwYq6sXWUfXC3rpxmH5a_pK-ATER2I9oDhNRLG03vhDHWO8zuyi2iCL-_bg==",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.8",
        "cache-control": "no-cache",
        "lang": "en",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://ads.tiktok.com/business/creativecenter/tiktok-topads-spotlight/pc/en",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Brave\";v=\"127\", \"Chromium\";v=\"127\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "timestamp": "1723405632",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "user-sign": "0b4e020c672133e4",
        "web-id": "7361860423677838864"
    }

    return requests.request("GET", url, data=payload, headers=headers, params=querystring)

"""
Retrieves data from the analysis page of each ad retrieved from a search.
"""
def get_analysis_data():
    pass

def main():
    response = search_all_ads()

    # Converting the string into valid JSON
    response_json = json.loads(response.text)

    # Saving the response data as a JSON file for parsing
    with open('tiktok-ads-data.json', 'w', encoding='utf-8') as f:
        json.dump(response_json, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()