export interface Problem {
  id: string;
  title: string;
  description: string;
  category: string;
  difficulty: 'Easy' | 'Medium' | 'Hard';
}

export const mockProblems: Problem[] = [
  {
    id: '1',
    title: 'Sustainable Energy Storage',
    description: 'Develop an innovative solution for storing renewable energy efficiently.',
    category: 'Energy',
    difficulty: 'Hard',
  },
  {
    id: '2',
    title: 'Smart Urban Transportation',
    description: 'Create a system to optimize city traffic flow and reduce congestion.',
    category: 'Transportation',
    difficulty: 'Medium',
  },
  // Add more mock problems here
];
