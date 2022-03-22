import json
from PIL import Image, ImageFont, ImageDraw


def word2Img(tweet_text):
    # init
    W, H = 640, 640
    font = ImageFont.truetype('./data/NotoSansTC-Regular.otf', 30)
    newim = Image.new(mode="RGB", size=(W, H))
    d = ImageDraw.Draw(newim)

    # wrap the sentense one by one
    texts = []
    for text in tweet_text.split("\n"):
        if not text:
            texts.append(text)  # empty line
        # wrap the word (English word will break sadly)
        cum_w = 0
        now_str = ""
        for ch in text:
            ch_w = font.getsize(ch)[0]
            if cum_w + ch_w > 640 - 60 * 2:
                texts.append(now_str)
                now_str = ""
                cum_w = 0
            now_str += ch
            cum_w += ch_w
        if cum_w:
            texts.append(now_str)

    # draw text on the center of image
    text = "\n".join(texts)
    d.multiline_text((60, H // 2), text, (255,255,255), anchor="lm", font=font)
    return newim


def plotImgs(imgs):
    from dash import Dash, html, dcc
    import plotly.express as px
    app = Dash(__name__)
    app.layout = html.Div(children=[
        dcc.Graph( figure=px.imshow(img, width=800, height=800) ) for img in imgs
    ])
    app.run_server(port=3001, debug=True)


if __name__ == "__main__":
    # load data
    tweets = json.load(open("tweets.json"))
    # tweet = tweets[2]
    imgs = [word2Img(tweet['text']) for tweet in tweets]
    plotImgs(imgs)
