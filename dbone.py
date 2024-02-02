import psycopg2


class InsetIntoDB:
    def __init__(self):
        self.conn = psycopg2.connect(dbname='youtube_parser_db', user='youtube_parser_user',
                                     password='youtube_parser_password', host='db', port='5432')
        self.cursor = self.conn.cursor()

    @staticmethod
    def creating_table(conn, cursor):
        query = 'CREATE TABLE IF NOT EXISTS videos (video_id VARCHAR(255), channel_username VARCHAR(255), video_href VARCHAR(255));'
        cursor.execute(query)
        conn.commit()

    @staticmethod
    def insert_data_to_db(video_data, conn, cursor):
        print('insert data to db')
        for data in video_data:
            query = f"INSERT INTO videos (video_id, channel_username, video_href) VALUES ('{data[0]}', '{data[1]}', '{data[2]}')"
            cursor.execute(query)
        conn.commit()

    def main(self):
        video_data = [
            ('123', 'channel1', 'https://example.com/video1'),
            ('456', 'channel2', 'https://example.com/video2'),
        ]

        InsetIntoDB.insert_data_to_db(video_data, self.conn, self.cursor)


insert_into_db = InsetIntoDB()
insert_into_db.main()
