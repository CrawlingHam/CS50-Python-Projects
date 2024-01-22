# biobiljetter (swedish) = movie tickets (english)


 #input från användaren
antal_biljetter = int(input("Hur många biljetter vill du köpa? "))
antal_barn = int(input("Hur många av er är under 18 år? "))
föreställning_start = int(input("När börjar föreställningen? "))

    
vuxen_biljett = 100
barn_biljett = 50

    # 0m föreställninen startar efter kl:18
antal_vuxna = antal_biljetter - antal_barn
vuxna_biljetter_kostnad = antal_vuxna * vuxen_biljett
barn_biljetter_kostnad = antal_barn * barn_biljett
biljetter_kostnad_summa = barn_biljetter_kostnad + vuxna_biljetter_kostnad


if föreställning_start > 18:
    print(f"Biljetterna kostar sammanlagt {biljetter_kostnad_summa} kr")

# Ex:
    # 10 biljetter (10 pers varav 8 är barn)
    # antal vuxna = 10 - 8 = 2 vuxna
    # vuxna_biljetter_kostnad = 2 vuxna * 100/vuxen = 200 kr
    # barn_biljetter_kostnad = 8 barn * 50/barn = 400 kr
    # biljett_kostnad_summa  = 400 + 200 = 600 kr


            # 0m föreställninen börjar före kl:18
else:
    biljetter_kostnad_summa2 = biljetter_kostnad_summa * 0.9
    print(f"Biljetterna kostar sammanlagt {biljetter_kostnad_summa2} kr")

#Ex:
    # 10 biljetter (10 pers varav 8 är barn)
    # antal vuxna = 10 - 8 = 2 vuxna
    # vuxna_biljetter_kostnad = 2 vuxna * 100/vuxen = 200 kr
    # barn_biljetter_kostnad = 8 barn * 50/barn = 400 kr
    # biljett_kostnad_summa  = 400 + 200 = 600 kr
    # biljett_sänkt_konstnad = biljett_kostnad_summa * 0.9
    # Skriv ut biljett_sänkt_konstnad
