import random


def kelimeTüret():
    gecerli_kelime = {
        "kelime": ["kelime","kem", "kim", "lim", "mil", "eke", "elk", "ile", "ilk", "kel", "kil", "ekim", "ekme", "elem", "elim",
                   "emek", "emel", "emik", "ilme", "keme", "lime", "meke", "ekli", "elek", "elik", "ilek", "ilke",
                   "kele", "kile", "leke", "eklem", "elmek", "emlik", "ilmek", "imlek", "kelem", "melek", "melik",
                   "ekilme", "emekli", "kelime", "melike"],
        "masa": ["asma", "masa", "mas", "sam", "ama", "asa"],
        "karmakarışık": ["karmakarışık","kırışmak", "karışmak", "karmaşık", "kararmak", "ışıma", "aşırı", "kamış", "kışır", "akşam",
                         "aşama", "aşmak", "karış", "karşı", "kaşık", "maraş", "şamar", "şarkı", "kaşar", "kırım",
                         "şakak", "ırmak", "kırık", "kırma", "rakım", "akmak", "arama", "karık", "karma", "marka",
                         "rakam", "ramak", "karar", "aşım", "ışık", "akış", "arış", "aşık", "aşma", "maaş", "marş",
                         "maşa", "şama", "şira", "aşar", "şaka", "şark", "akım", "akma", "arık", "arma", "ırak", "kama",
                         "kari", "kırk", "mark", "rakı", "akak", "akar", "akra", "arak", "arka", "kara", "aşı", "kış",
                         "maş", "şam", "şık", "arş", "aşk", "kaş", "şak", "akı", "ama", "arı", "ira", "ırk", "kam",
                         "kır", "ram", "aka", "ara", "ark", "kak", "kar"],
        "kalem": ["emlak", "kalem", "kelam", "kemal", "alem", "amel", "elma", "kame", "lame", "meal", "kale",
                  "lake", "kam", "kem", "lam", "mal", "ela", "kal", "kel"],
        "bilgisayar": ["bilgisayar","galiba", "gribal", "asgari", "baysal", "sigara", "giysi", "bilgi", "gayri", "giray", "ragbi",
                       "silgi", "albay", "balya", "ilbay", "libya", "asabi", "iblis", "libas", " salya", "saray",
                       "yasal", "bilir", "birli", "biga", "gibi", "bayi", "ilgi", "yaba", "asya", "saba", "sabi",
                       "saya", "yasa", "abla", "alay", "arya", "ayal", "ayar", "ayla", "bala", "bari", "bila", "bira",
                       "biri", "riya", "yara", "arsa", "asal", "asil", "asla", "asli", "asri", "iris", "isli", "sara",
                       "lari", "lira"],
        "kitap": ["katip", "kitap", "patik", "takip", "pakt", "pati", "akit", "atik", "kap", "kip", "pak", "pat", "pik",
                  "tip", "ait", "ati", "kat", "kit", "tak", "tik"],
        "telefon": ["telefon","teflon", "fenol", "telef", "entel", "font", "lenf", "tefe", "noel", "otel", "eten", "fol", "fon",
                    "efe", "fen", "lot", "not", "ton", "net", "tel", "ten"],
        "radyo": ["radyo","yad", "oda", "oya", "dar", "ray", "yar", "ora"],
        "televizyon": ["televizyon","vizyon", "levent", "lezyon", "eziyet", "zeytin", "ziynet", "etilen", "vizon", "tevzi", "vezin",
                       "vezne", "zelve", "levye", "telve", "velet", "teyze", "izole", "ezine", "nezle", "tezli",
                       "niyet", "entel", "linet", "nitel", "vize", "evye", "veto", "volt", "evet", "evin", "evli",
                       "nevi", "veli", "ezel", "iyon", "iyot", "oley", "zile", "neye", "niye", "yele", "yeni", "yeti",
                       "yine", "etol", "noel", "otel", "elit", "elti", "enli", "eten", "etil", "etli", "tel", 'yel'],
        "çanta": ["çanta","açan", "anaç", "anat", "naat", "çan", "çat", "taç", "ana", "ant", "ata", "tan"]
    }
    return gecerli_kelime

def hesapla_puan(kelime):
    uzunluk = len(kelime)
    return uzunluk
def harfleriKaristir(kelime):
    return "".join(random.sample(kelime, len(kelime)))



def oyun():
    while True:
        print("Bir kelime bir işlem")
        gecerli_kelime = kelimeTüret()
        ana_kelime = random.choice(list(gecerli_kelime.keys()))
        karisik_kelime = harfleriKaristir(ana_kelime)
        print(f"Kelimenin harflerini kullanarak en az 3 harfden oluşan sözcükler türetmeniz gerekmektedir.: {karisik_kelime}")

        bulunan_kelimeler = []
        kelimeListesi = [i.lower() for i in gecerli_kelime[ana_kelime]]
        toplamPuan=0
        while True:
            cevap = input("Türetebildiğiniz bir kelime girin (Oyunu sonlardırmak ve skoru görmek için 'q' basınız): ").strip().lower()
            if cevap == 'q':
                break
            if cevap in bulunan_kelimeler:
                print("Bu kelime daha önce bulundu!")
            elif cevap in kelimeListesi:
                bulunan_kelimeler.append(cevap)
                puan=hesapla_puan(cevap)
                toplamPuan += puan
                print(f"Geçerli kelime! +{puan} puan")
            else:
                print("Bu kelime geçerli değil!")

        print("Oyun sona erdi, bulduğunuz kelimeler:")
        for i in bulunan_kelimeler:
            print(f"- {i}")
        print(f"Toplam puan: {toplamPuan}")

        play_again = input("Tekrar oynamak ister misiniz? (e/h): ").strip().lower()
        if play_again != 'e':
            print("Teşekkürler!")
            break


if __name__ == "__main__":
    oyun()
