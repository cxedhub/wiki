// Florida state standards database for CxEd Hub — Florida lesson template
// Loads AFTER standards-db.js and merges Florida frameworks into window.STANDARDS_DB.
// Covers: B.E.S.T. ELA, B.E.S.T. Math, NGSSS Science, NGSSS Social Studies,
// Florida K-12 Computer Science Standards. Each framework maps code -> short description.
// Source: Florida Department of Education (CPALMS). See STANDARDS_FW_URLS below.
(function(){
  window.STANDARDS_DB = window.STANDARDS_DB || {};
  window.STANDARDS_FW_URLS = window.STANDARDS_FW_URLS || {};

  const FL = {
    "FL B.E.S.T. ELA": {
      "ELA.K.F.1.1":"Demonstrate phonological awareness",
      "ELA.K.F.1.2":"Demonstrate phonics skills when reading",
      "ELA.K.F.1.3":"Demonstrate letter-sound knowledge",
      "ELA.K.F.1.4":"Recognize and produce rhyming words",
      "ELA.K.R.1.1":"Describe main character(s), setting, events in a story",
      "ELA.K.R.1.2":"Identify and describe the rhyme and rhythm in poems",
      "ELA.K.R.1.3":"Explain the roles of author and illustrator of a story",
      "ELA.K.R.2.1":"Identify the topic of and relevant details in a text",
      "ELA.K.R.2.2":"Identify the structure of a text as descriptive",
      "ELA.K.R.2.3":"Explain the difference between opinions and facts",
      "ELA.K.R.3.1":"Identify and describe the characters, settings, and events",
      "ELA.K.R.3.2":"Retell a story orally using main story elements",
      "ELA.K.R.3.3":"Compare/contrast characters' adventures in familiar stories",
      "ELA.K.C.1.1":"Print many upper and lowercase letters",
      "ELA.K.C.1.2":"Using a combination of drawing/dictating/writing, tell about a topic",
      "ELA.K.C.1.3":"Using a combination of drawing/dictating/writing, tell a narrative",
      "ELA.K.C.1.4":"With support, produce complete sentences",
      "ELA.K.C.1.5":"With support, add details to improve a draft",
      "ELA.K.C.2.1":"Present information orally using complete sentences",
      "ELA.K.C.3.1":"Follow agreed-upon rules for discussion",
      "ELA.K.V.1.1":"Use grade-level academic vocabulary appropriately",
      "ELA.K.V.1.2":"Ask and answer questions about unfamiliar words",
      "ELA.K.V.1.3":"Identify and sort common words into basic categories"
    },
    "FL B.E.S.T. Math": {
      "MA.K.NSO.1.1":"Given a group of up to 20 objects, count the number of objects",
      "MA.K.NSO.1.2":"Given a number from 0 to 20, count out that many objects",
      "MA.K.NSO.1.3":"Identify the number, 0-20, that comes before/after a given number",
      "MA.K.NSO.1.4":"Compare the number of objects from 0 to 20 in two groups",
      "MA.K.NSO.2.1":"Recite the number names to 100 by ones and by tens",
      "MA.K.NSO.2.2":"Represent whole numbers from 10 to 20, using a unit of ten and units of ones",
      "MA.K.NSO.2.3":"Locate, order and compare numbers from 0 to 20 using the symbols <, > and =",
      "MA.K.NSO.3.1":"Explore addition of two whole numbers from 0 to 10",
      "MA.K.NSO.3.2":"Add two one-digit whole numbers with sums from 0 to 10",
      "MA.K.NSO.3.3":"Subtract a one-digit number from a whole number up to 10",
      "MA.K.AR.1.1":"For any number from 1 to 9, find the number that makes 10",
      "MA.K.AR.1.2":"Given a number from 0 to 10, find the different ways it can be represented",
      "MA.K.M.1.1":"Identify and compare the attributes of two objects (length, height, weight)",
      "MA.K.M.1.2":"Directly compare two objects with a common measurable attribute",
      "MA.K.GR.1.1":"Identify two- and three-dimensional figures regardless of orientation or size",
      "MA.K.GR.1.2":"Compare two-/three-dimensional figures based on attributes",
      "MA.K.GR.1.3":"Sort two-/three-dimensional figures based on their differences and similarities",
      "MA.K.DP.1.1":"Collect information about objects in the classroom and present it"
    },
    "FL NGSSS Science": {
      "SC.K.N.1.1":"Collaborate with a partner to collect information",
      "SC.K.N.1.2":"Make observations of the natural world and know that they are descriptors",
      "SC.K.N.1.3":"Keep records as appropriate—such as drawings, pictorial records",
      "SC.K.N.1.4":"Observe and create a visual representation of an object",
      "SC.K.N.1.5":"Recognize that learning can come from careful observation",
      "SC.K.E.5.1":"Explore the Law of Gravity by investigating how objects are pulled toward the Earth",
      "SC.K.E.5.3":"Recognize that the Sun can only be seen in the daytime",
      "SC.K.L.14.1":"Recognize the five senses and related body parts",
      "SC.K.L.14.2":"Recognize that some books and other media portray animals and plants unrealistically",
      "SC.K.L.14.3":"Observe plants and animals, describe how they are alike and how they are different",
      "SC.K.P.8.1":"Sort objects by observable properties, such as size, shape, color",
      "SC.K.P.10.1":"Observe that things that make sound vibrate",
      "SC.K.P.12.1":"Investigate that things move in different ways, such as fast, slow, straight",
      "SC.K.P.13.1":"Observe that a push or a pull can change the way an object is moving"
    },
    "FL NGSSS Social Studies": {
      "SS.K.A.1.1":"Develop an understanding of how to use and create a timeline",
      "SS.K.A.1.2":"Develop an awareness of a primary source",
      "SS.K.A.2.1":"Compare children and families of today with those in the past",
      "SS.K.A.2.2":"Recognize the importance of celebrations and national holidays",
      "SS.K.A.2.3":"Compare our nation's holidays with holidays of other cultures",
      "SS.K.A.3.1":"Use words and phrases related to chronology and time",
      "SS.K.A.3.2":"Explain that calendars represent days of the week and months of the year",
      "SS.K.C.1.1":"Define and give examples of rules and laws, and why they are important",
      "SS.K.C.1.2":"Explain the purpose and necessity of rules and laws at home, school, community",
      "SS.K.C.2.1":"Demonstrate the characteristics of being a good citizen",
      "SS.K.C.2.2":"Demonstrate that conflicts among friends can be resolved in ways that are consistent",
      "SS.K.C.2.3":"Describe fair ways for groups to make decisions",
      "SS.K.E.1.1":"Describe different kinds of jobs that people do and the tools or equipment used",
      "SS.K.E.1.2":"Recognize that United States currency comes in different forms",
      "SS.K.E.1.3":"Recognize that people work to earn money to buy things they need or want",
      "SS.K.G.1.1":"Describe the relative location of people, places, and things",
      "SS.K.G.1.2":"Explain that maps and globes help to locate different places",
      "SS.K.G.1.3":"Identify cardinal directions (north, south, east, west)",
      "SS.K.G.2.1":"Locate and describe places in the school and community",
      "SS.K.G.3.1":"Identify basic landforms",
      "SS.K.G.3.2":"Identify basic bodies of water",
      "SS.K.G.3.3":"Describe and give examples of seasonal weather changes"
    },
    "FL K-12 Computer Science": {
      "SC.K2.CS-CS.1.1":"Recognize that software is created to control computer operations",
      "SC.K2.CS-CS.1.2":"Identify different kinds of data (e.g., text, charts, graphs, numbers, pictures)",
      "SC.K2.CS-CS.1.3":"Identify ways people use computers at school, work, and daily life",
      "SC.K2.CS-CS.2.1":"Identify and describe hardware used to work with computers (e.g., keyboards)",
      "SC.K2.CS-CS.2.2":"Identify and locate keys (e.g., function keys, letter keys, arrow keys)",
      "SC.K2.CS-CS.2.3":"Describe the importance of maintaining good posture at the computer",
      "SC.K2.CS-CS.2.4":"Identify and describe simple actions using symbols in a sequence",
      "SC.K2.CS-CS.2.5":"Describe how 0s and 1s are used to represent data in a computer",
      "SC.K2.CS-CS.3.1":"Identify appropriate and inappropriate uses of technology",
      "SC.K2.CS-CS.3.2":"Identify the purpose and importance of online safety",
      "SC.K2.CS-CS.3.3":"Identify safe online communication practices",
      "SC.K2.CS-CP.1.1":"Identify that specific actions can cause specific results",
      "SC.K2.CS-CP.1.2":"Identify a simple sequence of steps that can be performed by a computer",
      "SC.K2.CS-CP.2.1":"Define an algorithm as a sequence of defined steps",
      "SC.K2.CS-CP.2.2":"Recognize that software is created to control computer operations",
      "SC.K2.CS-CP.3.1":"Identify that programs require a defined series of commands in order to run",
      "SC.K2.CS-PC.1.1":"Identify appropriate and inappropriate uses of technology when posting",
      "SC.K2.CS-PC.2.1":"Identify what passwords are and why they are used",
      "SC.K2.CS-PC.2.2":"Identify ways to keep personal information private",
      "SC.K2.CS-PC.2.3":"Identify common cyberbullying behaviors and know how to respond"
    }
  };

  Object.assign(window.STANDARDS_DB, FL);

  Object.assign(window.STANDARDS_FW_URLS, {
    "FL B.E.S.T. ELA": "https://www.cpalms.org/PublicPreviewStandardsBrowse/PreviewStandards.aspx?subject=ELA",
    "FL B.E.S.T. Math": "https://www.cpalms.org/PublicPreviewStandardsBrowse/PreviewStandards.aspx?subject=Math",
    "FL NGSSS Science": "https://www.cpalms.org/PublicPreviewStandardsBrowse/PreviewStandards.aspx?subject=Science",
    "FL NGSSS Social Studies": "https://www.cpalms.org/PublicPreviewStandardsBrowse/PreviewStandards.aspx?subject=SocialStudies",
    "FL K-12 Computer Science": "https://www.fldoe.org/academics/standards/subject-areas/computer-science.stml"
  });
})();
