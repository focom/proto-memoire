

def createQuery(name):
    beginQuery = "CREATE (student:Student {name:" + f"'{name}'" +",personality:[2,3,10]}),"
    createQuery = beginQuery + """
    (t1:Theme1 {name:"Syntax",grade:0,history:0,id_node:1}),(t2:Theme2 {name:"Homophone",grade:0,history:0,id_node:2}),
    //Level 1
    (cphrase:Chapitre {name:"Constituant de la phrase",grade:0,id_node:3,history:0}),(tphrase:Chapitre {name:"Types de phrase et accord du verbe",grade:0,id_node:4,history:0}),
    (homophone:Chapitre{name:"homophone",grade:0,id_node:5,history:0}),
    //Level 2
    (Ceasy:Chapitre {name:"Contenus dapprentissage",grade:0,id_node:6,history:0}), (Chard:Chapitre {name:"Contenus dappronfondissement",grade:0,id_node:7,history:0}),
    (Tphrase:Chapitre {name:"Type de phrase",grade:0,id_node:8,history:0}), (conjugaison:Chapitre {name:"Contenus pour laccord du verbe",grade:0,id_node:9,history:0}),
    (omonyme:Chapitre {name:"Homonyme",grade:0,id_node:10,history:0}),(autre:Chapitre {name:"Autre Cas",grade:0,id_node:11,history:0}),

    // Relation between chapter
    (student)-[:link]->(t1),
    (t1)-[:link]->(t2),
    (cphrase)-[:link]->(t1), (tphrase)-[:link]->(t1),(homophone)-[:link]->(t2),
    (Ceasy)-[:link]->(cphrase),(Chard)-[:link]->(cphrase),
    (Tphrase)-[:link]->(tphrase),(conjugaison)-[:link]->(tphrase),
    (omonyme)-[:link]->(homophone),(autre)-[:link]->(homophone),

    // Exercice 1
    (:Exercice {id_node:12,instruction:"Trouve le sujet", question:"Mon petit frere derange les visiteur", answer:["petit frere","visiteur"], correct:"petit frere"})-[:link]->(Ceasy),
    (:Exercice {id_node:13,instruction:"Trouve le sujet", question:"Je vais parler à mon pere, demain matin", answer:["je","pere"], correct:"je"})-[:link]->(Ceasy),
    (:Exercice {id_node:14,instruction:"Trouve le sujet", question:"Ma soeur Isabelle partage mes impressions", answer:["Isabelle","impressions"], correct:"Isabelle"})-[:link]->(Ceasy),
    (:Exercice {id_node:15,instruction:"Trouve le sujet", question:"Mon petit frere Pierre regrette ses gestes", answer:["Pierre","gestes"], correct:"Pierre"})-[:link]->(Ceasy),
    (:Exercice {id_node:16,instruction:"Trouve le sujet", question:"Au souper, mon pere le réprimandera", answer:["souper","pere"], correct:"pere"})-[:link]->(Ceasy),
    (:Exercice {id_node:17,instruction:"Trouve le complement de la phrase", question:"La petite sexcusera à la prochaine visite", answer:["La petite","à la prochaine visite"], correct:"à la prochaine visite"})-[:link]->(Ceasy),
    (:Exercice {id_node:18,instruction:"Trouve le complement de la phrase", question:"Mon pere doit le reprendre plusieurs fois", answer:["Pere","plusieur fois"], correct:"plusieur fois"})-[:link]->(Ceasy),
    (:Exercice {id_node:19,instruction:"Trouve le complement de la phrase", question:"Jaime la pizza avec du poivron", answer:["la pizza","avec du poivron"], correct:"avec du poivron"})-[:link]->(Ceasy),
    (:Exercice {id_node:20,instruction:"Trouve le complement de la phrase", question:"Morgane trouve un mouton rouge dans le champ", answer:["Morganne","dans le champ"], correct:"dans le champ"})-[:link]->(Ceasy),
    (:Exercice {id_node:21,instruction:"Trouve le complement de la phrase", question:"Le voisin decouvre le tresor dans le jardin", answer:["decouvre","dans le jardin"], correct:"dans le jardin"})-[:link]->(Ceasy),
    (:Exercice {id_node:22,instruction:"Trouve le verbe", question:"Morgane trouve un mouton rouge dans le champ", answer:["Sous","mange"], correct:"mange"})-[:link]->(Ceasy),
    (:Exercice {id_node:23,instruction:"Trouve le verbe", question:"Morgane trouve un mouton rouge dans le champ", answer:["meme si","jaime"], correct:"jaime"})-[:link]->(Ceasy),
    (:Exercice {id_node:24,instruction:"Trouve le verbe", question:"La vache broute lherbe", answer:["broute","lherbe"], correct:"broute"})-[:link]->(Ceasy),

    // Exercice 2
    (:Exercice {id_node:25,instruction:"Trouve le sujet", question:"Les mathematiques sont une matierre difficile", answer:["Matiere","mathemathique"], correct:"mathematique"})-[:link]->(Chard),
    (:Exercice {id_node:26,instruction:"Trouve le sujet", question:"Chaque cours, les eleves de ma classe tracillent fort ", answer:["les elevent","cours"], correct:"les elevent"})-[:link]->(Chard),
    (:Exercice {id_node:27,instruction:"Trouve le sujet", question:"Heuresement, notre professeur nous aide beaucoup", answer:["notre professeur","nous"], correct:"notre professeur"})-[:link]->(Chard),
    (:Exercice {id_node:28,instruction:"Trouve le sujet", question:"Madame Christine nous encourage sans cesse", answer:["Madame Christine","nous"], correct:"Madame Christine"})-[:link]->(Chard),
    (:Exercice {id_node:29,instruction:"Trouve le sujet", question:"Nous avons tous reussis lors du dernier test", answer:["Nous","tous"], correct:"Nous"})-[:link]->(Chard),
    (:Exercice {id_node:30,instruction:"Trouve le complement de la phrase", question:"La prochaine fois, ma classe participera a un concours", answer:["un concours","la prochaine fois"], correct:"la prochaine fois"})-[:link]->(Chard),
    (:Exercice {id_node:31,instruction:"Trouve le complement de la phrase", question:"Madame Christine exigera le meilleur de nous", answer:["de nous","exigera"], correct:"de nous"})-[:link]->(Chard),
    (:Exercice {id_node:32,instruction:"Trouve le complement de la phrase", question:"Chaque fin de cours, elle nous remet des problemes a resoudre.", answer:["chaque fin de cours","des problemes a resoudres"], correct:"chaque fin de cours"})-[:link]->(Chard),
    (:Exercice {id_node:33,instruction:"Trouve le complement de la phrase", question:"Le soir, à la maison, mes parents maident", answer:["à la maison","maident"], correct:"à la maison"})-[:link]->(Chard),
    (:Exercice {id_node:34,instruction:"Trouve le complement de la phrase", question:"Mon ami Mario et moi travaillons en equipe", answer:["decouvre","dans le jardin"], correct:"dans le jardin"})-[:link]->(Chard),
    (:Exercice {id_node:35,instruction:"Trouve le verbe", question:"Nous voulons gagner le concours le mois prochain", answer:["prochain","voulons"], correct:"voulons"})-[:link]->(Chard),
    (:Exercice {id_node:36,instruction:"Trouve le verbe", question:"Sous la pluis, je suis bien couvert sous mon parapluie", answer:["suis","couvert"], correct:"suis"})-[:link]->(Chard),
    (:Exercice {id_node:37,instruction:"Trouve le verbe", question:"Dans la savane, le lion est le rois des animaux.", answer:["est","des animaux"], correct:"est"})-[:link]->(Chard),

    // Exercice 3
    (:Exercice {id_node:38,instruction:"Identifie le type de phrase", question:"Avez vous vus Pierre ce matin ?", answer:["declaratif","interogatif"], correct:"interogatif"})-[:link]->(Tphrase),
    (:Exercice {id_node:39,instruction:"Identifie le type de phrase", question:"Repondez-moi.", answer:["exclamatif","imperatif"], correct:"imperatif"})-[:link]->(Tphrase),
    (:Exercice {id_node:40,instruction:"Identifie le type de phrase", question:"Comme il avait lair triste !", answer:["declaratif","exclamatif"], correct:"declaratif"})-[:link]->(Tphrase),
    (:Exercice {id_node:41,instruction:"Identifie le type de phrase", question:"Il a perdu mon beau gilet de laine.", answer:["est","des animaux"], correct:"declaratif"})-[:link]->(Tphrase),
    (:Exercice {id_node:42,instruction:"Identifie le type de phrase", question:"Vite, allez le chercher", answer:["interogatif","exclamatif"], correct:"imperatif"})-[:link]->(Tphrase),
    (:Exercice {id_node:43,instruction:"Identifie le type de phrase", question:"Pourrais-je amener mes amis?", answer:["interogatif","exclamatif"], correct:"interogatif"})-[:link]->(Tphrase),
    (:Exercice {id_node:44,instruction:"Identifie le type de phrase", question:"Vite retournez vers vos amis.", answer:["imperatif","declaratif"], correct:"imperatif"})-[:link]->(Tphrase),
    (:Exercice {id_node:45,instruction:"Identifie le type de phrase", question:"il vaut mieux revenir vers eux", answer:["declaratif","interogatif"], correct:"declaratif"})-[:link]->(Tphrase),
    (:Exercice {id_node:46,instruction:"Identifie le type de phrase", question:"Comme le soleil brule la peau!", answer:["declaratif","interogatif"], correct:"declaratif"})-[:link]->(Tphrase),
    (:Exercice {id_node:47,instruction:"Identifie le type de phrase", question:"Est-ce que le soleil brule la peau?", answer:["interogatif","exclamatif"], correct:"interogatif"})-[:link]->(Tphrase),
    (:Exercice {id_node:48,instruction:"Identifie le type de phrase", question:"Comme ce cycliste a la peau brulée", answer:["declaratif","interogatif"], correct:"declaratif"})-[:link]->(Tphrase),
    (:Exercice {id_node:49,instruction:"Identifie le type de phrase", question:"Il consultera surement le dermatologue", answer:["declaratif","interogatif"], correct:"declaratif"})-[:link]->(Tphrase),
    (:Exercice {id_node:50,instruction:"Identifie le type de phrase", question:"Reserve un rendez-vous", answer:["imperatif","declaratif"], correct:"imperatif"})-[:link]->(Tphrase),

    //Exercice 4
    (:Exercice {id_node:51,instruction:"choisis la bonne orthographe", question:"Michel et et moi (aller) au cinéma", answer:["allon","allons"], correct:"allons"})-[:link]->(conjugaison),
    (:Exercice {id_node:52,instruction:"choisis la bonne orthographe", question:"Michel et toi (aller) au cinéma", answer:["alles","allez"], correct:"allez"})-[:link]->(conjugaison),
    (:Exercice {id_node:53,instruction:"choisis la bonne orthographe", question:"Christine et lui (aller) au cinéma", answer:["vons","vont"], correct:"vont"})-[:link]->(conjugaison),
    (:Exercice {id_node:54,instruction:"choisis la bonne orthographe", question:"Le chat et la souris (danser)", answer:["danses","dansent"], correct:"dansent"})-[:link]->(conjugaison),
    (:Exercice {id_node:55,instruction:"choisis la bonne orthographe", question:"Je leur (pardonner) ces erreurs", answer:["pardonnent","pardonne"], correct:"pardonne"})-[:link]->(conjugaison),
    (:Exercice {id_node:56,instruction:"choisis la bonne orthographe", question:"Cest moi qui (etre) votre collaborateur", answer:["est","suis"], correct:"suis"})-[:link]->(conjugaison),
    (:Exercice {id_node:57,instruction:"choisis la bonne orthographe", question:"Une foule de gens (bloquer) la rue", answer:["bloquent","bloque"], correct:"bloque"})-[:link]->(conjugaison),
    (:Exercice {id_node:58,instruction:"choisis la bonne orthographe", question:"Les chiffres, les lettres, tout (etre) du chinois", answer:["fus","est"], correct:"est"})-[:link]->(conjugaison),
    (:Exercice {id_node:59,instruction:"choisis la bonne orthographe", question:"Dans le ravin (couler) un ruisselet", answer:["coulet","coule"], correct:"coule"})-[:link]->(conjugaison),
    (:Exercice {id_node:60,instruction:"choisis la bonne orthographe", question:"il (arriver) des touristes de partout", answer:["arrivent","arrive"], correct:"arrive"})-[:link]->(conjugaison),
    (:Exercice {id_node:61,instruction:"choisis la bonne orthographe", question:"Mon ami Martine et moi (rire) souvent pour rien", answer:["riont","rions"], correct:"rions"})-[:link]->(conjugaison),
    (:Exercice {id_node:62,instruction:"choisis la bonne orthographe", question:"Ma petite soeur Chantal les (adorer), ses chats", answer:["adore","adorent"], correct:"adore"})-[:link]->(conjugaison),

    //Exercice 5
    (:Exercice {id_node:63,instruction:"choisis la bonne orthographe", question:"les enfants _ couchent tôt", answer:["ce","se"], correct:"se"})-[:link]->(omonyme),
    (:Exercice {id_node:64,instruction:"choisis la bonne orthographe", question:"Sait-tu _ que tu veux?", answer:["ce","se"], correct:"se"})-[:link]->(omonyme),
    (:Exercice {id_node:65,instruction:"choisis la bonne orthographe", question:"_ chien me mordit à la main", answer:["ce","se"], correct:"ce"})-[:link]->(omonyme),
    (:Exercice {id_node:66,instruction:"choisis la bonne orthographe", question:"Léa _ prend pour une autre femme.", answer:["ce","se"], correct:"se"})-[:link]->(omonyme),
    (:Exercice {id_node:67,instruction:"choisis la bonne orthographe", question:"_ se trouve le chocolat?", answer:["où","ou"], correct:"où"})-[:link]->(omonyme),
    (:Exercice {id_node:68,instruction:"choisis la bonne orthographe", question:"Aime tu la vanille _ le chocolat", answer:["où","ou"], correct:"ou"})-[:link]->(omonyme),
    (:Exercice {id_node:69,instruction:"choisis la bonne orthographe", question:"La semaine derniere _ nous avons mangé, cetait un bon restaurant.", answer:["où","ou"], correct:"où"})-[:link]->(omonyme),
    (:Exercice {id_node:70,instruction:"choisis la bonne orthographe", question:"_ DVD sont les miens", answer:["ces","cest"], correct:"ces"})-[:link]->(omonyme),
    (:Exercice {id_node:71,instruction:"choisis la bonne orthographe", question:"_ voitures sont belles", answer:["ces","cest"], correct:"cest"})-[:link]->(omonyme),
    (:Exercice {id_node:72,instruction:"choisis la bonne orthographe", question:"_ tout se que jaime", answer:["ces","cest"], correct:"cest"})-[:link]->(omonyme),
    (:Exercice {id_node:73,instruction:"choisis la bonne orthographe", question:"il _ trouver une pépite", answer:["peut","peu"], correct:"peut"})-[:link]->(omonyme),
    (:Exercice {id_node:74,instruction:"choisis la bonne orthographe", question:"Il y a trop _ de chocolat", answer:["peut","peu"], correct:"peu"})-[:link]->(omonyme),

    //Exercie 6
    (:Exercice {id_node:75,instruction:"choisis la bonne orthographe", question:"il sortit (tout à coup/tout-à-coup) sans rien dire", answer:["tout à coup","tout-à-coup"], correct:"tout à coup"})-[:link]->(autre),
    (:Exercice {id_node:76,instruction:"choisis la bonne orthographe", question:"La sentinelle etait au (garde à vous/garde-à-vous)", answer:["garde à vous","garde-à-vous"], correct:"garde-à-vous"})-[:link]->(autre),
    (:Exercice {id_node:77,instruction:"choisis la bonne orthographe", question:"Ce tableau est un (chef doeuvre/chef-doeuvre)", answer:["chef doeuvre","chef-doeuvre"], correct:"chef-doeuvre"})-[:link]->(autre),
    (:Exercice {id_node:78,instruction:"choisis la bonne orthographe", question:"Jai recu un (coup-de-pied/coup de pied)", answer:["coup-de-pied","coup de pied"], correct:"coup de pied"})-[:link]->(autre),
    (:Exercice {id_node:79,instruction:"choisis la bonne orthographe", question:"Je suis entré à la maison (sur le champ/sur-le-champ)", answer:["sur le champ","sur-le-champ"], correct:"sur-le-champ"})-[:link]->(autre),
    (:Exercice {id_node:80,instruction:"choisis la bonne orthographe", question:"Mon (sac à dos/sac-à-dos)", answer:["sac à dos","sac-à-dos"], correct:"sac à dos"})-[:link]->(autre),
    (:Exercice {id_node:81,instruction:"choisis la bonne orthographe", question:"Venez me (sil-vous-plait/sil vous plait)", answer:["sil-vous-plait","sil vous plait"], correct:"sil vous plait"})-[:link]->(autre),
    (:Exercice {id_node:82,instruction:"choisis la bonne orthographe", question:"Je suis (tout-à-fait/tout à fait) daccord", answer:["tout-à-fait","tout à fait"], correct:"tout à fait"})-[:link]->(autre),
    (:Exercice {id_node:83,instruction:"choisis la bonne orthographe", question:"Un manteau pourpre (cest-a-dire/cest a dire) rouge foncé", answer:["cest-a-dire","cest a dire"], correct:"cest-a-dire"})-[:link]->(autre),
    (:Exercice {id_node:84,instruction:"choisis la bonne orthographe", question:"un (arc-en-ciel/arc en ciel)", answer:["arc-en-ciel","arc en ciel"], correct:"arc-en-ciel"})-[:link]->(autre);"""

    return createQuery