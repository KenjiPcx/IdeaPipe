import React from 'react';

interface ProblemCardProps {
  id: string;
  title: string;
  description: string;
  category: string;
  difficulty: string;
}

const ProblemCard = ({ title, description, category, difficulty }: ProblemCardProps) => {
  return (
    <div className="bg-white shadow-md rounded-lg p-4 mb-4">
      <h2 className="text-xl font-bold mb-2">{title}</h2>
      <p className="text-gray-600 mb-2">{description}</p>
      <div className="flex justify-between items-center">
        <span className="bg-blue-100 text-blue-800 px-2 py-1 rounded">{category}</span>
        <span className="text-gray-500">{difficulty}</span>
      </div>
    </div>
  );
};

export default ProblemCard;
