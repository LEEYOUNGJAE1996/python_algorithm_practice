import requests

url = "https://m.itsmung.store/image/create"
headers = {
    "Content-Type": "multipart/form-data",
    "deviceId": "12345678"  # deviceId를 적절한 값으로 대체해야 합니다.
}
files = {
    "image": open("D:/forTrainYolo/newDog/KakaoTalk_20230613_183422804.jpg", "rb")  # 전송할 이미지 파일의 경로와 이름을 적절하게 변경해야 합니다.
}

response = requests.post(url, headers=headers, files=files)

if response.status_code == 200:
    print("이미지 업로드 성공")
else:
    print("이미지 업로드 실패:", response.text)