import json
import re

text = """
### **Unit 2 (Assessment 01)**

* [cite_start]**Question 1:** Who is known as Father of structuralism? [cite: 213]
    * [cite_start]**Options:** Edward B. Titchener [cite: 214][cite_start], Thorndike [cite: 215][cite_start], Wilhelm Wundt [cite: 216][cite_start], William James [cite: 237]
    * [cite_start]**Accepted Answer:** Wilhelm Wundt [cite: 241]
* [cite_start]**Question 2:** Which psychology school proposed that mental activities can be broken down into basic operational elements [cite: 242]
    * [cite_start]**Options:** Behaviorism [cite: 243][cite_start], Structuralism [cite: 244][cite_start], Gestalt psychology [cite: 245][cite_start], Functionalism [cite: 246]
    * [cite_start]**Accepted Answer:** Structuralism [cite: 249]
* [cite_start]**Question 3:** Which "school" of psychology emphasized objectivity of research methods and [cite: 251]
    * [cite_start]**Options:** behaviorism [cite: 273] *(Note: Other options are obscured by the document's side menu text)*
    * [cite_start]**Accepted Answer:** behaviorism [cite: 273]
* [cite_start]**Question 4:** Which school of Psychology assume that psychological phenomena could not be reduced to simple elements but rather had to be analyzed and studied in their entirety [cite: 274, 277]
    * [cite_start]**Options:** Behaviorism [cite: 279][cite_start], Structuralism [cite: 282][cite_start], Functionalism [cite: 283][cite_start], Gestalt [cite: 286]
    * [cite_start]**Accepted Answer:** Gestalt [cite: 292]
* [cite_start]**Question 5:** The philosopher John Locke was a strong believer in _____ which rests on the assumption that knowledge comes from an individual's own experience [cite: 297]
    * [cite_start]**Options:** empiricism [cite: 298][cite_start], nativism [cite: 299][cite_start], introspection [cite: 300][cite_start], behaviorism [cite: 301]
    * [cite_start]**Accepted Answer:** empiricism [cite: 304]
* [cite_start]**Question 6:** Who proposed that - "Behavior is a learned response, reinforced by the consequences resulting from that behavior". [cite: 305]
    * [cite_start]**Options:** John B. Watson [cite: 306][cite_start], Thorndike [cite: 307][cite_start], Ivan Pavlov [cite: 308][cite_start], B.F. Skinner [cite: 309]
    * [cite_start]**Accepted Answer:** B.F. Skinner [cite: 313]
* [cite_start]**Question 7:** All connectionist models share the assumption that: [cite: 314]
    * [cite_start]**Options:** processing occurs serially [cite: 316][cite_start], a central processor directs the flow of information [cite: 317][cite_start], processing occurs in parallel [cite: 318][cite_start], knowledge is stored in various storehouses [cite: 319]
    * [cite_start]**Accepted Answer:** processing occurs in parallel [cite: 323]
* [cite_start]**Question 8:** Mental representation consists of [cite: 324]
    * [cite_start]**Options:** Form [cite: 334][cite_start], Content [cite: 335][cite_start], Form and Content [cite: 336][cite_start], None of the above [cite: 337]
    * [cite_start]**Accepted Answer:** Form and Content [cite: 341]
* [cite_start]**Question 9:** The earliest theories about cognitive abilities date back to: [cite: 342]
    * [cite_start]**Options:** Aristotle and Plato [cite: 343][cite_start], Sigmund Freud [cite: 344][cite_start], Williams James [cite: 345][cite_start], Benjamin Franklin [cite: 346]
    * [cite_start]**Accepted Answer:** Aristotle and Plato [cite: 350]
* [cite_start]**Question 10:** Boxes-and arrows models of cognition is based on which paradigm of psychology [cite: 351]
    * [cite_start]**Options:** Evolutionary approach [cite: 352][cite_start], Information processing approach [cite: 353][cite_start], Ecological Approach [cite: 354][cite_start], None of the above [cite: 355]
    * [cite_start]**Accepted Answer:** Information processing approach [cite: 359]

---

### **Unit 3 (Assessment 02)**

* [cite_start]**Question 1:** The process of sensory input and their meaningful interpretation of information is known as [cite: 414]
    * [cite_start]**Options:** Sensation [cite: 415][cite_start], Perception [cite: 416][cite_start], Recognition [cite: 417][cite_start], Identification [cite: 418]
    * [cite_start]**Accepted Answer:** Perception [cite: 421]
* [cite_start]**Question 2:** Which of the following sequence is correct for classic approach to perception [cite: 422]
    * [cite_start]**Options:** proximal stimulus, sensory registration, distal stimulus, percept [cite: 423][cite_start]; distal stimulus, proximal stimulus, percept, sensory registration [cite: 423][cite_start]; distal stimulus, sensory registration, proximal stimulus, percept [cite: 423][cite_start]; sensory registration, distal stimulus, proximal stimulus, percept [cite: 423]
    * [cite_start]**Accepted Answer:** distal stimulus, sensory registration, proximal stimulus, percept [cite: 426]
* [cite_start]**Question 3:** Which school of psychology explains the phenomena of figure-ground organization [cite: 427]
    * [cite_start]**Options:** Functionalism [cite: 430][cite_start], Gestalt [cite: 449] *(Note: Other options are obscured)*
    * [cite_start]**Accepted Answer:** Gestalt [cite: 449]
* [cite_start]**Question 4:** Reversible figures illustrate the principle of: [cite: 451]
    * [cite_start]**Options:** size constancy [cite: 461][cite_start], figure-ground organization [cite: 462][cite_start], dimensionality [cite: 463][cite_start], retinal imagery [cite: 465]
    * [cite_start]**Accepted Answer:** figure-ground organization [cite: 472]
* [cite_start]**Question 5:** The perceiver starts with small bits of information from the environment that he combines in various ways to form a percept is processed through [cite: 476]
    * [cite_start]**Options:** Template matching [cite: 481][cite_start], Theory-driven processing [cite: 482][cite_start], Data-driven processing [cite: 483][cite_start], Parallel processing [cite: 484]
    * [cite_start]**Accepted Answer:** Data-driven processing [cite: 488]
* [cite_start]**Question 6:** How many primitive geons were explained by Biederman [cite: 489]
    * [cite_start]**Options:** 36 [cite: 491][cite_start], 72 [cite: 492][cite_start], 44 [cite: 493][cite_start], 63 [cite: 494]
    * [cite_start]**Accepted Answer:** 36 [cite: 498]
* [cite_start]**Question 7:** People perceive and interpret complex things into its simplest form is known as [cite: 499]
    * [cite_start]**Options:** Principle of similarity [cite: 504][cite_start], Law of pragnanz [cite: 505][cite_start], Principle of proximity [cite: 506][cite_start], Principle of common fate [cite: 507]
    * [cite_start]**Accepted Answer:** Law of pragnanz [cite: 511]
* [cite_start]**Question 8:** Which of the following model consists demons as feature detector [cite: 512]
    * [cite_start]**Options:** Template matching [cite: 516][cite_start], Gestalt perception [cite: 517][cite_start], Prototype matching [cite: 518][cite_start], Pandemonium model [cite: 524]
    * [cite_start]**Accepted Answer:** Pandemonium model [cite: 526]
* **Question 9:** The top-down process of perception interacts with the bottom-up process also. [cite_start]What is the correct sequence for visual perception explained by David Marr [cite: 527, 528]
    * [cite_start]**Options:** 2-D sketch, 2½- D sketch, 3-D sketch[cite: 529]; [cite_start]1-D sketch, 2-D sketch, 3-D sketch [cite: 530][cite_start]; primal sketch, 2-D sketch, 3-D sketch [cite: 531][cite_start]; primal sketch, 2½-D sketch, 3-D sketch [cite: 532]
    * [cite_start]**Accepted Answer:** primal sketch, 2½-D sketch, 3-D sketch [cite: 536]
* [cite_start]**Question 10:** Who gave the idea of optic flow during world war II [cite: 537]
    * [cite_start]**Options:** Marr [cite: 538][cite_start], Cattell [cite: 541][cite_start], Gibson [cite: 542][cite_start], Rensink [cite: 543]
    * [cite_start]**Accepted Answer:** Gibson [cite: 547]

---

### **Unit 4 (Assessment 03)**

* [cite_start]**Question 1:** Dichotic listening task is used to investigates [cite: 567]
    * [cite_start]**Options:** selective attention [cite: 567][cite_start], auditory function [cite: 567][cite_start], hearing problems [cite: 567][cite_start], attention [cite: 567]
    * [cite_start]**Accepted Answer:** selective attention [cite: 567]
* [cite_start]**Question 2:** Jacob is attending only important information which are relevant to him and blocking the unwanted information, which attentional theory can explain this phenomenon [cite: 567]
    * [cite_start]**Options:** Attenuation theory [cite: 567][cite_start], Late selection theory [cite: 567][cite_start], Schema theory [cite: 567][cite_start], Filter theory [cite: 567]
    * [cite_start]**Accepted Answer:** Filter theory [cite: 567]
* [cite_start]**Question 3:** Greater effort or concentration results in better performance on: [cite: 567]
    * [cite_start]**Options:** tasks that require resource-limited processing [cite: 586] *(Note: Other options are obscured)*
    * [cite_start]**Accepted Answer:** tasks that require resource-limited processing [cite: 586]
* [cite_start]**Question 4:** In a book fair, most of the people tune into a single voice when hearing their own name and ignore other voices, this phenomenon is famously known as [cite: 589, 591]
    * [cite_start]**Options:** Priming effect [cite: 594][cite_start], Selective attention [cite: 597][cite_start], Cocktail party effect [cite: 600][cite_start], Dichotic listening [cite: 603]
    * [cite_start]**Accepted Answer:** Cocktail party effect [cite: 609]
* [cite_start]**Question 5:** Which of the following factors does NOT influence the allocation of mental resources in Kahneman's capacity model? [cite: 610]
    * [cite_start]**Options:** the lateness of selection [cite: 615][cite_start], the difficulty of the task [cite: 616][cite_start], enduring dispositions [cite: 617][cite_start], the state of arousal [cite: 618]
    * [cite_start]**Accepted Answer:** the lateness of selection [cite: 621]
* [cite_start]**Question 6:** Who describes the allocation policies for cognitive resources in attention process [cite: 622]
    * [cite_start]**Options:** Becklen [cite: 623][cite_start], Neisser [cite: 624][cite_start], Johnston & Heinz [cite: 625][cite_start], Kahneman [cite: 626]
    * [cite_start]**Accepted Answer:** Kahneman [cite: 630]
* [cite_start]**Question 7:** Which of the following criteria is required for cognitive process to be automatic processing according to Posner and Snyder [cite: 631]
    * [cite_start]**Options:** It must occur without intention [cite: 632][cite_start], It must occur without involving conscious awareness [cite: 633][cite_start], It must not interfere with other mental activity [cite: 634][cite_start], All of the above [cite: 635]
    * [cite_start]**Accepted Answer:** All of the above [cite: 638]
* [cite_start]**Question 8:** Which of the following task is better in explaining effect of practice in attention [cite: 639]
    * [cite_start]**Options:** Priming [cite: 650][cite_start], Visual search task [cite: 651][cite_start], Dichotic listening task [cite: 652][cite_start], Stroop task [cite: 653]
    * [cite_start]**Accepted Answer:** Stroop task [cite: 656]
* [cite_start]**Question 9:** Inattentional blindness occurs due to [cite: 657]
    * [cite_start]**Options:** Psychiatric deficits [cite: 658][cite_start], Lack of perception [cite: 659][cite_start], Visual blindness [cite: 660][cite_start], Lack of attention [cite: 661]
    * [cite_start]**Accepted Answer:** Lack of attention [cite: 666]
* [cite_start]**Question 10:** When attention is overloaded, then participants make integration error, result in [cite: 667]
    * [cite_start]**Options:** Illusory conjunction [cite: 668][cite_start], Inattention [cite: 669][cite_start], Memory illusion [cite: 670][cite_start], Divided attention [cite: 671]
    * [cite_start]**Accepted Answer:** Illusory conjunction [cite: 675]

---

### **Unit 5 (Assessment 04)**

* [cite_start]**Question 1:** Iconic memory is associated with which of the sensory modality [cite: 706]
    * [cite_start]**Options:** Auditory [cite: 709][cite_start], Smell [cite: 711][cite_start], Visual [cite: 716][cite_start], Touch [cite: 717]
    * [cite_start]**Accepted Answer:** Visual [cite: 726]
* **Question 2:** If two stimuli arrive at the same time, the response for second stimuli will be slower than first stimuli. [cite_start]This phenomenon is referred to as: [cite: 728, 731]
    * [cite_start]**Options:** Response time [cite: 737][cite_start], Latency period [cite: 738][cite_start], Psychological refractory period [cite: 741][cite_start], Relative dependence period [cite: 744]
    * [cite_start]**Accepted Answer:** Psychological refractory period_ [cite: 752]
* [cite_start]**Question 3:** The results of the Brown-Peterson short-term memory task can be explained by: [cite: 755]
    * [cite_start]**Options:** both decay and interference [cite: 786] *(Note: Other options are obscured)*
    * [cite_start]**Accepted Answer:** both decay and interference [cite: 786]
* [cite_start]**Question 4:** Haptic memory is associated with which of the sensory modality [cite: 787]
    * [cite_start]**Options:** Visual [cite: 788][cite_start], Auditory [cite: 789][cite_start], Touch [cite: 790][cite_start], Smell [cite: 791]
    * [cite_start]**Accepted Answer:** Touch [cite: 793]
* [cite_start]**Question 5:** Who gave magic number [cite: 794]
    * [cite_start]**Options:** George A. Miller [cite: 795][cite_start], Neisser [cite: 796][cite_start], R. Conrad [cite: 797][cite_start], Baddeley [cite: 798]
    * [cite_start]**Accepted Answer:** George A. Miller [cite: 802]
* [cite_start]**Question 6:** FBINSAKGBCBICIAMI5BND The total string can be learnt by breaking it into initials for security agencies around the world, it could be possible by [cite: 803, 807]
    * [cite_start]**Options:** Editing [cite: 808][cite_start], Chunking [cite: 809][cite_start], Memory [cite: 810][cite_start], Leaming [cite: 811]
    * [cite_start]**Accepted Answer:** Chunking [cite: 815]
* [cite_start]**Question 7:** Studies of coding in short-term memory suggest that which of the following would be most DIFFICULT to recall correctly? [cite: 816]
    * [cite_start]**Options:** big-large-huge-tall-wide [cite: 817][cite_start], C-O-G-Q-D [cite: 818][cite_start], A-E-I-O-U [cite: 819][cite_start], C-D-P-V-T [cite: 820]
    * [cite_start]**Accepted Answer:** C-D-P-V-T [cite: 824]
* [cite_start]**Question 8:** The primary function of central executive of working memory system [cite: 825]
    * [cite_start]**Options:** Rehearsal [cite: 831][cite_start], Attentional system [cite: 832][cite_start], Memory store [cite: 833][cite_start], Retrieval of information [cite: 834]
    * [cite_start]**Accepted Answer:** Attentional system [cite: 838]
* **Question 9:** John retrieves the information from past and uses this information to make some strategies to perform a specific task. [cite_start]Which of the working memory component was active during this? [cite: 839, 840]
    * [cite_start]**Options:** Phonological buffer [cite: 841][cite_start], Episodic buffer [cite: 842][cite_start], Central executive [cite: 843][cite_start], Visuospatial sketchpad [cite: 844]
    * [cite_start]**Accepted Answer:** Central executive [cite: 848]
* [cite_start]**Question 10:** Who proposed the working memory model [cite: 849]
    * [cite_start]**Options:** Hitch [cite: 850][cite_start], Baddeley [cite: 851][cite_start], Baddeley and Hitch [cite: 852][cite_start], Baddeley and Andrade [cite: 853]
    * [cite_start]**Accepted Answer:** Baddeley and Hitch [cite: 857]

---

### **Unit 6 (Assessment 05)**

* [cite_start]**Question 1:** Which of the following are most likely to be confused in long-term memory? [cite: 890]
    * [cite_start]**Options:** the words "see" and "bee" [cite: 893][cite_start], the words "big" and "large" [cite: 896][cite_start], the letters P and R [cite: 900][cite_start], the letters C and B [cite: 902]
    * [cite_start]**Accepted Answer:** the words "big" and "large" [cite: 911]
* **Question 2:** You had just heard some bad news and were very sad when you listened to a lecture on levels of processing. Now it is time to take a test on that lecture material. [cite_start]According to the mood-dependent memory effect, you should: [cite: 924, 925]
    * [cite_start]**Options:** sit in the same seat in the classroom as when you listened to the lecture [cite: 928][cite_start], try to associate the lecture with your own life [cite: 929][cite_start], watch a sad movie just before the exam [cite: 930][cite_start], attempt to visualize the material. [cite: 931]
    * [cite_start]**Accepted Answer:** watch a sad movie just before the exam [cite: 934]
* [cite_start]**Question 3:** Memory of facts and memory of time and event is respectively known as [cite: 935]
    * [cite_start]**Options:** Semantic memory, episodic memory [cite: 957] *(Note: Other options are obscured)*
    * [cite_start]**Accepted Answer:** Semantic memory, episodic memory [cite: 957]
* [cite_start]**Question 4:** Which memory system is temporal in nature [cite: 959]
    * [cite_start]**Options:** False memory [cite: 963][cite_start], Semantic memory [cite: 968][cite_start], Memory of facts [cite: 969][cite_start], Episodic memory [cite: 972]
    * [cite_start]**Accepted Answer:** Episodic memory [cite: 975]
* [cite_start]**Question 5:** Memory of past with emotionally arousing events is known as [cite: 976]
    * [cite_start]**Options:** Short-term memory [cite: 978][cite_start], Flashbulb memory [cite: 979][cite_start], Eyewitness memory [cite: 980][cite_start], Long-term memory [cite: 981]
    * [cite_start]**Accepted Answer:** Flashbulb memory [cite: 984]
* [cite_start]**Question 6:** Encoding and retrieval of information that actually did not happen in past, is known as [cite: 985]
    * [cite_start]**Options:** Repressed memory [cite: 986][cite_start], Flashbulb memory [cite: 987][cite_start], False memory [cite: 988][cite_start], episodic memory [cite: 991]
    * [cite_start]**Accepted Answer:** False memory [cite: 995]
* [cite_start]**Question 7:** Which of the following task is responsible for induction of false memory in laboratory conditions [cite: 996]
    * [cite_start]**Options:** Pair associative learning task [cite: 997][cite_start], Pursuit rotor task [cite: 998][cite_start], Auditory detection task [cite: 999][cite_start], Deese-Roediger-McDermott [cite: 1000]
    * [cite_start]**Accepted Answer:** Deese-Roediger-McDermott [cite: 1004]
* [cite_start]**Question 8:** What is the correct name for memories for events, experiences and personal information from one's own life [cite: 1005]
    * [cite_start]**Options:** Autobiographical memory [cite: 1006][cite_start], Flashbulb memory [cite: 1014][cite_start], Implicit memory [cite: 1015][cite_start], Eyewitness memory [cite: 1016]
    * [cite_start]**Accepted Answer:** Autobiographical memory [cite: 1019]
* [cite_start]**Question 9:** The "tip-of-the-tongue" phenomenon is a problem of [cite: 1020]
    * [cite_start]**Options:** Engram [cite: 1021][cite_start], Retrieval [cite: 1022][cite_start], Repression [cite: 1023][cite_start], Storage [cite: 1024]
    * [cite_start]**Accepted Answer:** Retrieval [cite: 1028]
* [cite_start]**Question 10:** Who proposed the idea that LTM is reconstructive: [cite: 1029]
    * [cite_start]**Options:** Frederic Bartlett [cite: 1030][cite_start], Ulric Neisser [cite: 1031][cite_start], Elizabeth Loftus [cite: 1032][cite_start], Marigold Linton [cite: 1033]
    * [cite_start]**Accepted Answer:** Frederic Bartlett [cite: 1037]

---

### **Unit 7 (Assessment 06)**

* [cite_start]**Question 1:** The memory of facts, knowledge and meaning is [cite: 1068]
    * [cite_start]**Options:** Recognition memory [cite: 1072][cite_start], Semantic memory [cite: 1079][cite_start], Implicit memory [cite: 1080][cite_start], Episodic memory [cite: 1082]
    * [cite_start]**Accepted Answer:** Semantic memory [cite: 1090]
* [cite_start]**Question 2:** Collins and Quillian's hierarchical network model would predict that which of the following statements would take the LONGEST time to verify? [cite: 1093]
    * [cite_start]**Options:** Boo has a popular Facebook page [cite: 1103][cite_start], Boo is an animal [cite: 1104][cite_start], Boo is a dog [cite: 1105][cite_start], Boo is a living thing [cite: 1106]
    * [cite_start]**Accepted Answer:** Boo is a living thing [cite: 1115]
* [cite_start]**Question 3:** The word superiority effect is related to the idea of: [cite: 1117]
    * [cite_start]**Options:** spreading activation [cite: 1138] *(Note: Other options are obscured)*
    * [cite_start]**Accepted Answer:** spreading activation [cite: 1138]
* [cite_start]**Question 4:** Who propose the Hierarchical Semantic Model [cite: 1140]
    * [cite_start]**Options:** Collins & Quillinan [cite: 1143][cite_start], Schacter [cite: 1149][cite_start], Tulving [cite: 1150][cite_start], Miller [cite: 1154]
    * [cite_start]**Accepted Answer:** Collins & Quillinan [cite: 1158]
* [cite_start]**Question 5:** The excitation propagation of one node to another associated node in semantic network is [cite: 1159]
    * [cite_start]**Options:** Spreading activation [cite: 1163][cite_start], Node activation [cite: 1164][cite_start], Network hierarchy [cite: 1165][cite_start], Semantic association [cite: 1166]
    * [cite_start]**Accepted Answer:** Spreading activation [cite: 1170]
* [cite_start]**Question 6:** Properties and facts are stored at highest level in network model to reduce mental energy, this concept is known as [cite: 1171]
    * [cite_start]**Options:** Economic theory [cite: 1175][cite_start], Semantic network [cite: 1176][cite_start], Cognitive economy [cite: 1177][cite_start], Cognitive revolution [cite: 1178]
    * [cite_start]**Accepted Answer:** Cognitive economy [cite: 1182]
* **Question 7:** The response is faster for "Robin is a bird" instead than "Turkey is a bird". [cite_start]It can be explained by [cite: 1183, 1184]
    * [cite_start]**Options:** Typical instance [cite: 1187][cite_start], Semantic association [cite: 1188][cite_start], Typicality effect [cite: 1189][cite_start], Spreading activation [cite: 1190]
    * [cite_start]**Accepted Answer:** Typicality effect [cite: 1194]
* [cite_start]**Question 8:** Who proposed the ACT model of memory [cite: 1195]
    * [cite_start]**Options:** John Watson [cite: 1198][cite_start], John Anderson [cite: 1199][cite_start], Collins and Qullins [cite: 1205][cite_start], Meyer and Schvaneveldt [cite: 1206]
    * [cite_start]**Accepted Answer:** John Anderson [cite: 1210]
* [cite_start]**Question 9:** The organization of packet of information available in brain which have fixed part and variables is consider as [cite: 1211]
    * [cite_start]**Options:** Prototype [cite: 1212][cite_start], Template [cite: 1213][cite_start], Schema [cite: 1214][cite_start], Feature [cite: 1215]
    * [cite_start]**Accepted Answer:** Schema [cite: 1219]
* [cite_start]**Question 10:** Who tells you, what to do and how to behave in restaurant when you go for food [cite: 1220]
    * [cite_start]**Options:** Waiter [cite: 1221][cite_start], Experience [cite: 1222][cite_start], Rules [cite: 1223][cite_start], Script [cite: 1224]
    * [cite_start]**Accepted Answer:** Script [cite: 1228]

---

### **Unit 8 (Assessment 07)**

* [cite_start]**Question 1:** The class of similar things that shares perceptual, biological, or functional similarities is known as [cite: 1248]
    * [cite_start]**Options:** Percept [cite: 1248][cite_start], Group [cite: 1248][cite_start], Category [cite: 1248][cite_start], Concept [cite: 1248]
    * [cite_start]**Accepted Answer:** Category [cite: 1248]
* [cite_start]**Question 2:** The mental representation of an object, event, or pattern that has stored in it much of the knowledge typically thought relevant to that object, event, or pattern, can be defined as a [cite: 1248]
    * [cite_start]**Options:** Category [cite: 1248][cite_start], Group [cite: 1248][cite_start], Concept [cite: 1248][cite_start], Percept [cite: 1248]
    * [cite_start]**Accepted Answer:** Concept [cite: 1248]
* [cite_start]**Question 3:** Which of the following approach need actual individual instance to make a category [cite: 1248]
    * [cite_start]**Options:** Exemplar view [cite: 1266] *(Note: Other options are obscured)*
    * [cite_start]**Accepted Answer:** Exemplar view [cite: 1266]
* [cite_start]**Question 4:** In which of the approach to concepts and categorization, people uses their own knowledge to guide tier classification of objects [cite: 1267]
    * [cite_start]**Options:** Classical view [cite: 1272][cite_start], Porotype view [cite: 1274][cite_start], Knowledge-based [cite: 1276][cite_start], Exemplar-based [cite: 1279]
    * [cite_start]**Accepted Answer:** Knowledge-based [cite: 1283]
* [cite_start]**Question 5:** Which of the following views are also uses by Schemata view for concept and categorization formation [cite: 1284]
    * [cite_start]**Options:** Prototype view [cite: 1285][cite_start], Exemplar view [cite: 1286][cite_start], Prototype and Exemplar views [cite: 1287][cite_start], None of the above [cite: 1288]
    * [cite_start]**Accepted Answer:** Prototype and Exemplar views [cite: 1292]
* **Question 6:** The dog is an animal, which has 4 legs & tail and is man's best friend. [cite_start]So what is Dog here [cite: 1293, 1294]
    * [cite_start]**Options:** Category [cite: 1295][cite_start], Concept [cite: 1296][cite_start], Knowledge [cite: 1297][cite_start], Animal [cite: 1298]
    * [cite_start]**Accepted Answer:** Concept [cite: 1302]
* [cite_start]**Question 7:** Possible strategies for concept formation involve [cite: 1303]
    * [cite_start]**Options:** Simultaneous Scanning [cite: 1304][cite_start], Successive Scanning [cite: 1305][cite_start], Conservative Focusing [cite: 1306][cite_start], All above [cite: 1307]
    * [cite_start]**Accepted Answer:** All above [cite: 1309]
* [cite_start]**Question 8:** You might have a "script" for [cite: 1310]
    * [cite_start]**Options:** what a "pet" is [cite: 1323][cite_start], what happens when you go to the barber/hairstylist [cite: 1324][cite_start], what a "cat" is [cite: 1325][cite_start], what a classroom looks like. [cite: 1326]
    * [cite_start]**Accepted Answer:** what happens when you go to the barber/hairstylist [cite: 1330]
* [cite_start]**Question 9:** Implicit learning is also known as: [cite: 1331]
    * [cite_start]**Options:** nominal-kind learning [cite: 1332][cite_start], nonanalytic concept formation [cite: 1333][cite_start], knowledge-based concept formation [cite: 1334][cite_start], analytic concept formation [cite: 1335]
    * [cite_start]**Accepted Answer:** nonanalytic concept formation [cite: 1338]
* [cite_start]**Question 10:** Which of the following poses a problem for the prototype view of concepts? [cite: 1340]
    * [cite_start]**Options:** an inability to explain why the typicality of a particular instance can depend upon context [cite: 1341][cite_start], an inability to explain the typicality effect [cite: 1342][cite_start], an inability to explain why people have a hard time providing strict definitions of their concepts [cite: 1343][cite_start], an inability to explain why some classifications are easy to make and others are unclear [cite: 1344]
    * [cite_start]**Accepted Answer:** an inability to explain why the typicality of a particular instance can depend upon context [cite: 1347]

---

### **Unit 9 (Assessment 08)**

* [cite_start]**Question 1:** The memory technique to make better encoding and recalling/recognizing information is known as [cite: 1390]
    * [cite_start]**Options:** Encoding specificity [cite: 1392][cite_start], Rehearsal [cite: 1393][cite_start], Mnemonics [cite: 1394][cite_start], Remembering [cite: 1395]
    * [cite_start]**Accepted Answer:** Mnemonics [cite: 1399]
* [cite_start]**Question 2:** Who proposed relational-organizational hypothesis for encoding of information in LTM [cite: 1400]
    * [cite_start]**Options:** Moyer [cite: 1401][cite_start], Paivio [cite: 1402][cite_start], Bower [cite: 1403][cite_start], Brooks [cite: 1406]
    * [cite_start]**Accepted Answer:** Bower [cite: 1415]
* [cite_start]**Question 3:** According to the dual-coding hypothesis of LTM, which of the following coding systems are available to represent information [cite: 1416]
    * [cite_start]**Options:** Verbal and Imagery [cite: 1446] *(Note: Other options are obscured)*
    * [cite_start]**Accepted Answer:** Verbal and Imagery [cite: 1446]
* [cite_start]**Question 4:** According to relational-organizational hypothesis which type of stimuli will help in improving memory [cite: 1447]
    * [cite_start]**Options:** Imagery [cite: 1448][cite_start], Verbal [cite: 1449][cite_start], Acoustic [cite: 1450][cite_start], All of above [cite: 1451]
    * [cite_start]**Accepted Answer:** Imagery [cite: 1456]
* [cite_start]**Question 5:** Internal processes of mental visualization and visual perception are same, this principle of visual imagery is known as [cite: 1457]
    * [cite_start]**Options:** Visual perception [cite: 1458][cite_start], Spatial equivalence [cite: 1459][cite_start], Implicit encoding [cite: 1460][cite_start], Perceptual equivalence [cite: 1461]
    * [cite_start]**Accepted Answer:** Perceptual equivalence [cite: 1465]
* [cite_start]**Question 6:** How many basic principles Finke gave to describes the nature and properties of visual images [cite: 1466]
    * [cite_start]**Options:** 3 [cite: 1467][cite_start], 5 [cite: 1468][cite_start], 2 [cite: 1469][cite_start], 4 [cite: 1470]
    * [cite_start]**Accepted Answer:** 5 [cite: 1474]
* [cite_start]**Question 7:** Which of the following property is not related to visual imagery [cite: 1475]
    * [cite_start]**Options:** Implicit encoding [cite: 1476][cite_start], Priming [cite: 1477][cite_start], Perceptual equivalence [cite: 1478][cite_start], Structural equivalence [cite: 1479][cite_start], Spatial equivalence [cite: 1480]
    * [cite_start]**Accepted Answer:** Priming [cite: 1483]
* [cite_start]**Question 8:** When experimenters unconsciously give subtle cues to participants, which influence participant to expect something is referred as [cite: 1485, 1490]
    * [cite_start]**Options:** Expectancy [cite: 1491][cite_start], Participant belief [cite: 1492][cite_start], Tacit knowledge [cite: 1493][cite_start], Experimenter expectancy effect [cite: 1494]
    * [cite_start]**Accepted Answer:** Experimenter expectancy effect [cite: 1497]
* [cite_start]**Question 9:** What are the controversies of visual imagery concept [cite: 1498]
    * [cite_start]**Options:** Tacit knowledge and demand characteristics [cite: 1499][cite_start], Picture metaphor [cite: 1500][cite_start], Propositional theory [cite: 1501][cite_start], All mentioned [cite: 1502]
    * [cite_start]**Accepted Answer:** All mentioned [cite: 1506]
* [cite_start]**Question 10:** Mental depiction of parts of our environment special landmarks and their spatial relationship is [cite: 1508]
    * [cite_start]**Options:** Cognitive map [cite: 1509][cite_start], Spatial map [cite: 1510][cite_start], Mental representation [cite: 1511][cite_start], Mental map [cite: 1512]
    * [cite_start]**Accepted Answer:** Cognitive map [cite: 1516]

---

### **Unit 10 (Assessment 09)**

* [cite_start]**Question 1:** Which of the following is NOT a characteristic of language [cite: 1535]
    * [cite_start]**Options:** Regular [cite: 1535][cite_start], Consistent [cite: 1535][cite_start], Arbitrary [cite: 1535][cite_start], Discrete [cite: 1535]
    * [cite_start]**Accepted Answer:** Consistent [cite: 1535]
* [cite_start]**Question 2:** The study in which various phonemes are combined together to yield meaningful units of language is called [cite: 1535]
    * [cite_start]**Options:** Pragmatics [cite: 1535][cite_start], Phonology [cite: 1535][cite_start], Semantics [cite: 1535][cite_start], Morphology [cite: 1535]
    * [cite_start]**Accepted Answer:** Morphology [cite: 1535]
* [cite_start]**Question 3:** Smallest meaningful units of language [cite: 1535]
    * [cite_start]**Options:** Morpheme [cite: 1550] *(Note: Other options are obscured)*
    * [cite_start]**Accepted Answer:** Morpheme [cite: 1550]
* [cite_start]**Question 4:** The study of speech sound and how they are produced is known as [cite: 1553]
    * [cite_start]**Options:** Morphology [cite: 1556][cite_start], Phonology [cite: 1558][cite_start], Voicing [cite: 1560][cite_start], Phonetics [cite: 1563]
    * [cite_start]**Accepted Answer:** Phonetics [cite: 1569]
* [cite_start]**Question 5:** The systematic ways of combining the speech sounds that help us in studying the sounds of language is studied under [cite: 1570]
    * [cite_start]**Options:** Phonetics [cite: 1571][cite_start], Phonology [cite: 1572][cite_start], Morphology [cite: 1573][cite_start], Pragmatics [cite: 1574]
    * [cite_start]**Accepted Answer:** Phonology [cite: 1579]
* [cite_start]**Question 6:** The smallest unit of sound that makes a meaningful difference in a given language is known as [cite: 1580]
    * [cite_start]**Options:** Lexemes [cite: 1581][cite_start], Morpheme [cite: 1582][cite_start], Phoneme [cite: 1583][cite_start], Syntax [cite: 1584]
    * [cite_start]**Accepted Answer:** Phoneme [cite: 1588]
* [cite_start]**Question 7:** The phoneme restoration effect was first documented by [cite: 1589]
    * [cite_start]**Options:** Milner [cite: 1590][cite_start], Garret [cite: 1591][cite_start], Warren [cite: 1592][cite_start], Bierwisch [cite: 1593]
    * [cite_start]**Accepted Answer:** Warren [cite: 1597]
* [cite_start]**Question 8:** The "given-new" strategy in text processing was given by [cite: 1598]
    * [cite_start]**Options:** Bierwisch [cite: 1599][cite_start], Just and carpenter [cite: 1600][cite_start], Kintsch and Keenan [cite: 1611][cite_start], Haviland and Clark [cite: 1612]
    * [cite_start]**Accepted Answer:** Haviland and Clark [cite: 1616]
* [cite_start]**Question 9:** A speech act such as "I promise to study my psychology textbook tonight" is called a(n): [cite: 1617]
    * [cite_start]**Options:** assertive [cite: 1618][cite_start], expressive [cite: 1619][cite_start], commissive [cite: 1620][cite_start], directive [cite: 1621]
    * [cite_start]**Accepted Answer:** commissive [cite: 1626]
* **Question 10:** Some African languages allow two consonants to appear together at the beginning of a word (as in "Nkomo"); English does not allow this to occur unless the first consonant is an "S" (as in "skull"). [cite_start]This example illustrates a difference in the _____ of the two languages. [cite: 1628-1630]
    * [cite_start]**Options:** semantics [cite: 1631][cite_start], phonetics [cite: 1632][cite_start], phonology [cite: 1633][cite_start], syntax [cite: 1634]
    * [cite_start]**Accepted Answer:** phonology [cite: 1638]

---

### **Unit 11 (Assessment 10)**

* [cite_start]**Question 1:** Which of the following is not a type of problem [cite: 1667]
    * [cite_start]**Options:** Ill-defined problem [cite: 1683][cite_start], Routine problem [cite: 1684][cite_start], Well defined problem [cite: 1685][cite_start], Narrow problem [cite: 1686]
    * [cite_start]**Accepted Answer:** Narrow problem [cite: 1690]
* [cite_start]**Question 2:** How many types of problems, Marr described [cite: 1691]
    * [cite_start]**Options:** 2 [cite: 1692][cite_start], 3 [cite: 1693][cite_start], 4 [cite: 1694][cite_start], 5 [cite: 1695]
    * [cite_start]**Accepted Answer:** 5 [cite: 1706]
* [cite_start]**Question 3:** Behaviorism school of psychology uses which of the following approach to solving the problems [cite: 1707]
    * [cite_start]**Options:** Associative learning approach [cite: 1726] *(Note: Other options are obscured)*
    * [cite_start]**Accepted Answer:** Associative learning approach [cite: 1726]
* [cite_start]**Question 4:** Law of effect was given by [cite: 1728]
    * [cite_start]**Options:** Wallas [cite: 1731][cite_start], Skinner [cite: 1734][cite_start], Wolfgang kohler [cite: 1739][cite_start], Thorndike [cite: 1740]
    * [cite_start]**Accepted Answer:** Thorndike [cite: 1753]
* [cite_start]**Question 5:** Which of the school of psychology uses the insight as a problem solving approach [cite: 1754]
    * [cite_start]**Options:** Functionalism [cite: 1755][cite_start], Gestalt psychology [cite: 1756][cite_start], Behaviorism [cite: 1757][cite_start], Structuralism [cite: 1758]
    * [cite_start]**Accepted Answer:** Gestalt psychology [cite: 1761]
* [cite_start]**Question 6:** Which of the following is an example of transformational problem [cite: 1762]
    * [cite_start]**Options:** Anagrams [cite: 1763][cite_start], Tower of hanoi [cite: 1764][cite_start], Analogy problems [cite: 1765][cite_start], Escaping form of maze [cite: 1766]
    * [cite_start]**Accepted Answer:** Tower of hanoi [cite: 1769]
* [cite_start]**Question 7:** "Creative acts are products of interpersonal, disciplinary and socio-cultural environments" is defined by [cite: 1770]
    * [cite_start]**Options:** Products [cite: 1771][cite_start], Person [cite: 1771][cite_start], Process [cite: 1775][cite_start], Press [cite: 1775]
    * [cite_start]**Accepted Answer:** Press [cite: 1779]
* [cite_start]**Question 8:** _____ is a very important technique for solving the Towers of Hanoi problem [cite: 1781]
    * [cite_start]**Options:** reasoning and analogy [cite: 1784][cite_start], generate-and-test [cite: 1785][cite_start], working backward [cite: 1786][cite_start], means-end-analysis [cite: 1791]
    * [cite_start]**Accepted Answer:** working backward [cite: 1793]
* [cite_start]**Question 9:** The strategy of working backward is most effective when: [cite: 1794]
    * [cite_start]**Options:** there are many possible paths to a solution [cite: 1795][cite_start], the backward path is unique [cite: 1796][cite_start], the optimal path leads you temporarily away from your goal [cite: 1797][cite_start], there are clear subgoals before the final goal [cite: 1797]
    * [cite_start]**Accepted Answer:** the backward path is unique [cite: 1801]
* [cite_start]**Question 10:** Which of the following is an example of an ill-defined problem? [cite: 1802]
    * [cite_start]**Options:** constructing a proof in geometry [cite: 1803][cite_start], putting together your schedule of classes for next semester [cite: 1804][cite_start], solving an algebra problem [cite: 1805][cite_start], solving the Tower of Hanoi problem [cite: 1806]
    * [cite_start]**Accepted Answer:** putting together your schedule of classes for next semester [cite: 1810]

---

### **Unit 12 (Assessment 11)**

* **Question 1:** if, someone likes Winnie-the-Pooh, they are a sensitive person. Mary likes Winnie-the-Pooh. Therefore, Mary is a sensitive person. [cite_start]Which of the reasoning can explain it? [cite: 1845-1849]
    * [cite_start]**Options:** Deductive reasoning [cite: 1853][cite_start], Inductive reasoning [cite: 1856][cite_start], Syllogistic reasoning [cite: 1859][cite_start], Conditional reasoning [cite: 1862]
    * [cite_start]**Accepted Answer:** Conditional reasoning [cite: 1875]
* [cite_start]**Question 2:** When general principles or assertions lead to a valid specific conclusion, it will be [cite: 1876]
    * [cite_start]**Options:** Inductive reasoning [cite: 1880][cite_start], Deductive reasoning [cite: 1881][cite_start], Syllogistic reasoning [cite: 1882][cite_start], Conditional reasoning [cite: 1883]
    * [cite_start]**Accepted Answer:** Deductive reasoning [cite: 1889]
* **Question 3:** *(Note: The question text is missing/obscured in the source document)*
    * [cite_start]**Accepted Answer:** Inductive reasoning [cite: 1911]
* [cite_start]**Question 4:** Typicality effect and diversity effect are seen in which of the reasoning [cite: 1913]
    * [cite_start]**Options:** Inductive reasoning [cite: 1922][cite_start], Syllogistic reasoning [cite: 1922][cite_start], Deductive reasoning [cite: 1923][cite_start], Conditional reasoning [cite: 1923]
    * [cite_start]**Accepted Answer:** Inductive reasoning [cite: 1925]
* [cite_start]**Question 5:** Who define that, judgment is the human ability to infer, estimate & predict the character of unknown events [cite: 1926-1928]
    * [cite_start]**Options:** Hastie & Dawes [cite: 1933][cite_start], Kahneman [cite: 1934][cite_start], Baron [cite: 1935][cite_start], Kahneman & Tversky [cite: 1936]
    * [cite_start]**Accepted Answer:** Hastie & Dawes [cite: 1940]
* [cite_start]**Question 6:** Newell and Simon (1972) proposed [cite: 1941]
    * [cite_start]**Options:** Tower of Hanoi [cite: 1942][cite_start], ACT [cite: 1943][cite_start], Problem Space [cite: 1944][cite_start], None of the above [cite: 1946]
    * [cite_start]**Accepted Answer:** Problem Space [cite: 1950]
* [cite_start]**Question 7:** _____ is the inability to see novel uses of everyday familiar objects [cite: 1955]
    * [cite_start]**Options:** Functional fixedness [cite: 1956][cite_start], Proactive inhibition [cite: 1957][cite_start], Interference [cite: 1958][cite_start], None of the above [cite: 1959]
    * [cite_start]**Accepted Answer:** Functional fixedness [cite: 1963]
* [cite_start]**Question 8:** Which of the following are the correct basic components of a problem [cite: 1964]
    * [cite_start]**Options:** Rules, problems, initial state [cite: 1966][cite_start], Initial state, goal state, rules, obstacles [cite: 1976][cite_start], Initial state, goal state, rewards, achievements [cite: 1979][cite_start], Goal state, initial state, rewards, obstacles [cite: 1980]
    * [cite_start]**Accepted Answer:** Initial state, goal state, rules, obstacles [cite: 1984]
* [cite_start]**Question 9:** Syllogisms consists of two [cite: 1985]
    * [cite_start]**Options:** Variables, hypothesis [cite: 1986][cite_start], Premises, conclusion [cite: 1987][cite_start], Heuristics, function [cite: 1988][cite_start], None of the above [cite: 1989]
    * [cite_start]**Accepted Answer:** Premises, conclusion [cite: 1992]
* [cite_start]**Question 10:** Ill-defined problems are [cite: 1993]
    * [cite_start]**Options:** Clear and solvable [cite: 1994][cite_start], Fuzzy and abstract [cite: 1995][cite_start], Full of constraints and obstacles [cite: 1996][cite_start], None of the above [cite: 1997]
    * [cite_start]**Accepted Answer:** Fuzzy and abstract [cite: 2001]

---

### **Unit 13 (Assessment 12)**

* [cite_start]**Question 1:** When Consumer faced with some type of uncertain choice, then they will make decisions based on [cite: 2031-2033]
    * [cite_start]**Options:** Their interest [cite: 2035][cite_start], Respective probability of outcomes [cite: 2036][cite_start], Expected utility of outcomes [cite: 2054][cite_start], Expected utility and respective probabilities of outcomes [cite: 2055]
    * [cite_start]**Accepted Answer:** Expected utility and respective probabilities of outcomes [cite: 2059]
* [cite_start]**Question 2:** Who proposed the Prospect theory [cite: 2060]
    * [cite_start]**Options:** Lichtenstein & Slovic [cite: 2065][cite_start], Kahneman & Tversky [cite: 2066][cite_start], Arkes and Blumer [cite: 2067][cite_start], Clemen [cite: 2068]
    * [cite_start]**Accepted Answer:** Kahneman & Tversky [cite: 2072]
* [cite_start]**Question 3:** Decisions are not valued based on the absolute value of the end result, as proposed by the expected utility instead, we value decisions based on the amount of gain or loss from what we have right [cite: 2075]
    * [cite_start]**Options:** Expected utility theory [cite: 2094][cite_start], Prospect theory [cite: 2114] *(Note: Other options are obscured)*
    * [cite_start]**Accepted Answer:** Prospect theory [cite: 2114]
* [cite_start]**Question 4:** Choose the correct option from the following [cite: 2115]
    * [cite_start]**Options:** MAUT - Main Attention Utility Technique [cite: 2116][cite_start], MAUT-Multi Attention Utility Task [cite: 2118][cite_start], MAUT-Multi Attribute Universal Task [cite: 2119][cite_start], MAUT - Multi Attribute Utility Theory [cite: 2120]
    * [cite_start]**Accepted Answer:** MAUT - Multi Attribute Utility Theory [cite: 2130]
* [cite_start]**Question 5:** Hsee & Rottenstreich (2004) suggest that in _____ we value things or take decisions by the feelings they evoke [cite: 2131-2132]
    * [cite_start]**Options:** Dual process view [cite: 2137][cite_start], Affective decision-making mode [cite: 2138][cite_start], Gain Frame [cite: 2139][cite_start], None of the above [cite: 2140]
    * [cite_start]**Accepted Answer:** Affective decision-making mode [cite: 2144]
* **Question 6:** You are offered a chance to buy a lottery ticket. The probability of winning is 1 in 100. If you win, the prize is $100,000. [cite_start]According to expected value, a "fair" price for this lottery ticket would be: [cite: 2146-2148]
    * [cite_start]**Options:** $5 [cite: 2149][cite_start], $100 [cite: 2150][cite_start], $1000 [cite: 2153][cite_start], $10 [cite: 2154]
    * [cite_start]**Accepted Answer:** $1000 [cite: 2158]
* **Question 7:** You have just spent 10 minutes trying to figure out the answer to a single problem on your math quiz. In spite of your lack of success, you continue to struggle, neglecting to continue on to other problems because you've already invested so much time and effort in this problem. [cite_start]You have fallen victim to [cite: 2159-2161]
    * [cite_start]**Options:** the anchor effect [cite: 2166][cite_start], the availability effect [cite: 2167][cite_start], the framing effect [cite: 2168][cite_start], the sunk cost effect [cite: 2169]
    * [cite_start]**Accepted Answer:** the sunk cost effect [cite: 2178]
* [cite_start]**Question 8:** _____ is a mistaken belief that the probability of a given random event such as winning or losing at a game of chance is influenced by previous random events [cite: 2180-2181]
    * [cite_start]**Options:** gamblers fallacy [cite: 2182][cite_start], psychological accounting [cite: 2183][cite_start], sunk cost [cite: 2184][cite_start], means end [cite: 2185]
    * [cite_start]**Accepted Answer:** gamblers fallacy [cite: 2189]
* **Question 9:** Patient Ravi is told that the operation has a 10% chance of failure, whereas patient Manoj is told that the same operation has a 90% chance of success. [cite_start]If Ravi chooses not to have surgery, while Manoj chooses to have the surgery, to what psychological phenomenon could we attribute this outcome? [cite: 2190-2191]
    * [cite_start]**Options:** representative heuristic [cite: 2192][cite_start], framing effect [cite: 2193][cite_start], availability [cite: 2195][cite_start], functional fixedness [cite: 2196]
    * [cite_start]**Accepted Answer:** framing effect [cite: 2200]
* [cite_start]**Question 10:** Normative models of decision making describe: [cite: 2201]
    * [cite_start]**Options:** how we ought to make decisions in realistic circumstances [cite: 2202][cite_start], what people actually do when they make decisions [cite: 2203][cite_start], ideal performance under ideal circumstances [cite: 2204][cite_start], cognitive illusions [cite: 2205]
    * [cite_start]**Accepted Answer:** ideal performance under ideal circumstances [cite: 2209]
"""

