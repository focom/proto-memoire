
//Delete all previous node
MATCH (n) DETACH DELETE n;


// theme1 -> theme2
// theme1 -> [1,2] | 1 -> [4,5] | 2 -> [6,7]
// theme2 -> [3] | 3 -> [8,9]

// First create Node
// Theme
CREATE (t1:Theme1 {name:'Syntax',grade:0}),(t2:Theme2 {name:'Homophone',grade:0}),
//Level 1
(cphrase:Chapitre {name:'Constituant de la phrase',grade:0,id_chap:'1'}),(tphrase:Chapitre {name:'Types de phrase et accord du verbe',grade:0,id_chap:'2'}),
(homophone:Chapitre{name:'homophone',grade:0,id_chap:'3'}),
//Level 2
(Ceasy:Chapitre {name:'Contenus d\'apprentissage',grade:0,id_chap:'4'}), (Chard:Chapitre {name:'Contenus d\'appronfondissement',grade:0},,id_chap:'5'),
(Tphrase:Chapitre {name:'Type de phrase',grade:0,id_chap:'6'}), (conjugaison:Chapitre {name:'Contenus pour l\'accord du verbe',grade:0,id_chap:'7'}),
(omonyme:Chapitre {name:'Homonyme',grade:0,id_chap:'8'}),(autre:Chapitre {name:'Autre Cas',grade:0,id_chap:'9'}),

// Relation between chapter
(t1)-[:ifMastered]->(t2),
(cphrase)-[:define]->(t1), (tphrase)-[:define]->(t1),(homophone)-[:define]->(t2),
(Ceasy)-[:define]->(cphrase),(Chard)-[:define]->(cphrase),
(Tphrase)-[:define]->(tphrase),(conjugaison)-[:define]->(tphrase),
(omonyme)-[:define]->(homophone),(autre)-[:define]->(homophone),

// Exercice 1
(:Exercice {instruction:'Trouve le sujet', question:'Mon petit frere derange les visiteur', answer:['petit frere','visiteur'], correct:'petit frere'})-[:verify]->(Ceasy),
(:Exercice {instruction:'Trouve le sujet', question:'Je vais parler à mon pere, demain matin', answer:['je','pere'], correct:'je'})-[:verify]->(Ceasy),
(:Exercice {instruction:'Trouve le sujet', question:'Ma soeur Isabelle partage mes impressions', answer:['Isabelle','impressions'], correct:'Isabelle'})-[:verify]->(Ceasy),
(:Exercice {instruction:'Trouve le sujet', question:'Mon petit frere Pierre regrette ses gestes', answer:['Pierre','gestes'], correct:'Pierre'})-[:verify]->(Ceasy),
(:Exercice {instruction:'Trouve le sujet', question:'Au souper, mon pere le réprimandera', answer:['souper','pere'], correct:'pere'})-[:verify]->(Ceasy),
(:Exercice {instruction:'Trouve le complement de la phrase', question:'La petite s\'excusera à la prochaine visite', answer:['La petite','à la prochaine visite'], correct:'à la prochaine visite'})-[:verify]->(Ceasy),
(:Exercice {instruction:'Trouve le complement de la phrase', question:'Mon pere doit le reprendre plusieurs fois', answer:['Pere','plusieur fois'], correct:'plusieur fois'})-[:verify]->(Ceasy),
(:Exercice {instruction:'Trouve le complement de la phrase', question:'J\'aime la pizza avec du poivron', answer:['la pizza','avec du poivron'], correct:'avec du poivron'})-[:verify]->(Ceasy),
(:Exercice {instruction:'Trouve le complement de la phrase', question:'Morgane trouve un mouton rouge dans le champ', answer:['Morganne','dans le champ'], correct:'dans le champ'})-[:verify]->(Ceasy),
(:Exercice {instruction:'Trouve le complement de la phrase', question:'Le voisin decouvre le tresor dans le jardin', answer:['decouvre','dans le jardin'], correct:'dans le jardin'})-[:verify]->(Ceasy),
(:Exercice {instruction:'Trouve le verbe', question:'Morgane trouve un mouton rouge dans le champ', answer:['Sous','mange'], correct:'mange'})-[:verify]->(Ceasy),
(:Exercice {instruction:'Trouve le verbe', question:'Morgane trouve un mouton rouge dans le champ', answer:['meme si','j\'aime'], correct:'j\'aime'})-[:verify]->(Ceasy),
(:Exercice {instruction:'Trouve le verbe', question:'La vache broute l\'herbe', answer:['broute','l\'herbe'], correct:'broute'})-[:verify]->(Ceasy),

