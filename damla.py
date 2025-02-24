import random
import requests


def load_valid_words():
    valid_words = {
        "kelime": ["kem", "kim", "lim", "mil", "eke", "elk", "ile", "ilk", "kel", "kil", "ekim", "ekme", "elem", "elim",
                   "emek", "emel", "emik", "ilme", "keme", "lime", "meke", "ekli", "elek", "elik", "ilek", "ilke",
                   "kele", "kile", "leke", "eklem", "elmek", "emlik", "ilmek", "imlek", "kelem", "melek", "melik",
                   "ekilme", "emekli", "kelime", "melike"],
        "masa": ["asma", "masa", "mas", "sam", "ama", "asa"],
        "karmakarışık": ["kırışmak", "karışmak", "karmaşık", "kararmak", "ışıma", "aşırı", "kamış", "kışır", "akşam",
                         "aşama", "aşmak", "karış", "karşı", "kaşık", "maraş", "şamar", "şarkı", "kaşar", "kırım",
                         "şakak", "ırmak", "kırık", "kırma", "rakım", "akmak", "arama", "karık", "karma", "marka",
                         "rakam", "ramak", "karar", "aşım", "ışık", "akış", "arış", "aşık", "aşma", "maaş", "marş",
                         "maşa", "şama", "şira", "aşar", "şaka", "şark", "akım", "akma", "arık", "arma", "ırak", "kama",
                         "kari", "kırk", "mark", "rakı", "akak", "akar", "akra", "arak", "arka", "kara", "aşı", "kış",
                         "maş", "şam", "şık", "arş", "aşk", "kaş", "şak", "akı", "ama", "arı", "ira", "ırk", "kam",
                         "kır", "ram", "aka", "ara", "ark", "kak", "kar"],
        "kalem": ["emlak", "kalem", "kelam", "kemal", "alem", "amel", "elma", "kame", "lame", "male", "meal", "kale",
                  "lake", "kam", "kem", "lam", "mal", "ela", "kal", "kel"],
        "bilgisayar": ["galiba", "gribal", "asgari", "baysal", "sigara", "giysi", "bilgi", "gayri", "giray", "ragbi",
                       "silgi", "albay", "balya", "ilbay", "libya", "asabi", "iblis", "libas", "salya", "saray",
                       "yasal", "bilir", "birli", "biga", "gibi", "bayi", "ilgi", "yaba", "asya", "saba", "sabi",
                       "saya", "yasa", "abla", "alay", "arya", "ayal", "ayar", "ayla", "bala", "bari", "bila", "bira",
                       "biri", "riya", "yara", "arsa", "asal", "asil", "asla", "asli", "asri", "iris", "isli", "sara",
                       "lari", "lira"],
        "kitap": ["katip", "kitap", "patik", "takip", "pakt", "pati", "akit", "atik", "kap", "kip", "pak", "pat", "pik",
                  "tip", "ait", "ati", "kat", "kit", "tak", "tik"],
        "telefon": ["teflon", "fenol", "telef", "entel", "font", "lenf", "tefe", "noel", "otel", "eten", "fol", "fon",
                    "efe", "fen", "lot", "not", "ton", "net", "tel", "ten"],
        "radyo": ["yad", "oda", "oya", "dar", "ray", "yar", "ora"],
        "televizyon": ["vizyon", "levent", "lezyon", "eziyet", "zeytin", "ziynet", "etilen", "vizon", "tevzi", "vezin",
                       "vezne", "zelve", "levye", "telve", "velet", "teyze", "izole", "ezine", "nezle", "tezli",
                       "niyet", "entel", "linet", "nitel", "vize", "evye", "veto", "volt", "evet", "evin", "evli",
                       "nevi", "veli", "ezel", "iyon", "iyot", "oley", "zile", "neye", "niye", "yele", "yeni", "yeti",
                       "yine", "etol", "noel", "otel", "elit", "elti", "enli", "eten", "etil", "etli"],
        "çanta": ["açan", "anaç", "anat", "naat", "çan", "çat", "taç", "ana", "ant", "ata", "tan"]
    }
    return valid_words


def is_turkish_word(word):
    return word in sum(load_valid_words().values(), [])


def play_game():
    while True:
        print("Kelime türetme oyununa hoş geldiniz!")
        valid_words = load_valid_words()
        base_word = random.choice(list(valid_words.keys()))
        print(f"Ana kelimeniz: {base_word}")

        found_words = []
        valid_word_list = [word.lower() for word in valid_words[base_word]]

        while True:
            user_input = input("Türetebildiğiniz bir kelime girin (Çıkmak için 'q'): ").strip().lower()
            if user_input == 'q':
                break
            if user_input in found_words:
                print("Bu kelimeyi zaten buldunuz!")
            elif user_input in valid_word_list or is_turkish_word(user_input):
                found_words.append(user_input)
                print("Geçerli kelime!")
            else:
                print("Bu kelime geçerli değil!")

        print("Oyun sona erdi, bulduğunuz kelimeler:")
        for word in found_words:
            print(f"- {word}")

        play_again = input("Tekrar oynamak ister misiniz? (e/h): ").strip().lower()
        if play_again != 'e':
            print("Teşekkürler, iyi günler!")
            break


if __name__ == "__main__":
    play_game()
