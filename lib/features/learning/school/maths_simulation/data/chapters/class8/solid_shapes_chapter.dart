import '../../../models/chapter_model.dart';
final ChapterModel class8SolidShapesChapter = ChapterModel(
  standard: 8, subject: "Mathematics", chapterId: "cls8_math_solidshapes", chapterName: "Visualising Solid Shapes",
  concepts: ["Views of 3-D shapes: top, front and side views.", "Mapping and scale.", "Faces, edges and vertices; Euler's formula."],
  formulas: [],
  fillInTheBlanks: [
    QuestionItem(id: "vs8_1", question: "Solids like cubes and cuboids that have flat polygonal faces are called [ polyhedrons / non-polyhedrons ].", answer: "polyhedrons"),
    QuestionItem(id: "vs8_2", question: "A polyhedron is convex if any line segment joining two points on its surface lies [ inside or on the polyhedron / outside the polyhedron ].", answer: "inside or on the polyhedron"),
    QuestionItem(id: "vs8_3", question: "A polyhedron whose faces are all congruent regular polygons, with the same number of faces meeting at each vertex, is called a [ regular polyhedron / prism ].", answer: "regular polyhedron"),
    QuestionItem(id: "vs8_4", question: "Euler's formula for any polyhedron states F + V − E = [ 2 / 1 ].", answer: "2"),
    QuestionItem(id: "vs8_5", question: "A solid with two congruent polygonal bases connected by rectangular faces is called a [ prism / pyramid ].", answer: "prism"),
    QuestionItem(id: "vs8_6", question: "A solid with one polygonal base and triangular faces meeting at a single apex is called a [ pyramid / prism ].", answer: "pyramid"),
    QuestionItem(id: "vs8_7", question: "Viewing an object exactly from above gives its [ top view / front view ].", answer: "top view"),
    QuestionItem(id: "vs8_8", question: "Viewing an object directly from the front gives its [ front view / side view ].", answer: "front view"),
    QuestionItem(id: "vs8_9", question: "A map is a representation of a region drawn on a [ flat surface, viewed from top / curved surface ].", answer: "flat surface, viewed from top"),
    QuestionItem(id: "vs8_10", question: "Maps use a fixed [ scale / colour code only ] to represent real distances proportionally.", answer: "scale"),
    QuestionItem(id: "vs8_11", question: "Unlike a photograph, a map does not depend on the [ observer's viewpoint or perspective / actual distances ].", answer: "observer's viewpoint or perspective"),
    QuestionItem(id: "vs8_12", question: "A cube has [ 6 / 4 ] identical square faces.", answer: "6"),
  ],
  numericalProblems: [
    NumericalProblem(id: "vs8n1", question: "A polyhedron has 8 faces and 12 vertices. Using Euler's formula, find the number of edges.", given: ["F = 8", "V = 12", "F + V − E = 2"], solutionSteps: ["8 + 12 − E = 2", "20 − E = 2", "E = 18"], numericAnswer: 18, unit: "edges"),
    NumericalProblem(id: "vs8n2", question: "A polyhedron has 5 faces and 9 edges. Find the number of vertices.", given: ["F = 5", "E = 9"], solutionSteps: ["F + V − E = 2", "5 + V − 9 = 2", "V = 6"], numericAnswer: 6, unit: "vertices"),
    NumericalProblem(id: "vs8n3", question: "A polyhedron has 20 faces and 12 vertices. Using Euler's formula, find the number of edges.", given: ["F = 20", "V = 12"], solutionSteps: ["F + V − E = 2", "20 + 12 − E = 2", "E = 30"], numericAnswer: 30, unit: "edges"),
    NumericalProblem(id: "vs8n4", question: "A map has a scale of 1 cm : 200 km. Find the actual distance if the map shows 6 cm.", given: ["Scale: 1 cm = 200 km", "Map distance = 6 cm"], solutionSteps: ["Actual distance = 6 × 200", "= 1200 km"], numericAnswer: 1200, unit: "km"),
    NumericalProblem(id: "vs8n5", question: "How many vertices does a cube have?", given: ["Cube"], solutionSteps: ["A cube has 8 vertices where 3 edges meet."], numericAnswer: 8, unit: ""),
    NumericalProblem(id: "vs8n6", question: "A prism with a pentagonal base has 7 faces and 15 edges. Using Euler's formula, find the number of vertices.", given: ["F = 7", "E = 15"], solutionSteps: ["F + V − E = 2", "7 + V − 15 = 2", "V = 10"], numericAnswer: 10, unit: "vertices"),
    NumericalProblem(id: "vs8n7", question: "On a map with scale 1 cm : 50 km, find the map distance for an actual distance of 350 km.", given: ["Scale: 1 cm = 50 km", "Actual distance = 350 km"], solutionSteps: ["Map distance = 350 ÷ 50", "= 7 cm"], numericAnswer: 7, unit: "cm"),
  ],
);
