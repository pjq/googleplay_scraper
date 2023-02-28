import json
import os
from typing import Any
import argparse

from google_play_scraper import app
from google_play_scraper import Sort, reviews_all, reviews


class GooglePlay:
    def app_detail(self):
        result = app(
            app_pkg,
            lang='en',  # defaults to 'en'
            country='us'  # defaults to 'us'
        )
        # print(result)
        self.write(f"app_detail_{output_file}", result)

    def app_reviews_all(self, lang="en", country="us"):
        result = reviews_all(
            app_pkg,
            sleep_milliseconds=0,  # defaults to 0
            lang=lang,  # defaults to 'en'
            country=country,  # defaults to 'us'
            sort=Sort.MOST_RELEVANT,  # defaults to Sort.MOST_RELEVANT
            count=30000,  # defaults to 100
            filter_score_with=None  # defaults to None(means all score)
        )

        # print(result)
        self.writeArray(f"app_reviews_all_{lang}_{country}_{output_file}", result)

    def write(self, file="default_output.txt", result=Any):
        print(f"write {output_file}")

        string = json.dumps(result)
        with open(file, "w") as output_f:
            output_f.write(str(string))
        #

    def writeArray(self, file="default_output.txt", result=Any):
        print(f"write {file}")

        # with open(file, "w") as output_f:
        #     output_f.write(str(result))
        with open(file, "w") as output_file:
            for review in result:
                user_name = review.get("userName", "")
                content = review.get("content", "")
                score = review.get("score", "")
                thumbs_up_count = review.get("thumbsUpCount", "")
                review_text = f"userName: {user_name}, score: {score}, thumbsUpCount: {thumbs_up_count}, content: {content}"
                output_file.write(review_text + '\n')
                # print(review_text)

    def app_reviews(self, lang="en", country="us"):
        result, continuation_token = reviews(
            app_pkg,
            lang=lang,  # defaults to 'en'
            country=country,  # defaults to 'us'
            sort=Sort.NEWEST,  # defaults to Sort.NEWEST
            count=3,  # defaults to 100
            filter_score_with=5  # defaults to None(means all score)
        )

        # print(result)
        self.writeArray(f"app_reviews_{lang}_{country}_{output_file}", result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Google Play Scraper")
    parser.add_argument("-p", "--app_pkg", type=str, default="com.google.android.apps.googlevoice", required=False,
                        help="The package name of the app to scrape")
    parser.add_argument("-x", "--http_proxy", type=str, help="The http proxy")
    parser.add_argument("-y", "--https_proxy", type=str, help="The https proxy")

    args = parser.parse_args()
    app_pkg = args.app_pkg
    output_file = f"{app_pkg}.txt"

    if args.http_proxy:
        os.environ["http_proxy"] = args.http_proxy
    if args.https_proxy:
        os.environ["https_proxy"] = args.https_proxy
    print(f"start to scraper {app_pkg}, http_proxy: {args.http_proxy} https_proxy {args.https_proxy} ")

    googleplay = GooglePlay()
    googleplay.app_detail()
    googleplay.app_reviews(lang="en", country="us")
    googleplay.app_reviews(lang="zh", country="CN")
    googleplay.app_reviews_all(lang="en", country="us")
    googleplay.app_reviews_all(lang="zh", country="CN")
