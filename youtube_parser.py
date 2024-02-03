from parser_entities import YouTubeParser


def main():
    youtube_parser = YouTubeParser()

    channels = [
        "https://www.youtube.com/@raily",
        "https://www.youtube.com/@adorplayer",
        "https://www.youtube.com/@soderlingoc",
        "https://www.youtube.com/@sodyan",
        "https://www.youtube.com/@restlgamer",
        "https://www.youtube.com/@drozhzhin",
        "https://www.youtube.com/@empatia_manuchi",
        "https://www.youtube.com/@barsikofficial",
        "https://www.youtube.com/@diodand",
        "https://www.youtube.com/@nedohackerslite"
    ]

    for channel in channels:
        video_data = youtube_parser.parse_channel(channel)
        if video_data:
            youtube_parser.insert_data_to_db(video_data)

    youtube_parser.close_connections()
    youtube_parser.cleanup()


if __name__ == '__main__':
    main()