// Exercice 2
(:Exercice {instruction:'Trouve le sujet', question:'Les mathematiques sont une matierre difficile', answer:['Matiere','mathemathique'], correct:'mathematique'})-[:verify]->(Chard),
(:Exercice {instruction:'Trouve le sujet', question:'Chaque cours, les eleves de ma classe tracillent fort ', answer:['les elevent','cours'], correct:'les elevent'})-[:verify]->(Chard),
(:Exercice {instruction:'Trouve le sujet', question:'Heuresement, notre professeur nous aide beaucoup', answer:['notre professeur','nous'], correct:'notre professeur'})-[:verify]->(Chard),
(:Exercice {instruction:'Trouve le sujet', question:'Madame Christine nous encourage sans cesse', answer:['Madame Christine','nous'], correct:'Madame Christine'})-[:verify]->(Chard),
(:Exercice {instruction:'Trouve le sujet', question:'Nous avons tous reussis lors du dernier test', answer:['Nous','tous'], correct:'Nous'})-[:verify]->(Chard),
(:Exercice {instruction:'Trouve le complement de la phrase', question:'La prochaine fois, ma classe participera a un concours', answer:['un concours','la prochaine fois'], correct:'la prochaine fois'})-[:verify]->(Chard),
(:Exercice {instruction:'Trouve le complement de la phrase', question:'Madame Christine exigera le meilleur de nous', answer:['de nous','exigera'], correct:'de nous'})-[:verify]->(Chard),
(:Exercice {instruction:'Trouve le complement de la phrase', question:'Chaque fin de cours, elle nous remet des problemes a resoudre.', answer:['chaque fin de cours','des problemes a resoudres'], correct:'chaque fin de cours'})-[:verify]->(Chard),
(:Exercice {instruction:'Trouve le complement de la phrase', question:'Le soir, à la maison, mes parents m\'aident', answer:['à la maison','m\'aident'], correct:'à la maison'})-[:verify]->(Chard),
(:Exercice {instruction:'Trouve le complement de la phrase', question:'Mon ami Mario et moi travaillons en equipe', answer:['decouvre','dans le jardin'], correct:'dans le jardin'})-[:verify]->(Chard),
(:Exercice {instruction:'Trouve le verbe', question:'Nous voulons gagner le concours le mois prochain', answer:['prochain','voulons'], correct:'voulons'})-[:verify]->(Chard),
(:Exercice {instruction:'Trouve le verbe', question:'Sous la pluis, je suis bien couvert sous mon parapluie', answer:['suis','couvert'], correct:'suis'})-[:verify]->(Chard),
(:Exercice {instruction:'Trouve le verbe', question:'Dans la savane, le lion est le rois des animaux.', answer:['est','des animaux'], correct:'est'})-[:verify]->(Chard),

