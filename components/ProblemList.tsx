import React from 'react';
import ProblemCard from './ProblemCard';

interface Problem {
  id: string;
  title: string;
  description: string;
  category: string;
  difficulty: string;
}

interface ProblemListProps {
  problems: Problem[];
}

const ProblemList: React.FC<ProblemListProps> = ({ problems }) => {
  return (
    <div>
      {problems.map((problem) => (
        <ProblemCard key={problem.id} {...problem} />
      ))}
    </div>
  );
};

export default ProblemList;
