from ap_wl.lang import Lang

SKILLS = {
    "1.A": "1.A Identify the meaning of Latin words and phrases",
    "1.B": "1.B Describe how grammar contributes to meaning",
    "1.C": "1.C Summarize Latin texts in English",
    "1.D": "1.D Translate Latin texts into English",
    "2.A": "2.A Describe stylistic elements, including meter",
    "2.B": "2.B Describe historical and cultural contexts",
}

L = Lang("ap_latin", "AP Latin", "AP Latin", "ap-latin",
         ask="Answer in English unless the question asks for Latin.", vocabheads="{Latina}{English}{Notes}", skills=SKILLS,
         setup="There is no listening section. Read each passage once through, then answer; allow about 75 seconds per item.")
