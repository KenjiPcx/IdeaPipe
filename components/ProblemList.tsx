import React from 'react';
import { Problem } from '../types/Problem';

interface ProblemListProps {
  problems: Problem[];
  onProblemSelect: (problem: Problem) => void;
}

const ProblemList: React.FC<ProblemListProps> = ({ problems, onProblemSelect }) => {
  return (
    <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
      <h2 className="text-xl font-bold mb-2">Problems</h2>
      <ul>
        {problems.map((problem) => (
          <li 
            key={problem.id} 
            className="cursor-pointer hover:bg-gray-100 p-2 rounded"
            onClick={() => onProblemSelect(problem)}
          >
            {problem.title}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProblemList;
