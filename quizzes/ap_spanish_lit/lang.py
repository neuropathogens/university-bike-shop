from ap_wl.lang import Lang

SKILLS = {
    "1.A": "1.A Comprehend literary texts and audio",
    "1.B": "1.B Identify the theme",
    "1.C": "1.C Identify literary elements, voices and stylistic features",
    "1.D": "1.D Identify perspective, attitude or tone",
    "1.E": "1.E Explain the function of rhetorical, structural and stylistic features",
    "1.F": "1.F Explain implied meanings and inferences",
    "1.G": "1.G Explain perspective, attitude or tone",
    "1.H": "1.H Explain the development of a theme",
    "1.I": "1.I Connect themes or ideas to characters",
    "2.A": "2.A Identify cultural products, practices or perspectives",
    "2.C": "2.C Relate texts to genres, periods, movements and techniques",
    "2.D": "2.D Situate language and registers in their contexts",
    "2.E": "2.E Relate texts to their literary, historical and sociocultural contexts",
    "2.G": "2.G Explain how a text reflects or challenges perceptions of a culture",
    "3.A": "3.A Compare structural or stylistic features of two texts",
    "3.B": "3.B Compare themes, perspectives or contexts of two texts",
}

L = Lang("ap_spanish_lit", "AP Spanish Literature", "AP Spanish Literature and Culture", "ap-spanish-literature",
         ask="Escribe tu respuesta en español.", vocabheads="{Español}{English}{Notes}", skills=SKILLS,
         setup="La sección de audio aparece aquí como transcripción: lee cada texto una vez y contesta sin volver a leer. "
               "Calcula unos 80 segundos por pregunta de audio y 70 segundos por pregunta de lectura.")
