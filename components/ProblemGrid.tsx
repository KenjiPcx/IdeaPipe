import React from 'react';
import ProblemCard from './ProblemCard';

interface Problem {
  id: string;
  title: string;
  description: string;
  category: string;
  difficulty: string;
}

interface ProblemGridProps {
  problems: Problem[];
}

const ProblemGrid = ({ problems }: ProblemGridProps) => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {problems.map((problem) => (
        <ProblemCard key={problem.id} {...problem} />
      ))}
    </div>
  );
};

export default ProblemGrid;
