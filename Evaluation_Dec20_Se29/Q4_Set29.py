import requests
api_url = "https://httpbin.org/patch"
headers = {
    "Authorization": "Bearer mytoken",
    "Content-Type": "application/json"
}
payload = { "mode": "test"}
response = requests.patch(api_url, headers=headers, json=payload)
if response.status_code == 200:
    data = response.json()
    patched_data = data.get("json", {})
    if patched_data == payload and len(patched_data) == 1:
        print(" Validation Passed: Only patched field exists.")
        print("Return Value:", patched_data)
    else:
        print(" Validation Failed: Unexpected fields present.")
        print("Return Value:", patched_data)
else:
    print("Request failed with status:", response.status_code)
    print("Response:", response.text)