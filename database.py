import sqlite3
import object
from contextlib import closing

conn = None

def connect():
    global conn
    if not conn:
        conn = sqlite3.connect("Cards.db")
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def addCard(card):
    query = '''INSERT INTO Cards (card_image, player_name, player_position, player_team)
                VALUES ( ?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(query, (card.image, card.name, card.position, card.team))
        conn.commit()
    print(card.name, "was added.")

def deleteCard(card):
    query = '''DELETE From Cards
            WHERE player_name = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (card,))
        conn.commit()
    print(card, "was deleted.")

def viewCards():
    cards = []
    query = '''SELECT * From Cards
            ORDER BY card_ID '''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()
        for result in results:
            card = object.Card(result["card_image"], result["player_name"], result["player_position"], result["player_team"])
            cards.append(card)
    return cards

def main():
    connect()

    close()

if __name__ == "__main__":
    main()