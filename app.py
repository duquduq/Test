from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Riot Data Dragon 최신 버전 가져오기
def get_latest_version():
    url = "https://ddragon.leagueoflegends.com/api/versions.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()[0]  # 최신 버전 반환

# 모든 챔피언 데이터 가져오기
def get_all_champions(version):
    url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/ko_KR/champion.json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()["data"]
    
    champions = []
    for champ in data.values():
        champions.append({
            "id": champ["id"],
            "name_ko": champ["name"],  # 한글 이름
            "image_url": f"https://ddragon.leagueoflegends.com/cdn/{version}/img/champion/{champ['id']}.png",
            "win_rate": "52.3%",  # 임시 데이터
            "pick_rate": "10.5%",  # 임시 데이터
            "build_images": [
                f"https://ddragon.leagueoflegends.com/cdn/{version}/img/item/3078.png",
                f"https://ddragon.leagueoflegends.com/cdn/{version}/img/item/3078.png",
                f"https://ddragon.leagueoflegends.com/cdn/{version}/img/item/3078.png",
                
            ]  # 임시 데이터
        })
    return champions




# 아이템 데이터 추가
def add_item_images(champion_data, version):
    for champion in champion_data:
        champion['build_images'] = [
            f"https://ddragon.leagueoflegends.com/cdn/{version}/img/item/{item_id}.png"
            for item_id in champion['build']
        ]
    return champion_data



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/champions')
def champions():
    latest_version = get_latest_version()
    champions = get_all_champions(latest_version)  # 모든 챔피언 데이터 가져오기
    return render_template('champions.html', champions=champions)



if __name__ == '__main__':
    app.run(debug=True)
