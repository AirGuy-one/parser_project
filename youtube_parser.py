from parser_entities import YouTubeParser
import psycopg2


def main():
    #conn = psycopg2.connect(dbname='youtube_parser_db', user='youtube_parser_user', password='youtube_parser_password',
    #                        host='db', port='5432')
    #cursor = conn.cursor()

    conn, cursor = '', ''

    youtube_parser = YouTubeParser()

    channels = [
        "https://www.youtube.com/@raily",
        "https://www.youtube.com/@adorplayer",
        # "https://www.youtube.com/@soderlingoc",
        # "https://www.youtube.com/@sodyan",
        # "https://www.youtube.com/@restlgamer",
        # "https://www.youtube.com/@drozhzhin",
        # "https://www.youtube.com/@empatia_manuchi",
        # "https://www.youtube.com/@barsikofficial",
        # "https://www.youtube.com/@diodand",
        # "https://www.youtube.com/@nedohackerslite"
    ]

    for channel in channels:
        video_data = youtube_parser.parse_channel(channel)
        print(video_data)
        youtube_parser.insert_data_to_db(video_data, conn, cursor)

    #youtube_parser.cleanup()
    #cursor.close()
    #conn.close()


if __name__ == '__main__':
    main()
