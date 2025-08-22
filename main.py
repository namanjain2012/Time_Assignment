from flask import Flask, jsonify
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/getTimeStories', methods=['GET'])
def get_time_stories():
    try:
        resp = requests.get("https://time.com/feed/")
        resp.raise_for_status()

        root = ET.fromstring(resp.content)
        items = root.findall('.//item')

        stories = []
        for item in items[:6]:
            title = item.find('title').text or ""
            link = item.find('link').text or ""
            stories.append({"title": title.strip(), "link": link.strip()})

        return jsonify(stories)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=8080)
