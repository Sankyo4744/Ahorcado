import random
from django.shortcuts import render 

# Create your views here.

diccionario_palabras = [
    {"palabra": "Naruto", "categoria": "anime", "frase": "Un joven ninja con el sueño de convertirse en el líder de su aldea."},
    {"palabra": "Dragon Ball", "categoria": "anime", "frase": "Una serie de anime y manga que sigue las aventuras de Son Goku en su búsqueda de las esferas del dragón."},
    {"palabra": "One Piece", "categoria": "anime", "frase": "Una historia de piratas que sigue las aventuras de Monkey D. Luffy y su tripulación en busca del One Piece, el mayor tesoro del mundo."},
    {"palabra": "Death Note", "categoria": "anime", "frase": "Un estudiante de secundaria encuentra un cuaderno que le permite matar a cualquier persona cuyo nombre escriba en él."},
    {"palabra": "Attack on Titan", "categoria": "anime", "frase": "La humanidad lucha por sobrevivir contra gigantes humanoides devoradores de hombres conocidos como Titanes."},
    {"palabra": "My Hero Academia", "categoria": "anime", "frase": "Un joven sin poderes se une a una academia para entrenar y convertirse en un héroe."},
    {"palabra": "Tokyo Ghoul", "categoria": "anime", "frase": "Un estudiante universitario se convierte en mitad humano, mitad ghoul, y debe aprender a vivir en ambos mundos."},
    {"palabra": "Fullmetal Alchemist", "categoria": "anime", "frase": "Dos hermanos buscan la Piedra Filosofal para restaurar sus cuerpos después de un intento fallido de resucitar a su madre."},
    {"palabra": "Sword Art Online", "categoria": "anime", "frase": "Los jugadores quedan atrapados en un juego de realidad virtual donde la muerte en el juego significa la muerte en la vida real."},
    {"palabra": "Hunter x Hunter", "categoria": "anime", "frase": "Un joven aspirante a cazador se embarca en una búsqueda para encontrar a su padre y convertirse en un cazador."},
    {"palabra": "Demon Slayer", "categoria": "anime", "frase": "Un joven se une a una organización para cazar demonios y vengar la muerte de su familia."},
    {"palabra": "One Punch Man", "categoria": "anime", "frase": "Un héroe demasiado poderoso derrota a sus enemigos de un solo golpe y se aburre de la falta de desafíos."},
    {"palabra": "Neon Genesis Evangelion", "categoria": "anime", "frase": "Un grupo de adolescentes pilotea robots gigantes para proteger la Tierra de misteriosos seres conocidos como Ángeles."},
    {"palabra": "Fairy Tail", "categoria": "anime", "frase": "Un gremio de magos vive aventuras mientras realizan trabajos y luchan contra enemigos poderosos."},
    {"palabra": "Bleach", "categoria": "anime", "frase": "Un joven adquiere los poderes de un Shinigami y se embarca en la misión de proteger a los vivos y guiar a las almas perdidas."},
    {"palabra": "Naruto Shippuden", "categoria": "anime", "frase": "La continuación de la historia de Naruto Uzumaki mientras entrena para volverse más fuerte y proteger a sus seres queridos."},
    {"palabra": "Boruto", "categoria": "anime", "frase": "La historia sigue las aventuras de Boruto Uzumaki, hijo de Naruto, mientras lucha por encontrar su propio camino como ninja."},
    {"palabra": "Cowboy Bebop", "categoria": "anime", "frase": "Un grupo de cazarrecompensas viaja por el espacio en busca de criminales mientras lidian con su pasado y sus demonios internos."},
    {"palabra": "Black Clover", "categoria": "anime", "frase": "Un joven sin magia busca convertirse en el Rey Mago y proteger a su reino."},
    {"palabra": "Tokyo Revengers", "categoria": "anime", "frase": "Un estudiante se transporta en el tiempo y busca cambiar el futuro para evitar la muerte de su novia."},
    {"palabra": "Mob Psycho 100", "categoria": "anime", "frase": "Un estudiante con habilidades psíquicas trabaja como exorcista mientras intenta controlar sus poderes y encontrar su propósito en la vida."},
    {"palabra": "Promised Neverland", "categoria": "anime", "frase": "Un grupo de huérfanos descubre los oscuros secretos detrás de su orfanato y lucha por escapar de su destino."},
    {"palabra": "Code Geass", "categoria": "anime", "frase": "Un joven con el poder del Geass busca vengarse del Imperio Británico y crear un mundo mejor para su hermana."},
    {"palabra": "Dr. Stone", "categoria": "anime", "frase": "Después de que toda la humanidad se petrifica, un joven científico despierta y trabaja para reconstruir la civilización con la ciencia."},
    {"palabra": "Steins;Gate", "categoria": "anime", "frase": "Un grupo de amigos descubre una manera de enviar mensajes al pasado y se ven envueltos en una conspiración que amenaza el mundo."},
    {"palabra": "JoJo's Bizarre Adventure", "categoria": "anime", "frase": "Una saga épica que sigue a varias generaciones de la familia Joestar mientras luchan contra el mal en diferentes épocas y lugares."},
    {"palabra": "Re:Zero", "categoria": "anime", "frase": "Un chico es transportado a un mundo de fantasía y queda atrapado en un ciclo de muerte y resurrección."},
    {"palabra": "Fruits Basket", "categoria": "anime", "frase": "Una joven se muda con una familia que está maldita para transformarse en animales del zodíaco chino."},
    {"palabra": "Seven Deadly Sins", "categoria": "anime", "frase": "Un grupo de caballeros legendarios se reúne para derrotar al malvado grupo conocido como los Siete Pecados Capitales."},
    {"palabra": "Promare", "categoria": "anime", "frase": "En un mundo donde las personas tienen poderes de fuego, un equipo de bomberos lucha contra monstruos de fuego y una conspiración gubernamental."},
    {"palabra": "Soul Eater", "categoria": "anime", "frase": "Los estudiantes de la Academia Death Weapon Meister luchan contra seres malvados para convertir sus armas en Death Scythes."},
    {"palabra": "Made in Abyss", "categoria": "anime", "frase": "Una niña y un robot descienden al abismo para encontrar a la madre perdida de la niña y descubren horrores inimaginables en el camino."},
    {"palabra": "Bleach", "categoria": "anime", "frase": "Un joven adquiere los poderes de un Shinigami y se embarca en la misión de proteger a los vivos y guiar a las almas perdidas."},
    {"palabra": "Cardcaptor Sakura", "categoria": "anime", "frase": "Una niña encuentra cartas mágicas que deben ser capturadas para evitar que causen estragos en el mundo."},
    {"palabra": "Clannad", "categoria": "anime", "frase": "Un estudiante de secundaria conoce a una chica peculiar y juntos experimentan amor, amistad y tragedia."},
    {"palabra": "Claymore", "categoria": "anime", "frase": "Una organización de mujeres mitad humano, mitad monstruo lucha contra criaturas demoníacas conocidas como Yoma."},
    {"palabra": "Death Parade", "categoria": "anime", "frase": "Las almas de los muertos son juzgadas en un bar por juegos de azar mientras un misterioso arbitro decide su destino."},
    {"palabra": "Digimon", "categoria": "anime", "frase": "Un grupo de niños viaja a un mundo digital para salvarlo de la destrucción y aprender lecciones sobre la amistad y el coraje."},
    {"palabra": "Durarara!!", "categoria": "anime", "frase": "Una serie de eventos extraños y personajes excéntricos se entrelazan en los distritos de Ikebukuro, Tokio."},
    {"palabra": "Elfen Lied", "categoria": "anime", "frase": "Una joven con poderes de mutante escapa de un laboratorio y busca venganza contra la humanidad que la maltrató."},
    {"palabra": "Fairy Tail", "categoria": "anime", "frase": "Un gremio de magos vive aventuras mientras realizan trabajos y luchan contra enemigos poderosos."},
    {"palabra": "Fate/stay night", "categoria": "anime", "frase": "Un grupo de magos y héroes legendarios luchan por el Santo Grial y el deseo que puede conceder."},
    {"palabra": "Food Wars!", "categoria": "anime", "frase": "Un estudiante de cocina asiste a una academia culinaria de élite donde los duelos culinarios deciden el destino de los chefs."},
    {"palabra": "Fullmetal Alchemist", "categoria": "anime", "frase": "Dos hermanos buscan la Piedra Filosofal para restaurar sus cuerpos después de un intento fallido de resucitar a su madre."},
    {"palabra": "Gantz", "categoria": "anime", "frase": "Las personas recién fallecidas son resucitadas para luchar contra alienígenas en misiones peligrosas y mortales."},
    {"palabra": "Gurren Lagann", "categoria": "anime", "frase": "Un joven y su compañero descubren un mecha gigante y se embarcan en una misión para liberar a la humanidad de la opresión."},
    {"palabra": "High School DxD", "categoria": "anime", "frase": "Un estudiante es asesinado por un ángel y resucitado como demonio, y se une a un club de investigación paranormal."},
    {"palabra": "Inuyasha", "categoria": "anime", "frase": "Una adolescente viaja en el tiempo al Japón feudal y se une a un medio demonio en busca de fragmentos de la joya de cuatro almas."},
    {"palabra": "K-On!", "categoria": "anime", "frase": "Un grupo de chicas se une para formar un club de música en la escuela y se embarcan en aventuras musicales juntas."},
    {"palabra": "Kill la Kill", "categoria": "anime", "frase": "Una estudiante busca venganza por la muerte de su padre y lucha contra un sistema escolar autoritario con ropa que otorga poderes."},
    {"palabra": "Love Live!", "categoria": "anime", "frase": "Un grupo de chicas forma un grupo de ídolos para salvar su escuela de la bancarrota y competir en el Love Live! competencia."},
    {"palabra": "Magi: The Labyrinth of Magic", "categoria": "anime", "frase": "Un niño descubre un genio y se embarca en una aventura para conquistar mazmorras y cambiar el mundo."},
    {"palabra": "Mirai Nikki", "categoria": "anime", "frase": "Un estudiante recibe un diario que predice el futuro y se ve envuelto en un juego de supervivencia mortal."},
    {"palabra": "My Hero Academia", "categoria": "anime", "frase": "Un joven sin poderes se une a una academia para entrenar y convertirse en un héroe."},
    {"palabra": "Naruto", "categoria": "anime", "frase": "Un joven ninja con el sueño de convertirse en el líder de su aldea y ser reconocido por todos."},
    {"palabra": "No Game No Life", "categoria": "anime", "frase": "Dos hermanos genios son transportados a un mundo de juegos donde deben ganar para sobrevivir y reclamar el trono."},
    {"palabra": "Noragami", "categoria": "anime", "frase": "Un dios menor busca aumentar su número de seguidores y encuentra aventuras junto a una chica con un destino misterioso."},
    {"palabra": "One Punch Man", "categoria": "anime", "frase": "Un héroe demasiado poderoso derrota a sus enemigos de un solo golpe y se aburre de la falta de desafíos."},
    {"palabra": "Ouran High School Host Club", "categoria": "anime", "frase": "Una chica sin recursos se une a un club de chicos ricos y guapos y se embarca en hilarantes aventuras románticas."},
    {"palabra": "Overlord", "categoria": "anime", "frase": "Un jugador queda atrapado en un juego de realidad virtual y se convierte en un gobernante temido en un mundo de fantasía."},
    {"palabra": "Puella Magi Madoka Magica", "categoria": "anime", "frase": "Una chica es reclutada por un gato mágico para convertirse en una chica mágica y luchar contra brujas que amenazan el mundo."},
    {"palabra": "Rurouni Kenshin", "categoria": "anime", "frase": "Un ex asesino busca redención por sus pecados y protege a los inocentes como un samurái errante."},
    {"palabra": "Shingeki no Kyojin", "categoria": "anime", "frase": "La humanidad lucha por sobrevivir contra gigantes humanoides devoradores de hombres conocidos como Titanes."},
    {"palabra": "Soul Eater", "categoria": "anime", "frase": "Los estudiantes de la Academia Death Weapon Meister luchan contra seres malvados para convertir sus armas en Death Scythes."},
    {"palabra": "Sword Art Online", "categoria": "anime", "frase": "Los jugadores quedan atrapados en un juego de realidad virtual donde la muerte en el juego significa la muerte en la vida real."},
    {"palabra": "Tokyo Ghoul", "categoria": "anime", "frase": "Un estudiante universitario se convierte en mitad humano, mitad ghoul, y debe aprender a vivir en ambos mundos."},
    {"palabra": "Toradora!", "categoria": "anime", "frase": "Dos estudiantes de secundaria con personalidades opuestas forman una inesperada amistad y romance."},
    {"palabra": "Trigun", "categoria": "anime", "frase": "Un pistolero pacifista viaja por el desierto y se enfrenta a su oscuro pasado mientras busca aventuras y justicia."},
    {"palabra": "Violet Evergarden", "categoria": "anime", "frase": "Una ex soldado se convierte en escritora de cartas para comprender el significado del amor y la emoción humana."},
    {"palabra": "Yu Yu Hakusho", "categoria": "anime", "frase": "Un adolescente es revivido como un detective espiritual y lucha contra demonios y monstruos en nombre del mundo de los vivos."},
    {"palabra": "Zankyou no Terror", "categoria": "anime", "frase": "Dos jóvenes terroristas planean una serie de ataques en Tokio como venganza por los experimentos que sufrieron en su infancia."},
    {"palabra": "Bakuman", "categoria": "anime", "frase": "Dos amigos de la infancia se unen para crear manga y alcanzar el éxito en el mundo editorial."},
    {"palabra": "Hellsing", "categoria": "anime", "frase": "Un grupo de cazadores de vampiros lucha contra fuerzas sobrenaturales y amenazas demoníacas."},
    {"palabra": "Serial Experiments Lain", "categoria": "anime", "frase": "Una chica se sumerge en un mundo virtual y se encuentra enredada en una conspiración que desafía la realidad misma."},
    {"palabra": "Akame ga Kill!", "categoria": "anime", "frase": "Un grupo de asesinos lucha contra un gobierno corrupto y poderoso en un mundo de traición y violencia."},
    {"palabra": "Black Butler", "categoria": "anime", "frase": "Un demonio sirviente y su amo humano realizan tareas para la reina de Inglaterra mientras investigan conspiraciones sobrenaturales."},
    {"palabra": "Parasyte", "categoria": "anime", "frase": "Los seres humanos son invadidos por parásitos alienígenas que se apoderan de sus cuerpos y buscan sobrevivir en un mundo hostil."},
    {"palabra": "Angel Beats!", "categoria": "anime", "frase": "Un grupo de estudiantes muertos se encuentra en un limbo escolar y lucha contra sus problemas pasados y su destino incierto."},
    {"palabra": "Fate/Zero", "categoria": "anime", "frase": "Los magos convocan héroes legendarios para luchar en una batalla real por el Santo Grial y el deseo que puede conceder."},
    {"palabra": "Psycho-Pass", "categoria": "anime", "frase": "En un futuro distópico, la policía utiliza un sistema de vigilancia para predecir y prevenir el crimen antes de que ocurra."}
    
]

def index(request):
    return render(request, 'menu/index.html')

def juego(request):
    palabra_aleatoria = random.choice(diccionario_palabras)
    palabra = palabra_aleatoria["palabra"]
    palabra_sin_espacios = palabra.replace(" ", "")
    aleatorio = random.choice(palabra_sin_espacios)
    print(aleatorio)
    print(len(diccionario_palabras))
    return render(request, 'juegazo/ahorquitos.html', {"palabra":palabra_aleatoria, "caracter": aleatorio})

