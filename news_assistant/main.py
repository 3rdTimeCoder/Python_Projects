from news_api_helper import *
from audio_helper import *


def get_input():
    user_in = ''
    valid = [1,2,3,4]

    print("1.Tech News \n2.South African News"
        "\n3. US Business News \n5.Search News Topic")
    while not user_in.isdigit() or int(user_in) not in valid:
        user_in = input("Enter Number: ")

    return int(user_in)


def get_url(choice):
    news_options = [from_tech_crunch, from_news24, business_new_from_usa, search_topic]
    return news_options[choice-1]()
        

def generate_news_string(user_in):
    url = get_url(user_in)
    res = send_request(url)
    f_res = filter_response(res)
    return f_res

def read_news(text):
    print("Preparing your news..")
    text_to_mp3(text)
    print("Reading news...")
    play_audio("text.mp3")
    print("Goodbye.")


def say_goodbye():
    play_audio("goodbye.mp3")

if __name__ == '__main__':
    user_input = get_input()
    news = generate_news_string(user_input)
    read_news(news)
    say_goodbye()