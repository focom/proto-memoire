
//Delete all previous node
MATCH (n) DETACH DELETE n;


// First create Node
// Theme
CREATE (t1:Theme {name:'Syntax'}),(t2:Theme {name:'Homophone'}),
//Level 1
(cphrase:Chapitre {name:'Constituant de la phrase'}),(tphrase:Chapitre {name:'Types de phrase'}),
(homophone:Chapitre{name:'homophone'}),
//Level 2
(Ceasy:Chapitre {name:'Contenus d\'apprentissage'}), (Chard:Chapitre {name:'Contenus d\'appronfondissement'}),
(Teasy:Chapitre {name:'Contenus d\'apprentissage'}), (Thard:Chapitre {name:'Contenus d\'appronfondissement'}),
(omonyme:Chapitre {name:'Homonyme'}),(autre:Chapitre {name:'Autre Cas'}),

// Relation between chapter
(t1)-[:ifMastered]->(t2),
(cphrase)-[:define]->(t1), (tphrase)-[:define]->(t1),(homophone)-[:define]->(t2),
(Ceasy)-[:define]->(cphrase),(Chard)-[:define]->(cphrase),
(Teasy)-[:define]->(tphrase),(Thard)-[:define]->(tphrase),
(omonyme)-[:define]->(homophone),(autre)-[:define]->(homophone);



//Get all database
MATCH (n) return n;

// Then create relationship

//  For the theme Constituant de la phrase

// Create theme and first level of chapter
CREATE (cphrase:Chapitre {name:'Constituant de la phrase'})-[:define]->(t:Theme {name:'Syntax'}),
 (tphrase:Chapitre {name:'Types de phrase'})-[:define]->(t),

 //Create second level
(easy1:Chapitre {name:'Apprentissage'})-[:define {weight:1}]->(cphrase),(hard1:Chapitre {name:'Approfondir'})-[:define {weight:2}]->(cphrase),

// Add exercice to low level chapter
(:Exercice {Instruction:'Répondre correctement:',Question:'La terre est elle plate?',Reponse:['Oui','Non'],Correct:'Oui'})-[:verify]->(easy1);