// Exercice 3
(:Exercice {instruction:'Identifie le type de phrase', question:'Avez vous vus Pierre ce matin ?', answer:['declaratif','interogatif'], correct:'interogatif'})-[:verify]->(Tphrase),
(:Exercice {instruction:'Identifie le type de phrase', question:'Repondez-moi.', answer:['exclamatif','imperatif'], correct:'imperatif'})-[:verify]->(Tphrase),
(:Exercice {instruction:'Identifie le type de phrase', question:'Comme il avait l\'air triste !', answer:['declaratif','exclamatif'], correct:'declaratif'})-[:verify]->(Tphrase),
(:Exercice {instruction:'Identifie le type de phrase', question:'Il a perdu mon beau gilet de laine.', answer:['est','des animaux'], correct:'declaratif'})-[:verify]->(Tphrase),
(:Exercice {instruction:'Identifie le type de phrase', question:'Vite, allez le chercher', answer:['interogatif','exclamatif'], correct:'imperatif'})-[:verify]->(Tphrase),
(:Exercice {instruction:'Identifie le type de phrase', question:'Pourrais-je amener mes amis?', answer:['interogatif','exclamatif'], correct:'interogatif'})-[:verify]->(Tphrase),
(:Exercice {instruction:'Identifie le type de phrase', question:'Vite retournez vers vos amis.', answer:['imperatif','declaratif'], correct:'imperatif'})-[:verify]->(Tphrase),
(:Exercice {instruction:'Identifie le type de phrase', question:'il vaut mieux revenir vers eux', answer:['declaratif','interogatif'], correct:'declaratif'})-[:verify]->(Tphrase),
(:Exercice {instruction:'Identifie le type de phrase', question:'Comme le soleil brule la peau!', answer:['declaratif','interogatif'], correct:'declaratif'})-[:verify]->(Tphrase),
(:Exercice {instruction:'Identifie le type de phrase', question:'Est-ce que le soleil brule la peau?', answer:['interogatif','exclamatif'], correct:'interogatif'})-[:verify]->(Tphrase),
(:Exercice {instruction:'Identifie le type de phrase', question:'Comme ce cycliste a la peau brulée', answer:['declaratif','interogatif'], correct:'declaratif'})-[:verify]->(Tphrase),
(:Exercice {instruction:'Identifie le type de phrase', question:'Il consultera surement le dermatologue', answer:['declaratif','interogatif'], correct:'declaratif'})-[:verify]->(Tphrase),
(:Exercice {instruction:'Identifie le type de phrase', question:'Reserve un rendez-vous', answer:['imperatif','declaratif'], correct:'imperatif'})-[:verify]->(Tphrase),

//Exercice 4
(:Exercice {instruction:'choisis la bonne orthographe', question:'Michel et et moi (aller) au cinéma', answer:['allon','allons'], correct:'allons'})-[:verify]->(conjugaison),
(:Exercice {instruction:'choisis la bonne orthographe', question:'Michel et toi (aller) au cinéma', answer:['alles','allez'], correct:'allez'})-[:verify]->(conjugaison),
(:Exercice {instruction:'choisis la bonne orthographe', question:'Christine et lui (aller) au cinéma', answer:['vons','vont'], correct:'vont'})-[:verify]->(conjugaison),
(:Exercice {instruction:'choisis la bonne orthographe', question:'Le chat et la souris (danser)', answer:['danses','dansent'], correct:'dansent'})-[:verify]->(conjugaison),
(:Exercice {instruction:'choisis la bonne orthographe', question:'Je leur (pardonner) ces erreurs', answer:['pardonnent','pardonne'], correct:'pardonne'})-[:verify]->(conjugaison),
(:Exercice {instruction:'choisis la bonne orthographe', question:'C\'est moi qui (etre) votre collaborateur', answer:['est','suis'], correct:'suis'})-[:verify]->(conjugaison),
(:Exercice {instruction:'choisis la bonne orthographe', question:'Une foule de gens (bloquer) la rue', answer:['bloquent','bloque'], correct:'bloque'})-[:verify]->(conjugaison),
(:Exercice {instruction:'choisis la bonne orthographe', question:'Les chiffres, les lettres, tout (etre) du chinois', answer:['fus','est'], correct:'est'})-[:verify]->(conjugaison),
(:Exercice {instruction:'choisis la bonne orthographe', question:'Dans le ravin (couler) un ruisselet', answer:['coulet','coule'], correct:'coule'})-[:verify]->(conjugaison),
(:Exercice {instruction:'choisis la bonne orthographe', question:'il (arriver) des touristes de partout', answer:['arrivent','arrive'], correct:'arrive'})-[:verify]->(conjugaison),
(:Exercice {instruction:'choisis la bonne orthographe', question:'Mon ami Martine et moi (rire) souvent pour rien', answer:['riont','rions'], correct:'rions'})-[:verify]->(conjugaison),
(:Exercice {instruction:'choisis la bonne orthographe', question:'Ma petite soeur Chantal les (adorer), ses chats', answer:['adore','adorent'], correct:'adore'})-[:verify]->(conjugaison),

