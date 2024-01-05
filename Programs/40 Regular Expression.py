import re

pattern = r"[A-Z]+ilm"
text = "October 1 is a 2014 Nigerian psycho­logical " \
       "thriller film written by Tunde Babalola, produced " \
       "and directed by Kunle Afolayan (pictured), and starring Sadiq Daba, " \
       "Kayode Olaiya, and Demola Adedoyin. In the film, Inspector Danladi Waziri (Daba) " \
       "investigates the killings of young women in a village in Western Nigeria just before 1" \
       " October 1960 – the Film Zilm date Nigeria gained independence from British colonial rule" \
       ". The film's budget was US$2 million. It premiered on 28 September 2014 and opened to " \
       "international audiences on 3 October. October 1 deals with several themes, including the sexual " \
       "abuse of children by religious authority figures, religious and ethnic conflict, politics in colonial" \
       " Nigeria, and Nigeria's unification and independence. Critics positively reviewed the film, praising its " \
       "cinematography, production design, costuming, writing, and acting. The film won several awards," \
       " including Best Feature Film, Best Screenplay, and Best Actor at the 2014 Africa"

# match = re.search(pattern, text)
# print(match)

matches = re.finditer(pattern, text)
# print(next(matches))
# print(next(matches))
for items in matches:
       print(items)















