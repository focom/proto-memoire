
//Delete all previous node
MATCH (n) DETACH DELETE n;


// First create Node
// Theme
CREATE (t1:Theme {name:'Syntax'}),(t2:Theme {name:'Homophone'}),
//Level 1
(cphrase:Chapitre {name:'Constituant de la phrase'}),(tphrase:Chapitre {name:'Types de phrase et accord du verbe'}),
(homophone:Chapitre{name:'homophone'}),
//Level 2
(Ceasy:Chapitre {name:'Contenus d\'apprentissage'}), (Chard:Chapitre {name:'Contenus d\'appronfondissement'}),
(Tphrase:Chapitre {name:'Type de phrase'}), (conjugaison:Chapitre {name:'Contenus pour l\'accord du verbe'}),
(omonyme:Chapitre {name:'Homonyme'}),(autre:Chapitre {name:'Autre Cas'}),

// Relation between chapter
(t1)-[:ifMastered]->(t2),
(cphrase)-[:define]->(t1), (tphrase)-[:define]->(t1),(homophone)-[:define]->(t2),
(Ceasy)-[:define]->(cphrase),(Chard)-[:define]->(cphrase),
(Tphrase)-[:define]->(tphrase),(conjugaison)-[:define]->(tphrase),
(omonyme)-[:define]->(homophone),(autre)-[:define]->(homophone);

// Exercice 1
(:Exercice {instruction:'Trouve le sujet', question:'Mon petit frere derange les visiteur', answer:[petit frere,visiteur], correct:'petit frere'})-[:verify]->()
(:Exercice {instruction:'Trouve le sujet', question:'Je vais parler à mon pere, demain matin', answer:[je,pere], correct:'je'})-[:verify]->()
(:Exercice {instruction:'Trouve le sujet', question:'Ma soeur Isabelle partage mes impressions', answer:[Isabelle,impressions], correct:'Isabelle'})-[:verify]->()
(:Exercice {instruction:'Trouve le sujet', question:'Mon petit frere Pierre regrette ses gestes', answer:[Pierre,gestes], correct:'Pierre'})-[:verify]->()
(:Exercice {instruction:'Trouve le sujet', question:'Au souper, mon pere le réprimandera', answer:[souper,pere], correct:'pere'})-[:verify]->()
(:Exercice {instruction:'Trouve le complement de la phrase', question:'La petite s\'excusera à la prochaine visite', answer:[La petite, à la prochaine visite], correct:''})-[:verify]->()
(:Exercice {instruction:'Trouve le complement de la phrase', question:'Mon pere doit le reprendre plusieurs fois', answer:[Pere, plusieur fois], correct:''})-[:verify]->()
(:Exercice {instruction:'Trouve le complement de la phrase', question:'J\'aime la pizza avec du poivron', answer:[la pizza, avec du poivron], correct:''})-[:verify]->()
(:Exercice {instruction:'Trouve le complement de la phrase', question:'Morgane trouve un mouton rouge dans le champ', answer:[Morganne, dans le champ], correct:''})-[:verify]->()
(:Exercice {instruction:'Trouve le complement de la phrase', question:'Le voisin decouvre le tresor dans le jardin', answer:[decouvre, dans le jardin], correct:''})-[:verify]->()
(:Exercice {instruction:'Trouve le verbe', question:'Morgane trouve un mouton rouge dans le champ', answer:[Sous, mange], correct:''})-[:verify]->()
(:Exercice {instruction:'Trouve le verbe', question:'Morgane trouve un mouton rouge dans le champ', answer:['meme si', 'j\'aime'], correct:''})-[:verify]->()
(:Exercice {instruction:'Trouve le verbe', question:'La vache broute l\'herbe', answer:[broute, 'l\'herbe'], correct:''})-[:verify]->()


//Get all database
MATCH (n) return n;