//Exercice 5
(:Exercice {instruction:'choisis la bonne orthographe', question:'les enfants _ couchent tôt', answer:['ce','se'], correct:'se'})-[:verify]->(omonyme),
(:Exercice {instruction:'choisis la bonne orthographe', question:'Sait-tu _ que tu veux?', answer:['ce','se'], correct:'se'})-[:verify]->(omonyme),
(:Exercice {instruction:'choisis la bonne orthographe', question:'_ chien me mordit à la main', answer:['ce','se'], correct:'ce'})-[:verify]->(omonyme),
(:Exercice {instruction:'choisis la bonne orthographe', question:'Léa _ prend pour une autre femme.', answer:['ce','se'], correct:'se'})-[:verify]->(omonyme),
(:Exercice {instruction:'choisis la bonne orthographe', question:'_ se trouve le chocolat?', answer:['où','ou'], correct:'où'})-[:verify]->(omonyme),
(:Exercice {instruction:'choisis la bonne orthographe', question:'Aime tu la vanille _ le chocolat', answer:['où','ou'], correct:'ou'})-[:verify]->(omonyme),
(:Exercice {instruction:'choisis la bonne orthographe', question:'La semaine derniere _ nous avons mangé, c\'etait un bon restaurant.', answer:['où','ou'], correct:'où'})-[:verify]->(omonyme),
(:Exercice {instruction:'choisis la bonne orthographe', question:'_ DVD sont les miens', answer:['ces','c\'est'], correct:'ces'})-[:verify]->(omonyme),
(:Exercice {instruction:'choisis la bonne orthographe', question:'_ voitures sont belles', answer:['ces','c\'est'], correct:'c\'est'})-[:verify]->(omonyme),
(:Exercice {instruction:'choisis la bonne orthographe', question:'_ tout se que j\'aime', answer:['ces','c\'est'], correct:'c\'est'})-[:verify]->(omonyme),
(:Exercice {instruction:'choisis la bonne orthographe', question:'il _ trouver une pépite', answer:['peut','peu'], correct:'peut'})-[:verify]->(omonyme),
(:Exercice {instruction:'choisis la bonne orthographe', question:'Il y a trop _ de chocolat', answer:['peut','peu'], correct:'peu'})-[:verify]->(omonyme),

//Exercie 6
(:Exercice {instruction:'choisis la bonne orthographe', question:'il sortit (tout à coup/tout-à-coup) sans rien dire', answer:['tout à coup','tout-à-coup'], correct:'tout à coup'})-[:verify]->(autre),
(:Exercice {instruction:'choisis la bonne orthographe', question:'La sentinelle etait au (garde à vous/garde-à-vous)', answer:['garde à vous','garde-à-vous'], correct:'garde-à-vous'})-[:verify]->(autre),
(:Exercice {instruction:'choisis la bonne orthographe', question:'Ce tableau est un (chef d\'oeuvre/chef-d\'oeuvre)', answer:['chef d\'oeuvre','chef-d\'oeuvre'], correct:'chef-d\'oeuvre'})-[:verify]->(autre),
(:Exercice {instruction:'choisis la bonne orthographe', question:'J\'ai recu un (coup-de-pied/coup de pied)', answer:['coup-de-pied','coup de pied'], correct:'coup de pied'})-[:verify]->(autre),
(:Exercice {instruction:'choisis la bonne orthographe', question:'Je suis entré à la maison (sur le champ/sur-le-champ)', answer:['sur le champ','sur-le-champ'], correct:'sur-le-champ'})-[:verify]->(autre),
(:Exercice {instruction:'choisis la bonne orthographe', question:'Mon (sac à dos/sac-à-dos)', answer:['sac à dos','sac-à-dos'], correct:'sac à dos'})-[:verify]->(autre),
(:Exercice {instruction:'choisis la bonne orthographe', question:'Venez me (s\'il-vous-plait/s\'il vous plait)', answer:['s\'il-vous-plait','s\'il vous plait'], correct:'s\'il vous plait'})-[:verify]->(autre),
(:Exercice {instruction:'choisis la bonne orthographe', question:'Je suis (tout-à-fait/tout à fait) d\'accord', answer:['tout-à-fait','tout à fait'], correct:'tout à fait'})-[:verify]->(autre),
(:Exercice {instruction:'choisis la bonne orthographe', question:'Un manteau pourpre (c\'est-a-dire/c\'est a dire) rouge foncé', answer:['c\'est-a-dire','c\'est a dire'], correct:'c\'est-a-dire'})-[:verify]->(autre),
(:Exercice {instruction:'choisis la bonne orthographe', question:'un (arc-en-ciel/arc en ciel)', answer:['arc-en-ciel','arc en ciel'], correct:'arc-en-ciel'})-[:verify]->(autre);

//Get all database
MATCH (n) return n;
