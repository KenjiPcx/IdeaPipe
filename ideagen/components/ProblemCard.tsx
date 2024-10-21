import { Problem } from '@/data/mockProblems';
import Link from 'next/link';

interface ProblemCardProps {
  problem: Problem;
}

export default function ProblemCard({ problem }: ProblemCardProps) {
  return (
    <div className="bg-white shadow-md rounded-lg p-6">
      <h3 className="text-xl font-semibold mb-2">{problem.title}</h3>
      <p className="text-gray-600 mb-4">{problem.description}</p>
      <div className="flex justify-between items-center">
        <span className="text-sm font-medium text-blue-600">{problem.category}</span>
        <span className={`text-sm font-medium px-2 py-1 rounded-full ${
          problem.difficulty === 'Easy' ? 'bg-green-100 text-green-800' :
          problem.difficulty === 'Medium' ? 'bg-yellow-100 text-yellow-800' :
          'bg-red-100 text-red-800'
        }`}>
          {problem.difficulty}
        </span>
      </div>
      <Link href={`/problems/${problem.id}`} className="mt-4 inline-block bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
        View Problem
      </Link>
    </div>
  );
}