# Extract units
units = re.split(r'### \*\*Unit \d+ \(Assessment (\d+)\)\*\*', text)
# units[1] is assessment num, units[2] is content, etc.

questions = []
for i in range(1, len(units), 2):
    assessment_num = int(units[i])
    unit_content = units[i+1]
    
    # Extract questions
    q_blocks = re.split(r'\* \[cite_start\]\*\*Question \d+:\*\*|\* \*\*Question \d+:\*\*', unit_content)[1:]
    
    for j, q_block in enumerate(q_blocks):
        q_num = j + 1
        
        # Extract question text
        q_text_match = re.search(r'(.*?)(?:\[cite:|\* \[cite_start\]\*\*Options:\*\*)', q_block, re.DOTALL)
        q_text = q_text_match.group(1).strip() if q_text_match else ""
        
        # Extract options
        options_match = re.search(r'\*\*Options:\*\* (.*?) \*(?:Note:|\*\*Accepted Answer:\*\*)', q_block, re.DOTALL)
        if not options_match:
            options_match = re.search(r'\*\*Options:\*\* (.*?)\*\*Accepted Answer:\*\*', q_block, re.DOTALL)
            
        options = []
        if options_match:
            # Split by [cite: ...] or [cite_start] or ;
            opts_raw = re.split(r'\[cite: \d+\](?:\[cite_start\])?|;|\n', options_match.group(1))
            for opt in opts_raw:
                opt = re.sub(r'\[cite_start\]', '', opt)
                opt = opt.strip().strip(',')
                if opt and not opt.startswith('**Options:**'):
                    options.append(opt)
        
        # Extract accepted answer
        answer_match = re.search(r'\*\*Accepted Answer:\*\* (.*?)(?:\[cite:|\n|$)', q_block)
        answer_text = answer_match.group(1).strip().strip('_') if answer_match else ""
        
        # Find index
        correct_index = -1
        for idx, opt in enumerate(options):
            if answer_text.lower() == opt.lower() or answer_text.lower() in opt.lower() or opt.lower() in answer_text.lower():
                correct_index = idx
                break
        
        if correct_index == -1 and options:
            correct_index = 0 # Fallback
            
        questions.append({
            "id": f"w{assessment_num}q{q_num}",
            "week": assessment_num,
            "question": q_text,
            "options": options,
            "correctAnswer": correct_index,
            "explanation": ""
        })

with open('/Users/vishnu/Desktop/cognitive/scratch/2020_questions.json', 'w') as f:
    json.dump(questions, f, indent=2)

print(f"Parsed {len(questions)} questions for 2020.")
